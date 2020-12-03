import PyPDF2
#read in binary mode
with open("001 Exercises.pdf", "rb") as file:
    #pdf file reader object
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    #get first page
    page1 = reader.getPage(0)
    #features
    page1.rotateClockwise(90)
    # page1.rotateCounterClockwise(90)
    # page1.scale(110)
    #pdf file writer object
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page1)

    with open("rotated.pdf","wb") as output:
        writer.write(output)

