import os
from dotenv import load_dotenv

# This line loads the variables from the .env file
load_dotenv()

class Config:
    # 1. Database Connection String
    # Prefer Neon/PostgreSQL DATABASE_URL, with a fallback for older local env files.
    database_url = os.getenv('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql+psycopg2://', 1)

    SQLALCHEMY_DATABASE_URI = database_url or (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    
    # 2. Security Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    # 3. File Settings
    # This finds your 'uploads' folder automatically
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit uploads to 16MB