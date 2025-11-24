from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from domain.question import question_router


app = FastAPI()

origins=[
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # 허용할 출처
    allow_credentials=True,      # 자격 증명(쿠키, 인증 헤더) 허용
    allow_methods=["*"],         # 모든 HTTP 메서드 (GET, POST 등) 허용
    allow_headers=["*"],         # 모든 HTTP 헤더 허용
)


app.include_router(question_router.router)