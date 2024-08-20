import pdfplumber

def text_extractor(pdf_path):
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text()
        return extracted_text


def column_text_extractor(pdf_path):
    extracted_table = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_table += page.extract_tables()
        return extracted_table


pdf_path = "C:/Users/ehdae/OneDrive/Desktop/python/how_good_python_is.pdf"
print("Here's the extraction of everything: \n" + text_extractor(pdf_path) + "\n")

tables = column_text_extractor(pdf_path)
print("Here's the extraction of ONLY the tables:\n")
for table in tables:    
    for row in table:    
        print(row) 