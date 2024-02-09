#Quiz 1


def run_quiz(): 
    questions = {
        "What is the capital of France?" : "Paris",
        "What is 2 + 2?" : "4",
        "What is the capital of Italy?": "Rome"
    }
    score = 0
    
    
    
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
        
        return score

run_quiz()

