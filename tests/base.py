# from flask_testing import TestCase
# from graphene.test import Client

# from app import create_app
# from schema import schema
# from helpers.database import engine, db_session, Base
# from api.users.models import User

# import sys
# import os
# import json

# sys.path.append(os.getcwd())


# class BaseTestCase(TestCase):

#     def create_app(self):
#         app = create_app('testing')
#         self.base_url = 'https://127.0.0.1:5000/mt'
#         self.headers = {'content-type': 'application/json'}
#         self.client = Client(schema)
#         return app

#     def setUp(self):
#         app = self.create_app()
#         self.app_test = app.test_client()
#         with app.app_context():
#             Base.metadata.create_all(bind=engine)
#             user = User(email="cwizard2011@gmail.com",
#                               password="september",
#                               firstname="Peter",
#                               lastname="Adeola")
#             user.save()
#             db_session.commit()

#     def tearDown(self):
#         app = self.create_app()
#         with app.app_context():
#             db_session.remove()
#             Base.metadata.drop_all(bind=engine)


# class CommonTestCases(BaseTestCase):
#     """Common test cases throught the code.
#     This code is used to reduce duplication
#     :params
#         - admin_token_assert_equal
#         - admin_token_assert_in
#         - user_token_assert_equal
#         - user_token_assert_in
#     """

#     def admin_token_assert_equal(self, query, expected_response):
#         """
#         Make a request with admin token and use assertEquals
#         to compare the values

#         :params
#             - query, expected_response
#         """
#         headers = {"Authorization": "Bearer" + " " + admin_api_token}
#         response = self.app_test.post(
#             '/mrm?query=' + query, headers=headers)
#         actual_response = json.loads(response.data)
#         self.assertEquals(actual_response, expected_response)

#     def lagos_admin_token_assert_equal(self, query, expected_response):
#         """
#         Make a request with admin token and use assertEquals
#         to compare the values

#         :params
#             - query, expected_response
#         """
#         headers = {"Authorization": "Bearer" + " " + admin_nigeria_token}
#         response = self.app_test.post(
#             '/mrm?query=' + query, headers=headers)
#         actual_response = json.loads(response.data)
#         self.assertEquals(actual_response, expected_response)

#     def admin_token_assert_in(self, query, expected_response):
#         """
#         Make a request with admin token and use assertIn
#         to compare the values

#         :params
#             - query, expected_response
#         """
#         headers = {"Authorization": "Bearer" + " " + admin_api_token}
#         response = self.app_test.post('/mrm?query=' + query, headers=headers)
#         self.assertIn(expected_response, str(response.data))

#     def lagos_admin_token_assert_in(self, query, expected_response):
#         """
#         Make a request with admin token and use assertIn
#         to compare the values

#         :params
#             - query, expected_response
#         """
#         headers = {"Authorization": "Bearer" + " " + admin_nigeria_token}
#         response = self.app_test.post('/mrm?query=' + query, headers=headers)
#         self.assertIn(expected_response, str(response.data))

#     def user_token_assert_equal(self, query, expected_response):
#         """
#         Make a request with user token and use assertEquals
#         to compare the values

#         :params
#             - query, expected_response
#         """
#         headers = {"Authorization": "Bearer" + " " + user_api_token}
#         response = self.app_test.post(
#             '/mrm?query=' + query, headers=headers)
#         actual_response = json.loads(response.data)
#         self.assertEquals(actual_response, expected_response)

#     def user_token_assert_in(self, query, expected_response):
#         """
#         Make a request with user token and use assertIn
#         to compare the values

#         :params
#             - query, expected_response
#         """
#         headers = {"Authorization": "Bearer" + " " + user_api_token}
#         response = self.app_test.post('/mrm?query=' + query, headers=headers)
#         self.assertIn(expected_response, str(response.data))


# def change_user_role_helper(func):
#     def func_wrapper(self):
#         headers = {"Authorization": "Bearer" + " " + user_api_token}
#         user = User(email='mrm@andela.com', name='this user',
#                     location="Nairobi", picture='www.andela.com/user')
#         user.save()
#         user_role = UsersRole(user_id=user.id, role_id=1)
#         user_role.save()
#         db_session().commit()
#         return headers
#     return func_wrapper
