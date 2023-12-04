from flask import Flask, render_template, request
from main import main

app = Flask(__name__)
selected_songs, song_names, file_path = [], [], []

@app.route('/')
def index():
    return render_template('/genre-selection.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    # user input
    country = request.form['region-input']
    metric = request.form['sorting-metric']
    selected_songs.extend(main(country, metric))
    for song in selected_songs:
        song_names.append(song[0])
        file_path.append(f'static/mp3/{song[1]}')

    return render_template('quiz-question.html', path1=file_path[0], path2=file_path[1], path3=file_path[2], path4=file_path[3], path5=file_path[4], path6=file_path[5], path7=file_path[6], path8=file_path[7], path9=file_path[8], path10=file_path[9])

@app.route('/submit', methods=['POST'])
def submitQuestions():

    # guess is the user input, results are the user's correct or incorrect guesses
    guess = []
    results = []

    # add all the user input into an array, so that it is easier to check
    for x in range(10):
        guess.append(request.form.get(f"guess-input{x+1}"))

    # check to see if the user guessed the correct song and append the results to an array
    for index, answer in enumerate(guess):
        if answer == song_names[index]:
            results.append("Correct!")
        else:
            results.append("Incorrect!")

    # calculate the percent correct
    sum = 0

    for answer in results:
        if answer == "Correct!":
            sum += 1

    percentage = "{:.0%}".format(sum/10)

    return render_template('results.html', 
                           percentage=percentage, merge_time=selected_songs[10][0], heap_time=selected_songs[10][1],
                           song1=song_names[0], song2=song_names[1], song3=song_names[2], song4=song_names[3], song5=song_names[4], song6=song_names[5], song7=song_names[6], song8=song_names[7], song9=song_names[8], song10=song_names[9],
                           result1=results[0], result2=results[1],result3=results[2], result4=results[3], result5=results[4], result6=results[5],result7=results[6], result8=results[7], result9=results[8], result10=results[9])

if __name__ == '__main__':
    app.run(debug=True)