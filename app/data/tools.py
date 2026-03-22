"""도구별 메타데이터·상세 설명·공식 링크 (단일 출처)."""

from __future__ import annotations

from typing import Any, TypedDict


class ToolLink(TypedDict):
    label: str
    url: str


class IconSpec(TypedDict, total=False):
    kind: str
    slug: str


class ToolRecord(TypedDict):
    slug: str
    name: str
    category_id: str
    category_label: str
    tagline: str
    icon: IconSpec
    detail: list[str]
    links: list[ToolLink]


TOOLS: dict[str, ToolRecord] = {
    "github": {
        "slug": "github",
        "name": "GitHub",
        "category_id": "infra",
        "category_label": "개발 인프라 · 데이터",
        "tagline": "Git 저장소·검토 요청·자동 빌드 — 협업의 허브.",
        "icon": {"kind": "si", "slug": "github"},
        "detail": [
            "GitHub는 Git 저장소를 클라우드에 호스팅하고, 이슈·프로젝트 보드·토론으로 작업을 관리하는 플랫폼입니다. 로컬에서 커밋한 내용을 원격에 push하고, 팀원과 브랜치·풀 리퀘스트(PR)로 코드 리뷰를 진행하는 흐름의 중심에 있습니다.",
            "GitHub Actions는 저장소 안에 설정만으로 빌드·시험·배포를 자동화할 수 있습니다. 취약점 알림·의존성 갱신 도우미 등과도 연동됩니다.",
            "오픈소스는 물론 기업용 GitHub Enterprise로 사내 정책·SSO와 맞춰 쓰는 경우가 많습니다. 개발자 포트폴리오·문서화(Pages, Wiki)와도 잘 맞습니다.",
        ],
        "links": [
            {"label": "GitHub 공식", "url": "https://github.com"},
            {"label": "문서", "url": "https://docs.github.com"},
        ],
    },
    "python": {
        "slug": "python",
        "name": "Python",
        "category_id": "infra",
        "category_label": "개발 인프라 · 데이터",
        "tagline": "스크립트·데이터·웹·ML까지 — 범용 인터프리터 언어.",
        "icon": {"kind": "si", "slug": "python"},
        "detail": [
            "Python은 읽기 쉬운 문법과 풍부한 표준 라이브러리로 스크립트 자동화·데이터 분석·웹 API·머신러닝까지 한 언어로 다루기 쉽습니다. 인터프리터 방식이라 개발-실행 사이클이 빠른 편입니다.",
            "추가 기능은 패키지로 묶어 설치하고, 버전을 맞춰 두는 방식이 일반적입니다. 웹 서버 뼈대·숫자·표·머신러닝 라이브러리가 생태계를 지탱합니다.",
            "운영체제 스크립트, 운영 도구, 노트북 기반 연구에도 널리 쓰이며, 여러 시스템을 잇는 말로 쓰이기도 합니다.",
        ],
        "links": [
            {"label": "Python.org", "url": "https://www.python.org"},
            {"label": "문서 튜토리얼", "url": "https://docs.python.org/3/tutorial/"},
        ],
    },
    "mysql": {
        "slug": "mysql",
        "name": "MySQL",
        "category_id": "infra",
        "category_label": "개발 인프라 · 데이터",
        "tagline": "널리 쓰이는 오픈소스 RDBMS.",
        "icon": {"kind": "si", "slug": "mysql"},
        "detail": [
            "MySQL은 관계형 데이터를 테이블·SQL로 다루는 오픈소스 데이터베이스입니다. 웹 호스팅·LAMP 스택·소규모~중규모 서비스에서 오래도록 기본 선택지로 쓰여 왔습니다.",
            "트랜잭션·복제·샤딩·클러스터 등 운영 요구에 맞춰 구성할 수 있고, 클라우드 관리형 서비스(RDS 등)와도 잘 붙습니다.",
            "표 구조 설계·검색 속도·질문 문장 다듬기는 다른 데이터베이스와 마찬가지로 중요하며, 앱이 오래 저장하는 데이터를 맡습니다.",
        ],
        "links": [
            {"label": "MySQL 공식", "url": "https://www.mysql.com"},
            {"label": "문서", "url": "https://dev.mysql.com/doc/"},
        ],
    },
    "postgresql": {
        "slug": "postgresql",
        "name": "PostgreSQL",
        "category_id": "infra",
        "category_label": "개발 인프라 · 데이터",
        "tagline": "표준 SQL·확장성 강한 오픈소스 RDBMS.",
        "icon": {"kind": "si", "slug": "postgresql"},
        "detail": [
            "PostgreSQL은 표준에 가깝게 질의하고, 글 검색·지도 좌표·JSON 형태까지 다루기 좋은 오픈소스 데이터베이스입니다.",
            "복제·논리 디코딩·파티셔닝 등으로 대규모 운영 사례가 많고, 오픈소스·클라우드 관리형 모두 선택지가 넓습니다.",
            "프로그램에서 ‘한곳에만 맞는 진짜 데이터’를 맡기는 경우가 많습니다.",
        ],
        "links": [
            {"label": "PostgreSQL 공식", "url": "https://www.postgresql.org"},
            {"label": "문서", "url": "https://www.postgresql.org/docs/"},
        ],
    },
    "microsoft-sql-server": {
        "slug": "microsoft-sql-server",
        "name": "Microsoft SQL Server",
        "category_id": "infra",
        "category_label": "개발 인프라 · 데이터",
        "tagline": "Microsoft 스택·엔터프라이즈용 상용 RDBMS.",
        "icon": {"kind": "si", "slug": "microsoftsqlserver"},
        "detail": [
            "SQL Server는 Microsoft가 제공하는 관계형 DBMS로, Windows·Azure·Linux에서 운영할 수 있습니다. .NET·Power BI·Active Directory와의 통합, 엔터프라이즈 라이선스·지원 체계가 강점입니다.",
            "T-SQL, SSIS·SSRS 등 BI·ETL 도구와 함께 쓰이는 경우가 많고, Always On 등 고가용성 구성이 문서화되어 있습니다.",
            "기업 내부 레거시·ERP·윈도우 서버 환경과 맞물릴 때 자주 선택됩니다.",
        ],
        "links": [
            {"label": "SQL Server", "url": "https://www.microsoft.com/sql-server"},
            {"label": "Microsoft Learn", "url": "https://learn.microsoft.com/sql/"},
        ],
    },
    "google-cloud": {
        "slug": "google-cloud",
        "name": "Google Cloud (클라우드 예시)",
        "category_id": "infra",
        "category_label": "개발 인프라 · 데이터",
        "tagline": "VM·DB·AI API 등 온디맨드 인프라 (예: GCP).",
        "icon": {"kind": "si", "slug": "googlecloud"},
        "detail": [
            "클라우드는 자체 데이터센터 대신 IaaS(가상 머신)·PaaS(관리형 DB, 컨테이너)·SaaS·AI API를 사용량·구독 기반으로 쓰는 모델입니다. 여기서는 대표로 Google Cloud Platform(GCP)을 예로 듭니다.",
            "Compute Engine, Cloud Run, BigQuery, Cloud Storage 등으로 웹 서비스·데이터 파이프라인·ML을 구성하고, IAM·VPC로 접근을 통제합니다.",
            "AWS·Azure와 유사하게 리전·가용 영역·규정 준수를 고려해 설계하며, ‘클라우드’는 벤더를 가리기보다 운영·비용·보안 패러다임을 가리키는 말로 쓰입니다.",
        ],
        "links": [
            {"label": "Google Cloud", "url": "https://cloud.google.com"},
            {"label": "문서", "url": "https://cloud.google.com/docs"},
        ],
    },
    "visual-studio-code": {
        "slug": "visual-studio-code",
        "name": "Visual Studio Code",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "확장형 경량 에디터 — 웹·다언어에 널리 쓰임.",
        "icon": {"kind": "si", "slug": "visualstudiocode"},
        "detail": [
            "VS Code는 Microsoft가 만든 크로스플랫폼 소스 코드 에디터로, 언어 서버·디버거·터미널·Git 통합이 기본에 가깝게 포함됩니다. 확장 마켓플레이스로 언어·프레임워크·테마를 더합니다.",
            "경량이라 일상 편집·스크립트·프론트엔드·원격 개발(SSH, Dev Containers)에 많이 쓰입니다. 팀 표준 에디터로 정하기도 쉽습니다.",
            "AI 코딩 확장(GitHub Copilot 등)·Settings Sync로 개인 워크플로를 맞춤화할 수 있습니다.",
        ],
        "links": [
            {"label": "VS Code", "url": "https://code.visualstudio.com"},
            {"label": "문서", "url": "https://code.visualstudio.com/docs"},
        ],
    },
    "jetbrains": {
        "slug": "jetbrains",
        "name": "JetBrains",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "IntelliJ·PyCharm 등 — 언어별 깊은 IDE 제품군.",
        "icon": {"kind": "si", "slug": "jetbrains"},
        "detail": [
            "JetBrains는 IntelliJ IDEA, PyCharm, WebStorm, Rider 등 언어·플랫폼별 IDE를 제공합니다. 정적 분석·리팩터링·탐색·디버깅이 강하고, 대규모 자바·코틀린·.NET 코드베이스에서 선호되는 경우가 많습니다.",
            "플러그인 생태계와 함께 팀 라이선스·All Products Pack으로 여러 IDE를 묶어 쓰기도 합니다.",
            "에디터보다 ‘프로젝트 전체를 이해하는 IDE’가 필요할 때 선택하는 경우가 많습니다.",
        ],
        "links": [
            {"label": "JetBrains", "url": "https://www.jetbrains.com"},
            {"label": "도구 목록", "url": "https://www.jetbrains.com/products/"},
        ],
    },
    "android-studio": {
        "slug": "android-studio",
        "name": "Android Studio",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "안드로이드 공식 IDE — 에뮬·빌드·프로파일링.",
        "icon": {"kind": "si", "slug": "androidstudio"},
        "detail": [
            "Android Studio는 Google이 권장하는 안드로이드 앱 개발 IDE로, Gradle 빌드·에뮬레이터·Layout Editor·Profiler가 한곳에 있습니다.",
            "Kotlin·Jetpack Compose·NDK 등 최신 안드로이드 스택과 릴리스 노트가 맞춰 업데이트됩니다.",
            "모바일 앱을 만들 때 필수에 가까운 도구이며, Play 배포 전 서명·번들 구성도 지원합니다.",
        ],
        "links": [
            {"label": "Android Studio", "url": "https://developer.android.com/studio"},
            {"label": "Android 개발자", "url": "https://developer.android.com"},
        ],
    },
    "visual-studio": {
        "slug": "visual-studio",
        "name": "Visual Studio",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "Microsoft 통합 IDE — .NET·C++·데스크톱 등.",
        "icon": {"kind": "si", "slug": "visualstudio"},
        "detail": [
            "Visual Studio(풀 IDE)는 Windows·맥용으로 제공되며, .NET·C++·데스크톱·일부 게임 클라이언트 워크플로에 맞춘 디버거·프로파일러·디자이너가 풍부합니다. VS Code와 이름이 비슷하지만 제품이 다릅니다.",
            "솔루션·프로젝트 단위로 대규모 솔루션을 관리하고, NuGet·Azure 배포와 연동하기 쉽습니다.",
            "엔터프라이즈 개발·윈도우 네이티브·레거시 .NET 유지보수에서 자주 쓰입니다.",
        ],
        "links": [
            {"label": "Visual Studio", "url": "https://visualstudio.microsoft.com"},
            {"label": "문서", "url": "https://learn.microsoft.com/visualstudio/"},
        ],
    },
    "cursor": {
        "slug": "cursor",
        "name": "Cursor",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "AI 우선 에디터(VS Code 계열) — 채팅·컨텍스트 보조.",
        "icon": {"kind": "silatest", "slug": "cursor"},
        "detail": [
            "Cursor는 VS Code를 기반으로 한 에디터로, 채팅·인라인 편집·코드베이스 인덱싱 등 AI 워크플로에 초점을 맞춥니다. 익숙한 단축키·확장과의 호환을 노리는 사용자가 많습니다.",
            "프로젝트 전체를 컨텍스트로 질문하거나, 선택 영역만 빠르게 수정하는 흐름이 강조됩니다.",
            "팀 정책·보안(코드 외부 전송 여부)을 확인한 뒤 도입하는 것이 좋습니다.",
        ],
        "links": [
            {"label": "Cursor", "url": "https://cursor.com"},
            {"label": "문서", "url": "https://docs.cursor.com"},
        ],
    },
    "unity": {
        "slug": "unity",
        "name": "Unity",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "실시간 3D·게임 엔진 — 멀티플랫폼 빌드.",
        "icon": {"kind": "si", "slug": "unity"},
        "detail": [
            "Unity는 실시간 3D 렌더링·물리·애니메이션을 포함한 게임·시뮬레이션 엔진입니다. 에디터에서 씬·프리팹·C# 스크립트로 동작을 구성하고 PC·모바일·콘솔 등으로 빌드합니다.",
            "에셋 스토어·URP/HDRP 등 그래픽 파이프라인 선택지가 있고, 비게임(건축 시각화, 교육)에도 쓰입니다.",
            "클라이언트 런타임·에디터 확장이 분리되어 있어 팀 역할(기획·아트·프로그래밍)이 나뉘기 좋습니다.",
        ],
        "links": [
            {"label": "Unity", "url": "https://unity.com"},
            {"label": "매뉴얼", "url": "https://docs.unity3d.com/Manual/index.html"},
        ],
    },
    "blender": {
        "slug": "blender",
        "name": "Blender",
        "category_id": "ide",
        "category_label": "IDE · 에디터 · 창작",
        "tagline": "3D 모델링·애니·렌더·VFX — 무료 DCC.",
        "icon": {"kind": "si", "slug": "blender"},
        "detail": [
            "Blender는 오픈소스 3D 제작 스위트로 모델링·스컬프트·리깅·애니메이션·렌더(Cycles, Eevee)·비디오 편집까지 한 앱에서 다룹니다.",
            "독립·인디·교육 현장에서 라이선스 부담 없이 쓰기 좋고, Python API로 자동화·애드온 개발이 가능합니다.",
            "게임 에셋·애니메이션·VFX 파이프라인에서 FBX/glTF 등으로 Unity·Unreal과 주고받는 경우가 많습니다.",
        ],
        "links": [
            {"label": "Blender", "url": "https://www.blender.org"},
            {"label": "문서", "url": "https://docs.blender.org"},
        ],
    },
    "gemini": {
        "slug": "gemini",
        "name": "Gemini",
        "category_id": "ai",
        "category_label": "AI · 에이전트",
        "tagline": "Google 멀티모달 LLM — 앱·코드 보조 연동.",
        "icon": {"kind": "si", "slug": "googlegemini"},
        "detail": [
            "Gemini는 Google이 제공하는 멀티모달 대규모 언어 모델 계열로, 텍스트·이미지 등 입력을 이해하고 생성합니다. 검색·Workspace·Android·클라우드 API와 연계되는 로드맵이 강합니다.",
            "개발자는 Google AI Studio·Vertex AI 등으로 API 키·엔드포인트를 통해 앱에 붙일 수 있습니다.",
            "프롬프트 설계·안전 필터·비용(토큰)을 고려해 프로덕션에 넣는 것이 일반적입니다.",
        ],
        "links": [
            {"label": "Gemini 앱", "url": "https://gemini.google.com"},
            {"label": "Google AI for Developers", "url": "https://ai.google.dev"},
        ],
    },
    "gpt": {
        "slug": "gpt",
        "name": "GPT (ChatGPT 등)",
        "category_id": "ai",
        "category_label": "AI · 에이전트",
        "tagline": "OpenAI 대화형 모델 — 글·코드·API 도구 호출.",
        "icon": {"kind": "si", "slug": "openai"},
        "detail": [
            "GPT 시리즈는 OpenAI의 텍스트(및 멀티모달) 생성 모델로, ChatGPT는 대화 UI·플러그인·코드 인터프리터 등 사용자 친화적 기능을 제공합니다.",
            "API로는 Responses·Chat Completions 등을 통해 앱·서비스에 붙이고, 함수 호출로 DB 조회·외부 API 연동을 설계할 수 있습니다.",
            "모델 버전·컨텍스트 길이·요금제가 자주 바뀌므로 공지·문서를 따라가며 사용하는 것이 좋습니다.",
        ],
        "links": [
            {"label": "OpenAI", "url": "https://openai.com"},
            {"label": "ChatGPT", "url": "https://chatgpt.com"},
            {"label": "API 문서", "url": "https://platform.openai.com/docs"},
        ],
    },
    "grok": {
        "slug": "grok",
        "name": "Grok",
        "category_id": "ai",
        "category_label": "AI · 에이전트",
        "tagline": "xAI 대화형 AI.",
        "icon": {"kind": "grok"},
        "detail": [
            "Grok은 xAI가 개발한 대화형 AI 제품으로, 실시간 정보·유머 톤 등 브랜드 특성이 강조되는 경우가 있습니다. X Premium 등 구독과 묶여 제공되는 흐름이 알려져 있습니다.",
            "다른 LLM과 마찬가지로 코드 초안·설명·브레인스토밍에 쓸 수 있으나, 정책·지역·요금은 수시로 변할 수 있습니다.",
            "기업·규제 환경에서는 데이터 처리 위치·학습 정책을 확인하고 도입하는 것이 좋습니다.",
        ],
        "links": [
            {"label": "xAI", "url": "https://x.ai"},
            {"label": "Grok (X)", "url": "https://x.com/i/grok"},
        ],
    },
    "cline": {
        "slug": "cline",
        "name": "Cline",
        "category_id": "ai",
        "category_label": "AI · 에이전트",
        "tagline": "VS Code AI 에이전트 — 터미널·파일 자동화.",
        "icon": {"kind": "silatest", "slug": "cline"},
        "detail": [
            "Cline(구 Claude Dev)은 VS Code 안에서 동작하는 AI 에이전트로, 자연어 지시에 따라 파일 편집·터미널 명령·멀티스텝 작업을 시도합니다. API 키를 연결해 Claude 등 모델을 선택하는 방식이 일반적입니다.",
            "‘에이전트’에 가깝게 폴더 단위 작업을 맡기는 워크플로에 맞고, 승인 단계를 두어 안전하게 쓰는 설정이 권장됩니다.",
            "확장 마켓플레이스·GitHub 릴리스 노트를 통해 업데이트·권한 모델을 확인하세요.",
        ],
        "links": [
            {"label": "Cline (GitHub)", "url": "https://github.com/cline/cline"},
            {"label": "VS Marketplace", "url": "https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev"},
        ],
    },
}


CATEGORIES: list[dict[str, Any]] = [
    {
        "id": "infra",
        "title": "개발 인프라 · 데이터",
        "tool_slugs": [
            "github",
            "python",
            "mysql",
            "postgresql",
            "microsoft-sql-server",
            "google-cloud",
        ],
    },
    {
        "id": "ide",
        "title": "IDE · 에디터 · 창작",
        "tool_slugs": [
            "visual-studio-code",
            "jetbrains",
            "android-studio",
            "visual-studio",
            "cursor",
            "unity",
            "blender",
        ],
    },
    {
        "id": "ai",
        "title": "AI · 에이전트",
        "tool_slugs": ["gemini", "gpt", "grok", "cline"],
    },
]


def get_tool(slug: str) -> ToolRecord | None:
    return TOOLS.get(slug)


def get_categories_for_slide() -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for cat in CATEGORIES:
        tools = []
        for s in cat["tool_slugs"]:
            t = TOOLS.get(s)
            if t:
                tools.append(t)
        out.append({"id": cat["id"], "title": cat["title"], "tools": tools})
    return out


def all_tool_slugs() -> list[str]:
    return list(TOOLS.keys())
