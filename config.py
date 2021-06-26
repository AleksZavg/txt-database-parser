from environs import Env

env = Env()
env.read_env()

config = {
    "dashboard":{
        "url_link": env.str("url_link"), 
        "file": env.str("file_name"),
        "timeout": env.str("timeout")
        },
    "port": env.int("port")
    }
