# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

# エンジンの作成
engine = create_engine(DATABASE_URL, echo=True)

# ベースクラスの作成
Base = declarative_base()

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# セッションの取得関数
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
