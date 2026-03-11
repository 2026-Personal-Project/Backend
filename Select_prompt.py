# OS 모듈과 subprocess 모듈 참조
import subprocess

# OPTIONS 딕셔너리 참조
from options import OPTIONS

# INTRO_OPTION 함수 참조
from Intro_option import intro_option

# 옵션을 선택하는 함수 (이미지 타입에서만 호출)
def select_prompt(options):
    value_length = 0

    # 무한 루프 방지용 초기값, 실제로는 사용자 입력을 받아야 함
    value = "default" 

    while True :
        # 콘솔 화면을 지우는 명령어 (Windows 기준)
        subprocess.run("cls", shell=True)  
        
         # OPTIONS 딕셔너리에 있는 옵션들을 출력하는 함수 호출
        intro_option()

         # OPTIONS 딕셔너리에 존재하지 않는 값일 경우 예외 처리
        if value not in OPTIONS and value not in ("exit", "stop"):
            # 첫번째 루프에 대해서는 
            if value != "default" :
                print("유효하지 않은 옵션입니다. 다시 입력해주세요.\n\n")
                if value != "return" :
                    value = "return"
                    continue
        
        print("옵션 선택을 중단하려면 'stop' 또는 'exit'를 입력하세요.")
        value = input("Select the options : ")

        # 종료 명령어 입력 시 반복 종료
        if value == "exit" or value == "stop":
            break

        # 유효한 옵션일 경우 리스트에 추가
        options.append(value)
        value_length += 1

    return value_length

