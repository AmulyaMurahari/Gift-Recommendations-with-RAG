import pandas as pd
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

os.environ["GOOGLE_API_KEY"] = "AIzaSyDGlITqTvl4XM5GyFlu_YaQFVm5FrjTiHQ"

# Helper function to preprocess the CSV file and clean the data
def preprocess_csv(file_path):
    df = pd.read_csv(file_path, nrows=1000)  # Limit to the first num_rows rows
    df.fillna("", inplace=True)  # Handle missing data by filling with an empty string
    df['text'] = df.apply(lambda row: f"Name: {row['name']}, Main Category: {row['main_category']}, "
                                  f"Sub Category: {row['sub_category']}, Image: {row['image']}, "
                                  f"Link: {row['link']}, Ratings: {row['ratings']}, "
                                  f"No. of Ratings: {row['no_of_ratings']}, Discount Price: {row['discount_price']}, "
                                  f"Actual Price: {row['actual_price']}, Age: {row['Age']}, "
                                  f"Gender: {row['Gender']}, Occasion: {row['Occasion']}, "
                                  f"Relationship: {row['Relationship']}", axis=1)
    return df['text'].tolist()

# Add human interaction phrases
def get_conversational_phrases():
    phrases = [
        "Hi, how can I help you today?",
        "Hello! How can I assist you?",
        "Goodbye, have a nice day!",
        "Welcome to our service!",
        "Tell me a joke.",
        "Thank you for visiting!",
        "Bye, take care!",
        "What's your name?",
        "How are you?",
        "I'm here to help you with gift suggestions."
    ]
    return phrases

# Load additional conversational data from a text file
def load_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Clean and process lines (remove newlines, strip spaces, etc.)
    processed_lines = [line.strip() for line in lines if line.strip()]
    return processed_lines

# Combine CSV data with conversational phrases and text file data
def get_combined_texts(csv_texts, conversational_phrases, text_file_data):
    return csv_texts + conversational_phrases + text_file_data

# Helper function to split text into chunks
def get_text_chunks(texts):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = []
    for text in texts:
        chunks.extend(text_splitter.split_text(text))
    return chunks

# Helper function to store text chunks in a vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Main function to process the CSV file, text file and save the FAISS index
def train_and_save_model():
    csv_file_path = 'amazon.csv'  # Path to your CSV file
    text_file_path = 'human_chat.txt'  # Path to your text file

    csv_texts = preprocess_csv(csv_file_path)
    conversational_phrases = get_conversational_phrases()
    text_file_data = load_text_file(text_file_path)

    combined_texts = get_combined_texts(csv_texts, conversational_phrases, text_file_data)
    text_chunks = get_text_chunks(combined_texts)

    # Train and save the model
    get_vector_store(text_chunks)

if __name__ == "__main__":
    train_and_save_model()
