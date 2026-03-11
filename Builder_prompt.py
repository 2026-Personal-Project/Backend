# OPTIONS 딕셔너리 참조
from options import OPTIONS

# 선택한 옵션을 기본 프롬프트에 추가하는 함수
def builder_prompt(base, options):
    prompt = base

    for opt in options:
        # 안전성을 위해 OPTIONS 존재 여부 재확인
        if opt in OPTIONS:
            prompt += ", " + OPTIONS[opt]

    return prompt

