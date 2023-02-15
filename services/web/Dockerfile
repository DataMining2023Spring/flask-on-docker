<<<<<<< HEAD
# pull official base image
=======
>>>>>>> bcc15e2dc7991fdf2486b2282223e7564742319c
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

<<<<<<< HEAD
# install system dependencies
RUN apt-get update && apt-get install -y netcat

=======
>>>>>>> bcc15e2dc7991fdf2486b2282223e7564742319c
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/
<<<<<<< HEAD

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
=======
>>>>>>> bcc15e2dc7991fdf2486b2282223e7564742319c
