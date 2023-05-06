import re
import types
import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
from pdfminer.high_level import extract_pages, extract_text

fileName = "test.pdf"

reader = PdfReader(fileName)
fields = reader.get_form_text_fields()

writer = PdfWriter()

page = reader.pages[0]

writer.add_page(page)

writer.update_page_form_field_values(
    writer.pages[0], {"0": 1}
)

# def updateCheckboxValues(page, fields):

# for i in range(len(page["/Annots"])): #in order to access the "Annots" key
#     print ((page["/Annots"][i].get_object()))
#     if (page["/Annots"][i].get_object())['/FT']=="/Btn" and (page["/Annots"][i].get_object())['/T']=='Check 1': #this is my filter so that I can filter checkboxes and the checkbox I want i.e. "Check Box 3"
#         print (page["/Annots"][i].get_object())
#         writer_annot = page["/Annots"][i].get_object()
#         writer_annot.update(
#         {
#             NameObject("/AP"): NameObject('/Yes'),
#             NameObject("/AS"): NameObject("/Yes"), # FINNE PROBLEMET HER
#         }
#     )
#         print("\n"+"\n")
# print (page["/Annots"][i].get_object())
# write "output" to PyPDF2-output.pdf
with open("fill-out.pdf", "wb") as output_stream:
    writer.write(output_stream)
