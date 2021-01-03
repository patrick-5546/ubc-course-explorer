# ubc-course-explorer

## How to Run
1. `cd` into the chosen directory and clone the repository
```
git clone https://github.com/patrick-5546/ubc-course-explorer
```
2. Install Django: [Django Quick Install Guide](https://docs.djangoproject.com/en/3.1/intro/install/)

3. `cd` into the root directory of the repository and run the server
```
python manage.py runserver
```
4. Open the link provided in the terminal to load the site

5. To load changes: save changes and refresh tab

6. To access the admin page (to view `Course` objects): [Introducing the Django Admin](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#introducing-the-django-admin)

7. To stop running the server: CTRL + C (for Windows systems) in the terminal where step 3 was executed

## Modifying `Course` Model
* If [`Course` fields](https://github.com/patrick-5546/ubc-course-explorer/blob/main/coursetracker/models.py#L5) are modified (added, renamed, deleted), the database will need to be updated: run `python manage.py makemigrations`, then `python manage.py migrate`
* If `Course` representation is changed (eg. changed `professors_info` field from dictionary to list), run `python manage.py updatecourseobjects` to refresh all the fields of all `Course` objects currently stored in the database

## Scripts
* [`updatescripts.py`](https://github.com/patrick-5546/ubc-course-explorer/blob/main/coursetracker/scrapers/updatescripts.py) is used to sync locally stored data with the APIs: uncomment the code block corresponding to the desired data to sync, then run the file. These will take a while to execute.
* [`testscripts.py`](https://github.com/patrick-5546/ubc-course-explorer/blob/main/coursetracker/scrapers/testscripts.py) is used to test the output of various scraper methods: uncomment the code block corresonding to the desired method(s) to test, modify the parameters as required, then run the file.
