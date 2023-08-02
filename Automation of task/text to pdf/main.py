import glob
from fpdf import FPDF
from pathlib import Path

def returntext(filepath):
    with open(filepath,"r") as file:
        text = file.read()
        return text


filepaths = glob.glob("text/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for one in filepaths:
    textforpdf = returntext(one)
    pdf.add_page()
    filename = Path(one).stem
    pdf.set_font(family="arial",size=32, style="B")
    pdf.cell(w=50, h=8,txt=filename.capitalize(),ln=1)
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0,h=6,txt=textforpdf)
pdf.output("ANSWER.pdf")