# 🐾 Pet Adoption & Pet Shop Management System

A full-stack Django web application for pet adoption, pet product shopping, and shop management.

This platform allows users to browse pets and products, place orders, manage profiles, send complaints, and securely reset passwords using OTP email verification.

---

# 🚀 Features

## 👤 User Module
- User Registration & Login
- Browse Pets
- Browse Pet Products
- Add Products to Cart
- Place Orders
- View Order Status
- Profile Management
- Change Password
- Forgot Password with OTP Verification
- Send Complaints to Admin

---

## 🏪 Shop Module
- Shop Registration & Login
- Add / Edit / Delete Pets
- Add / Edit / Delete Products
- View Orders
- Manage Shop Profile
- Change Password

---

## 👨‍💼 Admin Module
- Admin Dashboard
- View All Shops
- View Shop Pets
- View Shop Products
- View Orders
- View Users
- View User Complaints
- Reply to Complaints
- Change Password

---

# 🔐 Security Features

- Password Hashing using Django Authentication
- OTP-based Password Reset
- Environment Variables using `.env`
- Protected SMTP Credentials
- Git Security using `.gitignore`

---

# 🛠️ Technologies Used

- Python
- Django
- SQLite3
- HTML5
- CSS3
- JavaScript
- jQuery
- SMTP Email Service

---

# 📂 Project Structure

```bash
miniproject/
│
├── manage.py
├── .env
├── .gitignore
├── miniproject/
├── myapp/
└── templates/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Pet-Adoption.git
cd Pet-Adoption
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install django
pip install python-dotenv
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in project root and add:

```env
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

---

## 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Run Server

```bash
python manage.py runserver
```

Open browser:

```bash
http://127.0.0.1:8000/
```

---

# 📧 Email Configuration

Inside `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

---

# 🔒 Important Notes

- Do NOT push `.env` file to GitHub
- Do NOT upload `db.sqlite3`
- Use Gmail App Password for SMTP
- Keep repository private if storing sensitive data

---

# 👨‍💻 Author

Sudeep Singh

---

# 📜 License

This project is for educational purposes.