#!/usr/bin/python
import os
import sys
import getopt
import smtplib
import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


print 'Lets start some converting'
config = ConfigParser.RawConfigParser()
config.read('config.cfg')


def send_mail( send_from, send_to, subject, text, files=[], server="localhost", port=587, username='', password='', isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if isTls: smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

def main(argv):
   
   pdffile = ''
   try:
      opts, args = getopt.getopt(argv,"hp:",["pdffile="])
   except getopt.GetoptError:
      print 'paperToKindle.py -p <pdf>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'paperToKindle.py -p <pdf>'
         sys.exit()
      elif opt in ("-p", "--pfile"):
         pdffile = arg
   #print 'Pdf file is "', pdffile
   #print 'Email is "', email
   #print 'Config', config.get("smpt", "server")
   
   os.system(config.get("k2pdfopt", "k2file")+' '+pdffile+' -ui- -x -o out.pdf')
   send_mail(config.get("smpt", "email"), config.get("smpt", "kindleEmail"), 'This is the mail with a kindle file', 'This is the mail with a kindle file', ['out.pdf'], server=config.get("smpt", "server"), port=config.get("smpt", "port"), username=config.get("smpt", "username"), password=config.get("smpt", "password"))





if __name__ == "__main__":
   main(sys.argv[1:])
