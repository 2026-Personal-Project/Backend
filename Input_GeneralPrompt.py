from Input_SelectType import MAX_LENGTH

def input_general():
    while True:
        prompt = input("Input your base prompt for general: ")
        if len(prompt) > MAX_LENGTH:
            print("프롬프트 글자 수 제한을 초과했습니다. 다시 입력해주세요.\n")
            continue
        break
    return prompt