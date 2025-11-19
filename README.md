WhatsApp Product Review Collector

A full-stack application that collects product reviews from WhatsApp using Twilio Webhooks, stores them in PostgreSQL using a Flask API, and displays all reviews on a React frontend.

🚀 Features

WhatsApp-based chatbot using Twilio Sandbox

Multi-step conversation flow

Stores reviews in PostgreSQL

Flask REST API (/webhook, /api/reviews)

React frontend to display all reviews

Ngrok tunnel for public webhook access


🛠️ Prerequisites

Install the following:

Python 3.10+

PostgreSQL 15+

Node.js 16+

Ngrok

A Twilio account (WhatsApp Sandbox)

🔧 Backend Setup (Flask + PostgreSQL)

1️⃣ Navigate to backend folder

cd whatsapp-review-collector/backend

2️⃣ Create & activate virtual environment

python -m venv venv

.\venv\Scripts\Activate.ps1


3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure environment variables

Create .env inside backend:

DATABASE_URL=postgresql://postgres:<your_password>@localhost:5432/whatsapp_reviews

SECRET_KEY=secret123

5️⃣ Create PostgreSQL database

psql -U postgres

CREATE DATABASE whatsapp_reviews;

6️⃣ Run backend

python app.py


Backend will run at:

👉 http://127.0.0.1:5000

🌐 Ngrok Setup (Required for WhatsApp)

Open a new terminal (do NOT close backend):

ngrok http 5000


You will get a public HTTPS URL like:

https://abcd1234.ngrok-free.app

📲 Twilio Sandbox Setup

Go to Twilio Console →

Messaging → Try It Out → WhatsApp Sandbox

Join Sandbox by sending Twilio’s join code from your WhatsApp to:

+1 415 523 8886


Under Sandbox Configuration, set:

When a message comes in:

https://<your-ngrok-url>/webhook


Save changes.

🧪 Test WhatsApp Chatbot

Send “Hi” to your sandbox number.

Expected conversation:

<img width="1376" height="1018" alt="image" src="https://github.com/user-attachments/assets/ff4dfb3a-2659-4e49-9707-4aef097dd2e5" />


All reviews are stored in PostgreSQL.

📡 API Endpoints
✔ Get all reviews
GET /api/reviews

![WhatsApp Image 2025-11-19 at 14 01 07_9fc16290](https://github.com/user-attachments/assets/ce49a8b2-9e83-44f9-a657-fa05671b9006)


Example:

http://127.0.0.1:5000/api/reviews

🎨 Frontend Setup (React + Vite)

1️⃣ Navigate to frontend
cd whatsapp-review-collector/frontend

2️⃣ Install dependencies
npm install

3️⃣ Start frontend
npm run dev


Frontend runs at:

👉 http://localhost:5173

4️⃣ Frontend UI

![WhatsApp Image 2025-11-19 at 14 00 29_86870279](https://github.com/user-attachments/assets/07ca9bce-3d16-492e-a3fb-58612fbb32c4)


The app fetches data from:

http://localhost:5000/api/reviews


and displays all reviews in a table.
