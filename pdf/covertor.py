import PyPDF2

temp=PyPDF2.PdfFileReader(open('./files/all.pdf'),'rb')
watermark=PyPDF2.PdfFileReader(open('./files/wtr.pdf'),'rb')
output=PyPDF2.PdfFileWriter()
