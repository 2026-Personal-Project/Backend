MAX_LENGTH = 1500 # 프롬프트 최대 글자 수 제한 (1500자)

def input_prompt():
    while True:
        prompt = input("Input your base prompt : ")
        if len(prompt) > MAX_LENGTH:
            print("프롬프트 글자 수 제한을 초과했습니다. 다시 입력해주세요.\n")
            continue
        break
    return prompt
