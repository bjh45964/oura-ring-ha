"""Constants for oura_ring."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "oura_ring"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

"""Provides some constant for home assistant common things."""

CONF_ATTRIBUTE_STATE = 'attribute_state'

CONF_BACKFILL = 'max_backfill'
DEFAULT_BACKFILL = 0

CONF_MONITORED_DATES = 'monitored_dates'
DEFAULT_MONITORED_DATES = ['yesterday']
