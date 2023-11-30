# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .pdfprocess import extract_pdf_data
from django.core.exceptions import FieldError
from bardapi import Bard
import requests
import time
from .models import Coverlatter

import os
os.environ['_BARD_API_KEY']='your __Secure-1PSID'
token='your __Secure-1PSID'


# up
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# session.cookies.set("__Secure-1PSID", token) 


# end




def process_pdf(request):
    if request.method == 'POST':
        try: 
            uploaded_file = request.FILES['pdf_file']
            job_description=request.POST['job_desc']
            # print(job_description)
        except FieldError:
            return HttpResponse("Exception: Data not found")
       

      

        # Debugging: Print the uploaded file name
        # print(f"Uploaded file name: {uploaded_file.name}")

        # Extract data from the PDF without saving the file
        extracted_data = extract_pdf_data(uploaded_file)
        time.sleep(3)
        user_input=f"write cover latter using my resume `{extracted_data}` and a job description `{job_description}'"
        bard = Bard(token=token, session=session, timeout=30)

        bard_response=bard.get_answer(user_input)['content']
        user=Coverlatter(text=bard_response)
        user.save()
        
        return render(request, 'success.html', {'data':bard_response})
       


        # Debugging: Print the extracted data
        # print(f"Extracted data: {extracted_data}")


    return render(request, 'upload_pdf.html')


