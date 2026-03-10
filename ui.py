# msvcrt 헤더 참조
import msvcrt
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
    
def intro_option():
    # 이미지 프롬프트에 사용할 수 있는 태그(옵션)를 표시
    print("Available options : ")
    for key in OPTIONS:
        print(" - ", key)
