# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Ensure requirements.txt is copied separately
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose backend API port
EXPOSE 8000

# Command to start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
