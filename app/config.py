"""Application configuration (Vibe coding)."""


class Config:
    SECRET_KEY = "dev-change-in-production"
    APP_NAME = "Vibe coding"
    SLIDE_TITLE = "개발 도구 · AI · 데이터 생태계"


class DevelopmentConfig(Config):
    DEBUG = True


config_by_name = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
}
