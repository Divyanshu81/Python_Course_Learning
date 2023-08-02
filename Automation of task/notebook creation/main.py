from fpdf import FPDF
import pandas as p

df= p.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,200,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for j in range(25,255,10):
        pdf.line(10, j, 200, j)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        for j in range(25, 255, 10):
            pdf.line(10, j, 200, j)

pdf.output("hi.pdf")