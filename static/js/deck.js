/**
 * PPT 모드 / 페이지 탐색 모드, 좌측 챕터 패널 — localStorage 유지
 */
(function () {
  var STORAGE_MODE = "pptprepare:viewMode";
  var STORAGE_THEME = "pptprepare:theme";
  var STORAGE_SIDEBAR = "pptprepare:sidebarOpen";
  /** PPT일 때 챕터 펼침 여부 — 탐색 갔다가 PPT로 돌올 때 복원용 */
  var STORAGE_SIDEBAR_PPT_SNAPSHOT = "pptprepare:sidebarPptSnapshot";
  /** 좌측 트리 그룹별 접기/펼치기 */
  var STORAGE_NAV_GROUPS = "pptprepare:navGroupsExpand";

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

  function applyTheme(theme) {
    var t = theme === "light" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", t);
    var lightBtn = $("#theme-light-btn");
    var darkBtn = $("#theme-dark-btn");
    if (lightBtn && darkBtn) {
      var isLight = t === "light";
      lightBtn.setAttribute("aria-pressed", isLight ? "true" : "false");
      darkBtn.setAttribute("aria-pressed", isLight ? "false" : "true");
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var savedTheme = localStorage.getItem(STORAGE_THEME);
    if (savedTheme === "light" || savedTheme === "dark") {
      applyTheme(savedTheme);
    } else {
      applyTheme("dark");
    }

    var lightThemeBtn = $("#theme-light-btn");
    var darkThemeBtn = $("#theme-dark-btn");
    if (lightThemeBtn) {
      lightThemeBtn.addEventListener("click", function () {
        localStorage.setItem(STORAGE_THEME, "light");
        applyTheme("light");
      });
    }
    if (darkThemeBtn) {
      darkThemeBtn.addEventListener("click", function () {
        localStorage.setItem(STORAGE_THEME, "dark");
        applyTheme("dark");
      });
    }

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

    initNavGroups();
  });

  function setGroupExpanded(group, open) {
    group.classList.toggle("is-expanded", open);
    group.classList.toggle("is-collapsed", !open);
    var btn = group.querySelector(".deck-chapter-group-toggle");
    if (btn) {
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    }
  }

  function persistNavGroups(root) {
    var all = {};
    root.querySelectorAll(".deck-chapter-group").forEach(function (g) {
      var gid = g.getAttribute("data-group-id");
      if (gid) {
        all[gid] = g.classList.contains("is-expanded");
      }
    });
    try {
      localStorage.setItem(STORAGE_NAV_GROUPS, JSON.stringify(all));
    } catch (e) {}
  }

  function initNavGroups() {
    var root = $("#deck-chapter-tree");
    if (!root) return;

    var currentN = parseInt(root.getAttribute("data-current-n") || "0", 10);
    var saved = {};
    try {
      var raw = localStorage.getItem(STORAGE_NAV_GROUPS);
      if (raw) {
        saved = JSON.parse(raw);
      }
    } catch (e) {
      saved = {};
    }

    root.querySelectorAll(".deck-chapter-group").forEach(function (group) {
      var id = group.getAttribute("data-group-id");
      var min = parseInt(group.getAttribute("data-range-min"), 10);
      var max = parseInt(group.getAttribute("data-range-max"), 10);
      var hasActive =
        currentN > 0 && !isNaN(min) && !isNaN(max) && currentN >= min && currentN <= max;

      var expanded;
      if (hasActive) {
        expanded = true;
      } else if (id && Object.prototype.hasOwnProperty.call(saved, id)) {
        expanded = saved[id] === true;
      } else {
        expanded = false;
      }
      setGroupExpanded(group, expanded);
    });

    root.addEventListener(
      "click",
      function (ev) {
        var btn = ev.target.closest(".deck-chapter-group-toggle");
        if (!btn || !root.contains(btn)) return;
        ev.preventDefault();
        ev.stopPropagation();
        var group = btn.closest(".deck-chapter-group");
        if (!group || !root.contains(group)) return;
        var open = !group.classList.contains("is-expanded");
        setGroupExpanded(group, open);
        persistNavGroups(root);
      },
      false
    );
  }
})();
