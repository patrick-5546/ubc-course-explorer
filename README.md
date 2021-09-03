# UBC Path Explorer

Simple web application built with Django. The application aims to provide an one-stop interface for UBC students to find course information, including professor ratings, grade distribution, and nested prerequisite courses, in hopes of helping them better plan out their study path throughout university.

UBC Course Planner is the result of revising and completing the [Oakhacks 2020 first place project](https://devpost.com/software/university-path-explorer). See the [Wiki](https://github.com/patrick-5546/ubc-course-explorer/wiki) for screenshots of the website and information for developers that want to build on this application.

## Deployment

This repository is deployed using Gunicorn, Nginx, Docker, AWS, and GitHub Actions to the temporary domain name of [ubccourses.software](https://www.ubccourses.software) every time a commit is pushed to the main branch. Our deployment methodology is documented in an [old pull request](https://github.com/patrick-5546/ubc-course-explorer/pull/56).

## Application Data

For information about this site's data sources and the web scraping scripts used, see our data repository, [ubc_course_explorer_data](https://github.com/patrick-5546/ubc_course_explorer_data). The data repository is used as a submodule in this repository's `app/ubc_course_explorer_data` directory so that application data can be updated separate from the application itself.

## Setup

1. Install Docker: [Install Docker Engine](https://docs.docker.com/engine/install/)

2. Clone the repository, with the data repository as a submodule

    ```sh
    git clone https://github.com/patrick-5546/ubc-course-explorer.git --recurse-submodules
    ```

    - If the `app/ubc_course_explorer_data` directory is still empty, see the Wiki's [Submodules](https://github.com/patrick-5546/ubc-course-explorer/wiki/For-Developers#submodules) section for more information about Git submodules.

## How to Run (the development environment)

- Optional: build the containers in the production environment to check for Python linting errors

  ```sh
  docker-compose -f docker-compose.prod.yml build
  ```

1. Start the application

    ```sh
    docker-compose up
    ```

- The application homepage can be found at [127.0.0.1:8000](http://127.0.0.1:8000/)
- Stop the application with `CTRL+BREAK`
  - Run `docker-compose down` to stop all running containers
    - Add the `-v` argument to additionally remove all containers and volumes, serving to delete the database
