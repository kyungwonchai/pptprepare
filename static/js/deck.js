/**
 * PPT 모드 / 페이지 탐색 모드, 좌측 챕터 패널 — localStorage 유지
 */
(function () {
  var STORAGE_MODE = "pptprepare:viewMode";
  var STORAGE_SIDEBAR = "pptprepare:sidebarOpen";
  /** PPT일 때 챕터 펼침 여부 — 탐색 갔다가 PPT로 돌올 때 복원용 */
  var STORAGE_SIDEBAR_PPT_SNAPSHOT = "pptprepare:sidebarPptSnapshot";

  function $(sel) {
    return document.querySelector(sel);
  }

  function applyMode(mode) {
    var body = document.body;
    body.classList.remove("mode-ppt", "mode-browse");
    body.classList.add(mode === "browse" ? "mode-browse" : "mode-ppt");
    var pptBtn = $("#mode-ppt-btn");
    var browseBtn = $("#mode-browse-btn");
    if (pptBtn && browseBtn) {
      var isPpt = mode !== "browse";
      pptBtn.setAttribute("aria-pressed", isPpt ? "true" : "false");
      browseBtn.setAttribute("aria-pressed", isPpt ? "false" : "true");
    }
  }

  function applySidebar(open) {
    var panel = $("#deck-chapter");
    if (!panel) return;
    panel.classList.toggle("is-open", open);
    var btn = $("#chapter-toggle");
    if (btn) {
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var savedMode = localStorage.getItem(STORAGE_MODE);
    if (savedMode === "browse" || savedMode === "ppt") {
      applyMode(savedMode);
    } else {
      applyMode("ppt");
    }

    /* 탐색 모드에서는 페이지 제목 목록(챕터)을 항상 펼친 상태로 둠 */
    if (savedMode === "browse") {
      localStorage.setItem(STORAGE_SIDEBAR, "1");
      applySidebar(true);
    } else {
      var savedSidebar = localStorage.getItem(STORAGE_SIDEBAR);
      applySidebar(savedSidebar === "1");
    }

    var pptBtn = $("#mode-ppt-btn");
    var browseBtn = $("#mode-browse-btn");
    if (pptBtn) {
      pptBtn.addEventListener("click", function () {
        localStorage.setItem(STORAGE_MODE, "ppt");
        applyMode("ppt");
        var snap = localStorage.getItem(STORAGE_SIDEBAR_PPT_SNAPSHOT);
        if (snap === "0" || snap === "1") {
          localStorage.setItem(STORAGE_SIDEBAR, snap);
          applySidebar(snap === "1");
          localStorage.removeItem(STORAGE_SIDEBAR_PPT_SNAPSHOT);
        } else {
          applySidebar(localStorage.getItem(STORAGE_SIDEBAR) === "1");
        }
      });
    }
    if (browseBtn) {
      browseBtn.addEventListener("click", function () {
        var panel = $("#deck-chapter");
        if (document.body.classList.contains("mode-ppt") && panel) {
          localStorage.setItem(
            STORAGE_SIDEBAR_PPT_SNAPSHOT,
            panel.classList.contains("is-open") ? "1" : "0"
          );
        }
        localStorage.setItem(STORAGE_MODE, "browse");
        localStorage.setItem(STORAGE_SIDEBAR, "1");
        applyMode("browse");
        applySidebar(true);
      });
    }

    var chToggle = $("#chapter-toggle");
    if (chToggle) {
      chToggle.addEventListener("click", function () {
        var panel = $("#deck-chapter");
        var open = !panel.classList.contains("is-open");
        localStorage.setItem(STORAGE_SIDEBAR, open ? "1" : "0");
        applySidebar(open);
      });
    }
  });
})();
