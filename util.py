def GetInputInt(prompt: str) -> int:
    while True:
        print(prompt)
        print('Accepted answers are Integers.')
        try:
            output = int(input())
            return output
        except:
            continue

def display_answers(question_id: int, question_text: str, answers: list[str]) -> None:
    reminder = f'{question_id}. {question_text}\n'
    reminder += 'Type "cancel" to terminate the program.'
    for i, answer in enumerate(answers):
        if i % 27 is 0:
            print('\n\n', reminder, end='\n\n')
        print(f'Answer {i}: {answer}', end=' ')
        if input().lower() == 'cancel':
            quit(0)