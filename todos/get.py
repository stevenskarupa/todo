import os
import json
from todos import decimalencoder
import boto3

dynamodb = boto3.resource('dynamodb')

def get(event,context):
  table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

  result = table.get_item(
    Key={
      'id': event['pathParameters']['id']
    }
  )

  response = {
    "statusCode": 200,
    "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
  }
  return response