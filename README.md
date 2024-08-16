# Enhancing Gift Recommendatios Using RAG Pipeline

## Project Overview
The "Enhancing Gift Recommendations with RAG" project is a comprehensive system that combines the power of modern AI technologies with a user-friendly interface to deliver personalized gift recommendations. The project utilizes Flask for the backend, managing the logic and data processing, while React is employed for the front-end, ensuring a seamless and interactive user experience. This setup allows for efficient communication between the server and the user interface, making the recommendation process both fast and responsive.

At the core of the system is a Retrieval-Augmented Generation (RAG) model that integrates human interactions to continuously refine and improve its recommendations. By leveraging Gemini for natural language processing and understanding, the system can engage users in meaningful dialogues, capturing nuanced preferences and contextual information that are critical for accurate gift suggestions. The human-in-the-loop approach not only helps in training the model but also ensures that the system remains adaptable to changing user needs and preferences over time.

This combination of advanced AI, human interaction, and a robust technological stack results in a highly personalized and effective gift recommendation system, designed to enhance the gift-giving experience in a meaningful way.

## Key Features
- **Context-Aware Personalization:**

Tailors suggestions based on relationship type and occasion.

Dynamically adapts to user feedback and interaction history.

- **Curated and Diverse Gift Dataset:**

Specialized dataset with niche and artisanal products.

Regularly updated to reflect current trends and seasonal variations.

- **Intuitive User Interface:**

User-friendly, responsive, and customizable UI.

Users can refine recommendations based on budget, interests, and occasion 

- **Precision-Driven Metrics:**

Ensures recommendations are relevant to the context and user preferences.

## Data Sources
- **Kaggle Dataset**: Utilizes a comprehensive dataset from Kaggle featuring gift items with associated metadata.

## Set-up Instructions:
### Step 1: Create a Virtual Environment
1. Open your terminal or command prompt.
2. Run the following command to create a virtual environment named gift: python -m venv gift

This will create a directory named 'gift' containing your virtual environment.

### Step 2: Download the files from GitHub and Copy All Files from the Zip
1. Download all the required files or clone the project from the github repo.
2. Extract the contents of your zip file.
3. Copy all the extracted files into the 'gift' directory.

### Step 3: Navigate to the 'gift' Directory
1. Change your current directory to the newly created 'gift' virtual environment by running: cd gift

### Step 4: Activate the Virtual Environment
1. Activate the virtual environment with the appropriate command for your operating system:

   **macOS/Linux:** source bin/activate

   **Windows:** .\Scripts\activate

   After activation, your terminal prompt should reflect that the virtual environment is active, usually by displaying '(gift)' at the start of the prompt.

### Step 5: Install Required Packages
1. Install all necessary Python packages listed in the 'requirements.txt' file by running: pip install -r requirements.txt

### Step 6: Run the React Application
1. Navigate to your React project directory (if it's not already in the 'gift' directory, move it there).
2. Install the required Node.js packages by running: npm install
3. Start the React application using: npm start

The React application should now be running, and you can view it in your browser at 'http://localhost:3000'.

## Dataset Information

Due to the size of the dataset, it has been hosted externally. You can download the complete dataset from the following link: https://drive.google.com/drive/folders/1BZFqwr6BQ-8sEdthmR2g2BcsbKosYyei

Below is a sample of our dataset:![image](https://github.com/user-attachments/assets/8182ae96-da35-440c-83af-e21ad2c9cc69)

