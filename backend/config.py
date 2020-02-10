import os


class Config:
    REDIS_HOSTNAME = os.environ.get("REDIS_HOSTNAME") or "redis"
    TIMEOUT = 60


class DevConfig(Config):
    REDIS_HOSTNAME = "192.168.5.1"
