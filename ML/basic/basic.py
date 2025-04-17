import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load data from JSON files
def load_json_data(product_file, user_file):
    with open(product_file, 'r') as f:
        product_data = json.load(f)

    with open(user_file, 'r') as f:
        user_data = json.load(f)

    product_df = pd.DataFrame(product_data)
    user_df = pd.DataFrame(user_data)

    return product_df, user_df

# Create user-product interaction matrix
def create_interaction_matrix(user_df, product_df):
    interaction_matrix = np.random.randint(0, 2, size=(len(user_df), len(product_df)))
    return interaction_matrix

# Content-based similarity (using random product embeddings for demonstration)
def content_based_similarity(user_idx, product_embeddings):
    content_sim = cosine_similarity([product_embeddings[user_idx]], product_embeddings)
    return content_sim.flatten()

# Collaborative filtering similarity (using interaction matrix)
def collaborative_filtering(user_idx, interaction_matrix):
    user_interactions = interaction_matrix[user_idx]
    similarities = cosine_similarity([user_interactions], interaction_matrix)
    return similarities.flatten()

# Combine content-based and collaborative filtering scores
def combine_similarities(user_idx, product_embeddings, interaction_matrix, alpha=0.7, beta=0.3):
    content_sim = content_based_similarity(user_idx, product_embeddings)
    collab_sim = collaborative_filtering(user_idx, interaction_matrix)

    # Ensure both similarity arrays have the same shape (length)
    min_len = min(len(content_sim), len(collab_sim))
    content_sim = content_sim[:min_len]
    collab_sim = collab_sim[:min_len]

    combined_scores = alpha * content_sim + beta * collab_sim
    return combined_scores

# Recommendation function
def recommend_products(user_email, product_embeddings, user_embeddings, product_df, interaction_matrix, top_n=5):
    user_idx = user_df[user_df['email'] == user_email].index[0]  # Get user index
    combined_similarities = combine_similarities(user_idx, product_embeddings, interaction_matrix)

    # Filter out products with zero stock
    available_products = product_df[product_df['stock'] > 0]

    # Ensure the available products' indices correspond to combined_similarities
    available_product_indices = available_products.index

    # Ensure available_product_indices are within bounds for combined_similarities
    if len(combined_similarities) < len(product_df):
        # Truncate combined_similarities if it's shorter than the number of products
        combined_similarities = np.pad(combined_similarities, (0, len(product_df) - len(combined_similarities)), mode='constant')

    # Create a list of similarities only for available products using their positions in the original product list
    filtered_combined_similarities = combined_similarities[available_product_indices]

    # Rank products based on combined similarity scores
    recommended_idx = filtered_combined_similarities.argsort()[-top_n:][::-1]  # Get top N products

    # Return recommended products
    recommended_products = available_products.iloc[recommended_idx]
    return recommended_products[['id', 'name', 'price', 'rating', 'stock']]

# Example usage:
product_file = 'product_data.json'  # Replace with your file path
user_file = 'user_data.json'  # Replace with your file path

# Load data from JSON files
product_df, user_df = load_json_data(product_file, user_file)

# Generate random embeddings for demonstration purposes
product_embeddings = np.random.rand(len(product_df), 10)  # 10-dimensional embeddings for each product
user_embeddings = np.random.rand(len(user_df), 10)  # 10-dimensional embeddings for each user

# Create interaction matrix (for demonstration, using random interactions)
interaction_matrix = create_interaction_matrix(user_df, product_df)

# Example user email
user_email = "user1@example.com"
top_n = 5  # Number of recommended products

# Get top N recommended products for the user
recommended_products = recommend_products(user_email, product_embeddings, user_embeddings, product_df, interaction_matrix, top_n)

# Display recommended products
print(recommended_products)


"""
- make online training sothat the model can incrementally learn and can provide realtime updated data from database
- save the model sothat we can use it in api method
- during training next time, do i need to do full training or is there any easy way to update existing training model
- 
"""