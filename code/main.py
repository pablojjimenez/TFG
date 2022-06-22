import uvicorn

from config.general_config import get_config

if __name__ == "__main__":
    config = get_config()
    uvicorn.run("app:app", host=config.host, port=config.port, reload=config.debug_app)
