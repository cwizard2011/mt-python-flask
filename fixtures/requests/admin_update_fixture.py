approve_request_mutation = '''
    mutation {
        updateRequestStatus(requestId:2, action:"approve") {
            request{
                currentStatus
            }
        }
    }
'''

approve_request_response = {
    "data": {
        "updateRequestStatus": {
            "request": {
                "currentStatus": "approved"
            }
        }
    }
}

approve_request_invalid_id_mutation = '''
    mutation {
        updateRequestStatus(requestId:600, action:"approve") {
            request{
                currentStatus
            }
        }
    }
'''

resolve_request_mutation = '''
    mutation {
        updateRequestStatus(requestId:1, action:"resolve") {
            request{
                currentStatus
            }
        }
    }
'''

resolve_request_response = {
    "data": {
        "updateRequestStatus": {
            "request": {
                "currentStatus": "resolved"
            }
        }
    }
}

reject_request_mutation = '''
    mutation {
        updateRequestStatus(requestId:2, action:"reject") {
            request {
                currentStatus
            }
        }
    }
'''

reject_request_response = {
    "data": {
        "updateRequestStatus": {
            "request": {
                "currentStatus": "rejected"
            }
        }
    }
}

approve_request_invalid_action_mutation = '''
    mutation {
        updateRequestStatus(requestId:2, action:"approves") {
            request{
                currentStatus
            }
        }
    }
'''

approve_request_invalid_status_mutation = '''
    mutation {
        updateRequestStatus(requestId:1, action:"approve") {
            request{
                currentStatus
            }
        }
    }
'''

reject_request_invalid_status_mutation = '''
    mutation {
        updateRequestStatus(requestId:3, action:"reject") {
            request{
                currentStatus
            }
        }
    }
'''

resolve_request_invalid_status_mutation = '''
    mutation {
        updateRequestStatus(requestId:2, action:"resolve") {
            request{
                currentStatus
            }
        }
    }
'''

get_all_request_query = '''
    query {
        getAllRequest {
            title,
            details
        }
    }
'''

get_all_request_response = {
    "data": {
        "getAllRequest": [
            {
                "title": "My New Request",
                "details": "Setting a new request detail"
            },
            {
                "title": "New Request Two",
                "details": "Setting a new request detail again"
            },
            {
                "title": "New Request Three",
                "details": "Setting a new request detail now",
            }
        ]
    }
}
