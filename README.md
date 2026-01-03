# Raj Dance Fitness Studio Website 🕺💃

A modern, responsive website for **Raj Dance Fitness Studio**, built using **Flask**, **HTML**, **CSS**, and **JavaScript**, and deployed on **Render**.

---

## 🌟 Features

- 🎥 Video-based Hero Section
- 🧘 Multiple Dance & Fitness Programs
- 👨‍🏫 Instructor Profiles
- ⭐ Testimonials Section
- 🖼️ Image & Video Gallery
- 📩 Contact Form with Email & WhatsApp Redirect
- 📱 Fully Responsive (Mobile, Tablet & Desktop)
- ⚡ Fast & SEO-friendly design

___________________________________

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Email Service:** SMTP (Gmail)
- **Deployment:** Render(local)
-**Deployment:** Hostinger(main) 
- **Server:** Gunicorn

____________________________________

## 📂 Project Structure
RajDanceFS/
│
├── app.py
├── requirements.txt
├── README.md
├── static/
│ ├── css/
│ ├── images/
│ └── videos/
│
└── templates/
├── index.html
├── about.html
├── services.html
├── instructors.html
├── gallery.html
└── contact.html
____________________________________________

## ▶️ Run Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/raj-dance-fitness-studio.git
cd raj-dance-fitness-studio

2️⃣ Create virtual environment
```python -m venv venv
```source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies
```pip install -r requirements.txt

4️⃣ Run the app
http://127.0.0.1:5000

Open browser:
http://127.0.0.1:5000

______________________________________
🚀 Deployment (Render)

1. Build Command

```pip install -r requirements.txt

2. Start Command

````gunicorn app:app



