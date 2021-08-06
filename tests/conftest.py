import sys
import os
import shutil
import typing

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../adroa')))
import adroa


@pytest.fixture
def directories() -> typing.Generator[None, None, None]:
    adroa.create_directories('my-app')
    yield None
    shutil.rmtree('my-app')
