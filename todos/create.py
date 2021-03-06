import json
import logging
import os
import time
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if 'todo' not in data:
        logging.error("validation failed")
        raise Exception("Couldn't create the todo item")
      
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
      'id': str(uuid.uuid1()),
      'todo': data['todo'],
      'checked': False,
      'createdAt': timestamp,
      'updatedAt': timestamp,
    }

    table.put_item(Item=item)

    response = {
      "statusCode": 200,
      "body": json.dumps(item)
    }
    return response