import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    token = os.environ['TOKEN']
    prefix = "a!"