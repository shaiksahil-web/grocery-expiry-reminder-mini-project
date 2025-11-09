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


## 4️⃣ Lambda Functions Used
A) Add Grocery Item (addgroceryitems.py)

Called from the UI → API → Lambda → DynamoDB

B) View Grocery Items (getgroceryitems.py)

Fetches stored data for UI display.

C) Expiry Checker (expiryChecker.py)

Runs daily → checks dates → sends email via SNS.

---

## 5️⃣ Workflow Diagram
User → Web UI → API Gateway → addgroceryitems Lambda → DynamoDB Store
User → Web UI → API Gateway → getgroceryitems Lambda → Display Items
Daily Event → expiryChecker Lambda → SNS Email Alert

---

## 6️⃣ Errors Faced & Fixes
| Problem                 | Reason                             | Solution                                           |
| ----------------------- | ---------------------------------- | -------------------------------------------------- |
| SNS Email Not Received  | Subscription unconfirmed           | Confirm the email link from AWS SNS                |
| API Returning 500 Error | Lambda response missing statusCode | Always return `{"statusCode": 200, "body": "msg"}` |
| Wrong Date Comparison   | Comparing string to date           | Convert using `datetime.strptime(...).date()`      |
| CORS Issue in UI        | API not allowing browser requests  | Enable CORS in API Gateway                         |

---

## 7️⃣ Frontend (index.html)

Simple UI to input item and view stored items.
This can be hosted on EC2, S3, or local browser.

---

## 8️⃣ Future Enhancements
| Feature            | Description                          |
| ------------------ | ------------------------------------ |
| Mobile App Version | Replace HTML UI with Android/iOS app |
| Multi-User Support | Store items separately per user ID   |
| Expiry Forecasting | Show suggestions before expiry       |

---

## 9️⃣ Conclusion

This project demonstrates how AWS Serverless can automate everyday tasks.
No servers. No maintenance. Very low cost.
A simple and effective real-life use case of Lambda + DynamoDB + SNS.

---

👤 Author

SK Sahil
AWS | DevOps | Cloud Enthusiast
