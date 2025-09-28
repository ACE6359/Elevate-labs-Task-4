# REST API with Flask – Task 4

## 📌 Objective

Build a **REST API** using Flask to manage user data with CRUD operations.

## 🛠 Tools & Technologies

* **Python 3.x**
* **Flask** (for API development)
* **Postman / Curl** (for testing endpoints)

## 📂 Project Structure

```
Task-4/
│── app.py        # Flask app with CRUD API
│── README.md     # Documentation
│── requirements.txt (optional)
```

---

## 🚀 Setup & Run

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd Task-4
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Server starts at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📌 API Endpoints

### 🔹 Get All Users

**GET** `/users`
Response:

```json
{
  "1": {"id": 1, "name": "Alice", "email": "alice@example.com"}
}
```

---

### 🔹 Get User by ID

**GET** `/users/<id>`
Response:

```json
{"id": 1, "name": "Alice", "email": "alice@example.com"}
```

---

### 🔹 Create User

**POST** `/users`
Body (JSON):

```json
{"name": "Alice", "email": "alice@example.com"}
```

Response:

```json
{"id": 1, "name": "Alice", "email": "alice@example.com"}
```

---

### 🔹 Update User

**PUT** `/users/<id>`
Body (JSON):

json
{"name": "Alice Smith"}


Response:

json
{"id": 1, "name": "Alice Smith", "email": "alice@example.com"}




### 🔹 Delete User

**DELETE** `/users/<id>`
Response:

json
{"message": "User deleted", "user": {"id": 1, "name": "Alice Smith", "email": "alice@example.com"}}

## 📌 Outcome

* Learned **Flask REST API basics**
* Implemented **CRUD operations**
* Practiced with **Postman & Curl**

