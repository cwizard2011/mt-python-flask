from tests.base import BaseTestCase, CommonTestCases
from fixtures.requests.admin_update_fixture import (
    approve_request_invalid_action_mutation,
    approve_request_invalid_status_mutation,
    approve_request_mutation,
    approve_request_response,
    approve_request_invalid_id_mutation,
    reject_request_invalid_status_mutation,
    reject_request_mutation,
    reject_request_response,
    resolve_request_invalid_status_mutation,
    resolve_request_mutation,
    resolve_request_response
)
from fixtures.user.user_login import admin_login_mutation_token

import sys
import os
sys.path.append(os.getcwd())


class TestUpdateStatus(BaseTestCase):

    def test_approve_request(self):
        """
        Testing for Updating request status
        """

        login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            approve_request_mutation,
            approve_request_response
        )

    def test_reject_request(self):
        """Testing for rejecting a request"""

        login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            reject_request_mutation,
            reject_request_response
        )

    def test_resolve_request(self):
        """Testing for resolving a request"""

        login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            resolve_request_mutation,
            resolve_request_response
        )

    def test_update_invalid_action(self):
        """Testing for approving invalid action in kwargs"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            approve_request_invalid_action_mutation,
            "Request action can only be \\\'approve\\\', \\\'resolve\\\', or \\\'reject\\\'"  # noqa
        )

    def test_approve_request_invalid_id(self):
        """Testing for approving request with invalid id"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            approve_request_invalid_id_mutation,
            "The request with this id does not exist"
        )

    def test_approve_resolved_request(self):
        """Testing for approving a resolved request"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            approve_request_invalid_status_mutation,
            'You can only approve pending or rejected request'
        )

    def test_resolve_pending_request(self):
        """Testing for resolving a pending request"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            resolve_request_invalid_status_mutation,
            'You can only resolve an approved request'
        )

    def test_reject_resolved_request(self):
        """Testing for rejecting a resolved request"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            reject_request_invalid_status_mutation,
            'You can only reject a pending or approved request'
        )
