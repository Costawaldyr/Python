from reportlab.pdfgen import canvas


# Crée un fichier PDF nommé "clcoding.pdf"
c = canvas.Canvas("/Users/ecole/Python/clcoding.pdf")

# Ajouter du texte (x=100, y=750)
c.drawString(100, 750, "Bonjour, ceci est un PDF généré par Python sur Mac !")

# Sauvegarder le PDF
c.save()