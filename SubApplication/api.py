from fastapi import FastAPI


app = FastAPI()

@app.get('/app')
def read_main():
    return {"message": "Hello from the main app"}

subapp_one = FastAPI()

@subapp_one.get("/subone")
def