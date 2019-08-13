# Use an official Python runtime as an image
FROM python:3.6-alpine

# install machine level dependencies
RUN apk add --no-cache \
    bluez-libs eudev-libs glib-dev python py-pip\
    && apk add --no-cache gcc musl-dev cmake make

# The EXPOSE instruction indicates the ports on which a container # # will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 80

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY . /app
RUN pip3 install -r requirements.txt

# Run app.py when the container launches
CMD python3 app.py