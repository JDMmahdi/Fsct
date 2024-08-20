import PyPDF2

def extract_simple_pdf(pdf_path):
    extraced_text = ""
    with open(pdf_path, 'rb') as file:
        reader_obj = PyPDF2.PdfReader(file)
        for page in reader_obj.pages:
            extraced_text += page.extract_text()
    return extraced_text

pdf_path = "C:/Users/ehdae/OneDrive/Desktop/python/how_good_python_is.pdf"

print(extract_simple_pdf(pdf_path))