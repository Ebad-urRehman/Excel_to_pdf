import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# glob() method is used to format the file path
# in this case we import all the files with .xlsx extensions and store them as a list
filepaths = glob.glob("Invoices/*.xlsx")

# using pandas library method read_excel to read each file
for filepath in filepaths:
    dataframe = pd.read_excel(filepath, sheet_name="Sheet 1", engine='openpyxl')
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # filepath.stem re
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    # setting fonts and formatting of pdf text
    pdf.set_font(family="Times", size=26, style="B")
    pdf.cell(w=0, h=8, txt=f"Invoice number: {invoice_nr}", ln=1)

    # filename.split splits the text into two parts the 2nd path of filename is date so it can be accessed by [1] index
    date = filename.split("-")[1]
    pdf.set_font(family="Times", size=26, style="B")
    pdf.cell(w=0, h=10, txt=f"Date: {date}", ln=1)

    # add a header in a row to each column
    columns = list(dataframe.columns)
    columns = [items.replace("_", " ").title() for items in columns]
    pdf.set_font(family="Arial", size=11, style="i")
    pdf.cell(w=30, h=10, txt=columns[0], border=True)
    pdf.cell(w=70, h=10, txt=columns[1], border=True)
    pdf.cell(w=35, h=10, txt=columns[2], border=True)
    pdf.cell(w=30, h=10, txt=columns[3], border=True)
    pdf.cell(w=30, h=10, txt=columns[4], ln=1, border=True)

    # add all rows
    for index, row in dataframe.iterrows():
        pdf.set_font(family="Arial", size=16, style="I")
        pdf.cell(w=30, h=10, txt=str(row["product_id"]), border=True)
        pdf.cell(w=70, h=10, txt=str(row["product_name"]), border=True)
        pdf.cell(w=35, h=10, txt=str(row["amount_purchased"]), border=True)
        pdf.cell(w=30, h=10, txt=str(row["price_per_unit"]), border=True)
        pdf.cell(w=30, h=10, txt=str(row["total_price"]), ln=1, border=True)

    # Total_price and some text
    total_sum = dataframe["total_price"].sum()
    pdf.set_font(family="Arial", size=16, style="I")
    pdf.cell(w=30, h=10, txt="", border=True)
    pdf.cell(w=70, h=10, txt="", border=True)
    pdf.cell(w=35, h=10, txt="", border=True)
    pdf.cell(w=30, h=10, txt="", border=True)
    pdf.cell(w=30, h=10, txt=str(total_sum), ln=1, border=True)

    # total price description
    pdf.set_font(family="Arial", size=16, style="I")
    pdf.cell(w=35, h=10, txt=f"The total Price is {total_sum}", ln=1)
    # company name and image logo
    pdf.set_font(family="Arial", size=11, style="B")
    pdf.cell(w=30, h=10, txt=f"My Company")
    pdf.image("companyname.jpg", w=10)
    # creating file
    pdf.output(f"pdfs\\{filepath}.pdf")


"""glob.glob can access all files in a directory with same extension by using the syntax above
in excel documents there is a need to provide sheet argument
openpyxl library is needed to open excel files by panda and to store into a data frame"""