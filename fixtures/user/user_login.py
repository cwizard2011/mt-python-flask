null = None

user_login_mutation_token = '''
mutation {
  loginUser(email: "sjuliet07@gmail.com"
            password:"september"){
    token
  }
}
'''

admin_login_mutation_token = '''
mutation {
  loginUser(email: "cwizard2011@gmail.com"
            password:"september"){
    token
  }
}
'''

user_login_mutation = '''
mutation {
  loginUser(email: "cwizard2011@gmail.com"
            password:"september"){
    user {
      email,
      userRole,
      firstname
    }
  }
}
'''

user_mutation_response = {
    "data": {
        "loginUser": {
            "user": {
                "email": "cwizard2011@gmail.com",
                "userRole": "admin",
                "firstname": "Peter"
            }
        }
    }
}

user_login_invalid_email = '''
mutation {
  loginUser(email: "cwizard201@gmail.com"
            password:"september"){
    user {
      email,
      userRole,
      firstname
    }
  }
}
'''

user_login_invalid_email_response = {
    "errors": [{
        "message": "User not found",
        "locations": [{
            "line": 3,
            "column": 3
        }],
        "path": [
            "loginUser"
        ]
    }],
    "data": {
        "loginUser": null
    }
}

user_login_invalid_password = '''
mutation {
  loginUser(email: "cwizard2011@gmail.com"
            password:"password"){
    user {
      email,
      userRole,
      firstname
    }
  }
}
'''

user_login_invalid_password_response = {
    "errors": [{
        "message": "email and password does not match",
        "locations": [{
            "line": 3,
            "column": 3
        }],
        "path": [
            "loginUser"
        ]
    }],
    "data": {
        "loginUser": null
    }
}
