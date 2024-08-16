# Stage 1: Build the React app
FROM node:18-alpine as build

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app’s code into the container
COPY . .

# Build the React app for production
RUN npm run build

# Stage 2: Serve the React app with a simple server
FROM node:18-alpine

# Set working directory inside the container
WORKDIR /app

# Copy the built React app from the previous stage
COPY --from=build /app/build /app/build

# Install a simple server to serve the static files
RUN npm install -g serve

# Serve the React app
CMD ["serve", "-s", "build", "-l", "3000"]

# Expose port 80 to the outside world
EXPOSE 3000
