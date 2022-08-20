from distutils.command.clean import clean
import json
import pathlib

import pytest
from jsonschema import validate,RefResolver

from blog.app import app
from blog.models import Article

@pytest.fixture
def client():
    app.config['TESTING'] =True

    with app.test_client() as client:
        yield client

def validate_payload(payload, schema_name):
    """
    Validate payload with selected schema
    """
    schemas_dir = str(
        f"{pathlib.Path(__file__).parent.absolute()}/schemas"
    )
    schema = json.loads(pathlib.Path(f"{schemas_dir}/{schema_name}").read_text())
    validate(
        payload,
        schema,
        resolver=RefResolver(
            "file://" + str(pathlib.Path(f"{schemas_dir}/{schema_name}").absolute()),
            schema  # it's used to resolve the file inside schemas correctly
        )
    )


