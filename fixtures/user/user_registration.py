null = None

user_mutation_query = '''
mutation {
  createUser(email: "cwizard2013@gmail.com"
            password:"password",
            firstname:"Juliet",
            lastname:"Adeoye"){
    user {
      email,
      userRole,
    }
  }
}
'''

user_mutation_response = {
    "data": {
        "createUser": {
            "user": {
                "email": "cwizard2013@gmail.com",
                "userRole": "user"
            }
        }
    }
}

user_duplication_mutation_response = {
    "errors": [{
        "message": "cwizard2013@gmail.com User already exists",
        "locations": [{
            "line": 3,
            "column": 3
        }],
        "path": ["createUser"]
    }],
    "data": {
        "createUser": null
    }
}
