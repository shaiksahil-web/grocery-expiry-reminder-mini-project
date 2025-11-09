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

## 3️⃣ DynamoDB Table Structure

| Attribute | Type | Purpose |
|----------|------|---------|
| `itemName` | String (Partition Key) | Grocery item name |
| `expiryDate` | String (YYYY-MM-DD) | Expiry date of item |

Example Record:
```json
{
  "itemName": "Bread",
  "expiryDate": "2025-01-10"
}


## 3️⃣ DynamoDB Table Structure
