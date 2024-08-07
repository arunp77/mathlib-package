# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer stdout
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file, setup.py, and README.md into the container
COPY requirements.txt ./
COPY setup.py ./
COPY README.md ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY mathlib/ mathlib/
COPY tests/ tests/

# Install the package
RUN pip install .

# Optional: Run tests (uncomment if you want to run tests in the container)
# RUN pytest

# Command to run your application (if you have an entry point script, replace with actual script)
# CMD ["python", "setup.py"]
