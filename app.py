from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for using flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/bank security')
def bank_security():
    return render_template("bank_security.html")

@app.route('/prime house keeping service')
def prime_house_keeping_service():
    return render_template("prime_house_keeping_service.html")

@app.route('/hotel & stores security')
def hotel_security():
    return render_template("hotel_security.html")

@app.route('/commerical complex')
def commerical_complex():
    return render_template("commerical_complex.html")

@app.route('/residential security & construction site')
def residential_security_construction_site():
    return render_template("residential_security_construction_site.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Please fill out all fields.', 'error')
        return redirect(url_for('contact'))

    # Here you would typically save the data to a database or send an email

    flash('Thank you for your message!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
