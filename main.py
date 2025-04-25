from fastapi import FastAPI

app = FastAPI()


return_test = 'AI_TAT25A'
@app.get('/')
async def Here_We_GO():
  
    return {'message': return_test}

