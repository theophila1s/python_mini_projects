# Quiz data using dictionary and tuples
quiz = {
    1: {
        "question": "What is the capital of France?",
        "options": ("A. London", "B. Paris", "C. Berlin", "D. Rome"),
        "answer": "B"
    },
    2: {
        "question": "What is the square root of 64?",
        "options": ("A. 6", "B. 7", "C. 8", "D. 9"),
        "answer": "C"
    },
    3: {
        "question": "Which language is primarily used for data science?",
        "options": ("A. Python", "B. Java", "C. HTML", "D. C++"),
        "answer": "A"
    },
    4: {
        "question": "What does RAM stand for?",
        "options": ("A. Read Access Memory", "B. Random Access Memory", "C. Ready and Move", "D. Run All Memory"),
        "answer": "B"
    },
    5: {
        "question": "Which planet is known as the Red Planet?",
        "options": ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
        "answer": "B"
    }
}

# Lambda function to generate remarks
get_remark = lambda score, total: (
    "🌟 Excellent!" if score == total else
    "👍 Good Job!" if score >= total * 0.6 else
    "📚 Keep Practicing!"
)

# Function to display a question
def display_question(q_data):
    print(f"\n{q_data['question']}")
    for option in q_data['options']:
        print(option)

# Function to check the answer
def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer.upper()

# Main quiz runner
def run_quiz():
    score = 0
    total = len(quiz)

    print("🎮 Welcome to the Quiz App!\n")

    for q_no, q_data in quiz.items():
        display_question(q_data)
        user_ans = input("Your answer (A/B/C/D): ").strip()

        if check_answer(user_ans, q_data["answer"]):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q_data['answer']}\n")

    print("Quiz Completed!")
    print(f"Your Score: {score}/{total}")
    print(f"Remark: {get_remark(score, total)}\n")

# Run the quiz app
run_quiz()
