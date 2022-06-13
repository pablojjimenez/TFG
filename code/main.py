import uvicorn

from config.general_config import HOST, PORT, DEBUG_APP

if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT, reload=DEBUG_APP)
