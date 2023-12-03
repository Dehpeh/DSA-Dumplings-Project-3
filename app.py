from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/genre-selection.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['region-input']
    processed_result = f"You entered: {user_input}"
    return render_template('results.html', result=processed_result)

if __name__ == '__main__':
    app.run(debug=True)