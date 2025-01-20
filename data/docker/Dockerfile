FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY data/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Remove requirements.txt after installation
RUN rm requirements.txt

# Copy data directory
COPY data/ /app/data

CMD ["python3", "data/main.py"]