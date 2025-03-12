from src.service.Word2Vec import Word2VecService

word2vec = Word2VecService()
# this will take sometime to download the model
print(f"Vector for 'king': {word2vec.get_vector('king')}")
print(f"Similarity between 'sad' and 'happy': {word2vec.get_similarity('sad', 'happy')}")
print(f"Similarity between 'king' and 'queen': {word2vec.get_similarity('king', 'queen')}")
print(f"Most similar words to 'king': {word2vec.get_most_similar('king')}")
vec_king = word2vec.get_vector('king')
vec_man = word2vec.get_vector('man')
vec_woman = word2vec.get_vector('woman')
vec_queen = word2vec.get_vector('queen')
new_vec = vec_king - vec_man + vec_woman
print(f"Most similar for king - man + woman: {word2vec.get_model().similar_by_vector(new_vec)}")
