from flask import Flask, session, redirect, url_for, render_template, request
from datetime import datetime
from data import LESSONS, QUIZ_QUESTIONS

app = Flask(__name__)
app.secret_key = "token-optimizer-secret"

def compute_score(quiz_answers, quiz_questions):
    score = 0
    details = []
    for q in quiz_questions:
        # User answer comes from session which is saved as lists of strings, convert to ints
        user_ans = set([int(x) for x in quiz_answers.get(str(q["num"]), [])])
        correct_ans = set(q["correct"])
        is_correct = (user_ans == correct_ans)
        if is_correct:
            score += 1
        details.append({
            "question": q["question"],
            "user_answer_indices": list(user_ans),
            "correct_indices": list(correct_ans),
            "is_correct": is_correct,
            "explanation": q["explanation"],
            "options": q["options"]
        })
    return score, details

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start():
    session['start_time'] = datetime.now().isoformat()
    session['lesson_visits'] = {}
    session['quiz_answers'] = {}
    return redirect(url_for('learn', lesson_num=1))

@app.route('/learn/<int:lesson_num>')
def learn(lesson_num):
    if lesson_num < 1 or lesson_num > 4:
        return redirect(url_for('home'))
        
    # Store page entry timestamp
    if 'lesson_visits' not in session:
        session['lesson_visits'] = {}
    
    # Needs to be marked modified if updating a nested dict?
    # Session dicts are not always automatically tracked, so we assign back
    visits = session.get('lesson_visits', {})
    if str(lesson_num) not in visits:
        visits[str(lesson_num)] = datetime.now().isoformat()
        session['lesson_visits'] = visits
    
    lesson = next((l for l in LESSONS if l['num'] == lesson_num), None)
    if not lesson:
        return redirect(url_for('home'))
        
    page_context = f"Lesson {lesson_num} of 4"
    return render_template('learn.html', lesson=lesson, page_context=page_context)

@app.route('/learn/<int:lesson_num>/next', methods=['POST'])
def learn_next(lesson_num):
    if lesson_num < 4:
        return redirect(url_for('learn', lesson_num=lesson_num + 1))
    else:
        return redirect(url_for('quiz', q_num=1))

@app.route('/quiz/<int:q_num>')
def quiz(q_num):
    if q_num < 1 or q_num > 5:
        return redirect(url_for('home'))
        
    question = next((q for q in QUIZ_QUESTIONS if q['num'] == q_num), None)
    if not question:
        return redirect(url_for('home'))
        
    page_context = f"Quiz Q {q_num} of 5"
    
    show_feedback = request.args.get('feedback') == '1'
    feedback = None
    if show_feedback:
        answers_dict = session.get('quiz_answers', {})
        user_ans = set([int(x) for x in answers_dict.get(str(q_num), [])])
        correct_ans = set(question["correct"])
        is_correct = (user_ans == correct_ans)
        feedback = {
            "is_correct": is_correct,
            "user_answer_indices": list(user_ans),
            "correct_indices": list(correct_ans),
            "explanation": question["explanation"]
        }
        
    return render_template('quiz.html', question=question, page_context=page_context, feedback=feedback)

@app.route('/quiz/<int:q_num>/answer', methods=['POST'])
def quiz_answer(q_num):
    answers = request.form.getlist("answer")
    
    answers_dict = session.get('quiz_answers', {})
    answers_dict[str(q_num)] = answers
    session['quiz_answers'] = answers_dict
    
    return redirect(url_for('quiz', q_num=q_num, feedback=1))

@app.route('/results')
def results():
    answers_dict = session.get('quiz_answers', {})
    score, details = compute_score(answers_dict, QUIZ_QUESTIONS)
    page_context = "Results"
    return render_template('results.html', score=score, details=details, page_context=page_context)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
