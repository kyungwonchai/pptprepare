"""Slide routes — 발표용 한 장당 적당한 분량."""

from flask import Blueprint, abort, redirect, render_template, url_for

from app.data.tools import get_categories_for_slide, get_tool
from app.data.vibe_inspiration import LINK_GROUPS, PROCESS_NOTES
from app.data.vibe_stack import (
    KNOWHOW_PART1,
    KNOWHOW_PART2,
    VIBE_FLOW_STEPS,
    get_flow_block,
)
from app.data.slide_agent_features import AI_FEATURE_SLIDES
from app.data.slide_tool_tutorials import TOOL_TUTORIAL_SLIDES
from app.data.slide_vibe_playbook import VIBE_PLAYBOOK_SLIDES
from app.data.slide_agent_products import (
    AI_FOUR_OVERVIEW,
    ANTIGRAVITY_PAGE,
    CLAUDE_CODE_PAGE,
    CODEX_PAGE,
    CURSOR_PAGE,
)
from app.data.slide_api_vibe import API_VIBE_PAGE
from app.data.slide_free_apis import (
    API_BY_CATEGORY,
    ENTERPRISE_CLOUD_FREE,
    FREE_API_PAGE,
    TIER_LABELS,
)
from app.data.slide_tech import TECH_AGENT, TECH_PLAYWRIGHT, TECH_PYTHON_WHAT
from app.data.workflow_wlb import WORKFLOW_PART1, WORKFLOW_PART2

slides_bp = Blueprint("slides", __name__)


def _tool_tutorial_slide(tutorial_index: int):
    row = TOOL_TUTORIAL_SLIDES[tutorial_index]
    return render_template("slides/slide_tutorial_bubbles.html", **row)


def _vibe_playbook_slide(playbook_index: int):
    pb = VIBE_PLAYBOOK_SLIDES[playbook_index]
    return render_template(
        "slides/slide_knowhow.html",
        sections=pb["sections"],
        page_title=pb["page_title"],
        kicker=pb["kicker"],
    )


def _flow_slide(step_n: int):
    block = get_flow_block(step_n)
    if block is None:
        abort(404)
    return render_template("slides/tier_single.html", block=block)


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
    return _flow_slide(1)


@slides_bp.route("/6")
def slide_06():
    return _flow_slide(2)


@slides_bp.route("/7")
def slide_07():
    return _flow_slide(3)


@slides_bp.route("/8")
def slide_08():
    return _flow_slide(4)


@slides_bp.route("/9")
def slide_09():
    return _flow_slide(5)


@slides_bp.route("/10")
def slide_10():
    return _flow_slide(6)


@slides_bp.route("/11")
def slide_11():
    return render_template(
        "slides/slide_knowhow.html",
        sections=KNOWHOW_PART1,
        page_title="운영 노하우 (1/2)",
    )


@slides_bp.route("/12")
def slide_12():
    return render_template(
        "slides/slide_knowhow.html",
        sections=KNOWHOW_PART2,
        page_title="운영 노하우 (2/2)",
    )


@slides_bp.route("/13")
def slide_13():
    return render_template(
        "slides/slide_workflow.html",
        sections=WORKFLOW_PART1,
        page_title="본업 · 사내 제약 (1/2)",
    )


@slides_bp.route("/14")
def slide_14():
    return render_template(
        "slides/slide_workflow.html",
        sections=WORKFLOW_PART2,
        page_title="집–회사 · 워라벨 (2/2)",
    )


@slides_bp.route("/15")
def slide_15():
    return render_template(
        "slides/slide_inspiration.html",
        process_notes=PROCESS_NOTES,
        link_groups=LINK_GROUPS,
    )


@slides_bp.route("/16")
def slide_16():
    return render_template("slides/slide_technical.html", **TECH_AGENT)


@slides_bp.route("/17")
def slide_17():
    return render_template("slides/slide_technical.html", **TECH_PYTHON_WHAT)


@slides_bp.route("/18")
def slide_18():
    return render_template("slides/slide_technical.html", **TECH_PLAYWRIGHT)


@slides_bp.route("/19")
def slide_19():
    return render_template(
        "slides/slide_free_apis.html",
        **FREE_API_PAGE,
        categories=API_BY_CATEGORY,
        enterprise_blocks=ENTERPRISE_CLOUD_FREE,
        tier_labels=TIER_LABELS,
    )


@slides_bp.route("/20")
def slide_20():
    return render_template("slides/slide_technical.html", **API_VIBE_PAGE)


@slides_bp.route("/21")
def slide_21():
    return render_template("slides/slide_technical.html", **AI_FOUR_OVERVIEW)


@slides_bp.route("/22")
def slide_22():
    return render_template("slides/slide_technical.html", **ANTIGRAVITY_PAGE)


@slides_bp.route("/23")
def slide_23():
    return render_template("slides/slide_technical.html", **CLAUDE_CODE_PAGE)


@slides_bp.route("/24")
def slide_24():
    return render_template("slides/slide_technical.html", **CODEX_PAGE)


@slides_bp.route("/25")
def slide_25():
    return render_template("slides/slide_technical.html", **CURSOR_PAGE)


@slides_bp.route("/26")
def slide_26():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[0])


@slides_bp.route("/27")
def slide_27():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[1])


@slides_bp.route("/28")
def slide_28():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[2])


@slides_bp.route("/29")
def slide_29():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[3])


@slides_bp.route("/30")
def slide_30():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[4])


@slides_bp.route("/31")
def slide_31():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[5])


@slides_bp.route("/32")
def slide_32():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[6])


@slides_bp.route("/33")
def slide_33():
    return render_template("slides/slide_feature_plain.html", **AI_FEATURE_SLIDES[7])


@slides_bp.route("/34")
def slide_34():
    return _vibe_playbook_slide(0)


@slides_bp.route("/35")
def slide_35():
    return _vibe_playbook_slide(1)


@slides_bp.route("/36")
def slide_36():
    return _vibe_playbook_slide(2)


@slides_bp.route("/37")
def slide_37():
    return _vibe_playbook_slide(3)


@slides_bp.route("/38")
def slide_38():
    return _vibe_playbook_slide(4)


@slides_bp.route("/39")
def slide_39():
    return _vibe_playbook_slide(5)


@slides_bp.route("/40")
def slide_40():
    return _vibe_playbook_slide(6)


@slides_bp.route("/41")
def slide_41():
    return _vibe_playbook_slide(7)


@slides_bp.route("/42")
def slide_42():
    return _vibe_playbook_slide(8)


@slides_bp.route("/43")
def slide_43():
    return _vibe_playbook_slide(9)


@slides_bp.route("/44")
def slide_44():
    return _tool_tutorial_slide(0)


@slides_bp.route("/45")
def slide_45():
    return _tool_tutorial_slide(1)


@slides_bp.route("/46")
def slide_46():
    return _tool_tutorial_slide(2)


@slides_bp.route("/47")
def slide_47():
    return _tool_tutorial_slide(3)


@slides_bp.route("/48")
def slide_48():
    return _tool_tutorial_slide(4)


@slides_bp.route("/49")
def slide_49():
    return _tool_tutorial_slide(5)


@slides_bp.route("/50")
def slide_50():
    return _tool_tutorial_slide(6)


@slides_bp.route("/51")
def slide_51():
    return _tool_tutorial_slide(7)


@slides_bp.route("/52")
def slide_52():
    return _tool_tutorial_slide(8)


@slides_bp.route("/53")
def slide_53():
    return _tool_tutorial_slide(9)


@slides_bp.route("/54")
def slide_54():
    return _tool_tutorial_slide(10)


@slides_bp.route("/55")
def slide_55():
    return _tool_tutorial_slide(11)


# 예전 주소 호환: 23장 때 코덱스가 /23 이었음 → 지금은 /24
@slides_bp.route("/legacy-codex-23")
def legacy_codex_from_23():
    return redirect(url_for("slides.slide_24"), 301)


@slides_bp.route("/tool/<slug>")
def tool_detail(slug: str):
    tool = get_tool(slug)
    if tool is None:
        abort(404)
    return render_template("slides/tool_detail.html", tool=tool)
