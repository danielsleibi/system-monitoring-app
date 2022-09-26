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
To create a containarized database using docker, replace inside the quotations('') and run the command:
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

## APIs
The application has 6 APIs, see the following list:
- /api/cpu_util
- /api/cpu_util_current
- /api/disk_usage
- /api/disk_usage_current
- /api/memory_usage
- /api/memory_usage_current

*2 parameters can be used all, and hour, only use without the APIs that have _'current'_ in their names*

*Please note if you use the hour parameter with all it will not have any effect and will return all usage data regardless of the specified hour*

Examples:
- /api/cpu_util

Would return all cpu utilization for the current day

- /api/cpu_util?hour=10

Would return cpu utilization for the 10th hour of the current day

- /api/cpu_util?all=true

Would return all cpu utilization stored in the database regardless of time

