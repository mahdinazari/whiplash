
import os
from datetime import datetime

from .message_handler import MessageHandler
from .utils import upload_pdf


class UploadPrintHandler():

    def __init__(self):
        self.role = r'upload_print'

    def apply_handler(self, message):
        date = datetime.now().strftime('%Y_%m_%d_%H_%M')
        upload_pdf(message['directory'], date, message['password'])
        print('after pdf')
        cmd = r"C:\pprint.exe C:\upload_print.pdf"
        os.system(cmd) 
        
        #if os.path.exists('C:\upload_print.pdf'):
            #print('normal file exists')
            #cmd = r"C:\pprint.exe C:\upload_print.pdf"
            #os.system(cmd) 
    
