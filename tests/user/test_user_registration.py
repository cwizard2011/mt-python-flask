from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_registration import (
    user_mutation_query, user_mutation_response,
    user_duplication_mutation_response,
    user_mutation_query_empty_email,
    user_mutation_query_invalid_email,
    user_mutation_query_short_name,
    user_mutation_query_short_lastname,
    user_mutation_query_short_password
)
from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestCreateUser(BaseTestCase):

    def test_user_creation(self):
        """
        Testing for User creation
        """
        execute_query = self.client.execute(
            user_mutation_query,
            context={'session': db_session})

        expected_response = user_mutation_response
        self.assertEqual(execute_query, expected_response)

    def test_user_duplication(self):
        """
        Testing for creation of an already existing user
        """
        self.client.execute(user_mutation_query,
                            context={'session': db_session})
        # Try to create a user twice
        query_response = self.client.execute(
            user_mutation_query,
            context={'session': db_session})

        expected_response = user_duplication_mutation_response
        self.assertEqual(query_response, expected_response)

    def test_create_invalid_email_user(self):
        """Testing for creating user with invalid email"""

        CommonTestCases.user_registration_assert_in(
            self,
            user_mutation_query_invalid_email,
            'email is not valid'
        )

    def test_create_empty_email_field_user(self):
        """Creating user with empty email field"""

        CommonTestCases.user_registration_assert_in(
            self,
            user_mutation_query_empty_email,
            'email is required field'
        )

    def test_create_user_short_firstname(self):
        """Creating user with short name"""

        CommonTestCases.user_registration_assert_in(
            self,
            user_mutation_query_short_name,
            'firstname can only be alphabets between 2 to 15 characters'
        )

    def test_create_user_short_lastname(self):
        """Creating user with short name"""

        CommonTestCases.user_registration_assert_in(
            self,
            user_mutation_query_short_lastname,
            'lastname can only be alphabets between 2 to 15 characters'
        )

    def test_create_user_short_password(self):
        """Creating user with short password"""

        CommonTestCases.user_registration_assert_in(
            self,
            user_mutation_query_short_password,
            'password must be between 8 and 32 characters'
        )
