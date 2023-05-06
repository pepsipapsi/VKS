from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject, IndirectObject
from allFields import *


input_file = "nexans_doc.pdf"
output_file = "VKS nexans.pdf"

pdf_reader = PdfReader(input_file)
pdf_writer = PdfWriter()
fields = pdf_reader.get_form_text_fields()

page = pdf_reader.pages[0]

pdf_writer.add_page(page)


def writerUpdate(page, pdfwriter, field, output):
    pdfwriter.update_page_form_field_values(
        pdfwriter.pages[page], {field: output}
    )


def pdfRun():
    with open(output_file, "wb") as out:
        pdf_writer.write(out)
