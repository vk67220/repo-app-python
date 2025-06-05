# Use official Python image
#FROM python:3.10-slim

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# Set working directory
#WORKDIR /app

#COPY backend/ ./backend/
#COPY frontend/templates ./frontend/templates

# Copy dependencies
#COPY requirements.txt .

# Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
#COPY . .

# Expose port
#EXPOSE 8000

# Start FastAPI server
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements and install dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend/ ./

# Copy frontend templates (required by FastAPI Jinja2Templates)
COPY frontend/templates ./frontend/templates

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


