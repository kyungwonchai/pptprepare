"""바이브 코딩 프로세스 영감 — 슬라이드용 짧은 불릿."""

from __future__ import annotations

from typing import Any

PROCESS_NOTES: list[str] = [
    "자기주도학습이 바닥. 사내 레포는 Cline 중심, 밖에서는 구독 앱으로 시간을 두고 설계.",
    "무료 인공지능: 짧은 질문·용어 확인. 복잡한 코딩·여러 파일을 한꺼번에 손보는 일은 유료나 사내 허용.",
    "스펙을 먼저 짧게 → AI는 구현·보일러플레이트.",
    "테스트를 먼저 두고 AI가 통과하게 (회귀 잡기).",
    "PR은 작게. 문서는 목적 유형 1에서 한 줄씩 갱신.",
]

LINK_GROUPS: list[dict[str, Any]] = [
    {
        "title": "도구 · 공식",
        "links": [
            {"label": "Cursor", "url": "https://cursor.com/docs"},
            {"label": "VS Code + AI", "url": "https://code.visualstudio.com/docs/editor/artificial-intelligence"},
            {"label": "Claude 프롬프트", "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"},
            {"label": "OpenAI", "url": "https://platform.openai.com/docs/guides/prompt-engineering"},
            {"label": "Gemini", "url": "https://ai.google.dev/gemini-api/docs"},
        ],
    },
    {
        "title": "글 · 영감",
        "links": [
            {"label": "Simon Willison (AI)", "url": "https://simonwillison.net/tags/ai/"},
            {"label": "Martin Fowler", "url": "https://martinfowler.com/articles/exploring-gen-ai.html"},
            {"label": "Karpathy", "url": "https://karpathy.ai/"},
        ],
    },
    {
        "title": "패턴 · 에이전트",
        "links": [
            {"label": "Cursor Rules", "url": "https://docs.cursor.com/context/rules-for-ai"},
            {"label": "Cline", "url": "https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev"},
            {"label": "Copilot", "url": "https://docs.github.com/en/copilot"},
        ],
    },
]
