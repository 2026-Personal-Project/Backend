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


# 옵션을 선택하는 함수
def select_prompt(options):
    length = 0
    
    while True:
        # 콘솔 화면을 지우는 명령어 (Windows 기준)
        subprocess.run("cls", shell=True) 

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


# 프로그램 실행 함수
def execution():
    options = []

    ui.menu()  # ui 파일의 introduce 함수 호출
    prompt = input_prompt()
    options_len = select_prompt(options)
    print(builder_prompt(prompt, options))


# 다른 파일에서 import 될 때 자동 실행을 방지하기 위한 조건문
if __name__ == "__main__":
    execution()