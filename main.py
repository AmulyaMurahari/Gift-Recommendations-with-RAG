import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyDGlITqTvl4XM5GyFlu_YaQFVm5FrjTiHQ"
import re
from spellchecker import SpellChecker
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Define the conversational chain with noise robustness in the prompt

documents = [
    "Age: 25, Gender: Male, Relationship: Friend, Occasion: Birthday, Budget: $20, MaxBudget: $30, Gift: Book, Rating: 4.5, Link: example.com/book, Image Link: example.com/book.jpg, Interest: Reading",
    "Age: 30, Gender: Female, Relationship: Sister, Occasion: Graduation, Budget: $50, MaxBudget: $70, Gift: Necklace, Rating: 5.0, Link: example.com/necklace, Image Link: example.com/necklace.jpg, Interest: Jewelry",
    "Age: 35, Gender: Male, Relationship: Colleague, Occasion: Promotion, Budget: $40, MaxBudget: $60, Gift: Pen, Rating: 4.0, Link: example.com/pen, Image Link: example.com/pen.jpg, Interest: Stationery",
    "Age: 28, Gender: Female, Relationship: Girlfriend, Occasion: Anniversary, Budget: $100, MaxBudget: $150, Gift: Perfume, Rating: 4.8, Link: example.com/perfume, Image Link: example.com/perfume.jpg, Interest: Fragrances",
    "Age: 22, Gender: Male, Relationship: Brother, Occasion: Christmas, Budget: $30, MaxBudget: $50, Gift: Headphones, Rating: 4.6, Link: example.com/headphones, Image Link: example.com/headphones.jpg, Interest: Music"
]

spell = SpellChecker()


def preprocess_user_input(user_input):
    # Convert to lowercase
    user_input = user_input.lower()
    # Remove punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)
    # Split into words for spell checking
    words = user_input.split()
    # Correct each word if it's misspelled
    corrected_words = [spell.correction(word) if word not in spell else word for word in words]
    # Join the corrected words back into a single string
    return ' '.join(corrected_words)

# Define the conversational chain with noise robustness in the prompt
def get_conversational_chain():
    prompt_template = """
    You are an AI assistant providing gift suggestions. Please provide multiple gift ideas based on the given context. Consider the specified age, gender, relationship, occasion, budget, and interests. If specific details are not available or if the input is noisy or unclear, provide general suggestions and ask for clarification if needed.

    Context:
    {context}

    Question:
    {question}

    Please list at least 3-5 gift suggestions.

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Process user input and generate a response
def user_input_handler(user_question):
    # Preprocess the user input to handle noise
    cleaned_question = preprocess_user_input(user_question)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(cleaned_question, k=3)
    
    # Extract the context from each document (assuming they are dictionaries)
    contexts = [doc['text'] for doc in docs if 'text' in doc]
    
    chain = get_conversational_chain()
    response = chain({"input_documents": contexts, "question": cleaned_question}, return_only_outputs=True)
    st.write("Reply: ", response["output_text"])

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="AI Gift Suggestions")
    st.header("AI Gift Suggestions")

    user_question = st.text_input("Ask a Question")

    if user_question:
        user_input_handler(user_question)

if __name__ == "__main__":
    main()
