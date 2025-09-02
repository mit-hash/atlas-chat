FROM python:3.11-slim

# Set working directory
WORKDIR /app/src

# Install dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the app code
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Run with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
