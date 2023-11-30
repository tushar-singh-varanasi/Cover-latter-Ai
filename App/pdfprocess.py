# utils.py
import PyPDF2

def extract_pdf_data(file):
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    # Customized extraction logic
    extracted_data = []

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Split the text into lines and assume the name is on the first line
        extracted_data.append(text)
    return extracted_data



