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

---

### **B) View Grocery Items** (`getgroceryitems.py`)

**Purpose:**  
Fetches and returns all grocery items stored in DynamoDB, so the UI can display them.

**Code:**

---

## C) Expiry Checker Notification (expiryChecker.py)

Purpose:
Runs daily (using EventBridge Scheduler) to check items that are close to or past their expiry date.
If an item is expiring, it sends an email notification via SNS.

**Logic Used:**

Get today's date

Compare with each item's expiry date

If expiry date is today or tomorrow, send alert via SNS

**Code:**

---

## D) UI Web Page (index.html)

**Purpose:**
Front-end user interface to:

Add new grocery items

View the list of stored grocery items

**Flow:**
Web UI → API Gateway → Lambda → DynamoDB

**Features in UI:**
| Action           | Lambda Called        | API Triggered     |
| ---------------- | -------------------- | ----------------- |
| Add Grocery Item | `addgroceryitems.py` | POST API Endpoint |
| View All Items   | `getgroceryitems.py` | GET API Endpoint  |

## Note: The UI is static HTML + JavaScript, deployed:

**either locally**,

or in **AWS S3 (Static website hosting).**
