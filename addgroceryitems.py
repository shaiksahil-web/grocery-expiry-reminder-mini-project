import json
import boto3

# Table name is GroceryItem
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GroceryItem')

def lambda_handler(event, context):
    # Your new frontend sends: {"email": "...", "item": "...", "expiry_date": "..."}
    body = json.loads(event['body'])
    
    # Map the new field names to our DynamoDB column names
    user_email = body['email']
    item_name = body['item']
    expiry_date = body['expiry_date']

    # Put the item into our DynamoDB table
    table.put_item(
        Item={
            'user_email': user_email,    # Partition Key
            'expiry_date': expiry_date,  # Sort Key
            'itemName': item_name,
            'status': 'fresh'
            # We don't need purchaseDate anymore unless you want to add it
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        # The frontend expects a JSON response, so let's send one
        'body': json.dumps({'message': 'Item added successfully!'})
    }
