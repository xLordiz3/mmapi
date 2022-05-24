from fastapi import FastAPI

def createApp() -> FastAPI:
    app = FastAPI(
        title="mmapi",
        description="API for money management",
        version="1.0",
    )

    @app.get("/health")
    async def health() -> str:
        return "ok"

    #All transactions
    @app.get("")

    #Totals for all and per location
    @app.get("/totals")
    async def totals() -> str:
        return
    
    #Get specific location amounts
    @app.get("/{")
    async def locations() -> str:
        return
    return app