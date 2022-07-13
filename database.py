from sqlalchemy import create_engine


engine = create_engine(
    "sqlite:///sqlite.db",
    connect_args={"check_same_thread": False},
)


