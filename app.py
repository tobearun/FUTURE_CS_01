from flask import Flask, request, render_template, redirect, url_for, flash
import pyotp
import qrcode
import base64
from io import  BytesIO

app = Flask(__name__)
app.secret_key = "Testing"

key_gen = pyotp.random_base32()
totp = pyotp.TOTP(key_gen)

qr = totp.provisioning_uri(name="Arun", issuer_name="testing")
print(f"URI: {qr}")

qr_image = qrcode.make(qr)
buffer = BytesIO()
qr_image.save(buffer)
qr_data = base64.b64encode(buffer.getvalue()).decode()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        otp = request.form['otp']
        if totp.verify(otp):
            flash("OTP is Valid", "Success")
            return redirect(url_for('success'))
        else:
            flash("Invalid OTP", "Unsuccessful")
    return render_template('index.html', qr_data=qr_data)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)
