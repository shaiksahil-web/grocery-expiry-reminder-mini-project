import json
import boto3
from datetime import datetime, timedelta

# Initialize clients for DynamoDB and SNS
dynamodb = boto3.resource('dynamodb')
sns_client = boto3.client('sns')
table = dynamodb.Table('GroceryItem')

# === THIS IS THE UPDATED LINE ===
# The ARN for your SNS Topic has been added below.
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:415529767417:GroceryExpiryNotifications" 

def lambda_handler(event, context):
    today = datetime.now().date()
    # Let's check for items expiring in the next 2 days
    two_days_from_now = today + timedelta(days=2) 

    # Scan the entire table to check items for all users
    response = table.scan()
    items = response['Items']

    items_expiring_soon = []

    for item in items:
        # Get the item details from DynamoDB
        user_email = item['user_email']
        item_name = item['itemName']
        expiry_date_str = item['expiry_date']
        
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()

        # Check if the item is expiring soon and hasn't already been marked
        if today <= expiry_date <= two_days_from_now:
            # Add this item to a list of expiring items
            items_expiring_soon.append(f"- {item_name} (expires on {expiry_date_str}) for user {user_email}")
            
            # Update the item's status in DynamoDB so we don't notify again
            table.update_item(
                Key={
                    'user_email': user_email,
                    'expiry_date': expiry_date_str
                },
                UpdateExpression='SET #s = :val',
                ExpressionAttributeNames={'#s': 'status'},
                ExpressionAttributeValues={':val': 'expiring_soon'}
            )
    
    # If we found any expiring items, send ONE summary email
    if items_expiring_soon:
        subject = "Grocery Expiry Reminder!"
        
        # Create a nice, readable message for the email body
        message_body = "Hello!\n\nThis is a reminder from your Grocery Tracker. The following items are expiring soon:\n\n"
        message_body += "\n".join(items_expiring_soon)
        message_body += "\n\nDon't let your food go to waste!\n\n- Freshness Guardian"

        # Publish the message to the SNS topic
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message_body
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Found {len(items_expiring_soon)} expiring items and sent notification.")
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps("Expiry check complete. No expiring items found.")
    }
