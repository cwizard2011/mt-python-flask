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

user_mutation_query_empty_email = '''
mutation {
  createUser(email: ""
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

user_mutation_query_invalid_email = '''
mutation {
  createUser(email: "ssssss.cc"
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

user_mutation_query_short_name = '''
mutation {
  createUser(email: "cwiz@gmail.com"
            password:"password",
            firstname:"J",
            lastname:"Adeoye"){
    user {
      email,
      userRole,
    }
  }
}
'''

user_mutation_query_short_lastname = '''
mutation {
  createUser(email: "cwiz@gmail.com"
            password:"password",
            firstname:"Juliet",
            lastname:"A"){
    user {
      email,
      userRole,
    }
  }
}
'''

user_mutation_query_short_password = '''
mutation {
  createUser(email: "cwiz@gmail.com"
            password:"pas",
            firstname:"Juliet",
            lastname:"Adeoye"){
    user {
      email,
      userRole,
    }
  }
}
'''
