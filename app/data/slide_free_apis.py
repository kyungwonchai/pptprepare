"""무료 공개 API 큐레이션 — 용도별·완전 무료 vs 가입 무료 티어·클라우드 무료(요약).

실제 이용 전 각 서비스 최신 약관·한도·상업 이용 조건을 반드시 확인하세요.
‘세상의 모든’ API를 한 페이지에 나열할 수는 없으므로, 대표적인 공개·무료 티어를
넓게 모았고 메타 목록(public-apis 등) 링크를 포함합니다.
"""

from __future__ import annotations

from typing import Any

FREE_API_PAGE: dict[str, Any] = {
    "kicker": "참고 목록",
    "page_title": "무료로 쓸 수 있는 연결 (용도별)",
    "lead": (
        "가입 없이 또는 무료 가입만으로 쓸 수 있는, 다른 서비스와 연결하는 주소들을 용도별로 모았습니다. "
        "하루 호출 횟수·금지 용도는 서비스마다 다르므로, 실제 서비스에 넣기 전에 이용약관을 확인하세요. "
        "전 세계 모든 연결을 나열할 수는 없어, 대표 예와 더 찾아볼 수 있는 목록 링크를 넣었습니다."
    ),
    "meta_links": [
        {
            "label": "public-apis (GitHub) — 주제별 API 목록",
            "url": "https://github.com/public-apis/public-apis",
        },
        {
            "label": "RapidAPI Hub — 무료 티어 필터",
            "url": "https://rapidapi.com/hub",
        },
    ],
    "legend": [
        "비밀 번호 없이: 공개 주소만으로 부를 수 있는 경우가 많음(약관·호출 제한은 여전히 있음).",
        "무료 비밀 번호: 가입 후 발급, 무료 범위 안에서만 사용.",
        "클라우드·회사 서비스 무료 체험: 아래 별칸 — 약관·과금은 회사에서 확인.",
    ],
}

# 용도별 — tier: no_key | free_key | mixed
API_BY_CATEGORY: list[dict[str, Any]] = [
    {
        "title": "날씨 · 기후",
        "apis": [
            {"name": "Open-Meteo", "use": "전 세계 기상·기후 그리드, 키 없이 사용 가능한 경우가 많음", "tier": "no_key", "url": "https://open-meteo.com/en/docs"},
            {"name": "Open-Meteo Air Quality", "use": "대기질", "tier": "no_key", "url": "https://open-meteo.com/en/docs/air-quality-api"},
            {"name": "7Timer!", "use": "천문·날씨(취미)", "tier": "no_key", "url": "http://www.7timer.info/doc.php?lang=en"},
        ],
    },
    {
        "title": "지리 · 지도 · 지오코딩",
        "apis": [
            {"name": "OpenStreetMap Nominatim", "use": "지오코딩·역지오코딩(이용 정책 준수 필수)", "tier": "no_key", "url": "https://nominatim.org/release-docs/develop/api/Overview/"},
            {"name": "OpenTopoData", "use": "고도·지형", "tier": "no_key", "url": "https://opentopodata.org/"},
            {"name": "Photon (Komoot)", "use": "지오코딩 검색", "tier": "no_key", "url": "https://photon.komoot.io/"},
            {"name": "Overpass API", "use": "OSM 데이터 쿼리", "tier": "no_key", "url": "https://wiki.openstreetmap.org/wiki/Overpass_API"},
        ],
    },
    {
        "title": "HTTP · 목업 · 학습",
        "apis": [
            {"name": "HTTPBin", "use": "요청/응답 테스트", "tier": "no_key", "url": "https://httpbin.org/"},
            {"name": "JSONPlaceholder", "use": "가짜 REST CRUD", "tier": "no_key", "url": "https://jsonplaceholder.typicode.com/"},
            {"name": "ReqRes", "use": "가짜 사용자·로그인 연습", "tier": "no_key", "url": "https://reqres.in/"},
            {"name": "DummyJSON", "use": "목업 JSON", "tier": "no_key", "url": "https://dummyjson.com/docs"},
        ],
    },
    {
        "title": "환율 · 금융(공개 데이터)",
        "apis": [
            {"name": "Frankfurter", "use": "ECB 기준 환율", "tier": "no_key", "url": "https://www.frankfurter.app/docs/"},
            {"name": "ExchangeRate-API (open)", "use": "환율(무료 플랜 한도)", "tier": "free_key", "url": "https://www.exchangerate-api.com/docs/overview"},
            {"name": "CoinGecko", "use": "암호화폐 시세(무료 티어)", "tier": "free_key", "url": "https://www.coingecko.com/en/api/documentation"},
        ],
    },
    {
        "title": "국가 · 행정 · 공공(국제)",
        "apis": [
            {"name": "REST Countries", "use": "국가 메타데이터", "tier": "no_key", "url": "https://restcountries.com/"},
            {"name": "Open Government APIs (목록)", "use": "국가별 공공 API 인덱스", "tier": "mixed", "url": "https://www.data.gov/"},
            {"name": "Wikidata API", "use": "지식 그래프 쿼리", "tier": "no_key", "url": "https://www.wikidata.org/wiki/Wikidata:Data_access/ko"},
        ],
    },
    {
        "title": "도서 · 학술 · 지식",
        "apis": [
            {"name": "Open Library", "use": "도서 메타·대출 정보", "tier": "no_key", "url": "https://openlibrary.org/developers/api"},
            {"name": "OpenAlex", "use": "학술 논문·인용 그래프", "tier": "no_key", "url": "https://docs.openalex.org/"},
            {"name": "Crossref REST", "use": "DOI·논문 메타데이터", "tier": "no_key", "url": "https://github.com/CrossRef/rest-api-doc"},
            {"name": "Internet Archive", "use": "아카이브 검색·메타", "tier": "free_key", "url": "https://archive.org/services/docs/api/"},
        ],
    },
    {
        "title": "우주 · 과학",
        "apis": [
            {"name": "NASA Open APIs", "use": "우주 이미지·천체 데이터(키 발급)", "tier": "free_key", "url": "https://api.nasa.gov/"},
            {"name": "Open Notify", "use": "ISS 위치·우주인 수", "tier": "no_key", "url": "http://open-notify.org/Open-Notify-API/"},
            {"name": "SpaceX API", "use": "발사·로켓 정보(비공식)", "tier": "no_key", "url": "https://github.com/r-spacex/SpaceX-API"},
        ],
    },
    {
        "title": "취미 · 팝컬처",
        "apis": [
            {"name": "PokéAPI", "use": "포켓몬 데이터", "tier": "no_key", "url": "https://pokeapi.co/docs/v2"},
            {"name": "SWAPI", "use": "스타워즈 데이터", "tier": "no_key", "url": "https://swapi.dev/documentation"},
            {"name": "Rick and Morty API", "use": "에피소드·캐릭터", "tier": "no_key", "url": "https://rickandmortyapi.com/documentation"},
            {"name": "The Dog API / The Cat API", "use": "이미지", "tier": "free_key", "url": "https://thedogapi.com/"},
        ],
    },
    {
        "title": "인명 · 데모 데이터",
        "apis": [
            {"name": "RandomUser", "use": "가짜 프로필", "tier": "no_key", "url": "https://randomuser.me/documentation"},
            {"name": "Genderize / Agify / Nationalize", "use": "이름 기반 추정(통계)", "tier": "no_key", "url": "https://genderize.io/"},
        ],
    },
    {
        "title": "명언 · 텍스트",
        "apis": [
            {"name": "Quotable", "use": "명언 JSON", "tier": "no_key", "url": "https://github.com/lukePeavey/quotable"},
            {"name": "ZenQuotes", "use": "명언(무료 티어)", "tier": "free_key", "url": "https://zenquotes.io/"},
        ],
    },
    {
        "title": "Git · 개발 생태계",
        "apis": [
            {"name": "GitHub REST API", "use": "공개 레포·이슈(인증 시 한도 상향)", "tier": "free_key", "url": "https://docs.github.com/en/rest"},
            {"name": "GitLab API", "use": "프로젝트·파이프라인", "tier": "free_key", "url": "https://docs.gitlab.com/ee/api/"},
            {"name": "npm Registry API", "use": "패키지 메타", "tier": "no_key", "url": "https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md"},
            {"name": "PyPI JSON API", "use": "파이썬 패키지 메타", "tier": "no_key", "url": "https://warehouse.pypa.io/api-reference/json.html"},
        ],
    },
    {
        "title": "이미지 · 아바타",
        "apis": [
            {"name": "DiceBear", "use": "아바타 SVG/PNG", "tier": "no_key", "url": "https://www.dicebear.com/how-to-use/http-api/"},
            {"name": "UI Faces / Picsum", "use": "플레이스홀더 이미지", "tier": "no_key", "url": "https://picsum.photos/"},
        ],
    },
    {
        "title": "뉴스 · 미디어(제한적 무료)",
        "apis": [
            {"name": "NewsAPI.org", "use": "뉴스 헤드라인(무료: 비상업·한도)", "tier": "free_key", "url": "https://newsapi.org/docs"},
            {"name": "GNews", "use": "뉴스(무료 티어)", "tier": "free_key", "url": "https://gnews.io/docs/v4"},
        ],
    },
    {
        "title": "IP · 네트워크",
        "apis": [
            {"name": "ip-api.com", "use": "IP 지리(비상업 무료)", "tier": "no_key", "url": "https://ip-api.com/docs"},
            {"name": "ipinfo.io", "use": "IP 메타(무료 티어)", "tier": "free_key", "url": "https://ipinfo.io/developers"},
        ],
    },
    {
        "title": "교통 · 공공 데이터(지역)",
        "apis": [
            {"name": "Transport for London Unified API", "use": "런던 대중교통(키 등록)", "tier": "free_key", "url": "https://api.tfl.gov.uk/"},
            {"name": "OpenChargeMap", "use": "전기차 충전소(무료 키)", "tier": "free_key", "url": "https://openchargemap.org/site/develop/api"},
        ],
    },
    {
        "title": "시간 · 달력",
        "apis": [
            {"name": "WorldTimeAPI", "use": "타임존·현지 시각", "tier": "no_key", "url": "http://worldtimeapi.org/"},
            {"name": "Holidays API (Nager.Date)", "use": "공휴일(오픈소스)", "tier": "no_key", "url": "https://date.nager.at/"},
        ],
    },
    {
        "title": "언어 · 번역(제한)",
        "apis": [
            {"name": "LibreTranslate (공개 인스턴스)", "use": "기계번역(인스턴스별 한도)", "tier": "mixed", "url": "https://libretranslate.com/docs/"},
            {"name": "Lingva Translate API", "use": "Google 번역 프런트 프록시(인스턴스)", "tier": "no_key", "url": "https://github.com/thedaviddelta/lingva-translate"},
        ],
    },
    {
        "title": "색상 · 디자인 토큰",
        "apis": [
            {"name": "The Color API", "use": "이름↔HEX 등", "tier": "no_key", "url": "https://www.thecolorapi.com/docs"},
        ],
    },
    {
        "title": "위키미디어 · 위키백과",
        "apis": [
            {"name": "Wikipedia REST API", "use": "요약·검색", "tier": "no_key", "url": "https://en.wikipedia.org/api/rest_v1/"},
            {"name": "MediaWiki API", "use": "편집·조회(정책 준수)", "tier": "no_key", "url": "https://www.mediawiki.org/wiki/API:Main_page/ko"},
        ],
    },
]

TIER_LABELS: dict[str, str] = {
    "no_key": "비밀 번호 없이(공개)",
    "free_key": "무료 비밀 번호·한도",
    "mixed": "서비스마다 다름",
}

# 기업·클라우드·B2B에서 자주 쓰는 ‘무료 티어·크레딧’ 요약 (법·과금은 사내 검토)
ENTERPRISE_CLOUD_FREE: list[dict[str, Any]] = [
    {
        "title": "하이퍼스케일러 무료 티어",
        "rows": [
            {"name": "AWS Free Tier", "notes": "12개월·항상 무료 범위 혼합", "url": "https://aws.amazon.com/free/"},
            {"name": "Google Cloud Free", "notes": "신규 크레딧 + 일부 Always Free", "url": "https://cloud.google.com/free"},
            {"name": "Microsoft Azure Free Account", "notes": "크레딧 + 일부 서비스 무료", "url": "https://azure.microsoft.com/free/"},
            {"name": "Oracle Cloud Free Tier", "notes": "ARM·스토리지 등 장기 무료 구성", "url": "https://www.oracle.com/cloud/free/"},
        ],
    },
    {
        "title": "DB · 백엔드 SaaS (무료 플랜)",
        "rows": [
            {"name": "Supabase", "notes": "Postgres·Auth·스토리지 무료 티어", "url": "https://supabase.com/pricing"},
            {"name": "Neon", "notes": "서버리스 Postgres", "url": "https://neon.tech/pricing"},
            {"name": "MongoDB Atlas", "notes": "M0 클러스터", "url": "https://www.mongodb.com/pricing"},
            {"name": "PlanetScale", "notes": "MySQL 호환(플랜 변동 시 문서 확인)", "url": "https://planetscale.com/pricing"},
        ],
    },
    {
        "title": "배포 · 엣지",
        "rows": [
            {"name": "Cloudflare Workers", "notes": "무료 요청 한도", "url": "https://developers.cloudflare.com/workers/platform/pricing/"},
            {"name": "Vercel Hobby", "notes": "개인·소규모 호스팅", "url": "https://vercel.com/pricing"},
            {"name": "Netlify", "notes": "스타터 티어", "url": "https://www.netlify.com/pricing/"},
        ],
    },
    {
        "title": "결제 · 커뮤니케이션(개발용)",
        "rows": [
            {"name": "Stripe Test Mode", "notes": "테스트 키로 결제 흐름 검증(실결제 아님)", "url": "https://stripe.com/docs/test-mode"},
            {"name": "Twilio Trial", "notes": "SMS·음성 트라이얼 크레딧", "url": "https://www.twilio.com/docs/guides/how-to-use-your-free-trial-account"},
        ],
    },
]
