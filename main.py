
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.index import router_index


app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in router_index:
    app.include_router(router=router)

@app.get("/test")
def root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,workers=2, reload=True, log_level="debug")
      