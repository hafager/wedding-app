# Wedding site

### Run
Edit settings.py, and change SECRET_KEY.  
Copy in db.sqlite3  


```
sudo docker build . -t wedding
sudo docker run -p 9000:9000 -d wedding
```

### Development
Copy in /migrations/  
Change in settings.py  
```
DEBUG = True
``` 
