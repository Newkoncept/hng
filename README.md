# hng

# 🐱 Stage 0 — Dynamic Profile Endpoint (`/me`)

This project is part of the **HNG 13 Backend Internship (Backend Wizards)**.  
It implements a simple Django REST Framework API endpoint that returns your profile information,  
a random cat fact from the [Cat Facts API](https://catfact.ninja/fact),  
and the current UTC timestamp in ISO 8601 format.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Newkoncept/hng.git
cd hng
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
# Activate the virtual environment
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3️⃣ Install project dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Generate a Django secret key

Use Django’s built-in utility to create a secure key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key — you’ll add it to your environment file in the next step.

### 5️⃣ Create an `.env` file and add environment variables

Create a new file named `.env` in your project’s root directory and add:

```env
SECRET_KEY=<paste-your-generated-key-here>
PROFILE_EMAIL=you@example.com
PROFILE_NAME=Your Full Name
PROFILE_STACK=Python/Django
```

### 6️⃣ Run the Django development server

```bash
python manage.py runserver 0.0.0.0:8000
```

### 7️⃣ Test the API

Open your browser or use curl/Postman:

```bash
curl -s http://127.0.0.1:8000/me
```

✅ Expected Response:

```json
{
  "status": "success",
  "user": {
    "email": "you@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-17T12:34:56.789Z",
  "fact": "A random cat fact..."
}
```

---

## 📦 List of Dependencies

Main project dependencies:

```
Django>=5.0,<6.0
djangorestframework>=3.15,<3.17
requests>=2.31,<3.0
django-environ>=0.10,<1.0
```

Additional standard libraries automatically installed:

- asgiref
- sqlparse
- urllib3
- certifi
- charset-normalizer
- idna
- tzdata (for timezone support)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables Needed

| Variable        | Required | Description                                                |
| --------------- | -------- | ---------------------------------------------------------- |
| `SECRET_KEY`    | ✅       | Django secret key (generated with `get_random_secret_key`) |
| `PROFILE_EMAIL` | ✅       | Your personal email address                                |
| `PROFILE_NAME`  | ✅       | Your full name                                             |
| `PROFILE_STACK` | ✅       | Your backend stack (e.g., `Python/Django`)                 |

> ⚠️ **Note:** Never commit your `.env` file to GitHub.  
> Add `.env` to your `.gitignore` to keep your credentials safe.

---

## 🧪 Example Usage

Once the server is running locally:

- Visit [`http://127.0.0.1:8000/me`](http://127.0.0.1:8000/me) in your browser.
- Or use `curl` to fetch data:
  ```bash
  curl -i http://127.0.0.1:8000/me
  ```

Expected headers:

```
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
```

---

## 🧱 Project Structure

```
hng/
├── api/
│   ├── __init__.py
│   ├── urls.py          # Route for /me endpoint
│   ├── utils.py         # Helper functions (timestamp + external API)
│   └── views.py         # Core logic for /me endpoint
│
├── stage0/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py      # Django settings (env-based config)
│   ├── urls.py          # Root URL router
│   └── wsgi.py
│
├── .gitignore           # Ignore .env, venv, etc.
├── manage.py            # Django entry point
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🧠 Notes

- No database is used (no persistence required for Stage 0).
- A new cat fact is fetched on each request.
- If the external API fails, a fallback message is returned with HTTP 200.
- The timestamp always reflects the current UTC time in ISO 8601 format.
- Uses environment variables for sensitive data.

---

## 🧑‍💻 Author

**Oluwagbemiga Taiwo** 

---

## 🪪 License

MIT License © 2025 — _Feel free to fork and learn!_
