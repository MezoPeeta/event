import os
from .base import *
from dotenv import load_dotenv

load_dotenv()

if os.getenv("ENV_NAME") == "production":
    from .production import *
else:
    from .local import *

