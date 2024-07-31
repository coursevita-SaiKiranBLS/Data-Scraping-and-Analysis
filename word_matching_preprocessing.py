import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#USED for word comparsion and also solve the problem of skills such as initially break the data set based on the industry wise and save them. Then after, Do skills similarity such as take top 20 skills based on frequency and then compare the skills with all the other and save the words if it is match percentage is more than 8 or 80% then replace or else leave that. 

# Input list of sentences
sentences = [
    "This is the first sentence.",
    "Here is another sentence.",
    "This sentence is different from the others."
]

# Step 1: Vectorize the sentences using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

# Step 2: Compute cosine similarity between all sentences
cosine_similarities = cosine_similarity(tfidf_matrix)

# Step 3: Prepare the data for the Excel sheet
data = []

for i in range(len(sentences)):
    for j in range(len(sentences)):
        if i != j:  # Optional: avoid self-similarity
            data.append([sentences[i], sentences[j], cosine_similarities[i, j]])

# Convert the data to a DataFrame
df = pd.DataFrame(data, columns=["Sentence1", "Sentence2", "Cosine Similarity"])

# Step 4: Save the DataFrame to an Excel file
output_path = '/mnt/data/cosine_similarity.xlsx'
df.to_excel(output_path, index=False)

print(f"Excel file saved to {output_path}")
