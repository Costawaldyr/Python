from textblob import TextBlob

#miss spelled words
texte = "Je sui tré content d'aprendre le python."
blob = TextBlob("I havv a guud ideea, and my friinde eat meet")
#blob = TextBlob(texte)

#perform spelling correction
corrected_blob = blob.correct()

print("Original Text :", blob)
print("Corrected Text :", corrected_blob)