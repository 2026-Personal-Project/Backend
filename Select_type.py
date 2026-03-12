def select_type():
    print("일반과 이미지 중 사용하시려는 타입을 선택 해 주세요")
    while True:
        value = input("Choose prompt type ('general' or 'image'): ").strip().lower()
        if value in ("general", "image"):
            return value
        print("잘못된 입력입니다. 'general' 또는 'image'를 입력해주세요.")