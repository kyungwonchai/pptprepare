"""Slide routes — 발표용 한 장당 적당한 분량."""

import io
import os
import re
from datetime import datetime

from flask import Blueprint, abort, jsonify, redirect, render_template, request, send_file, url_for

from app.data.tools import get_categories_for_slide, get_tool
from app.data.vibe_stack import (
    KNOWHOW_PART1,
    KNOWHOW_PART2,
    VIBE_FLOW_STEPS,
)
from app.data.slide_agent_features import AI_FEATURE_SLIDES
from app.data.slide_edu_cline_web import EDU_CLINE_WEB_SLIDES
from app.data.slide_tool_tutorials import TOOL_TUTORIAL_SLIDES
from app.data.slide_vibe_playbook import VIBE_PLAYBOOK_SLIDES
from app.data.slide_agent_products import AI_FOUR_OVERVIEW
from app.data.slide_api_vibe import API_VIBE_PAGE
from app.data.slide_free_apis import (
    API_BY_CATEGORY,
    ENTERPRISE_CLOUD_FREE,
    FREE_API_PAGE,
    TIER_LABELS,
)
from app.data.slide_tech import TECH_AGENT, TECH_PLAYWRIGHT, TECH_PYTHON_WHAT
from app.data.slide_chapters import TOTAL_SLIDES
from app.export_render import build_pdf_from_images, build_pptx_from_images, capture_slide_frames

slides_bp = Blueprint("slides", __name__)


def _playwright_base_url() -> str:
    """Playwright가 같은 기기에서 앱에 접속할 URL. 테스트 클라이언트의 포트 없는 localhost 보정."""
    root = request.url_root
    if re.match(r"^https?://localhost/?$", root) or root in ("http://localhost/", "http://localhost"):
        port = os.environ.get("FLASK_RUN_PORT", "54321")
        return f"http://127.0.0.1:{port}/"
    return root


def _tool_tutorial_slide(tutorial_index: int):
    row = TOOL_TUTORIAL_SLIDES[tutorial_index]
    return render_template("slides/slide_tutorial_bubbles.html", **row)


def _edu_cline_web_slide(index: int):
    row = EDU_CLINE_WEB_SLIDES[index]
    return render_template("slides/slide_tutorial_bubbles.html", **row)


def _vibe_playbook_slide(playbook_index: int):
    pb = VIBE_PLAYBOOK_SLIDES[playbook_index]
    return render_template(
        "slides/slide_knowhow.html",
        sections=pb["sections"],
        page_title=pb["page_title"],
        kicker=pb["kicker"],
    )


@slides_bp.route("/")
def slide_01():
    return render_template("slides/slide_01.html")


@slides_bp.route("/2")
def slide_02():
    return render_template("slides/slide_02.html", categories=get_categories_for_slide())


@slides_bp.route("/3")
def slide_03():
    return render_template("slides/slide_03.html")


@slides_bp.route("/4")
def slide_04():
    return render_template("slides/slide_04.html", flow_steps=VIBE_FLOW_STEPS)


@slides_bp.route("/5")
def slide_05():
    return render_template(
        "slides/slide_knowhow.html",
        sections=KNOWHOW_PART1,
        page_title="운영 노하우 (1/2)",
    )


@slides_bp.route("/6")
def slide_06():
    return render_template(
        "slides/slide_knowhow.html",
        sections=KNOWHOW_PART2,
        page_title="운영 노하우 (2/2)",
    )


@slides_bp.route("/7")
def slide_07():
    return render_template("slides/slide_technical.html", **TECH_AGENT)


@slides_bp.route("/8")
def slide_08():
    return render_template("slides/slide_technical.html", **TECH_PYTHON_WHAT)


@slides_bp.route("/9")
def slide_09():
    return render_template("slides/slide_technical.html", **TECH_PLAYWRIGHT)


@slides_bp.route("/10")
def slide_10():
    return render_template(
        "slides/slide_free_apis.html",
        **FREE_API_PAGE,
        categories=API_BY_CATEGORY,
        enterprise_blocks=ENTERPRISE_CLOUD_FREE,
        tier_labels=TIER_LABELS,
    )


@slides_bp.route("/11")
def slide_11():
    return render_template("slides/slide_technical.html", **API_VIBE_PAGE)


@slides_bp.route("/12")
def slide_12():
    return render_template("slides/slide_technical.html", **AI_FOUR_OVERVIEW)


@slides_bp.route("/13")
def slide_13():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[0])


@slides_bp.route("/14")
def slide_14():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[1])


@slides_bp.route("/15")
def slide_15():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[2])


@slides_bp.route("/16")
def slide_16():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[3])


@slides_bp.route("/17")
def slide_17():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[4])


@slides_bp.route("/18")
def slide_18():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[5])


@slides_bp.route("/19")
def slide_19():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[6])


@slides_bp.route("/20")
def slide_20():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[7])


@slides_bp.route("/21")
def slide_21():
    return _vibe_playbook_slide(0)


@slides_bp.route("/22")
def slide_22():
    return _vibe_playbook_slide(1)


@slides_bp.route("/23")
def slide_23():
    return _vibe_playbook_slide(2)


@slides_bp.route("/24")
def slide_24():
    return _vibe_playbook_slide(3)


@slides_bp.route("/25")
def slide_25():
    return _vibe_playbook_slide(4)


@slides_bp.route("/26")
def slide_26():
    return _tool_tutorial_slide(0)


@slides_bp.route("/27")
def slide_27():
    return _tool_tutorial_slide(1)


@slides_bp.route("/28")
def slide_28():
    return _tool_tutorial_slide(2)


@slides_bp.route("/29")
def slide_29():
    return _tool_tutorial_slide(3)


@slides_bp.route("/30")
def slide_30():
    return _tool_tutorial_slide(4)


@slides_bp.route("/31")
def slide_31():
    return _tool_tutorial_slide(5)


@slides_bp.route("/32")
def slide_32():
    return _tool_tutorial_slide(6)


@slides_bp.route("/33")
def slide_33():
    return _tool_tutorial_slide(7)


@slides_bp.route("/34")
def slide_34():
    return _tool_tutorial_slide(8)


@slides_bp.route("/35")
def slide_35():
    return _tool_tutorial_slide(9)


@slides_bp.route("/36")
def slide_36():
    return _edu_cline_web_slide(0)


@slides_bp.route("/37")
def slide_37():
    return _edu_cline_web_slide(1)


@slides_bp.route("/38")
def slide_38():
    return _edu_cline_web_slide(2)


@slides_bp.route("/39")
def slide_39():
    return _edu_cline_web_slide(3)


# 예전 주소 호환
@slides_bp.route("/legacy-codex-23")
def legacy_codex_from_23():
    return redirect(url_for("slides.slide_12"), 301)


@slides_bp.post("/export/download")
def export_download():
    """선택 슬라이드를 PDF 또는 PPTX로 내보냅니다(Playwright 화면 캡처)."""
    data = request.get_json(silent=True) or {}
    raw_nums = data.get("slides") or []
    fmt = (data.get("format") or "pdf").lower().strip()
    theme = (data.get("theme") or "dark").lower().strip()

    if not isinstance(raw_nums, list) or not raw_nums:
        return jsonify({"error": "내보낼 슬라이드 번호를 하나 이상 선택하세요."}), 400

    nums: list[int] = []
    for x in raw_nums:
        try:
            n = int(x)
        except (TypeError, ValueError):
            return jsonify({"error": f"잘못된 슬라이드 번호: {x!r}"}), 400
        if n < 1 or n > TOTAL_SLIDES:
            return jsonify({"error": f"범위 밖 번호: {n} (1~{TOTAL_SLIDES})"}), 400
        nums.append(n)

    nums = sorted(set(nums))
    if fmt not in ("pdf", "pptx"):
        return jsonify({"error": "format은 pdf 또는 pptx만 가능합니다."}), 400
    if theme not in ("dark", "light"):
        theme = "dark"

    base_url = _playwright_base_url()
    try:
        images = capture_slide_frames(base_url, nums, theme)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 503
    except Exception as e:
        return jsonify({"error": f"캡처 실패: {e!s}"}), 500

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    if fmt == "pdf":
        try:
            pdf_bytes = build_pdf_from_images(images)
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 503
        except Exception as e:
            return jsonify({"error": f"PDF 생성 실패: {e!s}"}), 500
        buf = io.BytesIO(pdf_bytes)
        buf.seek(0)
        return send_file(
            buf,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=f"slides-{ts}.pdf",
        )

    try:
        pptx_bytes = build_pptx_from_images(images)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 503
    except Exception as e:
        return jsonify({"error": f"PPTX 생성 실패: {e!s}"}), 500
    buf = io.BytesIO(pptx_bytes)
    buf.seek(0)
    return send_file(
        buf,
        mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        as_attachment=True,
        download_name=f"slides-{ts}.pptx",
    )


@slides_bp.route("/tool/<slug>")
def tool_detail(slug: str):
    tool = get_tool(slug)
    if tool is None:
        abort(404)
    return render_template("slides/tool_detail.html", tool=tool)
