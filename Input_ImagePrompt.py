from Input_SelectType import MAX_LENGTH
from Select_PromptOption import select_prompt
from Build_NewPrompt import builder_prompt

def input_image(options):
    while True:
        prompt = input("Input your base prompt for image: ")
        if len(prompt) > MAX_LENGTH:
            print("프롬프트 글자 수 제한을 초과했습니다. 다시 입력해주세요.\n")
            continue
        break
    return builder_prompt(prompt,select_prompt(options))