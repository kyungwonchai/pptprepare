"""전체 슬라이드 챕터 목록 — 내비·총 장수·좌측 트리 그룹."""

from __future__ import annotations

from typing import Any

# 새 슬라이드 추가 시 여기와 slides.py 라우트를 함께 수정합니다.

SLIDE_NAV_GROUPS: list[dict[str, Any]] = [
    {
        "id": "intro",
        "label": "도입·도구",
        "chapters": [
            {"n": 1, "endpoint": "slides.slide_01", "title": "표지"},
            {"n": 2, "endpoint": "slides.slide_02", "title": "분류별 역할"},
            {"n": 3, "endpoint": "slides.slide_03", "title": "생태계 관계도"},
            {"n": 4, "endpoint": "slides.slide_04", "title": "목적별 유형 개요"},
        ],
    },
    {
        "id": "ops",
        "label": "운영·워크플로·영감",
        "chapters": [
            {"n": 5, "endpoint": "slides.slide_05", "title": "운영 노하우 (1/2)"},
            {"n": 6, "endpoint": "slides.slide_06", "title": "운영 노하우 (2/2)"},
        ],
    },
    {
        "id": "tech",
        "label": "기술·연결·에이전트",
        "chapters": [
            {"n": 7, "endpoint": "slides.slide_07", "title": "AI 에이전트"},
            {"n": 8, "endpoint": "slides.slide_08", "title": "파이썬으로 할 수 있는 것"},
            {"n": 9, "endpoint": "slides.slide_09", "title": "브라우저 자동화"},
            {"n": 10, "endpoint": "slides.slide_10", "title": "무료 연결 목록"},
            {"n": 11, "endpoint": "slides.slide_11", "title": "외부 연결 노하우"},
            {"n": 12, "endpoint": "slides.slide_12", "title": "3대장 AI + Cursor"},
        ],
    },
    {
        "id": "features",
        "label": "공통 기능 (편집기)",
        "chapters": [
            {"n": 13, "endpoint": "slides.slide_13", "title": "맥락 주기"},
            {"n": 14, "endpoint": "slides.slide_14", "title": "에이전트"},
            {"n": 15, "endpoint": "slides.slide_15", "title": "말 vs 한 덩어리 고치기"},
            {"n": 16, "endpoint": "slides.slide_16", "title": "검은 창·CLI"},
            {"n": 17, "endpoint": "slides.slide_17", "title": "바깥 연결·MCP"},
            {"n": 18, "endpoint": "slides.slide_18", "title": "팀 규칙·룰"},
            {"n": 19, "endpoint": "slides.slide_19", "title": "안전·승인"},
            {"n": 20, "endpoint": "slides.slide_20", "title": "변경 확인·적용"},
        ],
    },
    {
        "id": "outlook",
        "label": "전망",
        "chapters": [
            {"n": 21, "endpoint": "slides.slide_21", "title": "전망 · 지금 수준"},
            {"n": 22, "endpoint": "slides.slide_22", "title": "로봇과의 관계"},
            {"n": 23, "endpoint": "slides.slide_23", "title": "미래에 중요한 지식"},
            {"n": 24, "endpoint": "slides.slide_24", "title": "대체·자원·시간"},
            {"n": 25, "endpoint": "slides.slide_25", "title": "개인 업무 효율"},
        ],
    },
    {
        "id": "cline",
        "label": "Cline 실습",
        "chapters": [
            {"n": 26, "endpoint": "slides.slide_26", "title": "Cline 설치·활성화"},
            {"n": 27, "endpoint": "slides.slide_27", "title": "모델·API 키·비용"},
            {"n": 28, "endpoint": "slides.slide_28", "title": "작업 폴더 열기"},
            {"n": 29, "endpoint": "slides.slide_29", "title": "계획과 실행"},
            {"n": 30, "endpoint": "slides.slide_30", "title": "요청 문장 쓰기"},
            {"n": 31, "endpoint": "slides.slide_31", "title": "골뱅이 맥락·제외"},
            {"n": 32, "endpoint": "slides.slide_32", "title": "변경 내용 검토·적용"},
            {"n": 33, "endpoint": "slides.slide_33", "title": "터미널·명령"},
            {"n": 34, "endpoint": "slides.slide_34", "title": "오류·재시도"},
            {"n": 35, "endpoint": "slides.slide_35", "title": "커밋·병합 요청"},
        ],
    },
    {
        "id": "web",
        "label": "엑셀·Flask·웹 (핵심)",
        "chapters": [
            {"n": 36, "endpoint": "slides.slide_36", "title": "엑셀은 레포 안의 파일로"},
            {"n": 37, "endpoint": "slides.slide_37", "title": "Flask URL 한 바퀴"},
            {"n": 38, "endpoint": "slides.slide_38", "title": "FastAPI·API·웹"},
            {"n": 39, "endpoint": "slides.slide_39", "title": "배치 vs 웹 · 정리"},
        ],
    },
]

SLIDE_CHAPTERS: list[dict[str, str | int]] = [
    ch for g in SLIDE_NAV_GROUPS for ch in g["chapters"]
]

TOTAL_SLIDES: int = len(SLIDE_CHAPTERS)

ENDPOINT_TO_SLIDE_NUM: dict[str, int] = {str(c["endpoint"]): int(c["n"]) for c in SLIDE_CHAPTERS}
