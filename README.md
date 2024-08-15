# Enhancing Gift Recommendatios Using RAG Pipeline

## Project Overview
This project utilizes the Retrieval-Augmented Generation (RAG) pipeline to create a sophisticated gift recommendation system. By integrating dense retrieval with a sequence-to-sequence model, the system personalizes gift suggestions based on user input and trends captured from various data sources.

## Features
- **Personalized Recommendations**: Generates gift suggestions tailored to individual preferences and occasions.
- **Efficient Data Retrieval**: Leverages dense retrieval for fast and relevant document fetching.
- **Scalable Architecture**: Designed to handle large datasets and high query volumes effectively.

## Data Sources
- **Kaggle Dataset**: Utilizes a comprehensive dataset from Kaggle featuring gift items with associated metadata.
- **E-commerce APIs**: Data collected from e-commerce platforms via APIs.
- **Social Media**: Trends and preferences extracted using social media listening tools.

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

   macOS/Linux: source bin/activate

   Windows: .\Scripts\activate

   After activation, your terminal prompt should reflect that the virtual environment is active, usually by displaying '(gift)' at the start of the prompt.

### Step 5: Install Required Packages
1. Install all necessary Python packages listed in the 'requirements.txt' file by running: pip install -r requirements.txt

### Step 6: Run the React Application
1. Navigate to your React project directory (if it's not already in the 'gift' directory, move it there).
2. Install the required Node.js packages by running: npm install
3. Start the React application using: npm start

Your React application should now be running, and you can view it in your browser at 'http://localhost:3000'.
