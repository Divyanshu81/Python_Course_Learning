import pandas as pd
import glob
from fpdf import FPDF

allfilepaths = glob.glob("resources/*.xlsx")

for one in allfilepaths:
    df = pd.read_excel(one, sheet_name="Sheet 1")

    pdf = FPDF(orientation="L", unit="mm", format="A5")
    pdf.add_page()

    filename = one[10:]
    Invoice_number, date = filename.split("-")
    date=date[:-5]
    pdf.set_font(family="arial", size=14, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Number. {Invoice_number}", ln=1)
    pdf.set_font(family="arial", size=14, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Date. {date}", ln=1)

    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    cname = df.columns
    pdf.set_font(family="Times", size=10,style="B")
    pdf.set_text_color(80, 80, 80)
    for name in columns:
        if name != "product_name":
            pdf.cell(w=70, h=8, txt=name, border=1)
        elif name=="total_price":
            pdf.cell(w=30, h=8, txt=name, border=1,ln=1)
        else:
            pdf.cell(w=30, h=8, txt=name, border=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(90,90,90)
        pdf.cell(w=30, h=8, txt=cname[0], border=1)
        pdf.cell(w=70, h=8, txt=cname[1], border=1)
        pdf.cell(w=30, h=8, txt=cname[2], border=1)
        pdf.cell(w=30, h=8, txt=cname[3], border=1,ln=1)

    pdf.output(f"Outputs/{filename}Final Product.pdf")
