import os
import environ
from pathlib import Path

from drf_template.loggers.dev import LOGGER_DEV
from drf_template.loggers.pro import LOGGER_PRO


class Environment:
    env = None

    ENV_MODE = None
    ENV_DEV = "DEV"
    ENV_PRO = "PRO"

    SECRET_KEY = None

    BASE_URL = "api/"
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOCAL_STORAGE = f"{BASE_DIR}/files"

    LOGGER_CFG = None

    _LOAD_STATUS = False

    @staticmethod
    def is_dev_mode():
        return Environment.ENV_MODE == Environment.ENV_DEV

    @staticmethod
    def load():
        if not Environment._LOAD_STATUS:
            Environment.__prepare_environ()
            Environment.__create_default_local_storage()
            Environment.__load_logger_configuration()

        Environment._LOAD_STATUS = True

    @staticmethod
    def get_enviroment_settings():
        Environment.load()
        if Environment.is_dev_mode():
            setting = 'drf_template.settings.dev'
        else:
            setting = 'drf_template.settings.pro'
        return setting

    @staticmethod
    def __create_default_local_storage():
        if not os.path.exists(Environment.LOCAL_STORAGE):
            os.makedirs(Environment.LOCAL_STORAGE)

    @staticmethod
    def __prepare_environ():
        Environment.env = environ.Env()
        Environment.env.read_env(Path(Environment.BASE_DIR, '.env'))
        Environment.ENV_MODE = Environment.env('ENV_MODE')

    @staticmethod
    def __load_logger_configuration():
        if Environment.is_dev_mode():
            Environment.LOGGER_CFG = LOGGER_DEV
        else:
            if not os.path.exists(Environment.env('LOGS_DIRECTORY')):
                raise Exception(f"[Logger] Directory does not exist - {Environment.env('LOGS_DIRECTORY')}")
            Environment.LOGGER_CFG = LOGGER_PRO
            Environment.LOGGER_CFG['handlers']['rotate']['filename'] = f"{Environment.env('LOGS_DIRECTORY')}/{Environment.LOGGER_CFG['handlers']['rotate']['filename']}"

if not Environment._LOAD_STATUS:
    Environment.load()
