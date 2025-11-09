# Grocery Expiry Reminder – Mini Project (Serverless)

This mini project reminds users when their grocery items are about to expire.  
It reduces food waste and works **fully serverless** using AWS services.

---

## 1️⃣ Problem Statement

We often forget grocery expiry dates which leads to **food and money waste**.  
This project sends an **email alert** before any stored grocery item expires.

---

## 2️⃣ AWS Architecture Used

| Service | Purpose |
|--------|---------|
| **API Gateway** | Provides HTTP endpoints for frontend |
| **Lambda Functions** | Runs backend logic without servers |
| **DynamoDB** | Stores grocery item information |
| **SNS** | Sends email notifications to the user |
| **EventBridge Scheduler** | Triggers expiry check daily |
| **HTML UI** | Simple form-based UI for adding/viewing items |

---
step 3 in the last
---

## 4️⃣ Lambda Functions Used

This project uses **three AWS Lambda functions**, each serving a specific purpose in the Grocery Expiry Reminder workflow.

---

### A) Add Grocery Item (`addgroceryitems.py`)

**Purpose:**  
Adds a new grocery item along with its expiry date to DynamoDB.

**Flow:**  
UI → API Gateway → Lambda → DynamoDB

**Code:**
```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('groceryitems')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    table.put_item(Item={
        'itemName': body['itemName'],
        'expiryDate': body['expiryDate']
    })
    return {"statusCode": 200, "body": "Item Added Successfully"}

---

### B) View Grocery Items (getgroceryitems.py)

Purpose:
Retrieves all grocery items stored in DynamoDB and displays them in the UI.

Code:

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('groceryitems')

def lambda_handler(event, context):
    response = table.scan()
    return {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    }

