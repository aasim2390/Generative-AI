# 📌 API vs Webhook — Simple & Memorable Note  

## 🔹 What is an API?
- **API = Application Programming Interface**  
- Like a **menu in a restaurant** 🍔.  
  - You (the app) ask the waiter (API) for something.  
  - The kitchen (server) prepares it and gives it back.  
- It’s **pull-based** → You must **ask** every time.  

👉 Example:  
- Weather App → "Hey server, what’s the temperature?"  
- Server → "It’s 28°C today."  

---

## 🔹 API Request Types (HTTP Methods)
APIs usually work over the web using **HTTP methods**.  

1. **GET** → 📖 "Give me data"  
   - Example: Open Instagram feed → `api.instagram.com/feed`  

2. **POST** → ✍️ "Send new data"  
   - Example: Upload a new photo → `api.instagram.com/new_post`  

3. **PUT** → 🔄 "Update data"  
   - Example: Change profile picture → `api.instagram.com/profile/update`  

4. **DELETE** → 🗑 "Remove data"  
   - Example: Delete a comment → `api.instagram.com/comment/delete`  

---

## 🔹 API Status Codes (Server’s Reply)
When you ask an API, it **replies with a status code**:  

| Status Code | Meaning                              | Example Response                          |
|-------------|--------------------------------------|-------------------------------------------|
| **200** ✅   | OK – Request successful              | Weather data sent back                     |
| **201** 🎉  | Created – New data added             | New post uploaded successfully             |
| **400** ⚠️  | Bad Request – Wrong input            | You forgot required info                   |
| **401** 🔒  | Unauthorized – Not logged in         | You need to sign in                        |
| **404** ❓  | Not Found – Wrong URL                | The API endpoint doesn’t exist             |
| **500** 💥  | Server Error – Problem on their side | Instagram server is down                   |

---

## 🔹 What is a Webhook?
- **Webhook = Automated Messenger** 📩  
- Instead of you asking, the **server pushes info** to you when something happens.  
- It’s **push-based** → You **wait**, and the server tells you.  

👉 Example:  
- Customer makes a payment 💳  
- Payment service sends you → "Order #123 paid successfully ✅"  

---

## 🔹 Key Differences  

| Feature              | API (Pull)                               | Webhook (Push)                             |
|----------------------|-------------------------------------------|--------------------------------------------|
| Who starts?          | You (the app)                            | Server (automatically)                      |
| Data delivery        | Only when you ask                        | Instantly, as soon as it happens            |
| Status codes         | Yes ✅ (200, 404, 500, etc.)             | Not really – just sends you a message       |
| Best for             | On-demand info (weather, profile data)   | Real-time alerts (payments, notifications)  |
| Control              | You control timing                       | Server controls timing                      |

---

## 🔹 When to Use What?  
- ✅ **Use API** → If you need info whenever **you want** (e.g., check user profile, fetch stock price).  
- ✅ **Use Webhook** → If you need info **the moment it happens** (e.g., payment confirmation, order shipped).  

---

## 🎯 Quick Memory Tip  
- **API = Ask for it** (you pull data using GET, POST, PUT, DELETE → with status codes like 200, 404, 500).  
- **Webhook = Wait for it** (the server pushes data to you without asking).  
