import json

from lib.utils.mongo_client import MongoDBClient
from lib.validators import mongo_validators
from lib.logging.custom_logging import CustomizeLogger
from pathlib import Path

log_config_path = Path(__file__).resolve().parent / "logging" / "logging_config.json"
class APIController:

    def __init__(self):
        self.logger = CustomizeLogger.make_logger(log_config_path)
        self.mongo_client = MongoDBClient(self.logger) if mongo_validators.check_mongodb_parameters() else None