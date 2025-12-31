# 🚀 Flask REST API Demo

A small but well-structured **Flask REST API** project built for **backend learning and portfolio demonstration**.

This project emphasizes **clean API design**, **consistent response schemas**, and **basic backend engineering practices** commonly used in real-world services.

---

## ✨ Highlights

- REST-style, resource-oriented API design
- Consistent JSON response format across all endpoints
- Centralized error handling
- Lightweight in-memory data store (demo purpose)
- Automated tests using `pytest`
- Clear project structure following Flask best practices

---

## 🛠 Tech Stack

- **Python 3**
- **Flask**
- **pytest**
- Git & GitHub for version control

---

## 📁 Project Structure

```text
RESTAPI/
├── app/
│   ├── __init__.py      # Application factory
│   ├── routes.py        # API endpoints
│   ├── errors.py        # Centralized error handlers
│   └── utils.py         # Shared utilities & response helpers
├── tests/
│   └── test_api.py      # API-level tests
├── run.py               # Application entry point
├── requirements.txt
└── README.md