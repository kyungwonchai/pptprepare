"""실습 캡처 + 말풍선 데모 — Cursor · Cline · Gemini (슬라이드 44~55).

이미지는 저장소에 포함된 SVG 목업입니다. 실제 화면으로 바꾸려면 static/img/tutorials/ 에
같은 이름의 PNG 등을 두고 image_path 확장자만 조정하면 됩니다.
"""

from __future__ import annotations

from typing import Any

TOOL_TUTORIAL_SLIDES: list[dict[str, Any]] = [
    # —— Cursor ——
    {
        "series": "cursor",
        "kicker": "실습 데모 · Cursor",
        "page_title": "① 워크스페이스로 폴더 열기",
        "lead": "레포 루트를 연 상태가 기본입니다. 파일 트리가 보여야 맥락이 안정됩니다.",
        "image_path": "img/tutorials/cursor_01.svg",
        "caption": "File → Open Folder(또는 드래그)로 프로젝트 루트를 엽니다.",
        "bubbles": [
            {
                "text": "빈 폴더가 아니라, package.json·README가 있는 「최상위」를 여는 게 좋습니다.",
                "top": 8,
                "left": 52,
                "w": 44,
                "align": "right",
            },
            {
                "text": "처음이면 터미널에서 `git status`로 깨끗한지 한 번만 확인해 두면 이후가 편합니다.",
                "top": 58,
                "left": 6,
                "w": 40,
                "align": "left",
            },
        ],
        "foot_note": (
            "이 장부터 이미지는 「강의용 목업」입니다. 본인 PC 캡처로 바꾸려면 `static/img/tutorials/`에 "
            "같은 파일명의 PNG를 넣고 `slide_tool_tutorials.py`의 해당 `image_path`만 바꾸면 됩니다."
        ),
    },
    {
        "series": "cursor",
        "kicker": "실습 데모 · Cursor",
        "page_title": "② 채팅에 @로 파일 붙이기",
        "lead": "말만 하지 말고, ‘이 파일 봐’라고 「참조」를 걸면 답이 좁아집니다.",
        "image_path": "img/tutorials/cursor_02.svg",
        "caption": "채팅 입력창에서 @ 파일명 또는 @폴더로 맥락을 붙입니다.",
        "bubbles": [
            {
                "text": "에러가 난 파일만 @ 하면, 불필요한 다른 코드 설명이 줄어듭니다.",
                "top": 12,
                "left": 4,
                "w": 38,
                "align": "left",
            },
            {
                "text": "답이 길면 ‘한 파일만 고쳐’ ‘diff만’처럼 「출력 형식」을 한 줄 덧붙입니다.",
                "top": 42,
                "left": 48,
                "w": 48,
                "align": "right",
            },
        ],
    },
    {
        "series": "cursor",
        "kicker": "실습 데모 · Cursor",
        "page_title": "③ 인라인 · 컴포저로 국소 수정",
        "lead": "채팅이 아니라 「보이는 코드」를 직접 가리킬 때 씁니다.",
        "image_path": "img/tutorials/cursor_03.svg",
        "caption": "블록을 드래그한 뒤 인라인(또는 Composer)으로 ‘이 부분만’ 요청합니다.",
        "bubbles": [
            {
                "text": "단축키는 제품 버전마다 다릅니다. 메뉴에 ‘Inline’ ‘Composer’로 찾아보세요.",
                "top": 10,
                "left": 50,
                "w": 46,
                "align": "right",
            },
            {
                "text": "한 함수·한 문단 단위로 잘라서 부탁하면 되돌리기도 쉽습니다.",
                "top": 62,
                "left": 8,
                "w": 42,
                "align": "left",
            },
        ],
    },
    {
        "series": "cursor",
        "kicker": "실습 데모 · Cursor",
        "page_title": "④ 터미널에서 빌드·실행 확인",
        "lead": "고친 뒤 「같은 화면에서」 돌려 보는 습관이 오류를 줄입니다.",
        "image_path": "img/tutorials/cursor_04.svg",
        "caption": "하단 터미널 패널을 열고 npm/pnpm 등 팀이 쓰는 명령을 실행합니다.",
        "bubbles": [
            {
                "text": "빨간 로그가 나오면 「그 블록을 복사」해 채팅에 붙이면 다음 지시가 정확해집니다.",
                "top": 18,
                "left": 48,
                "w": 48,
                "align": "right",
            },
        ],
    },
    # —— Cline ——
    {
        "series": "cline",
        "kicker": "실습 데모 · Cline",
        "page_title": "① VS Code에 Cline 설치",
        "lead": "확장(Extensions)에서 설치하고, 사이드바에 아이콘이 뜨는지 확인합니다.",
        "image_path": "img/tutorials/cline_01.svg",
        "caption": "마켓플레이스에서 Cline을 검색 → Install.",
        "bubbles": [
            {
                "text": "회사 PC면 「마켓플레이스 허용」 여부를 먼저 확인하세요.",
                "top": 14,
                "left": 48,
                "w": 46,
                "align": "right",
            },
            {
                "text": "설치 후 「API 키·모델」 연결은 팀 정책에 맞게만.",
                "top": 55,
                "left": 6,
                "w": 42,
                "align": "left",
            },
        ],
    },
    {
        "series": "cline",
        "kicker": "실습 데모 · Cline",
        "page_title": "② 작업 지시 입력 (Plan / Act)",
        "lead": "한 번에 크게 맡기기 전에, 「무엇을 하면 성공인지」 한 문장을 적습니다.",
        "image_path": "img/tutorials/cline_02.svg",
        "caption": "Cline 패널에 목표·제약을 적습니다. (버전에 따라 Plan/Act 표기가 다를 수 있음)",
        "bubbles": [
            {
                "text": "‘전부 리팩터’보다 ‘이 API만 분리’처럼 「범위」를 좁힐수록 안전합니다.",
                "top": 8,
                "left": 4,
                "w": 44,
                "align": "left",
            },
            {
                "text": "레포가 열려 있어야 파일 읽기·쓰기가 이어집니다.",
                "top": 48,
                "left": 46,
                "w": 48,
                "align": "right",
            },
        ],
    },
    {
        "series": "cline",
        "kicker": "실습 데모 · Cline",
        "page_title": "③ diff 확인 후 승인",
        "lead": "자동으로 고쳐도 「사람이 눈으로」 한 번은 봅니다.",
        "image_path": "img/tutorials/cline_03.svg",
        "caption": "제안된 변경을 Accept/Reject — 민감 파일은 더 신중히.",
        "bubbles": [
            {
                "text": "삭제·권한·환경 변수 줄이 「빨간 줄」이면 특히 천천히 읽습니다.",
                "top": 12,
                "left": 50,
                "w": 46,
                "align": "right",
            },
        ],
    },
    {
        "series": "cline",
        "kicker": "실습 데모 · Cline",
        "page_title": "④ 터미널 로그로 디버깅",
        "lead": "실패한 명령 출력은 「그대로 복사」해 질문에 넣으면 됩니다.",
        "image_path": "img/tutorials/cline_04.svg",
        "caption": "터미널에 나온 에러 전체를 붙이고 ‘원인만 짧게’라고 해도 좋습니다.",
        "bubbles": [
            {
                "text": "‘안 돼요’만 말하지 말고, 「명령 + 로그 앞부분」까지 같이.",
                "top": 20,
                "left": 6,
                "w": 44,
                "align": "left",
            },
        ],
    },
    # —— Gemini ——
    {
        "series": "gemini",
        "kicker": "실습 데모 · Gemini",
        "page_title": "① 질문을 한 번에 구체적으로",
        "lead": "Gemini(웹/앱)는 「목적·제약·톤」을 같이 적을수록 초안이 좋아집니다.",
        "image_path": "img/tutorials/gemini_01.svg",
        "caption": "예: ‘누구에게 / 몇 분 분량 / 금지어 / 말투’를 한 블록에.",
        "bubbles": [
            {
                "text": "민감한 회사 정보는 「가짜 수치」로 바꿔 먼저 문장 구조만 잡아도 됩니다.",
                "top": 10,
                "left": 48,
                "w": 48,
                "align": "right",
            },
        ],
    },
    {
        "series": "gemini",
        "kicker": "실습 데모 · Gemini",
        "page_title": "② 모델 · AI Studio",
        "lead": "빠른 응답이 필요하면 Flash 계열, 깊은 추론이 필요하면 Pro 계열을 고릅니다.",
        "image_path": "img/tutorials/gemini_02.svg",
        "caption": "Google AI Studio는 API·프로토타입용 — 키는 절대 슬라이드·Git에 넣지 않기.",
        "bubbles": [
            {
                "text": "제품 화면은 업데이트될 수 있어, 「공식 문서의 모델 이름」을 기준으로 삼으세요.",
                "top": 14,
                "left": 4,
                "w": 44,
                "align": "left",
            },
            {
                "text": "Studio에서 만든 프롬프트는 나중에 「팀 룰」로 옮기기 좋습니다.",
                "top": 52,
                "left": 46,
                "w": 48,
                "align": "right",
            },
        ],
    },
    {
        "series": "gemini",
        "kicker": "실습 데모 · Gemini",
        "page_title": "③ 이미지·캡처로 물어보기",
        "lead": "UI 버그·표 디자인은 「말보다 스크린샷」이 빠른 경우가 많습니다.",
        "image_path": "img/tutorials/gemini_03.svg",
        "caption": "캡처를 넣고 ‘이 부분만’ ‘기대한 동작’을 적습니다.",
        "bubbles": [
            {
                "text": "개인정보·주소창은 「가리고」 올리기.",
                "top": 8,
                "left": 50,
                "w": 44,
                "align": "right",
            },
        ],
    },
    {
        "series": "gemini",
        "kicker": "실습 데모 · Gemini",
        "page_title": "④ Google 워크스페이스와 함께",
        "lead": "Gmail·Docs·Drive 등과 묶인 기능은 「계정·지역·요금제」에 따라 다릅니다.",
        "image_path": "img/tutorials/gemini_04.svg",
        "caption": "메일 초안·문서 요약 등 — 회사 정책 허용 범위 안에서만.",
        "bubbles": [
            {
                "text": "외부로 나가는 메일은 「자동 발송 전」에 사람이 꼭 읽기.",
                "top": 22,
                "left": 6,
                "w": 46,
                "align": "left",
            },
            {
                "text": "‘검색 연동’이 켜져 있으면 「어디까지 인용되는지」 UI를 확인하세요.",
                "top": 58,
                "left": 44,
                "w": 50,
                "align": "right",
            },
        ],
    },
]
