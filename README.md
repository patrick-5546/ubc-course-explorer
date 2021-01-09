# UBC Course Planner
Simple web application built with Django. The application aims to provide an one-stop interface for UBC students to find course information, including professor ratings, grade distribution, and nested prerequisite courses, in hopes of helping them better plan out their study path throughout university. The data was collected from [UBCGrades](https://ubcgrades.com/), [UBC Course Explorer](https://ubcexplorer.io/), and [Rate My Professors](https://www.ratemyprofessors.com/campusRatings.jsp?sid=1413). 

See the [Wiki](https://github.com/patrick-5546/ubc-course-explorer/wiki) for screenshots of the website, as well as useful information for developers who want to build on this application.

UBC Course Planner is the result of revising and completing the [Oakhacks 2020 first place project](https://github.com/ad2969/university-path-explorer).

#### Change List
- Added support for any UBC course offered in the last 25 years
- Added support for professor ratings of all course professors in the last 25 years
- Added support vertical aspect ratios
- Stored data locally to increase speed, enable offline functionality, and reduce dependency on APIs
- Created scripts to test methods and update local data
- View recent course professors by section
- View tree of all nested prerequisites required for a course

## How to Run
1. `cd` into the chosen directory and clone the repository
```
git clone https://github.com/patrick-5546/ubc-course-explorer
```
2. Install Django: [Django Quick Install Guide](https://docs.djangoproject.com/en/3.1/intro/install/)

3. `cd` into the root directory of the repository. If it is the first time running the application, migrate data
```
python manage.py migrate
```
4. Run the server
```
python manage.py runserver
```
5. Open the link provided in the terminal to load the site

6. To stop running the server: CTRL + C (for Windows systems) in the terminal where step 3 was executed
