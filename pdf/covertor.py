import PyPDF2

temp=PyPDF2.PdfFileReader(open('./files/all.pdf'),'rb')
watermark=PyPDF2.PdfFileReader(open('./files/wtr.pdf'),'rb')
output=PyPDF2.PdfFileWriter()

for i in range(temp.getNumPages()):
    page=temp.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.add(page)

 with open('water-all.pdf','wb') as file:
     output.write(file)   

