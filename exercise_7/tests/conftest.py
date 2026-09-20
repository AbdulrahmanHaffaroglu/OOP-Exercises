from datetime import date

import pytest

from hotel_reservation_system.models import Guest, Hotel, Room


@pytest.fixture
def hotel():
    return Hotel()


@pytest.fixture
def rooms():
    return (
        Room(101, "single", 80),
        Room(201, "double", 120),
        Room(301, "suite", 220),
    )


@pytest.fixture
def guests():
    return (
        Guest("G001", "Ada Lovelace", "ada@example.com"),
        Guest("G002", "Grace Hopper", "grace@example.com"),
        Guest("G003", "Alan Turing", "alan@example.com"),
    )


@pytest.fixture
def stay_dates():
    return date(2026, 10, 1), date(2026, 10, 4)
