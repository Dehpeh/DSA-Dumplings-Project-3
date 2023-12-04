from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/genre-selection.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    country = request.form['region-input']
    metric = request.form['sorting-metric']

    print(f'Text Input: {country}')
    print(f'Selected Option: {metric}')

    return render_template('quiz-question.html')

if __name__ == '__main__':
    app.run(debug=True)