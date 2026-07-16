import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DB_HOST"))
print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))