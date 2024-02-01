# word2vec_alchemy
Merging words with word2vec embeddings in pure javascript

The embeddings are used in as a word => embedding map.

Embeddings are downloaded from [https://nlp.stanford.edu/projects/glove/]
then filtered down to words from [https://www.desiquintans.com/nounlist].

The result is then converted to json.

Merging words works by calculating the arithmetic mean of embedding vectores for all merged words,
and then finding the nearest word in the embedding map using cosine similarity.
Words that are used during merging are excluded and won't be chosen.
