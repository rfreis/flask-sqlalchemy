# Base Image
FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

# install environment dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Add current directory code to working directory
ADD . /app

EXPOSE 5000
CMD ["python"]