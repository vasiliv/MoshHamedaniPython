import PyPDF2

merger = PyPDF2.PdfFileMerger()
file_names = ["001 Exercises.pdf","11.1 Data Annotations Cheat Sheet.pdf"]

for file_name in file_names:
    merger.append(file_name)

merger.write("combined.pdf")