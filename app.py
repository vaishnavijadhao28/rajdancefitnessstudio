from flask import Flask, render_template, request, redirect
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
app = Flask(__name__)

# ---------------- EMAIL CONFIG ----------------
OWNER_EMAIL = "theycallmehimansh@gmail.com"          # CHANGE THIS
SENDER_EMAIL = "digikeycentro@gmail.com"          # CHANGE THIS
SENDER_PASSWORD = "axgg bbka alna lsoy"        # CHANGE THIS
OWNER_WHATSAPP = "918275068637"                # CHANGE THIS


def send_email(name, phone, email, program, message):
    body = f"""
New Enquiry Received 🚨

Name: {name}
Phone: {phone}
Email: {email}
Program: {program}
Message: {message}
"""

    msg = MIMEText(body)
    msg["Subject"] = "New Dance Studio Enquiry"
    msg["From"] = SENDER_EMAIL
    msg["To"] = OWNER_EMAIL

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        program = request.form.get("program")
        message = request.form.get("message")

        # 1️⃣ Send Email to Owner
        send_email(name, phone, email, program, message)

        # 2️⃣ Prepare WhatsApp Message
        whatsapp_text = f"""
📩 New Enquiry – Raj Fitness Dance Studio (Amravati)
Name: {name}
Phone: {phone}
Email: {email}
Program: {program}
Message: {message}
"""
        encoded_text = urllib.parse.quote(whatsapp_text)

        whatsapp_url = f"https://wa.me/{OWNER_WHATSAPP}?text={encoded_text}"

        # 3️⃣ Redirect to WhatsApp
        return redirect(whatsapp_url)

    return render_template("contact.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/instructors")
def instructors():
    return render_template("instructors.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/privacy-policy")
def privacy_policy():
    return render_template(
        "privacy-policy.html",
        year=datetime.now().year
    )

@app.route("/terms-of-service")
def terms_of_service():
    return render_template(
        "terms-of-service.html",
        year=datetime.now().year
    )

if __name__ == "__main__":
    app.run(debug=True)
