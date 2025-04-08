import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Coletar e preparar os dados
documentos = [(list(movie_reviews.words(fileid)), categoria)
              for categoria in movie_reviews.categories()
              for fileid in movie_reviews.fileids(categoria)]

textos, labels = zip(*[(" ".join(doc), cat) for doc, cat in documentos])
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)
y = [1 if label == 'pos' else 0 for label in labels]

# Treinar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = MultinomialNB()
modelo.fit(X_train, y_train)
print("Acurácia:", modelo.score(X_test, y_test))