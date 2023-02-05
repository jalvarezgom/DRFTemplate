log_file_bc = "drf_template_api.log"
LOGGER_PRO = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)-8s] %(name)-15s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "rotate": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "filename": log_file_bc,
            "when": "midnight",
            "interval": 1,
            "backupCount": 0,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["rotate"]
        }
    },
}