from fastapi import FastAPI

app = FastAPI()

@app.get('/pets/')
async def get_all_pets():
    pets = [{'name': 'cat'}, {'name': 'dog'}]
    return pets
