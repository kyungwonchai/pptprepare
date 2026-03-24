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
            {"n": 2, "endpoint": "slides.slide_02", "title": "도구 역할 한눈에"},
            {"n": 3, "endpoint": "slides.slide_03", "title": "도구 연결 흐름"},
            {"n": 4, "endpoint": "slides.slide_04", "title": "무엇부터 만들지"},
        ],
    },
    {
        "id": "ops",
        "label": "운영·워크플로·영감",
        "chapters": [
            {"n": 5, "endpoint": "slides.slide_05", "title": "운영 순서 (핵심)"},
            {"n": 6, "endpoint": "slides.slide_06", "title": "운영 체크리스트"},
        ],
    },
    {
        "id": "tech",
        "label": "기술·연결·에이전트",
        "chapters": [
            {"n": 7, "endpoint": "slides.slide_07", "title": "AI 에이전트란"},
            {"n": 8, "endpoint": "slides.slide_08", "title": "파이썬 실전 범위"},
            {"n": 9, "endpoint": "slides.slide_09", "title": "브라우저 자동화 핵심"},
            {"n": 10, "endpoint": "slides.slide_10", "title": "무료 API 찾는 법"},
            {"n": 11, "endpoint": "slides.slide_11", "title": "외부 API 붙이는 6원칙"},
            {"n": 12, "endpoint": "slides.slide_12", "title": "도구 4종 비교"},
        ],
    },
    {
        "id": "features",
        "label": "공통 기능 (편집기)",
        "chapters": [
            {"n": 13, "endpoint": "slides.slide_13", "title": "맥락 넣는 법"},
            {"n": 14, "endpoint": "slides.slide_14", "title": "에이전트"},
            {"n": 15, "endpoint": "slides.slide_15", "title": "채팅 vs 파일수정"},
            {"n": 16, "endpoint": "slides.slide_16", "title": "터미널 기본"},
            {"n": 17, "endpoint": "slides.slide_17", "title": "외부도구 연결"},
            {"n": 18, "endpoint": "slides.slide_18", "title": "팀 규칙 고정"},
            {"n": 19, "endpoint": "slides.slide_19", "title": "승인·안전"},
            {"n": 20, "endpoint": "slides.slide_20", "title": "변경 검토·적용"},
        ],
    },
    {
        "id": "home_web",
        "label": "집 서버 · 웹 운영",
        "chapters": [
            {"n": 21, "endpoint": "slides.slide_21", "title": "브레인스토밍 AI 역할"},
            {"n": 22, "endpoint": "slides.slide_22", "title": "쇼핑몰 운영 흐름도"},
            {"n": 23, "endpoint": "slides.slide_23", "title": "쇼핑몰 화면 예시"},
            {"n": 24, "endpoint": "slides.slide_24", "title": "쇼핑몰 관리 예시"},
            {"n": 25, "endpoint": "slides.slide_25", "title": "쇼핑몰 자동화 예시"},
        ],
    },
    {
        "id": "cline",
        "label": "Cline 실습",
        "chapters": [
            {"n": 26, "endpoint": "slides.slide_26", "title": "설치 시작"},
            {"n": 27, "endpoint": "slides.slide_27", "title": "모델·비용"},
            {"n": 28, "endpoint": "slides.slide_28", "title": "작업 폴더"},
            {"n": 29, "endpoint": "slides.slide_29", "title": "계획→실행"},
            {"n": 30, "endpoint": "slides.slide_30", "title": "요청 잘 쓰기"},
            {"n": 31, "endpoint": "slides.slide_31", "title": "맥락 지정·제외"},
            {"n": 32, "endpoint": "slides.slide_32", "title": "변경 검토"},
            {"n": 33, "endpoint": "slides.slide_33", "title": "명령 실행"},
            {"n": 34, "endpoint": "slides.slide_34", "title": "오류 대응"},
            {"n": 35, "endpoint": "slides.slide_35", "title": "커밋·PR"},
        ],
    },
]

SLIDE_CHAPTERS: list[dict[str, str | int]] = [
    ch for g in SLIDE_NAV_GROUPS for ch in g["chapters"]
]

TOTAL_SLIDES: int = len(SLIDE_CHAPTERS)

ENDPOINT_TO_SLIDE_NUM: dict[str, int] = {str(c["endpoint"]): int(c["n"]) for c in SLIDE_CHAPTERS}
