# Metabase Test

this repository, is a test repository, to use and being familiar with metabase

### technologies

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


### how to run

first install the requirements:
``` shell
pip install -r requirements.txt
```

migrate data to your database

``` shell
python manage.py migrate
```

migrate dataset to your database

``` shell
python main.py
```
note: before this migration, you should put the dataset inside your root directory.

you can find the data from this link:  https://www.kaggle.com/datasets/stephengoldie/big-databiopharmaceutical-manufacturing


use docker to install metabase
``` shell
cd metabase & docker compose up --build -d
```
note: you need to have docker installed on you system

### Critical Note

in django settings, in database section, you should change the credential and another settings.

also you should change it in docker compose of metabase.


