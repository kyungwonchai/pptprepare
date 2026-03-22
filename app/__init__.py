"""Flask application factory (Vibe coding)."""

from flask import Flask, request

from app.blueprints.slides import slides_bp


def create_app(config_name: str = "default") -> Flask:
    from app.config import config_by_name
    from app.data.slide_chapters import (
        ENDPOINT_TO_SLIDE_NUM,
        SLIDE_CHAPTERS,
        SLIDE_NAV_GROUPS,
        TOTAL_SLIDES,
    )

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    app.config.from_object(config_by_name[config_name])

    @app.context_processor
    def inject_app_name() -> dict[str, str]:
        return {"app_name": app.config["APP_NAME"]}

    @app.context_processor
    def inject_slide_nav() -> dict:
        ep = request.endpoint
        n = ENDPOINT_TO_SLIDE_NUM.get(ep) if ep else None
        return {
            "slide_chapters": SLIDE_CHAPTERS,
            "slide_nav_groups": SLIDE_NAV_GROUPS,
            "current_slide_n": n,
            "total_slides": TOTAL_SLIDES,
        }

    app.register_blueprint(slides_bp)
    return app
