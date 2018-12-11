import smtplib

mailserver = smtplib.SMTP()
mailserver.connect('smtp.partner.outlook.cn:587')
mailserver.ehlo()
mailserver.starttls()
mailserver.login('alert@mail.cn', 'Bpassword')
mailserver.sendmail('alert@mail.cn','touser@mail.cn','python email')
mailserver.quit()
