"""Test configuration for SDR Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "sdr-agent", "category": "Sales"}
