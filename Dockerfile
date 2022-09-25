FROM python:3.8

WORKDIR /monitoring-app
COPY ./ /monitoring-app

RUN apt-get update \
    && apt-get install -y cron \
    && apt-get autoremove -y
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["./monitoring-app/app.py"]
