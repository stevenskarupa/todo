import json
import time
import logging
import os
from todos import decimalencoder
import boto3

dynamodb = boto3.resource('dynamodb')

def update(event, context):
  data = json.loads(event['body'])
  if 'todo' not in data or 'checked' not in data:
    logging.error("Validation Error - missing data")
    raise Exception("Couldn't update the todo item")
    return
  timestamp = int(time.time() * 1000)

  table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
  
  result = table.update_item(
    Key={
      'id': event['pathParameters']['id']
    },
    UpdateExpression = "set todo=:t, checked=:c, updatedAt=:u",
    ExpressionAttributeValues={
      ':t': data['todo'],
      ':c': data['checked'],
      ':u': timestamp
    },
    ReturnValues="UPDATED_NEW"   
  )

  response = {
    "statusCode": 200,
    "body": "Worked!"
  }

  return response