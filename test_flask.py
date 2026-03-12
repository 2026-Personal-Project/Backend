from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "success", "message": "AI 프롬프트 제작 사이트 백엔드 작동 중!"}

@app.get("/ai-test")
def test_ai():
    return {"result": "여기에 AI API 결과값이 출력될 예정입니다."}