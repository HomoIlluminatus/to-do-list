from fastapi import FastAPI

from core.config import APP_NAME, APP_HOST, APP_PORT, DEBUG

app = FastAPI(debug=DEBUG, title=APP_NAME)

app.include_router()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(host=APP_HOST, port=APP_PORT)
