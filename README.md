# system-monitoring-app
A flask based system monitoring webapp using Python3

## Starting The Application
The application can be started using the following command:
> $ python3 run ./monitoring-app/app.py

*Please note that the cwd must be this projects directory*

This application connects to a ***MYSQL*** database and therefore you must have the connection information to the DB set in the enviroment variables or the defaults would be used.
Default enviroment variables are:
- DB_HOST: "0.0.0.0"
- DB_PORT: "3306"
- DB_NAME: "system_stats"
- DB_USER: "root"
- DB_PASSWORD: ""

## MYSQL Database
**The application _will_ create missing tables in the database on startup but it _will not_ create a new database**
To create a containarized database using docker, replace inside the cotations('') and run the command:
> \# docker run --name *'NAME_OF_CONTAINER'* -p *'ANY_EMPTY_PORT'*:3306 -e MY_SQL_ROOT_PASSWORD=*'PASSWORD'* -d mysql

*Please note the you must run and set enviroment variables for the application after creating the database*

## Application on Docker
A Dockerfile is avaiable with the project also an image is published on dockerhub.

*link for image: DONT FORGET TO ADD LINK*

To build the image, run command:
> \# docker build .

*Please note that the cwd must be this projects directory*

To run the built image, run command:
> \# docker run *IMAGE_ID* -p 5000:5000 --env DB_HOST=*ip* --env DB_PORT=*port* --env DB_NAME=*name* --env DB_USER=*username* --env DB_PASSWORD=*password*, 
