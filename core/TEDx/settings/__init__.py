import os
from .base import *
from dotenv import main

main.load_dotenv()

if os.getenv("ENV_NAME") == "production":
    from .production import *
else:
    from .local import *

