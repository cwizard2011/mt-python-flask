
create_request_mutation = '''
    mutation {
        createRequest(
            title: "New request 2", details:"trying to make this work") {
            request{
                title,
                details
            }
        }
    }
'''

create_request_response = {
    "data": {
        "createRequest": {
            "request": {
                "title": "New Request 2",
                "details": "trying to make this work"
            }
        }
    }
}

create_request_short_title = '''
    mutation {
        createRequest(
            title: "new", details:"trying to make this work") {
            request{
                title,
                details
            }
        }
    }
'''

create_request_short_details = '''
    mutation {
        createRequest(
            title: "New request 11", details:"trying") {
            request{
                title,
                details
            }
        }
    }
'''
