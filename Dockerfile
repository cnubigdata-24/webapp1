# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Command to run Gunicorn WSGI server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]



