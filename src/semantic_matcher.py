from sentence_transformers import SentenceTransformer, util

# könnyű, gyors modell (jó default)
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match(text1: str, text2: str) -> float:
    # embeddingek
    emb1 = model.encode(text1, convert_to_tensor = True)
    emb2 = model.encode(text2, convert_to_tensor = True)

    # cosine similarity
    score = util.cos_sim(emb1, emb2)

    return float(score.item())