#DAY22
#1.1.	Read a jpeg image and print the image file

from PIL import Image
import PyPDF2
im = Image.open(r"C:\Users\RAVI\Pictures\website.jpg")
print("copied image")
print("showing image")
im1 = im.copy()
im1.show()

#2.	Merge two pdf files using python script
pdf1File = open('KARTHIK.N.R Certificate.pdf', 'rb')
pdf2File = open('KARTHIK.N.R Certificate.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()