FROM python:3.9-slim

# Set the working directory
WORKDIR /volunteers_are_nearby

# Copy the requirements file
COPY requirements.txt .

# Install virtualenv package
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install virtualenv

# Create a virtual environment and install dependencies
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["venv/bin/python", "app.py"]
