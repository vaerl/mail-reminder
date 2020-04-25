from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import docker
import time
from conf import Conf

conf = Conf()

DOCKER_NAME = conf.ConfigSectionMap("docker")["database"]
DATABASE_DRIVER = conf.ConfigSectionMap("database")["driver"]
DATABASE_USERNAME = conf.ConfigSectionMap("database")["username"]
DATABASE_PASSWORD = conf.ConfigSectionMap("database")["password"]
DATABASE_HOST = conf.ConfigSectionMap("database")["host"]
DATABASE_PORT = conf.ConfigSectionMap("database")["port"]
DATABASE_DATABASE = conf.ConfigSectionMap("database")["database"]

# start docker-container using (docker-py)
client = docker.from_env()
client.containers.get(DOCKER_NAME).start()
# sleep as container starts up
time.sleep(0.5)

url = URL(DATABASE_DRIVER, DATABASE_USERNAME, DATABASE_PASSWORD,
          DATABASE_HOST, DATABASE_PORT, DATABASE_DATABASE)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
