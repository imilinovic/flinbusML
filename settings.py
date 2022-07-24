from environs import Env

env = Env()
env.read_env()

FLINBUSML_HOST_ADDRESS = env.str("FLINBUSML_HOST_ADDRESS", "0.0.0.0:8080")
