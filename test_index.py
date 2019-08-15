from index import *
import json

print('Loading function')
 
def test_handler():
    file_event = open('event.json')
    event = json.load(file_event)
    status = handler(event, None)
    assert status['statusCode'] == 200
    assert status['body'] == "Hello \"SAM Local\""
    assert status['headers']['Content-Type'] == 'application/json'
