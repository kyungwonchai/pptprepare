"""바이브 코딩 기준 핵심: 엑셀×Cline · Flask · API·웹 — 슬라이드 36~39 (4장).

이미지는 `image_url`로 공식·위키 등 웹 참조(HTTPS). 오프라인은 `image_path` 폴백.
"""

from __future__ import annotations

from typing import Any

# 참조 이미지(안정적인 HTTPS). 깨지면 static `image_path`로 교체 가능.
_WIKI_EXCEL = (
    "https://upload.wikimedia.org/wikipedia/commons/3/34/"
    "Microsoft_Office_Excel_%282019%E2%80%93present%29.svg"
)
_WIKI_FLASK = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg"
_FASTAPI_LOGO = "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
_WIKI_DOCKER = (
    "https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg"
)

EDU_CLINE_WEB_SLIDES: list[dict[str, Any]] = [
    {
        "series": "cline",
        "kicker": "바이브 코딩 · 엑셀",
        "page_title": "엑셀은 레포 안의 파일로",
        "lead": (
            "엑셀은 화면이 아니라 **프로젝트 폴더 안의 파일**입니다. 워크스페이스를 연 상태에서 "
            "경로·시트·출력 형식(예: CSV)을 **한 블록으로** 적고, Cline이 만든 스크립트를 터미널로 돌립니다. "
            "에러가 나면 메시지를 **통째로** 붙여 넣어 다시 묻습니다."
        ),
        "image_url": _WIKI_EXCEL,
        "image_path": "img/edu/excel_flow_overview.svg",
        "caption": "흐름: `data/*.xlsx` → 요구 정리 → 스크립트 → `python ...` 실행 → 결과·로그로 검증.",
        "bubbles": [
            {
                "text": "민감열·한글 경로는 요구에 미리 적거나, 가명 처리·raw 문자열을 시키면 사고가 줄어듭니다.",
                "align": "left",
            },
        ],
        "foot_note": (
            "이미지: Microsoft Excel 로고(위키미디어 커먼스). 강의에서는 본인 캡처로 바꿔도 됩니다."
        ),
    },
    {
        "series": "flask",
        "kicker": "바이브 코딩 · Flask",
        "page_title": "URL 한 바퀴 (페이지·정적파일)",
        "lead": (
            "**요청 URL → 파이썬 함수 → HTML 또는 JSON**이 Flask의 기본 그림입니다. "
            "`templates/`·`static/` 규칙만 지키면 경로가 단순하고, 교육·시험은 **한 파일 app.py**로 시작해도 됩니다."
        ),
        "image_url": _WIKI_FLASK,
        "image_path": "img/edu/flask_overview.svg",
        "caption": "`render_template` / `jsonify` · GET/POST. 폼·CSRF·엑셀 업로드는 필요해질 때 단계적으로.",
        "bubbles": [
            {
                "text": "`url_for('static', filename='…')` 로 CSS·JS 경로를 이름으로 묶어 두면 리팩터가 쉽습니다.",
                "align": "right",
            },
        ],
        "foot_note": "이미지: Flask 로고(위키미디어 커먼스).",
    },
    {
        "series": "stack",
        "kicker": "바이브 코딩 · API·웹",
        "page_title": "FastAPI = JSON API + /docs",
        "lead": (
            "역할은 **프론트(화면) ↔ API(규칙·검증) ↔ DB(저장)** 세 덩어리로 나누면 설명이 빨라집니다. "
            "FastAPI는 **JSON API**와 자동 **`/docs`** 로 시험 호출하기 좋습니다. 프론트·API 도메인이 다르면 **CORS**만 기억해 두면 됩니다."
        ),
        "image_url": _FASTAPI_LOGO,
        "image_path": "img/edu/fastapi_role.svg",
        "caption": "ORM·뷰·저장 프로시저·마이그레이션은 팀 DB·제품 표준에 맡기고, 여기서는 역할 구분만.",
        "bubbles": [
            {
                "text": "로컬에서 `/docs` 만으로도 ‘API가 있다’는 설득이 큽니다.",
                "align": "left",
            },
        ],
        "foot_note": "이미지: FastAPI 공식 사이트 로고(tiangolo.com).",
    },
    {
        "series": "stack",
        "kicker": "바이브 코딩 · 정리",
        "page_title": "배치 vs 웹 — 언제 Flask·FastAPI?",
        "lead": (
            "**엑셀 반복·배치**는 스크립트+Cline으로 끝낼 수 있고, **브라우저에 올릴 업로드·화면**이 필요해지면 그때 Flask/FastAPI로 확장합니다. "
            "**Flask**는 페이지·Jinja 중심, **FastAPI**는 API·SPA·다른 클라이언트와 붙일 때 자주 고릅니다. "
            "배포는 컨테이너·환경 변수·역프록시 **개념만** 잡아 두면 충분합니다."
        ),
        "image_url": _WIKI_DOCKER,
        "image_path": "img/edu/web_deploy.svg",
        "caption": "DB: 테이블·뷰·저장 프로시저는 ‘저장·조회 단위’만 구분. 실무는 팀 표준을 따릅니다.",
        "bubbles": [
            {
                "text": "엑셀만 다루는 내부 배치와, 외부에 노출하는 웹은 요구·보안·운영이 다릅니다.",
                "align": "right",
            },
        ],
        "foot_note": "이미지: Docker 로고(위키미디어 커먼스). 배포 세부는 인프라 과정에서 연결.",
    },
]
