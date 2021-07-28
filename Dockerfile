# pull official base image
FROM python:3.8.7-slim-buster

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# run server cmd
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]