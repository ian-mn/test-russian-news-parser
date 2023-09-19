from seventy_eight_ru.settings import settings
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

url = URL.create(
    drivername="postgresql",
    username=settings.pg_user,
    password=settings.pg_pass.get_secret_value(),
    host=settings.pg_host,
    port=settings.pg_port,
    database=settings.pg_db,
)

engine = create_engine(url)
Base.prepare(autoload_with=engine, schema="content")

Posts = Base.classes.posts


def get_session() -> Session:
    """Returns session."""
    return Session(engine)
