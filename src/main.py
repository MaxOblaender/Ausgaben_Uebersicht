import os
import pandas as pd
from modules import extract_from_pdf as extract

def main():
    folder_path = 'bank_statements'
    read_file = os.path.join(folder_path, 'read.txt')
    unread_pdf_files = extract.get_unread_pdf_files(folder_path, read_file)
    
    extracted_text_list = []
    for pdf_path in unread_pdf_files:
        extracted_text = extract.extract_text_from_pdf(pdf_path)
        extracted_text_list.append(extracted_text)
        extract.add_read_pdf_file(os.path.basename(pdf_path),read_file)
    
    # Concatenate text from all PDFs
    concatenated_text = '\n'.join(extracted_text_list)
    
    # Split text into lines and create a DataFrame
    lines = concatenated_text.split('\n')
    
    # Create or load existing DataFrame
    csv_path = 'pdf_text.csv'
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        df = pd.DataFrame(columns=['Text'])
    
    # Append new text to the DataFrame
    new_df = pd.DataFrame({'Text': lines})
    df = pd.concat([df, new_df], ignore_index=True)
    
    # Save DataFrame to a CSV file
    os.chdir("bank_statements")
    df.to_csv('pdf_text.csv', index=False)
    print("Text extracted from PDFs and saved to 'pdf_text.csv'.")

if __name__ == "__main__":
    main()
