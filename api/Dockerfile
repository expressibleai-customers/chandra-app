# Use a slim Python image compatible with 3.13
FROM python:3.13-slim

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        jq \
        awscli \
        build-essential \
        libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/app

# Copy application code
COPY . .

# Set up virtualenv explicitly (optional)
ENV VIRTUAL_ENV=/usr/app/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Make sure init.sh is executable
RUN chmod +x init.sh

# Expose API port
EXPOSE 8000

# Entrypoint script
CMD ["./init.sh"]
