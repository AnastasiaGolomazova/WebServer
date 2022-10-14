import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).parent.parent))
from start import get_application


@pytest.fixture
def cli(event_loop, aiohttp_client):
    return event_loop.run_until_complete(aiohttp_client(get_application()))
