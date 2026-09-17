import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


# =========================================================
# Load environment variables
# =========================================================

load_dotenv()


# =========================================================
# Database Configuration
# =========================================================

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")


# =========================================================
# Validate Configuration
# =========================================================

required_variables = {
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
    "DB_NAME": DB_NAME,
}


missing_variables = [
    name
    for name, value in required_variables.items()
    if not value
]


if missing_variables:
    raise RuntimeError(
        "Missing database environment variables: "
        + ", ".join(missing_variables)
    )


# =========================================================
# Database Connection
# =========================================================

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_connection():
    """
    Create and return a SQLAlchemy PostgreSQL engine.
    """

    return create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
    )