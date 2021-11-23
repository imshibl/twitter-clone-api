# Twitter-Clone-Api(build with Python FastAPI)

This is a simple twitter clone that include login/signup,tweets,followers and followings.

## Technologies used:

python(Fast-API)  
postgresql  
sqlalchemy  
deta(for api deployment)  
herkou(postgresql)  

### Try it out

deta link(published api url): https://pio7h0.deta.dev/docs   
you can try this using ThunderClient(vscode) or in Postman

## To use

1.Create a new virtualenvironment and install the requirements.txt 
```
(venv) pip install -r requirements.txt
```
2.setup your datbase in database.py.refer https://fastapi.tiangolo.com/tutorial/sql-databases/

3.Run on your machine:  
```
(venv) PS E:\twitter clone\backend\app>uvicorn main:app --reload
```
4.After making changes you can deploy it into Deta.refer https://fastapi.tiangolo.com/deployment/deta/



