from Select_type import select_type
from Input_prompt import input_prompt
from Select_prompt import select_prompt
from Builder_prompt import builder_prompt
from options import OPTIONS

def menu() :
    print (
        "|"+" Hello! Welcome to the Prompt_Builder.  " + "|\n" +
        "|"+" Try selecting options directly to make " + "|\n" +
        "|"+" the prompt more precise.               " + "|\n\n" 
    )
    print("프롬프트를 사용하는 목적을 입력해 주세요(ex : flower)")

def execution():
    options = []

    menu()  # 시작 메뉴
    prompt = input_prompt()
    prompt_type = select_type()

    if prompt_type == "image":
        # 이미지모드
        options_len = select_prompt(options)
        print(builder_prompt(prompt, options))
    else:
        #일반모드
        print(prompt)


# 다른 파일에서 import 될 때 자동 실행을 방지하기 위한 조건문
if __name__ == "__main__":
    execution()