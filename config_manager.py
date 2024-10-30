import yaml
from pathlib import Path
import logging
import logging.config
import secrets

class ConfigManager:
    """Manages configuration and settings"""
    def __init__(self, config_path: Path = Path("config/jarvis.yml")):
        self.config_path = config_path
        self.config = self._load_config()
        self._setup_directories()
        self._setup_logging()

    def _load_config(self) -> dict:
        """Load configuration from YAML file"""
        if self.config_path.exists():
            with open(self.config_path) as f:
                return yaml.safe_load(f)
        return self._create_default_config()

    def _create_default_config(self) -> dict:
        """Create default configuration"""
        config = {
            "system": {
                "data_dir": "data/",
                "models_dir": "models/",
                "config_dir": "config/",
                "log_level": "INFO",
            },
            "security": {
                "enable_voice_auth": True,
                "encryption_key": self._generate_encryption_key(),
                "allowed_users": []
            },
        }
        self._save_config(config)
        return config

    def _save_config(self, config: dict):
        """Save configuration to YAML file"""
        # Ensure the config directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as f:
            yaml.dump(config, f)

    def _generate_encryption_key(self) -> str:
        """Generate a secure encryption key"""
        return secrets.token_hex(32)

    def _setup_directories(self):
        """Create necessary directories"""
        for dir_path in [self.config["system"]["data_dir"],
                         self.config["system"]["models_dir"],
                         self.config["system"]["config_dir"],
                         "logs"]:  # Adding logs directory here
            Path(dir_path).mkdir(parents=True, exist_ok=True)

    def _setup_logging(self):
        """Configure logging system"""
        logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                }
            },
            "handlers": {
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "standard",
                    "filename": "logs/jarvis.log",  # Ensure logs directory exists
                    "maxBytes": 10485760,
                    "backupCount": 5
                },
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard"
                }
            },
            "loggers": {
                "": {
                    "handlers": ["file", "console"],
                    "level": self.config["system"]["log_level"]
                }
            }
        }
        logging.config.dictConfig(logging_config)

    def get_encryption_manager(self):
        pass
