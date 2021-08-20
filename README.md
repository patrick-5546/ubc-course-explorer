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

1. Install Docker: [Install Docker Engine](https://docs.docker.com/engine/install/)

2. Clone the repository and its submodules

    ```sh
    git clone https://github.com/patrick-5546/ubc-course-explorer.git --recurse-submodules
    ```

    - For more about submodules, see the Wiki's [Submodules](https://github.com/patrick-5546/ubc-course-explorer/wiki/For-Developers#submodules) section.

## How to Run

### Development

1. Start the application

    ```sh
    docker-compose up --build
    ```

- The application homepage can be found at http://127.0.0.1:8000/
- Stop the application with `CTRL+BREAK`
  - Run `docker-compose down -v` to remove all containers and volumes before switching to the production environment

### Production

Uses [Gunicorn](https://gunicorn.org/) WSGI server and [NGINX](https://www.nginx.com/) reverse proxy.

0. Ensure that the production files, `.env.prod` and `.env.prod.db`, are in the root directory

    - These files are not on GitHub for security reasons

1. Start the application

    ```sh
    docker-compose -f docker-compose.prod.yml up -d --build
    ```

    - The application will not start if it does not follow our Python linting style guide, which can be found in our Wiki's [Linting](https://github.com/patrick-5546/ubc-course-explorer/wiki/For-Developers#linting) section

2. Migrate database

    ```sh
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    ```

3. Serve up static files

    ```sh
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
    ```

- The application homepage can be found at http://127.0.0.1:1337/
- Stop the application with `docker-compose -f docker-compose.prod.yml down`
  - Add the `-v` argument to remove the associated volumes (use when switching to the development environment)
