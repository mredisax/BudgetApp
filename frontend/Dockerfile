# Use the official Node.js image as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY ./frontend/package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the React app code to the container
COPY ./frontend .

# Build the React app
RUN npm run build

# Expose port 3000 for the React app
EXPOSE 3000

# Start the React app when the container runs
CMD ["npm", "start"]

