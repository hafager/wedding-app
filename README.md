# Wedding site

### Run
Edit settings.py, and change SECRET_KEY. 

```
sudo docker build . -t wedding
sudo docker run -p 9000:9000 -d wedding
```