from textblob import TextBlob
frase = "O atendimento foi excelente, mas o produto demorou a chegar."
blob = TextBlob(frase)
print(blob.sentiment)