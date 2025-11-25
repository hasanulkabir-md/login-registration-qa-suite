# 📘 **Login & Registration QA Suite**

*A Complete QA Testing Project — Manual Tests • API Automation • Mock Backend • DB Validation*

---

## 🚀 Project Overview

This project demonstrates a **full QA workflow** for testing a Login & Registration system.
It includes:

* ✔️ Manual test cases (functional, negative, regression)
* ✔️ Bug reports in Jira-style format
* ✔️ API automation using **pytest + requests**
* ✔️ A mock backend built using **FastAPI**
* ✔️ SQLite database validation
* ✔️ Professional QA folder structure
* ✔️ Python virtual environment setup

This project is designed to reflect real-world QA work in SaaS platforms, membership systems, and authentication services.

---

## 📂 Folder Structure

```
login-registration-qa-suite/
├── backend/                 # FastAPI mock authentication service
│   └── main.py
│
├── api-tests/               # Automated API test suite
│   ├── test_api_login.py
│   └── utils/
│       └── client.py
│
├── db-validation/           # Checks database entries created by the backend
│   └── tests_db_validation.py
│
├── manual-tests/            # Manual QA work
│   ├── TestCases_Login_Registration.md
│   └── BugReports_Login_Registration.md
│
├── requirements.txt         # Dependencies for Python venv
└── README.md                # Documentation (this file)
```

---

## 🛠️ Tools & Technologies

| Area           | Tools                         |
| -------------- | ----------------------------- |
| Programming    | Python 3                      |
| API Framework  | FastAPI                       |
| API Automation | pytest, requests              |
| DB Validation  | SQLite (sqlite3)              |
| Manual QA      | Markdown                      |
| Environment    | Linux (Ubuntu), VS Code, venv |

---

## ▶️ How to Run the Project

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/login-registration-qa-suite.git
cd login-registration-qa-suite
```

---

### **2. Create & Activate Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### **3. Install Requirements**

```bash
pip install -r requirements.txt
```

---

## 🟦 Run the Mock FastAPI Backend

Open **Terminal 1**, activate venv, and run:

```bash
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

✔️ Keep this terminal running
❗ Do NOT close it

---

## 🟩 Run API Tests

Open **Terminal 2**, activate venv, and run:

```bash
pytest api-tests -q
```

Expected output:

```
2 passed in X.XXs
```

---

## 🟧 Test the API Manually (optional)

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"Password123!"}'
```

Expected:

```json
{"token":"fake-jwt-token"}
```

---

## 📄 Manual Testing Documentation

### **Test Cases**

`manual-tests/TestCases_Login_Registration.md`
Includes:

* Positive & negative login tests
* Registration tests
* Field validation
* Boundary Value Analysis (BVA)
* Equivalence Partitioning (EP)

---

### **Bug Reports**

`manual-tests/BugReports_Login_Registration.md`

Reports include:

* Steps to reproduce
* Expected vs actual
* Severity & priority
* Environment info

---

## 🗄️ Database Validation

`db-validation/tests_db_validation.py` validates:

* User entries stored after registration
* Correct fields in SQLite DB
* Data consistency

---

## 🎯 Why This Project is Valuable

This project shows:

* Understanding of QA fundamentals
* Ability to write structured manual test cases
* Ability to automate API tests
* Knowledge of backend API behavior
* Practical database validation skills
* Realistic QA workflow experience
* Clean and professional repository structure

---

## 📬 Author

**Md Hasanul Kabir**
📧 Email: hasanul.kabir09@gmail.com
🔗 GitHub: [https://github.com/hasanulkabir-md](https://github.com/hasanulkabir-md)

---


