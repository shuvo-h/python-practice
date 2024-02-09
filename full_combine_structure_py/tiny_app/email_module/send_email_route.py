from flask import Blueprint, jsonify, render_template, request
from tiny_app import send_email_bp
from tiny_app.email_module.email_controller import send_email

@send_email_bp.post('/send-email',)
def sendEmailBySMTP():
    data = request.get_json()
    print(785)
    result, status_code = send_email(data)
    return jsonify(result), status_code

@send_email_bp.get('/tpl')
def send_tpl():
    return render_template('ab.html')