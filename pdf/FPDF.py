from fpdf import FPDF

# Créer un document PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Lire le fichier texte
with open("mon_fichier.txt", "r", encoding="utf-8") as file:
    for line in file:
        pdf.cell(200, 10, txt=line.strip(), ln=True)

# Sauvegarder le PDF
pdf.output("mon_fichier.pdf")