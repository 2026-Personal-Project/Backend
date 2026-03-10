# ui 파일 참조
import ui

# OS 모듈과 subprocess 모듈 참조
import subprocess

# OPTIONS 딕셔너리 참조
from options import OPTIONS

# 프롬프트 최대 글자 수 제한 (1500자)
MAX_LENGTH = 1500


# 기본 프롬프트를 입력받는 함수 (글자 수 제한 적용)
def input_prompt():
    while True:
        prompt = input("Input your base prompt : ")
        if len(prompt) > MAX_LENGTH:
            print("프롬프트 글자 수 제한을 초과했습니다. 다시 입력해주세요.\n")
            continue
        break
    return prompt


# 옵션을 선택하는 함수 (이미지 타입에서만 호출)
def select_prompt(options):
    length = 0
    
    while True :

        # OPTIONS 딕셔너리에 있는 옵션들을 출력하는 함수 호출
        ui.intro_option()
        print("옵션 선택을 중단하려면 'stop' 또는 'exit'를 입력하세요.")
        value = input("Select the options : ")

        # 종료 명령어 입력 시 반복 종료
        if value == "exit" or value == "stop":
            break

        # OPTIONS 딕셔너리에 존재하지 않는 값일 경우 예외 처리
        if value not in OPTIONS:
            print("유효하지 않은 옵션입니다.")
            continue

        # 유효한 옵션일 경우 리스트에 추가
        options.append(value)
        length += 1

    return length


# 선택한 옵션을 기본 프롬프트에 추가하는 함수
def builder_prompt(base, options):
    prompt = base

    for opt in options:
        # 안전성을 위해 OPTIONS 존재 여부 재확인
        if opt in OPTIONS:
            prompt += ", " + OPTIONS[opt]

    return prompt


# 프롬프트 타입(일반/이미지)을 선택하는 함수

def select_type():
    while True:
        value = input("Choose prompt type ('general' or 'image'): ").strip().lower()
        if value in ("general", "image"):
            return value
        print("잘못된 입력입니다. 'general' 또는 'image'를 입력해주세요.")


# 프로그램 실행 함수
def execution():
    options = []

    ui.menu()  # 초기 메뉴 출력
    prompt = input_prompt()
    print("일반과 이미지 중 사용하시려는 타입을 선택 해 주세요")
    prompt_type = select_type()

    if prompt_type == "image":
        # 이미지일 때만 태그(옵션) 선택
        options_len = select_prompt(options)
        print(builder_prompt(prompt, options))
    else:
        # 일반 텍스트 프롬프트는 옵션 없이 그대로
        print(prompt)


# 다른 파일에서 import 될 때 자동 실행을 방지하기 위한 조건문
if __name__ == "__main__":
    execution()