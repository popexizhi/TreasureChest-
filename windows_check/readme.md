# check dir for 1 hour has *.dmp, save res in send_main.txt
run try_dir.ahk 

# send mail in send_mail.txt
python sendMail.py 
python pm.py   # send mail use startssl
python sender.py # send message to web server
