import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8000))
DEBUG_APP = bool(os.getenv('DEBUG', True)) in ('true', 'false')
