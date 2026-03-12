import subprocess
from options import OPTIONS
from Intro_option import intro_option
def select_prompt(options):
    value_length = 0
    value = "default" 

    while True :
        subprocess.run("cls", shell=True)  
        intro_option()
        if value not in OPTIONS and value not in ("exit", "stop"):
            if value != "default" :
                print("유효하지 않은 옵션입니다. 다시 입력해주세요.\n\n")
                if value != "return" :
                    value = "return"
                    continue
        
        print("옵션 선택을 중단하려면 'stop' 또는 'exit'를 입력하세요.")
        value = input("Select the options : ")

        if value == "exit" or value == "stop":
            break

        options.append(value)
        value_length += 1

    return value_length

