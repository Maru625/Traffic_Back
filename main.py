from fastapi import FastAPI
import uvicorn

from router import index

app = FastAPI()

for router in index.router_index:
    app.include_router(router=router)

@app.get("/test")
def root():
    return {"Hello": "World"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# conda install -c conda-forge uvicorn
# conda install -c conda-forge fastapi


