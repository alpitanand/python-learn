import textblob

opinion = textblob.TextBlob("Ujjwal fucks a lot")
print(opinion.translate(to='es'))

