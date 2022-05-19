# Wedding site

### Create new db
Create folder and file:
```
mkdir db
touch db.sqlite3
```
Create admin user:
```
python manage.py createsuperuser
```
Load models into database:
```
python manage.py makemigrations mainsite
python manage.py showmigrations mainsite
python manage.py sqlmigrate mainsite 0001
python manage.py migrate
```

### Run
Edit settings.py, and change SECRET_KEY.  
Copy in db.sqlite3  


```
sudo docker build . -t wedding
sudo docker run -p 9000:9000 -d wedding
sudo docker run -p 9000:9000 -v /FULL/PATH/wedding-app/db:/usr/src/app/db -d wedding
```

```
docker-compose up -d --build
```



### Create staticfiles
```
docker-compose run web /app/manage.py collectstatic --no-input
```

### Development
Copy in /migrations/  
Change in settings.py  
```
DEBUG = True
``` 
