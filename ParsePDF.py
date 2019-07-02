import PyPDF2
import re

def get_text(path):
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        numberOfPages = pdf.getNumPages()
        pageObj = pdf.getPage(0)
        text = pageObj.extractText()
        
        test = re.search("(?<=KID-nr.).*?(?=\s)", text)
        test2 = re.search("(?<=Kontonummer).*?(?=K)", text)
        test3 = re.search("(?<=betale).*?(?=k)", text)

        print('''
        [ PAYMENT INFO ]
        ''')
        print("KID number is:", test.group(0))
        print("Account nr is:", test2.group(0))
        print("Amount to pay:", test3.group(0))
        wantRawText = input('\nDo you want to print raw text info? (N/y)')
        if wantRawText == 'y':
            print(text)
            print("\nThe document has", numberOfPages,"pages")
        else:
            return

path = "telenor.pdf"

if __name__ == "__main__":
    get_text(path)
