import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Добавьте путь к проекту в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from models import Base, Category, SubCategory, Good, Size, Stock, Income, SupplierStock, Order, Sale, \
    ReportDetail

# Load .env file
from dotenv import load_dotenv

load_dotenv()

config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set up target metadata for 'autogenerate' support
target_metadata = Base.metadata

# Get the database URL from .env file
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
