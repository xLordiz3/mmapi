from fastapi import FastAPI

def createApp() -> FastAPI:
    app = FastAPI(
        title="mm",
        description="API for money management",
        version="1.0",
    )

    @app.get("/health")
    async def health() -> str:
        return "ok"
    return app