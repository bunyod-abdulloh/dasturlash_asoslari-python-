from pywebio.input import input_group, input, radio
from pywebio.output import put_text, put_success, put_error
from pywebio import start_server

# Savollar va to'g'ri javoblar ro'yxati
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct": "Mars"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Leo Tolstoy", "Mark Twain", "Charles Dickens"],
        "correct": "William Shakespeare"
    }
]


# Foydalanuvchiga savollarni berish
def quiz_test():
    score = 0
    answers = []

    for i, q in enumerate(questions):
        user_answer = input_group(f"Question {i + 1}", [
            radio(f"{q['question']}", options=q["options"], name=f"q{i}")
        ])
        answers.append(user_answer[f'q{i}'])

        # Javobni tekshirish
        if user_answer[f'q{i}'] == q['correct']:
            score += 1

    # Natijalarni chiqarish
    put_text("Quiz results:")
    for i, q in enumerate(questions):
        if answers[i] == q['correct']:
            put_success(f"Question {i + 1}: Correct!")
        else:
            put_error(f"Question {i + 1}: Wrong! Correct answer is {q['correct']}")

    put_text(f"Your total score: {score}/{len(questions)}")


# Web serverni boshlash
if __name__ == '__main__':
    start_server(quiz_test, port=8080)
