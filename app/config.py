class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_crud"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key"