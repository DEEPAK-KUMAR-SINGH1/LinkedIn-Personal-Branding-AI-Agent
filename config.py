from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./influence.db'
    SECRET_KEY: str = 'replace_this'
    LINKEDIN_CLIENT_ID: str = ''
    LINKEDIN_CLIENT_SECRET: str = ''
    LINKEDIN_REDIRECT_URI: str = 'http://localhost:8000/auth/linkedin/callback'
    OPENAI_API_KEY: str = ''

    class Config:
        env_file = Path('.') / '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
