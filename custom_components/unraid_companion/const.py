"""Constants for the Unraid integration."""

from datetime import timedelta

from homeassistant.const import CONF_API_KEY, CONF_HOST

DOMAIN = "unraid"

DEFAULT_POLL_INTERVAL = timedelta(minutes=30)
COORD_DATA_KEY = "unraid_data"
