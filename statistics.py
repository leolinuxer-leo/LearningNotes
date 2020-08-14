import os
import sys

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    '''
    Information about {pdf_path}:
    
    Author:{information.author}
    Creator:{information.creator}
    Producer:{information.producer}
    Subject:{information.subject}
    Title:{information.title}
    Number of pages:{number_of_pages}
    '''
    with open(pdf_path,'rb') as f:
        try:
            pdf = PdfFileReader(f)
            #information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
        except Exception as e:
            print(pdf_path + ' Error: ' + str(e))
            number_of_pages = 0
        return number_of_pages

if __name__ == '__main__':
    total_file_num = 0
    total_page_num = 0
    for root, dirs, files in os.walk('.'):
        for name in files:
            if not name.endswith('pdf'):
                continue
            path = (os.path.join(root, name))
            if path.find('技术资料') != -1:
                continue
            total_file_num += 1
            pages = extract_information(path)
            print(path + ' ' + str(pages))
            total_page_num += pages
    print('total pdf num: %d'%(total_file_num))
    print('total page num: %d'%(total_page_num))
