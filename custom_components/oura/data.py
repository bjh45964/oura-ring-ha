"""Custom types for oura_ring."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import OuraRingApiClient
    from .coordinator import OuraRingDataUpdateCoordinator


type OuraRingConfigEntry = ConfigEntry[OuraRingData]


@dataclass
class OuraRingData:
    """Data for the Oura Ring integration."""

    client: OuraRingApiClient
    coordinator: OuraRingDataUpdateCoordinator
    integration: Integration
