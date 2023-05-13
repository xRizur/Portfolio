#Using the python alpine image
FROM python:alpine

#  Expose the port 5000 of the docker container
EXPOSE 5000

# Create a folder app in container and work inside it
WORKDIR /app

# Copy the requirements.txt file into the WORKDIR
COPY ../requirements.txt .

# Install all the requirements
RUN pip3 install -r requirements.txt

# Copy all the flask project files into the WORKDIR
COPY .. .

# Run the app.py file
CMD python3 app.py