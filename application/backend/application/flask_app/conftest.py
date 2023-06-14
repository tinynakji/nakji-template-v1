import contextlib
import logging
import os
import pytest
from unittest.mock import patch
import uuid

from sqlalchemy import create_engine, text as sql_text, schema as sqlalchemy_schema
from sqlalchemy.orm import sessionmaker

from flask_app.app import create_app

from flask_app.api.users.models import User
from flask_app.config import TestConfig
from flask_app.db.models import BaseModel
from flask_app.db.database import TEST_DB_URI, DB_SCHEMA
from flask_app.utils.constants import TEST_USER_PHONE_NUMBER, TEST_USER_FULL_NAME, TEST_USER_EMAIL, TEST_USER_USERNAME



##########################################
# Authentication related
##########################################
# Commenting this out until needed
# @pytest.fixture(scope="session", autouse=True)
# def default_session_fixture():
#     """
#     :type request: _pytest.python.SubRequest
#     :return:
#     """
#     logging.info("Patching auth service")

#     with patch('flask_app.utils.auth0_service.Auth0Service.validate_request') as patched_validate_request:
#         patched_validate_request.return_value = {
#             "sub": "arbitrary|sub"
#         }

#         with patch('flask_app.utils.auth0_service.Auth0Service.get_auth0_user') as get_auth0_user_patched:
#             get_auth0_user_patched.return_value = {     
#                 "phone_number": TEST_USER_PHONE_NUMBER
#             }
#             yield
    
#     logging.info("Patching complete. Unpatching")

##########################################
# Application and DB Session fixtures
##########################################
from sqlalchemy import DDL, event
from sqlalchemy.schema import CreateSchema

# Create schema!
event.listen(BaseModel.metadata, 'before_create', DDL(f"CREATE SCHEMA IF NOT EXISTS {DB_SCHEMA}"))

@pytest.fixture(scope="session")
def test_db_engine():
    """
Taking cues from https://coderpad.io/blog/development/a-guide-to-database-unit-testing-with-pytest-and-sqlalchemy/
"""
    engine = create_engine(TEST_DB_URI)
    return engine

@pytest.yield_fixture(scope="function")
def test_app():
    app = create_app(TestConfig)
    with app.app_context():   
        yield app

@pytest.fixture(scope='function')
def session(test_app):
    return test_app.session

@pytest.yield_fixture(scope='function')
def client(test_app, test_db_engine):
    # This is done for every test; create all tables and then drop them
    BaseModel.metadata.create_all(test_db_engine)

    yield test_app.test_client()

    # Need to close the session to prevent hanging
    test_app.session.close()
    BaseModel.metadata.drop_all(bind=test_db_engine)
    

##########################################
# CLEAN UP SUITE
##########################################
def pytest_sessionfinish(session, exitstatus):
    # Leaving here in case there is clean up needed
    pass

class TestBase:

    def add_authenticated_user(self, session):
        # Use this to test endpoints that require an authenticated user
        auth_user = User(
            uuid=uuid.uuid4(),
            email=TEST_USER_EMAIL,
            username=TEST_USER_USERNAME
        )

        session.add(auth_user)
        session.commit()

        return auth_user