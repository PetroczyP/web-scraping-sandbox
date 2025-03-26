# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Copy the React app files and build the React app
WORKDIR /app/ui
RUN npm install
RUN npm run build

# Install supervisord
RUN pip install supervisord

# Copy the supervisord configuration file
COPY supervisord.conf /etc/supervisord.conf

# Set supervisord as the entry point
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
