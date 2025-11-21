from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[
    'http://127.0.0.1:5173',
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # 허용할 출처
    allow_credentials=True,      # 자격 증명(쿠키, 인증 헤더) 허용
    allow_methods=["*"],         # 모든 HTTP 메서드 (GET, POST 등) 허용
    allow_headers=["*"],         # 모든 HTTP 헤더 허용
)



@app.get("/hello")
def hello():
    return {'message':'안녕하세요2'}