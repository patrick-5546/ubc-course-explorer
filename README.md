# UBC Path Explorer

Simple web application built with Django. The application aims to provide an one-stop interface for UBC students to find course information, including professor ratings, grade distribution, and nested prerequisite courses, in hopes of helping them better plan out their study path throughout university.

The data was collected from [UBCGrades](https://ubcgrades.com/), [UBC Course Explorer](https://ubcexplorer.io/), and [Rate My Professors](https://www.ratemyprofessors.com/campusRatings.jsp?sid=1413). **RateMyProf local data was last updated January 9th, 2021. The most recent term available from UBCGrades is 2020S for grades, and 2018S for section professors.**

See the [Wiki](https://github.com/patrick-5546/ubc-course-explorer/wiki) for screenshots of the website, updating the RateMyProf data, as well as useful information for developers who want to build on this application.

UBC Course Planner is the result of revising and completing the [Oakhacks 2020 first place project](https://github.com/ad2969/university-path-explorer).

## Change List

- Added support for any UBC course offered in the last 25 years
- Added support for professor ratings of all course professors in the last 25 years
- Added support vertical aspect ratios
- Stored data locally to increase speed, enable offline functionality, and reduce dependency on APIs
- Created scripts to test methods and update local data
- View recent course professors by section
- View tree of all nested prerequisites required for a course

## Setup

First, clone the repository and its submodules with this command

      ```sh
      git clone https://github.com/patrick-5546/ubc-course-explorer.git --recurse-submodules
      ```
### PostgreSQL and local development server

###### _If you are using Docker exclusively with this application then you may skip this step._

Before setting up the Django server, you will need to install and setup a local PostgreSQL client since our application relies on PostgreSQL.

1. Go to [PostgreSQL](https://www.postgresql.org/download/) and download the latest version for your machine. 

2. After setting up Postgres, enter your postgres superuser credentials and secret key into `ubc_course_explorer/.env`. 

###### Note that by default, PostgreSQL will setup a database named 'postgres' (very creative indeed). If you want to use a different database locally, you will need to manually create it.

When you run a local server, the application will automatically parse the env file for your credentials and secret key for use. Make sure to keep this file in your `.gitignore` if you are committing to your forked version. 


## How to Run

The following commands are for Windows machines, they might be slightly different for other operating systems

### Python

1. Install Python 3


2. Install the required packages in a virtual environment: [Python 3 Virtual Environments](https://gist.github.com/patrick-5546/29e7060139f057d2696d3260a3bb8eeb)

3. Apply database migrations

      ```sh
      py manage.py migrate
      ```

4. Start the application

      ```sh
      py manage.py runserver
      ```

      - The application homepage can be found at `http://127.0.0.1:8000/`
      - Stop the application with `CTRL+BREAK`

### Docker

1. Apply database migrations

      ```sh
      docker-compose run web python manage.py migrate
      ```

2. Start the application

      ```sh
      docker-compose up
      ```

      - The application homepage can be found at `http://127.0.0.1:8000/`
      - Stop the application with `CTRL+BREAK`
