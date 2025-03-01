# export.py

import pandas as pd
from fpdf import FPDF

def export_csv(df, filename="relatorio_tiktok.csv"):
    """
    Exporta os dados do DataFrame para um arquivo CSV.
    """
    df.to_csv(filename, index=False)
    print(f"📄 Relatório CSV gerado: {filename}")

def export_pdf(df, filename="relatorio_tiktok.pdf"):
    """
    Exporta os dados do DataFrame para um relatório em PDF.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Relatório de Retenção de Vídeos - TikTok", ln=True, align="C")
    pdf.ln(10)

    for index, row in df.iterrows():
        pdf.cell(200, 10, f"{row['title']}: {round(row['retention_rate'] * 100, 2)}% Retenção", ln=True)

    pdf.image("retention_chart.png", x=50, y=None, w=100)
    pdf.output(filename)
    print(f"📄 Relatório PDF gerado: {filename}")
