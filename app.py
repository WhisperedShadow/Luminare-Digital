from flask import Flask, render_template, request, redirect, url_for
from ourmail import send_mail
from db import services, subservices, highlights
import os
from dotenv import load_dotenv

cloud = os.getenv('CLOUD')

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = services()
    subser = subservices()
    highlight = highlights()
    if request.method=='POST':
        name = request.form['user-name']
        company_name = request.form['company-name']
        email = request.form['email']
        phone_number = request.form['ph-no']
        interest_service = request.form['serv']  
        message = request.form['msg']
        print(name, company_name, email,phone_number,interest_service,message)
        send_mail(name, company_name, email, phone_number, interest_service, message)
        return redirect(url_for('index'))
        
    else:
        return render_template('index.html', data=data, subdata=subser, cloud=cloud, highlights=highlight)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))