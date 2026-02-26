# OPTIONS 딕셔너리 참조
from options import OPTIONS

# 프롬프트 빌더 프로그램 안내 문구를 출력하는 함수
def introduce() :
    print (
        "Hello! Welcome to the Prompt_Builder.\n" +
        "Try selecting options directly to make the prompt more precise."
    )

    print("Available options : ")
    for key in OPTIONS:
        print(" - ", key)
