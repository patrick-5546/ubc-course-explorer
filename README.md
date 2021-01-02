# ubc-course-explorer

## How to Run
1. `cd` into the directory you want to use and clone the repository
```
git clone https://github.com/patrick-5546/ubc-course-explorer
```
2. Install Django: [Django Quick Install Guide](https://docs.djangoproject.com/en/3.1/intro/install/)

3. `cd` into the root directory of the repository and run the application locally
```
python manage.py runserver
```
4. Open the link provided in the terminal to open the website

5. To load changes: save changes and refresh tab

6. Access the admin page to view and edit `Course` instances: [Introducing the Django Admin](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#introducing-the-django-admin)

7. Stop running server: CTRL + C (for Windows systems) in the terminal where step 3 was executed

## Modifying `Course` Model
If the [fields are `Course`](https://github.com/patrick-5546/ubc-course-explorer/blob/main/coursetracker/models.py#L5) are modified (added, renamed, deleted), will need to update the database: run `python manage.py makemigrations`, then `python manage.py migrate`

## Scripts
* [`updatescripts.py`](https://github.com/patrick-5546/ubc-course-explorer/blob/main/coursetracker/scrapers/updatescripts.py) is used to update the locally stored data with the data from the APIs. Uncomment the code block that you want to update, and run the file. These will take a while to execute.
* [`testscripts.py`](https://github.com/patrick-5546/ubc-course-explorer/blob/main/coursetracker/scrapers/testscripts.py) is used to test the output of various scraper methods. Uncomment the code block that you want to test, modify the parameters accordingly, and run the file.
