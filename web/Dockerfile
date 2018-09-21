FROM python:3.6.6 
MAINTAINER Wolksvidia <wolksvidia@gmail.com>
 
# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask
 
# Create the working directory (and set it as the working directory) /home/flask/app/web
RUN mkdir -p /app/web
WORKDIR /app/web
 
# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requerimientos.txt /app/web
RUN pip install --no-cache-dir -r requerimientos.txt
 
# Copy the source code into the container
COPY . /app/web
 
RUN chown -R flask:flaskgroup /app/web
 
USER flask