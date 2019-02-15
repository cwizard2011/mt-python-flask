from tests.base import BaseTestCase, CommonTestCases
from fixtures.requests.request_fixture import (
    create_request_mutation,
    create_request_response,
    create_request_short_title,
    create_request_short_details
)
from fixtures.user.user_login import (
    user_login_mutation_token, admin_login_mutation_token)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRequest(BaseTestCase):

    def test_create_request(self):
        """
        Testing for Creating request
        """

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            create_request_mutation,
            create_request_response
        )

    def test_create_request_short_title(self):
        """Testing for creating a request with short title"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            create_request_short_title,
            'title of a request can only be between 5 and 30 character'
        )

    def test_create_request_short_details(self):
        """Testing for creating a request with short title"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            create_request_short_details,
            'details of a request can only be between 15 and 300 characters'
        )

    def test_create_request_admin(self):
        """Testing for admin create request"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            create_request_mutation,
            'You are not authorized to perform this action'
        )

    def test_create_request_invalid_token(self):
        """Testing for creating request with invalid token"""
        token = 'gahahj-njdjd14525-jkhddj-jhjdj'
        CommonTestCases.token_assert_in(
            self,
            token,
            create_request_mutation,
            'Invalid token, please provide a valid token'
        )
