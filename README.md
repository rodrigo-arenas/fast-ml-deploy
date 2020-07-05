# fast-ml-deploy
Example repo of machine learning model deployment with Fast API and Docker

#Demo instructions


### 1. Install requirements
```
pip install -r requirements.txt --no-cache-dir
```

### 2. Run de app
* Use --reload only in dev environment
```
uvicorn app:app --reload --port 5000
```

### 3. Go to localhost
http://127.0.0.1:5000/docs


### 4. Try out the post /predict method
```
curl -X POST "http://127.0.0.1:5000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[4.8,3,1.4,0.3],[2,1,3.2,1.1]]}"
```
### 5. Stop the server
```
ctrl + c
```
