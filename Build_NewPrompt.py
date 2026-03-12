from List_Option import OPTIONS

def builder_prompt(base, options):
    prompt = base

    for opt in options:
        if opt in OPTIONS:
            prompt += ", " + OPTIONS[opt]

    return prompt

