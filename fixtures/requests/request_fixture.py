
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

update_request_mutation = '''
    mutation {
        updateRequest(requestId:2, title: "New request update") {
            request{
                title
            }
        }
    }
'''

update_request_response = {
    "data": {
        "updateRequest": {
            "request": {
                "title": "New Request Update",
            }
        }
    }
}

update_request_details_mutation = '''
    mutation {
        updateRequest(requestId:2, details: "New request details update") {
            request{
                details
            }
        }
    }
'''

update_request_details_response = {
    "data": {
        "updateRequest": {
            "request": {
                "details": "New request details update",
            }
        }
    }
}

update_request_invalid_title = '''
    mutation {
        updateRequest(requestId:2, title: "New") {
            request{
                title
            }
        }
    }
'''

update_request_invalid_id = '''
    mutation {
        updateRequest(requestId:10, title: "New request update") {
            request{
                title
            }
        }
    }
'''

update_approved_request = '''
    mutation {
        updateRequest(requestId:1, title: "New request update") {
            request{
                title
            }
        }
    }
'''

delete_request_mutation = '''
    mutation {
        deleteRequest(requestId:2) {
            request{
                id
            }
        }
    }
'''

delete_request_response = {
    "data": {
        "deleteRequest": {
            "request": {
                "id": "2",
            }
        }
    }
}

delete_request_invalid_id = '''
    mutation {
        deleteRequest(requestId:10) {
            request{
                id
            }
        }
    }
'''

delete_approved_request = '''
    mutation {
        deleteRequest(requestId:1) {
            request{
                id
            }
        }
    }
'''
