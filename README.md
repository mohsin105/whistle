Absolutely! Here's a complete and professional `README.md` file for your **Whistle** social media backend project built with Django REST Framework:

---

```markdown
# 📣 Whistle — Social Media Backend API (DRF)

Whistle is a RESTful social media backend built with Django REST Framework. It provides a scalable and secure API structure for handling common social networking features like user authentication, story sharing, comments, and profile management. Swagger (OpenAPI) documentation is included for easy testing and collaboration.

---

## 🚀 Features

- ✅ **User Authentication & Authorization**
  - JWT-based authentication using **Djoser** + **SimpleJWT**
  - Email verification flow
- 👤 **Profile Management**
  - User profile creation and updates
  - Secure endpoint handling for profile data
- 📸 **Stories Endpoint**
  - Create, retrieve, and list user stories
  - Basic CRUD operations for user content
- 💬 **Comments Endpoint**
  - Comment on user stories
  - Nested serializers and relationship handling
- 📘 **API Documentation**
  - Integrated with **Swagger UI** via `drf_yasg`

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** Djoser, SimpleJWT
- **Docs:** drf-yasg (Swagger/OpenAPI)
- **Database:** PostgreSQL / SQLite (development)
- **Email Service:** Django's Email Backend (configurable for SMTP)

---

## 📂 Project Structure (Simplified)

```

whistle/
├── manage.py
├── whistle/               # Project settings
├── users/                 # User auth, registration, profiles
├── stories/               # Story creation and listing
├── comments/              # Comment handling
├── templates/             # Email templates
├── static/                # Static files
└── requirements.txt

````

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/whistle.git
cd whistle
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 📨 Email Verification Setup

Configure your email backend in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

---

## 🔑 Authentication (Djoser + JWT)

Sample login endpoint:

```http
POST /auth/jwt/create/
{
  "email": "user@example.com",
  "password": "password123"
}
```

Token refresh:

```http
POST /auth/jwt/refresh/
```

---

## 🧪 API Documentation

Visit Swagger UI at:

```
http://localhost:8000/swagger/
```

---

## 📌 Endpoints Overview

| Feature      | Endpoint                  | Method(s)       |
| ------------ | ------------------------- | --------------- |
| Auth         | `/auth/jwt/create/`       | POST            |
| Register     | `/auth/users/`            | POST            |
| Verify Email | `/auth/users/activation/` | POST            |
| Profile      | `/users/me/`         | GET, PUT, PATCH |
| Stories      | `/stories/`               | GET, POST       |
| Comments     | `stories/pk/comments/`              | GET, POST       |

---



Absolutely! Here's a ready-to-use **`.env` variables section** you can include in your `README.md`, showing developers how to configure the environment variables required to run the **Whistle** project securely.

---

### 🔐 Environment Variables

Create a `.env` file in your project root and add the following environment variables:

<details>
<summary><strong>📄 Sample <code>.env</code> file</strong> (click to expand)</summary>

```dotenv
# Django settings
SECRET_KEY=your-django-secret-key
DEBUG=True

# Allowed hosts
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Email settings (for verification)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_app_password

# JWT Settings (Optional overrides for SimpleJWT)
SIMPLE_JWT_ACCESS_TOKEN_LIFETIME=5  # in minutes
SIMPLE_JWT_REFRESH_TOKEN_LIFETIME=1  # in days
```

</details>

---

### ✅ How to Use the `.env` File

1. Install **`python-decouple`**:

   ```bash
   pip install python-decouple
   ```

2. Replace direct values in your `settings.py` with `config()` calls:

   ```python
   from decouple import config

   SECRET_KEY = config('SECRET_KEY')
   DEBUG = config('DEBUG', cast=bool)
   EMAIL_HOST_USER = config('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
   ```

3. Make sure to **add `.env` to your `.gitignore`** file:

   ```gitignore
   .env
   ```

---



## 🧑‍💻 Contribution

Feel free to fork, contribute, or suggest improvements via issues and PRs!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For queries or collaboration:

* **Author:** Your Name
* **Email:** [mohsinibnaftab@gmail.com](mailto:your.email@example.com)
* **GitHub:** [@yourusername](https://github.com/yourusername)

```

---

Would you like me to help you generate the `requirements.txt` or include deployment instructions (e.g., for Render or Fly.io)?
```
