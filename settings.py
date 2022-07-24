from environs import Env

env = Env()
env.read_env()

GUNICORN_PORT = env.int("GUNICORN_PORT", 8080)
