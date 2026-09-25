from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

    title='Choose Your own Story For Game',
    description='Api generates story',
    version='0.10.0',
    docs_url='/docs',
    redoc_url='/redoc'
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)