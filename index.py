import json
 
print('Loading function')
 
def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return {'statusCode': 200,
            'body': "Hello " + json.dumps(event['body']),
            'headers': {'Content-Type': 'application/json'}}
