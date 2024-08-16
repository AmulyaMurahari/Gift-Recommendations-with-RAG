from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyDGlITqTvl4XM5GyFlu_YaQFVm5FrjTiHQ"
from spellchecker import SpellChecker
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Initialize the Flask app and CORS
app = Flask(__name__)
CORS(app)

# Load models, embeddings, FAISS index globally
spell = SpellChecker()
model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
faiss_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Define the prompt template
prompt_template = """
You are an assistant providing personalized gift suggestions. Please provide multiple gift ideas based on the given context. Consider the specified age, gender, relationship, occasion, budget, and interests. If specific details are not available or if the input is noisy or unclear, provide general suggestions and ask for clarification if needed.

Context:
{context}

Question:
{question}

Please list at least 3-5 gift suggestions.

Answer:
"""

def preprocess_user_input(user_input):
    """Preprocess user input to clean and correct it."""
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)
    words = user_input.split()
    corrected_words = [spell.correction(word) if word not in spell else word for word in words]
    return ' '.join(corrected_words)

def get_conversational_chain():
    """Create and return the conversational chain for querying."""
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

@app.route('/suggestions', methods=['POST'])
def get_suggestions():
    """API endpoint to process user input and return gift suggestions."""
    data = request.json
    user_question = data.get('question', '')

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    cleaned_question = preprocess_user_input(user_question)

    docs = faiss_db.similarity_search(cleaned_question, k=3)

    if not docs:
        return jsonify({"suggestions": [], "message": "No matching gift suggestions found."})

    contexts = [doc['text'] for doc in docs if 'text' in doc]

    chain = get_conversational_chain()
    response = chain({"input_documents": contexts, "question": cleaned_question}, return_only_outputs=True)

    return jsonify({"suggestions": response["output_text"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

