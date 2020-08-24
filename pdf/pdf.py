import PyPDF2
import os
import sys

inputs=sys.argv[1:]

merger=PyPDF2.PdfFileMerger()
for pdf in inputs:
    merger.append('./files/'+pdf)

merger.write('./files/all.pdf')