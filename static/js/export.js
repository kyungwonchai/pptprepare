/**
 * 슬라이드 PDF / PPTX 내보내기 (선택 번호 → POST /export/download)
 */
(function () {
  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function $all(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  document.addEventListener("DOMContentLoaded", function () {
    var dialog = $("#export-dialog");
    var openBtn = $("#export-open-btn");
    var cancelBtn = $("#export-cancel");
    var submitBtn = $("#export-submit");
    var selectAllBtn = $("#export-select-all");
    var clearBtn = $("#export-clear");
    var statusEl = $("#export-status");

    if (!dialog || !openBtn) return;

    var postUrl = dialog.getAttribute("data-export-url") || "/export/download";

    function setStatus(msg) {
      if (statusEl) statusEl.textContent = msg || "";
    }

    function getSelectedNums() {
      return $all('input.export-slide-cb:checked', dialog).map(function (cb) {
        return parseInt(cb.value, 10);
      });
    }

    openBtn.addEventListener("click", function () {
      if (typeof dialog.showModal === "function") {
        dialog.showModal();
      } else {
        dialog.setAttribute("open", "");
      }
      setStatus("");
    });

    if (cancelBtn) {
      cancelBtn.addEventListener("click", function () {
        if (typeof dialog.close === "function") dialog.close();
        else dialog.removeAttribute("open");
      });
    }

    $all(".export-group-cb", dialog).forEach(function (gcb) {
      gcb.addEventListener("change", function () {
        var gid = gcb.getAttribute("data-group-id");
        var group = dialog.querySelector('.export-group[data-group-id="' + gid + '"]');
        if (!group) return;
        var on = gcb.checked;
        $all(".export-slide-cb", group).forEach(function (cb) {
          cb.checked = on;
        });
      });
    });

    if (selectAllBtn) {
      selectAllBtn.addEventListener("click", function () {
        $all("input.export-slide-cb", dialog).forEach(function (cb) {
          cb.checked = true;
        });
        $all(".export-group-cb", dialog).forEach(function (cb) {
          cb.checked = true;
        });
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        $all("input.export-slide-cb", dialog).forEach(function (cb) {
          cb.checked = false;
        });
        $all(".export-group-cb", dialog).forEach(function (cb) {
          cb.checked = false;
        });
      });
    }

    if (submitBtn) {
      submitBtn.addEventListener("click", function () {
        var nums = getSelectedNums();
        if (!nums.length) {
          setStatus("슬라이드를 하나 이상 선택하세요.");
          return;
        }
        nums.sort(function (a, b) {
          return a - b;
        });

        var fmtEl = dialog.querySelector('input[name="export-format"]:checked');
        var themeEl = dialog.querySelector('input[name="export-theme"]:checked');
        var format = fmtEl ? fmtEl.value : "pdf";
        var theme = themeEl ? themeEl.value : "dark";

        setStatus("생성 중… (슬라이드 " + nums.length + "장 · 잠시만 기다려 주세요)");
        submitBtn.disabled = true;

        fetch(postUrl, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/octet-stream" },
          body: JSON.stringify({ slides: nums, format: format, theme: theme }),
        })
          .then(function (r) {
            var ct = r.headers.get("Content-Type") || "";
            if (!r.ok) {
              if (ct.indexOf("json") !== -1) {
                return r.json().then(function (j) {
                  throw new Error(j.error || r.statusText);
                });
              }
              throw new Error(r.statusText || "오류");
            }
            var cd = r.headers.get("Content-Disposition") || "";
            var name = "slides-export.bin";
            var m = /filename\*?=(?:UTF-8'')?["']?([^\";\n]+)/i.exec(cd);
            if (m) name = decodeURIComponent(m[1].replace(/['"]/g, "").trim());
            return r.blob().then(function (blob) {
              return { blob: blob, name: name };
            });
          })
          .then(function (o) {
            var a = document.createElement("a");
            a.href = URL.createObjectURL(o.blob);
            a.download = o.name;
            a.rel = "noopener";
            document.body.appendChild(a);
            a.click();
            URL.revokeObjectURL(a.href);
            a.remove();
            setStatus("다운로드가 시작되었습니다.");
            if (typeof dialog.close === "function") dialog.close();
            else dialog.removeAttribute("open");
          })
          .catch(function (e) {
            setStatus(e.message || String(e));
          })
          .finally(function () {
            submitBtn.disabled = false;
          });
      });
    }
  });
})();
