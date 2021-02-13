# html2pdf
Python code for converting HTML files into pdf with necessary header and footer information (with page numbers)

## Requirements

- Python 3.8
- [pdfkit 0.6.1](https://pypi.org/project/pdfkit/) 

[wkhtmltopdf](https://wkhtmltopdf.org/) needs to be installed in order for pdfkit to work.

```python
$ wkhtmltopdf -V 
wkhtmltopdf 0.12.6 (with patched qt)
``` 

HTML is prepared with [Bootstrap v4.0.0](https://getbootstrap.com/)
- Rendering engine of pdfkit acts weird when it comes to bootstrap grids; ergo, one of the old versions is used
