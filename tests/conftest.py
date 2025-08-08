from unittest.mock import Mock
from sphinxcontrib.ansi import ANSIColorParser
import pytest

# -----------------------------------------------------------------------------
# FIXTURES:
# -----------------------------------------------------------------------------
@pytest.fixture
def app():
    the_app = Mock()
    the_app.builder.name = "html"
    return the_app


@pytest.fixture
def parser():
    return ANSIColorParser()
