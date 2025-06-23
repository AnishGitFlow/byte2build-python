from PyPDF2 import PdfWriter, PdfReader

def merge_pdfs():
    merger = PdfWriter()
    pdfs = []
    n = int(input("How many PDFs do you want to merge?\n"))

    for i in range(n):
        name = input(f"Enter the name of PDF {i + 1}: ")
        pdfs.append(name)

    try:
        for pdf in pdfs:
            merger.append(pdf)
        with open("merged-pdf.pdf", "wb") as output:
            merger.write(output)
        print("PDFs merged successfully!")
    except FileNotFoundError:
        print("One or more PDFs not found. Please check the file names and paths.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    merge_pdfs()