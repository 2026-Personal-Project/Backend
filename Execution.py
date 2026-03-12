from Show_Intro import menu
from Input_SelectType import select_type
from Input_ImagePrompt import input_image
from Input_GeneralPrompt import input_general

def execution():
    options = []

    menu()  # 시작 메뉴
    prompt_type = select_type()

    if prompt_type == "image":
        # 이미지모드
        print(input_image(options))
    else:
        #일반모드
        print(input_general())

# 다른 파일에서 import 될 때 자동 실행을 방지하기 위한 조건문
if __name__ == "__main__":
    execution()