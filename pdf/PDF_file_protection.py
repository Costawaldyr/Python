from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(inpud_pdf, output_pdf):
    reader = PdfReader(inpud_pdf)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    
    password = getpass.getpass("Enter a password : ")
    writer.encrypt(password)
    
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"The PDF has password.")

protect_pdf("/Users/ecole/Python/clcoding.pdf", "/Users/ecole/Python/protected_file.pdf")