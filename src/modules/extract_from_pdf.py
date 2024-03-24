import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def get_pdf_files(folder_path):
    pdf_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(folder_path, file))
    return pdf_files

def get_unread_pdf_files(folder_path, read_file):
    all_pdf_files = get_pdf_files(folder_path)
    with open(read_file, 'r') as file:
        read_files = file.read().splitlines()
    unread_pdf_files = [file for file in all_pdf_files if os.path.basename(file) not in read_files]
    return unread_pdf_files

def add_read_pdf_file(read_pdf_file,read_file):
    with open(read_file,"a") as file:
        file.write(read_pdf_file+"\n")