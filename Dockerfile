# pull official base image
FROM python:3.8-slim as production

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY manage.py ./manage.py

COPY . .

EXPOSE 8000

# run server cmd
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]