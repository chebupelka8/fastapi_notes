from dotenv import load_dotenv

import os


load_dotenv()

if (DATABASE_URL := os.getenv("DATABASE_URL")) is None:
    raise Exception("Not found DATABASE_URL.")
