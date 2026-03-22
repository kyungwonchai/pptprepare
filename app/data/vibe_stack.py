"""바이브 코딩 — 제작물의 목적에 따른 유형·운영 노하우 (슬라이드용 짧은 문장)."""

from __future__ import annotations

from typing import Any

VIBE_FLOW_STEPS: list[dict[str, Any]] = [
    {
        "n": 1,
        "label": "이해 · 설치 허브",
        "one_liner": "개념·설치 순서를 한 페이지에. 여기가 흔들리면 전부 흔들립니다.",
        "links": [
            {"label": "MDN", "url": "https://developer.mozilla.org/ko/"},
            {"label": "Google Developers", "url": "https://developers.google.com/"},
        ],
    },
    {
        "n": 2,
        "label": "스크립트 · 패턴 · Cline",
        "one_liner": "룰·패턴을 모아 두고 Cline을 붙이면 레포 안 구현 자유도가 크게 열립니다.",
        "links": [
            {"label": "Cursor Rules", "url": "https://docs.cursor.com/context/rules-for-ai"},
            {"label": "Cline", "url": "https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev"},
        ],
    },
    {
        "n": 3,
        "label": "사내 AI 모아 두기",
        "one_liner": "허용된 인공지능을 한곳에. 용도별로 나누면 질문이 섞이지 않습니다.",
        "links": [
            {"label": "질문 예시 모음 (Claude)", "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"},
        ],
    },
    {
        "n": 4,
        "label": "모니터링 · Git",
        "one_liner": "Playwright로 핵심 화면 스냅샷. GitHub와 PR·브랜치를 이어 붙입니다.",
        "links": [
            {"label": "Playwright", "url": "https://playwright.dev"},
            {"label": "GitHub", "url": "https://docs.github.com"},
        ],
    },
    {
        "n": 5,
        "label": "업무 → 우선순위 메일",
        "one_liner": "할 일을 정해진 형식으로 넣으면 우선순위·다음 액션이 메일로 정리됩니다.",
        "links": [
            {"label": "GTD", "url": "https://gettingthingsdone.com/what-is-gtd/"},
        ],
    },
    {
        "n": 6,
        "label": "메모 · 검색",
        "one_liner": "메모를 태그·검색으로 바로 찾는 두 번째 뇌.",
        "links": [
            {"label": "PARA", "url": "https://fortelabs.com/blog/para/"},
        ],
    },
]

FLOW_DETAIL_BLOCKS: list[dict[str, Any]] = [
    {
        "n": 1,
        "title": "목적 유형 1 — 이해 · 설치 허브",
        "role": "팀 기준·설치 경로를 한곳에 모읍니다. 링크가 흩어지면 매번 검색하게 됩니다.",
        "cultivate": [
            "설치는 체크리스트만 유지하고, 본문은 한 줄 요약.",
            "‘바이브 코딩’ 범위(자동화·리뷰)를 문서 한 블록에 고정.",
            "자주 쓰는 공식 문서는 허브 표에 제목·용도만 붙입니다.",
        ],
        "links": [
            {"label": "MDN", "url": "https://developer.mozilla.org/ko/"},
            {"label": "Google Developers", "url": "https://developers.google.com/"},
        ],
    },
    {
        "n": 2,
        "title": "목적 유형 2 — 패턴 · Cline",
        "role": "Cline을 켜면 레포·터미널·파일이 한 흐름으로 묶여 구현 자유도가 사실상 풀에 가깝게 열립니다. 무엇을 먼저 만들지·목적 유형을 적용하는 순서는 사람마다 다릅니다. 공통은 룰·패턴만 맞춥니다.",
        "cultivate": [
            "아이디어·우선순위는 개인별로. 목적 유형 5·6과 짝 지어 ‘오늘 방향’만 짧게.",
            "상황 태그(코드 정리·점검·보안) + 금지/권장 한 줄.",
            "팀 룰 파일명은 Cursor·Cline과 동기화.",
        ],
        "links": [
            {"label": "Cursor Rules", "url": "https://docs.cursor.com/context/rules-for-ai"},
            {"label": "Cline", "url": "https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev"},
        ],
    },
    {
        "n": 3,
        "title": "목적 유형 3 — 사내 인공지능",
        "role": "용도별로 나누면 코드 질문과 규정 질문이 섞이지 않습니다. 어떤 것을 중심에 둘지는 역할에 맞게 조합합니다.",
        "cultivate": [
            "첫 화면에 ‘이 화면의 용도’ 한 문장 고정.",
            "로그 보존·가리기는 보안 숫자 그대로 문서에.",
            "같은 질문은 미리 만든 질문 틀로 반복.",
        ],
        "links": [
            {"label": "질문 예시 (Claude)", "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"},
        ],
    },
    {
        "n": 4,
        "title": "목적 유형 4 — Playwright · GitHub",
        "role": "배포 상태를 스냅샷으로 남기고 PR·브랜치와 이어 붙입니다.",
        "cultivate": [
            "시나리오는 핵심 사용자 여정만. 실패 시 스크린샷·트레이스.",
            "이슈 템플릿·라벨·보호 브랜치를 미리.",
            "로컬·스테이징·운영 URL을 표로.",
        ],
        "links": [
            {"label": "Playwright", "url": "https://playwright.dev"},
            {"label": "GitHub Actions", "url": "https://docs.github.com/actions"},
        ],
    },
    {
        "n": 5,
        "title": "목적 유형 5 — 업무 · 우선순위 메일",
        "role": "입력 형식을 고정해야 인공지능이 만든 순위도 흔들리지 않습니다.",
        "cultivate": [
            "매일/매주 같은 시각에 덤프 (시간 박스와 짝).",
            "메일 제목 접두어·수신자 규칙 고정.",
            "자동 순위는 사람이 한 번 더 확인.",
        ],
        "links": [
            {"label": "GTD", "url": "https://gettingthingsdone.com/what-is-gtd/"},
        ],
    },
    {
        "n": 6,
        "title": "목적 유형 6 — 메모 · 검색",
        "role": "수집은 빠르게, 정리는 주간 배치로 나눕니다.",
        "cultivate": [
            "수집함 → 주간 정리 두 단계.",
            "태그·날짜·프로젝트 필터 기본 제공.",
            "민감 정보는 볼트·암호 규칙 명시.",
        ],
        "links": [
            {"label": "PARA", "url": "https://fortelabs.com/blog/para/"},
        ],
    },
]

KNOWHOW: list[dict[str, Any]] = [
    {
        "title": "실행 원칙 — 자기주도·맥락·AI 비용",
        "body": [
            "이 덱의 바닥은 자기주도학습입니다. 도구 이름을 외우는 것이 아니라, 왜 이렇게 나누는지 스스로 설명할 수 있어야 합니다.",
            "회사(사내 레포)에서는 Cline을 중심에 두고 룰·패턴과 맞춰 구현합니다. 집에서 만든 초안은 비밀·내부 코드 없이, 블록 단위로만 옮깁니다.",
            "집·카페 등 밖에서는 구독형 앱으로 시간을 두고 설계·용어를 다듬습니다. 짧은 질문·용어 확인은 무료로도 되지만, 여러 파일을 한꺼번에 손보는 일·복잡한 코딩은 유료 플랜이나 사내에서 허용한 인공지능에 맡기는 편이 낫습니다.",
        ],
    },
    {
        "title": "Cline과 개인별 구조",
        "body": [
            "Cline 설치 후 레포 안에서는 구현·가공 자유도가 거의 풀에 가깝게 열립니다.",
            "무엇을 만들지·목적 유형을 쌓는 순서는 사람마다 다릅니다. ‘같은 방식’보다 ‘같은 목적·말투로 말하는 방식’만 맞추면 됩니다.",
        ],
    },
    {
        "title": "시간 박스",
        "body": [
            "25~50분 박스만 잡고 그 안에서만 에이전트를 돌립니다.",
            "목표는 다음 커밋 단위로 쪼갭니다. 박스가 끝나면 저장·요약 한 줄로 끊습니다.",
        ],
    },
    {
        "title": "몰입 · 아이디어 폭주",
        "body": [
            "아이디어는 메모(목적 유형 6)로만 받고, 구현은 다음 박스로 미룹니다.",
            "스코프가 커지면 ‘이번에 안 할 것’ 한 줄을 먼저 적습니다.",
        ],
    },
    {
        "title": "정기 점검",
        "body": [
            "목적 유형 1 링크는 월 1회 · 목적 유형 2 프리셋은 3개월 미사용이면 보관함으로.",
            "목적 유형 4 시나리오는 깨졌을 때만 원인 분석합니다.",
        ],
    },
]

KNOWHOW_PART1: list[dict[str, Any]] = KNOWHOW[:3]
KNOWHOW_PART2: list[dict[str, Any]] = KNOWHOW[3:]


def get_flow_block(step_n: int) -> dict[str, Any] | None:
    for b in FLOW_DETAIL_BLOCKS:
        if b["n"] == step_n:
            return b
    return None
