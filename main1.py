from fastapi import FastAPI

app = FastAPI()


@app.get('/getbalance')
def getbalance():
    return 'Balance'


