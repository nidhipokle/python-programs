from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

files = filedialog.askopenfilenames(
    title="Select PDF files to merge",
    filetypes=[("PDF Files", "*.pdf")]
)

merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write("merged_file.pdf")
merger.close()

print("PDF files merged successfully!")
print("New file created: merged_file.pdf")
