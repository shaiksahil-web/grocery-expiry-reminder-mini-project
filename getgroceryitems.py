import json
import boto3
from boto3.dynamodb.conditions import Key

# Table name is GroceryItem
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GroceryItem')

def lambda_handler(event, context):
    # Your new frontend sends the parameter as 'email'
    user_email = event['queryStringParameters']['email']

    # Query the table using the partition key 'user_email'
    response = table.query(
        KeyConditionExpression=Key('user_email').eq(user_email)
    )
    items = response['Items']

    # IMPORTANT: Wrap the list of items in a dictionary with the key "items"
    # because your JavaScript expects this structure: result.items
    response_body = {
        'items': items
    }

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response_body)
    }
