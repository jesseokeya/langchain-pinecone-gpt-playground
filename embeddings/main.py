import numpy as np


# Function to get embeddings (example, actual function may vary)
def get_embedding(text):
    return np.random.rand(1536).tolist()

def main():
    # Sample data
    texts = ["sample text 1", "sample text 2", "sample text 3"]

    # Generate embeddings
    embeddings = [get_embedding(text) for text in texts]

    print(embeddings)


# embeddings = [
#     [0.1, 0.2, 0.3, 0.4, 0.5, ..., 0.1536],  # Embedding for "sample text 1" -> Total of 1536 values
#     [0.6, 0.7, 0.8, 0.9, 1.0, ..., 0.1536],  # Embedding for "sample text 2" -> Total of 1536 values
#     [0.11, 0.12, 0.13, 0.14, 0.15, ..., 0.1536]  # Embedding for "sample text 3" -> Total of 1536 values
# ]

main()