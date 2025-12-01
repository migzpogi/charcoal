import global_settings
from config import AppConfig

# This uses a Python file for configuration (global_settings.py)
if global_settings.DEBUG:
    print("Debug mode is ON")
else:
    print("Debug mode is OFF")

# This also uses a Python file for configuration (config.py)
app_config = AppConfig("my_app")
print(app_config.host)
print(repr(app_config))