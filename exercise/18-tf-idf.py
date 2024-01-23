import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    docs = [line.split() for line in text.split('\n')]
    words = list(set(text.split()))
    N = len(docs)

    term_frequency = {}
    doc_frequency = {}
    for word in words:
        term_frequency[word] = [doc.count(word) / len(doc) for doc in docs]
        doc_frequency[word] = sum([word in doc for doc in docs]) / N

    tfidf = []
    for i, doc in enumerate(docs):
        tfidf.append([])
        for word in words:
            tfidf[i].append(term_frequency[word][i] * math.log(1 / doc_frequency[word], 10))

    dist = np.empty((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i, j] = np.Inf
            else:
                dist[i, j] = np.sqrt(sum((tfidf[i][k] - tfidf[j][k]) ** 2 for k in range(len(tfidf[i]))))
    print(np.unravel_index(np.argmin(dist), dist.shape))


main(text)
