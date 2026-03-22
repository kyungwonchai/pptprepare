"""4가지 AI 도구 공통 기능 — 용어는 기능당 한 번만 풀고, 제품별로는 짧게 비교 (슬라이드 26~33)."""

from __future__ import annotations

from typing import Any

# SVG는 슬라이드 안 작은 도형 설명용(장식 수준, 본문과 중복되지 않게)
_D_CTX = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><linearGradient id="ctxg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#6366f1"/><stop offset="100%" stop-color="#22c55e"/></linearGradient><marker id="ctxm" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7z" fill="#64748b"/></marker></defs><rect x="8" y="28" width="72" height="56" rx="8" fill="rgba(99,102,241,0.15)" stroke="rgba(129,140,248,0.5)"/><text x="44" y="58" text-anchor="middle" fill="#94a3b8" font-size="11">내 화면</text><line x1="82" y1="56" x2="115" y2="56" stroke="#64748b" stroke-width="2" marker-end="url(#ctxm)"/><rect x="120" y="18" width="100" height="76" rx="10" fill="rgba(34,197,94,0.12)" stroke="url(#ctxg)"/><text x="170" y="48" text-anchor="middle" fill="#cbd5e1" font-size="10">맥락</text><text x="170" y="64" text-anchor="middle" fill="#94a3b8" font-size="9">파일·폴더·메모</text><line x1="222" y1="56" x2="255" y2="56" stroke="#64748b" stroke-width="2" marker-end="url(#ctxm)"/><ellipse cx="318" cy="56" rx="88" ry="36" fill="rgba(99,102,241,0.08)" stroke="rgba(199,210,254,0.35)"/><text x="318" y="52" text-anchor="middle" fill="#e2e8f0" font-size="11">답</text><text x="318" y="68" text-anchor="middle" fill="#94a3b8" font-size="9">같은 질문도 달라짐</text></svg>"""

_D_AGENT = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="40" width="56" height="36" rx="6" fill="rgba(99,102,241,0.2)" stroke="#818cf8"/><text x="48" y="62" text-anchor="middle" fill="#cbd5e1" font-size="10">①</text><path d="M78 58 L108 58" stroke="#64748b"/><rect x="110" y="36" width="56" height="36" rx="6" fill="rgba(34,197,94,0.15)" stroke="#4ade80"/><text x="138" y="58" text-anchor="middle" fill="#cbd5e1" font-size="10">②</text><path d="M168 58 L198 58" stroke="#64748b"/><rect x="200" y="32" width="56" height="40" rx="6" fill="rgba(232,168,56,0.15)" stroke="#fbbf24"/><text x="228" y="58" text-anchor="middle" fill="#cbd5e1" font-size="10">③</text><path d="M258 58 L288 58" stroke="#64748b"/><rect x="290" y="28" width="100" height="48" rx="8" fill="rgba(99,102,241,0.1)" stroke="rgba(129,140,248,0.45)"/><text x="340" y="52" text-anchor="middle" fill="#e2e8f0" font-size="11">결과</text><text x="340" y="66" text-anchor="middle" fill="#94a3b8" font-size="9">중간은 사람이 안 눌러도</text></svg>"""

_D_CHAT = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><rect x="16" y="20" width="170" height="64" rx="8" fill="rgba(99,102,241,0.15)" stroke="#818cf8"/><text x="101" y="44" text-anchor="middle" fill="#e2e8f0" font-size="11">말로 주고받기</text><text x="101" y="62" text-anchor="middle" fill="#94a3b8" font-size="9">채팅</text><rect x="220" y="20" width="184" height="64" rx="8" fill="rgba(34,197,94,0.12)" stroke="#4ade80"/><rect x="236" y="36" width="120" height="14" rx="2" fill="rgba(248,113,113,0.25)"/><text x="312" y="46" text-anchor="middle" fill="#fecaca" font-size="9">드래그한 줄</text><text x="312" y="68" text-anchor="middle" fill="#94a3b8" font-size="9">한 줄·한 파일 단위</text></svg>"""

_D_TERM = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><rect x="120" y="18" width="180" height="64" rx="6" fill="#0f172a" stroke="#334155"/><rect x="130" y="28" width="160" height="10" fill="#1e293b"/><text x="210" y="54" text-anchor="middle" fill="#94a3b8" font-size="11">검은 창 = 버튼을 글로 치는 곳</text><text x="210" y="72" text-anchor="middle" fill="#64748b" font-size="9">실행·실험·로그</text></svg>"""

_D_MCP = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><circle cx="210" cy="50" r="22" fill="rgba(99,102,241,0.25)" stroke="#818cf8"/><text x="210" y="54" text-anchor="middle" fill="#e2e8f0" font-size="10">AI</text><circle cx="80" cy="50" r="16" fill="rgba(34,197,94,0.2)" stroke="#4ade80"/><circle cx="340" cy="50" r="16" fill="rgba(232,168,56,0.2)" stroke="#fbbf24"/><circle cx="140" cy="22" r="14" fill="rgba(56,189,248,0.2)" stroke="#38bdf8"/><circle cx="280" cy="78" r="14" fill="rgba(244,114,182,0.2)" stroke="#f472b6"/><path d="M96 50 L186 50" stroke="#64748b" stroke-dasharray="4 3"/><path d="M234 50 L324 50" stroke="#64748b" stroke-dasharray="4 3"/><path d="M200 36 L210 28" stroke="#64748b" stroke-dasharray="4 3"/><path d="M220 64 L210 72" stroke="#64748b" stroke-dasharray="4 3"/><text x="210" y="96" text-anchor="middle" fill="#64748b" font-size="9">메일·이슈·DB 등 바깥과 표준 잭으로</text></svg>"""

_D_RULE = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="12" width="220" height="76" rx="8" fill="rgba(99,102,241,0.15)" stroke="#818cf8"/><text x="210" y="36" text-anchor="middle" fill="#e2e8f0" font-size="11">팀 규칙 메모</text><line x1="120" y1="48" x2="300" y2="48" stroke="rgba(148,163,184,0.4)"/><line x1="120" y1="58" x2="280" y2="58" stroke="rgba(148,163,184,0.25)"/><line x1="120" y1="68" x2="260" y2="68" stroke="rgba(148,163,184,0.25)"/><text x="210" y="88" text-anchor="middle" fill="#94a3b8" font-size="9">매번 같은 말 안 해도 됨</text></svg>"""

_D_SAFE = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><rect x="60" y="30" width="300" height="44" rx="10" fill="rgba(15,23,42,0.9)" stroke="#475569"/><rect x="70" y="38" width="90" height="28" rx="6" fill="rgba(34,197,94,0.2)" stroke="#4ade80"/><text x="115" y="55" text-anchor="middle" fill="#bbf7d0" font-size="9">읽기만</text><rect x="170" y="38" width="90" height="28" rx="6" fill="rgba(232,168,56,0.2)" stroke="#fbbf24"/><text x="215" y="55" text-anchor="middle" fill="#fde68a" font-size="9">제한 실행</text><rect x="270" y="38" width="80" height="28" rx="6" fill="rgba(248,113,113,0.15)" stroke="#f87171"/><text x="310" y="55" text-anchor="middle" fill="#fecaca" font-size="9">확인</text><text x="210" y="92" text-anchor="middle" fill="#94a3b8" font-size="9">단계를 올려갈수록 먼저 물어봄</text></svg>"""

_D_DIFF = """<svg class="ppt-feature-svg" viewBox="0 0 420 100" xmlns="http://www.w3.org/2000/svg"><rect x="40" y="28" width="150" height="48" rx="6" fill="rgba(34,197,94,0.12)" stroke="#4ade80"/><text x="115" y="48" text-anchor="middle" fill="#86efac" font-size="10">+ 추가</text><text x="115" y="64" text-anchor="middle" fill="#94a3b8" font-size="9">초록</text><rect x="230" y="28" width="150" height="48" rx="6" fill="rgba(248,113,113,0.12)" stroke="#f87171"/><text x="305" y="48" text-anchor="middle" fill="#fecaca" font-size="10">− 삭제</text><text x="305" y="64" text-anchor="middle" fill="#94a3b8" font-size="9">빨강</text></svg>"""

AI_FEATURE_SLIDES: list[dict[str, Any]] = [
    {
        "kicker": "공통 기능 1/8",
        "page_title": "맥락 주기 (컨텍스트)",
        "lead": (
            "여기서 말하는 ‘맥락’은 「인공지능이 답하기 전에 같이 보게 만드는 묶음」입니다. "
            "같은 질문을 해도, 자료를 한 장만 넣었는지·서랍 전체를 요약했는지에 따라 답이 달라집니다."
        ),
        "metaphor": (
            "회의에 갈 때 「누구에게 무엇을 펼쳐 놓을지」 정하는 것과 같습니다. "
            "빈손으로 “어떻게 생각해?”라고 하면 막연하고, 지난주 회의록·표·금지 사항까지 올리면 구체적입니다."
        ),
        "usage_plain": (
            "처음엔 「한 파일·한 문단」만 넣고 답을 보고, 부족하면 “폴더 전체 맥락”을 켜는 식으로 넓히면 됩니다. "
            "한 번에 다 넣으면 오히려 엉뚱한 데 집중할 수 있어요."
        ),
        "diagram_svg": _D_CTX,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「컨텍스트 / 맥락 / @멘션 / 인덱싱」 같은 말은 뜻이 같습니다. “지금 이 대화에 AI가 뭘 끼워 넣고 볼지”입니다. "
                    "제품마다 버튼 이름만 다르고, 아래 네 칸에서 그 차이만 짧게 적었습니다.",
                ],
            },
            {
                "title": "실전 예: 보고서 요약",
                "paragraphs": [
                    "상사에게 “이번 주 보고서 톤만 맞춰줘”라고 부탁한다고 칩시다. 「보고서 파일만」 맥락에 넣으면 문장만 다듬어지고, "
                    "「회사 전체 규정 PDF까지」 넣으면 표현이 급격히 조심스러워질 수 있습니다. 무엇을 보여줄지가 곧 결과의 방향입니다.",
                    "비개발 일이라면: 엑셀 한 시트만 넣고 “이 표를 보고 설명 문단 써줘” vs “전체 통계 파일까지 넣고 요약해줘”를 비교해 보세요. 후자가 더 길고 넓은 답이 나옵니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "여러 에이전트·작업 공간이 「서로 다른 맥락」을 나눠 둡니다. “관리 화면”에서 어떤 일꾼이 어떤 자료를 보는지 나뉘는 느낌에 가깝습니다.",
            },
            {
                "label": "Claude Code",
                "bite": "프로젝트 폴더를 통째로 읽는 흐름이 강합니다. 「“이 저장소 안에서”」라는 맥락이 기본에 가깝습니다.",
            },
            {
                "label": "Codex",
                "bite": "검은 창·클라우드 작업 등 「환경마다」 맥락이 갈립니다. “어디서 실행 중인지”가 곧 답의 범위입니다.",
            },
            {
                "label": "Cursor",
                "bite": "「열린 파일·커서 위치·@로 찍은 파일」이 맥락이 됩니다. “지금 보고 있는 줄”에 가장 강합니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 2/8",
        "page_title": "에이전트 (알아서 여러 단계)",
        "lead": (
            "「에이전트」는 “한 번 시키면 중간 단계를 스스로 밟고, 필요한 만큼 파일·명령·검사를 이어 가는 모드”를 가리킬 때 씁니다. "
            "사람이 매번 ‘다음 버튼’을 누르지 않아도 됩니다."
        ),
        "metaphor": (
            "편의점에 “김밥이랑 음료 싸 주고, 영수증은 이메일로”라고 맡기면, 「진열·계산·봉투·발송」까지 알아서 하는 것과 비슷합니다. "
            "같은 “에이전트”라도 가게마다(제품마다) 할 수 있는 일의 범위가 다릅니다."
        ),
        "usage_plain": (
            "처음엔 「짧은 목표」를 주고, 중간 산출물(파일 목록·스크린샷·짧은 요약)을 확인한 뒤 다음을 시키는 식이 안전합니다. "
            "한 번에 “전부 다”보다 “이 기능 하나만”이 이해하기 쉽습니다."
        ),
        "diagram_svg": _D_AGENT,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「에이전트 / 자율 / 멀티스텝 / 백그라운드 작업」은 같은 축을 말할 때가 많습니다. “한 번의 부탁이 여러 동작으로 이어진다”는 뜻입니다. "
                    "제품마다 「동시에 몇 개의 일꾼을 둘 수 있는지」, 「멈추고 물어보는지」가 다릅니다.",
                ],
            },
            {
                "title": "실전 예: 신규 페이지 하나 만들기",
                "paragraphs": [
                    "“로그인 화면이랑 같은 스타일로 ‘비밀번호 찾기’ 페이지만 만들어줘”라고 부탁한다고 합시다. 에이전트 모드는 「파일 복사 → 글자 수정 → 화면에서 확인」까지 한 줄로 이어갈 수 있습니다. "
                    "사람은 마지막에 「화면 캡처나 문장만」 검토하면 됩니다.",
                    "비개발 예로 치면: 행사 준비를 “이 체크리스트대로 알아서 진행하고, 매일 저녁 한 줄만 보고해”라고 맡기는 것과 비슷합니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "여러 에이전트를 「띄워 두고」 각각 다른 일을 돌리는 그림이 강조됩니다. “통제실에서 여러 로봇”에 가깝습니다.",
            },
            {
                "label": "Claude Code",
                "bite": "프로젝트 안에서 「긴 대화·긴 작업」으로 이어지는 경우가 많습니다. 터미널·편집기·데스크톱 앱이 같은 엔진이라는 설명이 공식에 있습니다.",
            },
            {
                "label": "Codex",
                "bite": "CLI·검은 창 중심으로 「자동·재개」 같은 키워드가 자주 붙습니다. 팀에서 이미 쓰는 오픈AI 흐름에 붙이기 좋다는 설명이 많습니다.",
            },
            {
                "label": "Cursor",
                "bite": "「에이전트 모드」로 여러 파일을 한 번에 고치기도 하고, 반대로 「한 줄만」 고치는 모드와 나눠 쓰는 경우가 많습니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 3/8",
        "page_title": "말로 주고받기 vs 한 덩어리로 고치기",
        "lead": (
            "대부분의 도구에는 「채팅창」(말로 설명·질문)과 「편집기 안에서 바로 고치기」(드래그한 부분만) 두 갈래가 같이 있습니다. "
            "같은 회사가 만든 제품이라도 버튼 이름이 달라 헷갈릴 수 있어, 여기서는 「역할만」 통일합니다."
        ),
        "metaphor": (
            "「채팅」은 카운터에서 주문하며 말을 주고받는 것, 「고치기 모드」는 종이에 빨간 펜으로 “이 문장만 이렇게”라고 적는 것에 가깝습니다. "
            "긴 설계는 채팅이, 문장 한 줄은 고치기가 편할 때가 많습니다."
        ),
        "usage_plain": (
            "“왜 이렇게 동작하지?”처럼 「이해·설명」이 필요하면 채팅. “이 변수 이름만 바꿔줘”처럼 「좁은 수정」은 드래그해서 고치기 쪽을 먼저 써 보세요."
        ),
        "diagram_svg": _D_CHAT,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「채팅 / 대화 / 인라인 / 컴포저 / 커맨드 팔레트」 같은 말은 “말로 길게” vs “화면에 보이는 코드만 짧게”로 나뉩니다. "
                    "제품마다 이름이 달라도, 「한 장에 두 가지 길이」가 있다고 기억하면 됩니다.",
                ],
            },
            {
                "title": "실전 예: 이메일 초안",
                "paragraphs": [
                    "「채팅」: “이번 달 실적 요약 메일을 상사 톤으로 써줘. 길이는 10문장 안으로.”처럼 조건을 말로 쌓습니다. "
                    "「고치기」: 초안을 붙여 넣고 세 번째 문장만 드래그해 “이 문장만 부드럽게”라고 합니다.",
                    "코드가 아니어도 똑같습니다. 긴 설계는 채팅, 한 줄 톤은 드래그 쪽이 부담이 적습니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "편집 화면과 「에이전트·관리 화면」이 나뉘는 느낌에 가깝습니다. 말로 맡기는 쪽이 “관리”에 가깝습니다.",
            },
            {
                "label": "Claude Code",
                "bite": "대화·명령이 「검은 창·브라우저 탭」 등 여러 얼굴이 있지만, 같은 엔진이라는 설명이 공식에 있습니다.",
            },
            {
                "label": "Codex",
                "bite": "검은 창·앱에서 「대화형으로 묶기」와 「자동 실행」을 나눠 말하는 경우가 많습니다.",
            },
            {
                "label": "Cursor",
                "bite": "「채팅」과 「한 파일·여러 파일을 한 번에 고치는 창」이 나란히 있는 케이스가 많고, 「인라인」으로 줄 단위 수정도 강합니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 4/8",
        "page_title": "검은 창·명령줄 (터미널 / CLI)",
        "lead": (
            "「터미널·CLI」는 검은 창에 글자로 명령을 쳐서 프로그램을 돌리는 화면입니다. "
            "인공지능 도구들은 이 창을 「대신 눌러 주거나」, 로그를 읽어 “됐다/안 됐다”를 판단하게 만듭니다."
        ),
        "metaphor": (
            "마우스로 아이콘을 누르는 대신, 「공장 조작판에 스위치 이름을 적어 넣는 것」입니다. "
            "같은 공장이라도 “어떤 스위치까지 눌러도 되는지”는 제품·설정마다 다릅니다."
        ),
        "usage_plain": (
            "처음엔 “빌드(만들기)·테스트(시험)”처럼 「팀에서 이미 쓰는 단어」만 적어 두고, 인공지능에게 “이 명령 그대로 실행해줘”라고 맡기면 됩니다. "
            "낯선 명령을 한꺼번에 늘리지 않는 편이 안전합니다."
        ),
        "diagram_svg": _D_TERM,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「터미널 / CLI / 셸 / 콘솔」은 같은 종류의 창을 가리킬 때가 많습니다. "
                    "인공지능 도구 설명에서는 “검은 창에서 무엇을 실행할지”가 핵심이고, 제품마다 「자동 실행 허용 범위」가 다릅니다.",
                ],
            },
            {
                "title": "실전 예: “어제는 됐는데 오늘은 안 됨”",
                "paragraphs": [
                    "개발자가 아니어도, 「로그 한 줄」을 붙여 넣고 “이게 무슨 뜻이야?”라고 물으면 됩니다. "
                    "다음 단계로는 “같은 명령을 다시 실행해 보고, 결과만 붙여 줘”라고 부탁할 수 있습니다.",
                    "비유로는: 복사기가 “용지 걸림”이라고 뜰 때, 「전원만 끄지 말고」 에러 코드를 검색하는 것과 같습니다. "
                    "인공지능은 그 검색·해석을 대신해 줄 수 있습니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "에이전트가 「편집기·검은 창·브라우저」를 한 흐름으로 잡는 그림이 소개됩니다.",
            },
            {
                "label": "Claude Code",
                "bite": "프로젝트 안에서 「명령 실행」이 자주 등장합니다. 같은 엔진을 쓰는 여러 화면이 있다는 설명이 공식에 있습니다.",
            },
            {
                "label": "Codex",
                "bite": "「CLI」가 제품 소개의 중심에 자주 나옵니다. 검은 창·자동화 스크립트와 잘 맞는다는 취지입니다.",
            },
            {
                "label": "Cursor",
                "bite": "편집기 안에 「터미널 패널」이 붙어 있어, “고친 뒤 같은 화면에서 실행”하기 쉽습니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 5/8",
        "page_title": "바깥 프로그램과 연결 (MCP·확장)",
        "lead": (
            "「연결」은 인공지능이 「메일·이슈 트래커·데이터베이스·회사 전용 도구」 같은 바깥 세계와 통신하게 만드는 설정입니다. "
            "‘말’만 하는 게 아니라 「실제 시스템에 손이 닿게」 하는 층입니다."
        ),
        "metaphor": (
            "집에 「콘센트 규격」이 맞아야 청소기가 돌아가듯, 「표준 잭(MCP 같은 것)」을 맞춰 두면 여러 앱을 같은 방식으로 꽂을 수 있습니다. "
            "제품마다 “지원하는 콘센트 목록”이 다릅니다."
        ),
        "usage_plain": (
            "처음엔 「하나만」 연결해 보세요. 예: “이슈 번호만 가져와서 요약해줘”. "
            "여러 개를 한꺼번에 열면 어디서 권한이 막혔는지 찾기 어렵습니다."
        ),
        "diagram_svg": _D_MCP,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「MCP / 플러그인 / 통합 / 연동」은 “인공지능이 바깥 도구를 호출할 수 있게 한다”는 뜻에서 겹칩니다. "
                    "이 장에서는 「MCP」를 「대표적인 표준 이름」으로만 쓰고, 세부 설정은 각 제품 문서를 따릅니다.",
                ],
            },
            {
                "title": "실전 예: 티켓 번호로 요약",
                "paragraphs": [
                    "팀에서 “이슈 1234만 보고 오늘 할 일 정리해줘”라고 하려면, 인공지능이 「이슈 시스템을 읽을 권한」이 있어야 합니다. "
                    "연결은 그 「권한과 통로」를 한 번에 준비하는 설정입니다.",
                    "비개발 예: 회사 그룹웨어에 「읽기 전용 계정」을 만들어 두고, “이 계정으로만 일정을 가져와줘”처럼 범위를 좁히는 상상을 해보면 이해가 쉽습니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "여러 에이전트·도구가 「한 무대」에서 돌아가는 그림과 함께, 외부 연결을 「넓게」 다루는 소개가 있습니다.",
            },
            {
                "label": "Claude Code",
                "bite": "「허용된 외부 도구」와 연결한다는 설명이 공식에 있습니다. 팀 정책에 맞게 켜고 끕니다.",
            },
            {
                "label": "Codex",
                "bite": "「MCP」 등 도구 연결을 문서에서 다루는 흐름이 있습니다. 팀·오픈AI 환경에 맞춰 설정합니다.",
            },
            {
                "label": "Cursor",
                "bite": "「MCP 서버」를 넣어 다른 프로그램과 붙이는 설정이 문서에 있습니다. 편집기 안에서 바로 쓰는 그림이 강합니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 6/8",
        "page_title": "팀 규칙·메모 (룰·지시문)",
        "lead": (
            "「룰·지시문」은 매번 채팅으로 “이름은 이렇게, 금지는 이렇게”라고 반복하지 않게, 「파일이나 설정에 적어 두는 메모」입니다. "
            "프로젝트마다 팀이 정한 스타일을 인공지능이 「먼저 읽게」 합니다."
        ),
        "metaphor": (
            "집 현관에 「‘실내화 필수, 애완동물은 거실 금지’」 같은 안내문을 붙여 두는 것과 같습니다. "
            "손님(인공지능)이 들어올 때마다 같은 말을 하지 않아도 됩니다."
        ),
        "usage_plain": (
            "세 줄만 적어도 좋습니다. 예: “존댓말”, “숫자는 세 자리마다 쉼표”, “외부 링크는 각주”. "
            "늘어날수록 「진짜로 지키는 규칙만」 남기고 나머지는 지워도 됩니다."
        ),
        "diagram_svg": _D_RULE,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「룰 / Rules / AGENTS.md / 지시문 / 프로젝트 메모」는 “저장해 두면 매번 같은 출발선을 잡는 메모”로 묶을 수 있습니다. "
                    "형식은 제품마다 다르지만, 「목적은 하나」입니다.",
                ],
            },
            {
                "title": "실전 예: 보고서 톤 맞추기",
                "paragraphs": [
                    "“우리 회사는 결론을 맨 위에 쓴다” “표는 캡션을 아래에 둔다”를 파일에 적어 두면, "
                    "인공지능이 초안을 쓸 때마다 「같은 습관」으로 맞춥니다. "
                    "채팅으로 매번 말하는 것보다 「실수가 줄어듭니다」.",
                    "비개발 예: 회사 공문 양식이 있으면 그 PDF를 첨부하거나, 「한 페이지짜리 ‘말투 샘플’」만 넣어도 효과가 큽니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "프로젝트·에이전트가 「오래 기억할 맥락」을 쌓는 설명이 블로그 등에 나옵니다. 팀 규칙도 그 일부에 해당합니다.",
            },
            {
                "label": "Claude Code",
                "bite": "저장소 안의 「설명 파일·메모」를 읽는 흐름이 강합니다. 팀이 정한 문서를 같이 두면 반영됩니다.",
            },
            {
                "label": "Codex",
                "bite": "팀·조직 설정과 「클라우드 작업」 규칙을 맞춘다는 설명이 문서에 있습니다. 회사 정책과 연결됩니다.",
            },
            {
                "label": "Cursor",
                "bite": "「Rules」로 편집기·프로젝트에 규칙을 박아 두는 방식이 문서에 잘 정리되어 있습니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 7/8",
        "page_title": "안전·승인·샌드박스",
        "lead": (
            "인공지능이 파일을 지우거나, 내부망에 접속하거나, 돈이 드는 작업을 할 때 「먼저 물어보는 단계」가 있습니다. "
            "「샌드박스」는 “모래상자 안에서만 놀게” 해서 밖으로 나가는 피해를 줄이는 설정입니다."
        ),
        "metaphor": (
            "아파트 「자동문」처럼, 「1층 → 지하 주차장 → 옥상」으로 갈수록 열쇠가 달라지는 것과 비슷합니다. "
            "“읽기만”은 문 앞, “실행”은 한 단계 안쪽, “위험한 일”은 「사람 확인」이 더 자주 낍니다."
        ),
        "usage_plain": (
            "처음엔 「읽기·검색만」 켜 두고, 익숙해지면 「제한 실행」으로 올리는 식이 안전합니다. "
            "한 번에 “전부 허용”은 나중에 되돌리기 어렵습니다."
        ),
        "diagram_svg": _D_SAFE,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「승인 / 승인 요청 / 읽기 전용 / 자동 모드 / 샌드박스」는 “얼마나 멀리 손이 닿게 할지”를 나누는 말입니다. "
                    "제품마다 버튼 이름이 다르지만, 「단계를 올릴수록 먼저 물어본다」는 그림은 같습니다.",
                ],
            },
            {
                "title": "실전 예: 외부에 메일 보내기",
                "paragraphs": [
                    "인공지능이 「메일 초안」까지는 쓰고, 「보내기 버튼」은 사람이 누르게 두는 팀이 많습니다. "
                    "이 장면이 바로 “승인”의 일상 버전입니다.",
                    "비개발 예: 회사 카드로 결제할 때 「이중 확인」이 뜨는 것과 같습니다. "
                    "인공지능도 “삭제·전송·결제” 같은 동작은 「한 번 더」 묻게 해 두는 편이 안전합니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "여러 에이전트를 돌리면서 「산출물로 검토」한다는 설명이 있습니다. 위험한 행동 전에 멈추는 UX가 강조됩니다.",
            },
            {
                "label": "Claude Code",
                "bite": "프로젝트 밖 「허용 범위」를 넘는 행동은 「허용 목록」과 정책에 맡긴다는 설명이 공식에 있습니다.",
            },
            {
                "label": "Codex",
                "bite": "「읽기 모드 / 자동 / 허용 수준」 등을 고르는 말이 소개됩니다. 검은 창·자동화 스크립트와 함께 설명됩니다.",
            },
            {
                "label": "Cursor",
                "bite": "편집기 안에서 바로 고치기 때문에 「실행·파일 변경」 전에 확인하는 흐름이 중요합니다. 팀 룰과 같이 씁니다.",
            },
        ],
        "links": [],
    },
    {
        "kicker": "공통 기능 8/8",
        "page_title": "바꾼 내용 확인·적용·되돌리기",
        "lead": (
            "인공지능이 파일을 고치면 「어디가 어떻게 바뀌었는지」를 색으로 보여 줍니다. "
            "「적용」은 그 제안을 진짜 파일에 반영하는 것이고, 「되돌리기」는 반영 전·후 모두에서 가능해야 안심입니다."
        ),
        "metaphor": (
            "교정 스티커를 「초록(추가)·빨강(삭제)」으로 붙여 보는 것과 같습니다. "
            "스티커를 「붙일지 말지」는 사람이 마지막에 고릅니다."
        ),
        "usage_plain": (
            "처음엔 「작은 파일 하나」부터 적용해 보고, 화면이 기대와 같으면 그다음 폴더로 넓히면 됩니다. "
            "한 번에 수십 파일을 적용했다가 되돌리기 어려워질 수 있습니다."
        ),
        "diagram_svg": _D_DIFF,
        "sections": [
            {
                "title": "이 장에서 한 번만 정리하는 말",
                "paragraphs": [
                    "「diff / 패치 / 적용 / 리뷰」는 “제안 → 검토 → 반영”의 줄입니다. "
                    "제품마다 버튼 이름은 다르지만, 「초록·빨강으로 보이는 것」은 같은 이야기입니다.",
                ],
            },
            {
                "title": "실전 예: 문서 번역 톤",
                "paragraphs": [
                    "인공지능이 문단을 고쳤다면, 「빨간 줄이 지워진 부분」이 원문에서 빠지는 것이고, 「초록 줄」이 새로 들어가는 것입니다. "
                    "마음에 들면 적용, 아니면 「그 문단만」 다시 시키면 됩니다.",
                    "비개발 예: 회사 양식 워드 파일에서 「‘변경 내용 표시’」를 켜 두고 검토하는 것과 같습니다.",
                ],
            },
        ],
        "compare_rows": [
            {
                "label": "Antigravity",
                "bite": "「산출물·스크린샷」으로 바뀐 결과를 보여 주는 흐름이 강합니다. 댓글로 고치라고 할 수 있다는 설명이 있습니다.",
            },
            {
                "label": "Claude Code",
                "bite": "파일 여러 개를 「연속으로 고치는」 흐름이 강하고, 변경은 「Git 같은 기록」과 함께 쓰는 경우가 많습니다.",
            },
            {
                "label": "Codex",
                "bite": "검은 창·클라우드 작업에서 「변경을 적용」하고 「재개」하는 말이 자주 나옵니다.",
            },
            {
                "label": "Cursor",
                "bite": "편집기 안에서 「diff를 보고 적용」하는 경험이 직관적입니다. 한 파일·여러 파일 모두 가능합니다.",
            },
        ],
        "links": [],
    },
]
