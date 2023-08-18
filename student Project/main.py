# this is student project about reading text files and converting them into pdf
import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF

# function used to get all .extension files in a folder
filepaths = glob.glob("textfiles/*.txt")
# creating PDF
pdf = FPDF(orientation="P", format="A4", unit="mm")

# reading text files
for filepath in filepaths:
    dataframe = pd.read_fwf(filepath)
    # removing folder path and .txt extension below
    filename = Path(filepath).stem
    text_head = filename.capitalize()

    with open(f"textfiles/{filename}.txt", "r") as file:
        text = file.read()
# creating pdf writing text
    pdf.add_page()
    pdf.set_font(family="Times", size=25, style="B")
    pdf.cell(w=20, h=0, align="L", txt=text_head)
    pdf.set_font(family="Arial", size=16, style="I")
    pdf.multi_cell(w=0, h=16, txt=str(text))
pdf.output(f"pdfs/file.pdf")