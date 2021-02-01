# fast-ml-deploy
Example repo of machine learning model deployment with Fast API and Docker

This is a minimalistic build, consider to use user auth in a production environment

#Demo instructions


### 1. Build the docker image

```
docker build -t iris-ml-build .
```

### 2. Run the container

```
docker run -d -p 80:80 --name iris-api iris-ml-build 
```


### 3. Go to localhost
http://127.0.0.1/docs


### 4. Try out the post /predict method
```
curl -X POST "http://127.0.0.1/predict" -H\
 "accept: application/json"\
 -H "Content-Type: application/json"\
 -d "{\"data\":[[4.8,3,1.4,0.3],[2,1,3.2,1.1]]}"
```
### 5. Stop the server
```
ctrl + c
```
