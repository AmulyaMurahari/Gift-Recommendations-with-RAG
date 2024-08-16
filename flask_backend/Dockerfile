# Stage 1: Build the Python environment
FROM python:3.10-slim as build

# Set working directory
WORKDIR /app

# Copy only the requirements file first for caching dependencies
COPY requirements.txt ./

# Install the dependencies
RUN pip install -r requirements.txt

RUN pip install pyspellchecker

# Copy the rest of the application code
COPY . .

# Set working directory
WORKDIR /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app directly using Python
CMD ["python", "app.py"]
