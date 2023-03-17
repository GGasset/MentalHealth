def GetInputInt(prompt: str) -> int:
    while True:
        print(prompt)
        print('Accepted answers are Integers.')
        try:
            output = int(input())
            return output
        except:
            continue