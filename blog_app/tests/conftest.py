import os
import tempfile

import pytest

from blog.models import Article

@pytest.fixture(autouse=True)
# The autouse flag is set to True so that it's automatically used by default before (and after) each test in the test suite
def database():
# creates a new database before each test and removes it after
    _, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.unlink(file_name)