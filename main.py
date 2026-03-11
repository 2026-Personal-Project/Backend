# 프롬프트 타입 선택 함수 참조
from Select_type import select_type

#프롬프트 입력 함수 참조
from Input_prompt import input_prompt

# 옵션 선택 함수 참조
from Select_prompt import select_prompt

# 프롬프트 빌더 함수 참조
from Builder_prompt import builder_prompt

# OPTIONS 딕셔너리 참조
from options import OPTIONS

# 프롬프트 빌더 프로그램 안내 문구를 출력하는 함수
def menu() :
    print (
        "|"+" Hello! Welcome to the Prompt_Builder.  " + "|\n" +
        "|"+" Try selecting options directly to make " + "|\n" +
        "|"+" the prompt more precise.               " + "|\n\n" 
    )
    #"|"+" Select Menu with number 1,2,3          " + "|\n" +
        #"  > 1.Add options to existing prompts.    " + "|\n" +
        #"  > 2.Build prompts with Tag.             " + "|\n" +
        #"  > 3.Exit the program.                   " + "|\n" 
    print("프롬프트를 사용하는 목적을 입력해 주세요(ex : flower)")

# 프로그램 실행 함수
def execution():
    options = []

    menu()  # 초기 메뉴 출력
    prompt = input_prompt()
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