
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

get_user_request_query = '''
    query {
        getUserRequest {
            title,
            details
        }
    }
'''

get_single_request_query = '''
    query {
        getSingleRequest (requestId:1) {
            title,
            details
        }
    }
'''

get_single_request_query_no_request = '''
    query {
        getSingleRequest (requestId:500) {
            title,
            details
        }
    }
'''

get_user_request_response = {
    "data": {
        "getUserRequest": [
            {
                "title": "My New Request",
                "details": "Setting a new request detail"
            }, {
                "title": "New Request Two",
                "details": "Setting a new request detail again"
            }
        ]
    }
}

get_single_request_response = {
    "data": {
        "getSingleRequest": {
            "title": "My New Request",
            "details": "Setting a new request detail"
        }
    }
}
