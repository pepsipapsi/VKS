`imports pypdf for global scope and allFields, containing most of the most common used variables`
```python
input_file = "test.pdf"
output_file = "exported.pdf"
```
* `input_file` - defines the starting pdf file, that is nexans document.
* `output_file` - defines the final, extracted and manipulated pdf file.
`file used with pypdf, class to manipulate a file and extractin all the fields from the pdf file.`
```python
pdf_reader = PdfReader(input_file)
pdf_writer = PdfWriter()
fields = pdf_reader.get_form_text_fields()
```
* `pdf_reader` - defines the in-built function that pypdf provieds with given file argument as ==input_file== (test.pdf)
* `pdf_writer` - this class supports writing PDF files out, given pages produced by another class

