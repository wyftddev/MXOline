#encoding=utf-8
import random, string

from django.core.mail import send_mail

from users.models import EmailVertifyRecord
from MXOnline.settings import EMAIL_FROM

def send_email(email, send_type="register"):
    email_record = EmailVertifyRecord()
    code = "".join(random.sample(string.ascii_letters + string.digits, 16))
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = u"慕学在线网"
        email_body = u"请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(subject=email_title, message=email_body, from_email=EMAIL_FROM, recipient_list=[email])
        return send_status
    elif send_type == "forget":
        email_title = u"慕学在线网"
        email_body = u"请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(subject=email_title, message=email_body, from_email=EMAIL_FROM, recipient_list=[email])
        return send_status
