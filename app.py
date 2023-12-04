from flask import Flask, render_template, request

app = Flask(__name__)

# song names from sorting algorithms
song_names = ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]

# run-times
merge = "0.2s"
heap = "0.4s"

@app.route('/')
def index():
    return render_template('/genre-selection.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    # user input
    country = request.form['region-input']
    metric = request.form['sorting-metric']

    print(f'Text Input: {country}')
    print(f'Selected Option: {metric}')

    filePath = ["spotifydown.com - Would I Lie to You - Radio Edit.mp3", "/static/mp3/spotifydown.com - Treat You Better.mp3", "/static/mp3/spotifydown.com - Would I Lie to You - Radio Edit.mp3", "/static/mp3/spotifydown.com - Treat You Better.mp3", "/static/mp3/spotifydown.com - Would I Lie to You - Radio Edit.mp3", "/static/mp3/spotifydown.com - Treat You Better.mp3", "/static/mp3/spotifydown.com - Would I Lie to You - Radio Edit.mp3", "/static/mp3/spotifydown.com - Treat You Better.mp3", "/static/mp3/spotifydown.com - Would I Lie to You - Radio Edit.mp3", "/static/mp3/spotifydown.com - Treat You Better.mp3"]
   
    return render_template('quiz-question.html', path1=filePath[0], path2=filePath[1], path3=filePath[2], path4=filePath[3], path5=filePath[4], path6=filePath[5], path7=filePath[6], path8=filePath[7], path9=filePath[8], path10=filePath[9])

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
                           percentage=percentage, merge_time=merge, heap_time=heap,
                           song1=song_names[0], song2=song_names[1], song3=song_names[2], song4=song_names[3], song5=song_names[4], song6=song_names[5], song7=song_names[6], song8=song_names[7], song9=song_names[8], song10=song_names[9],
                           result1=results[0], result2=results[1],result3=results[2], result4=results[3], result5=results[4], result6=results[5],result7=results[6], result8=results[7], result9=results[8], result10=results[9])

if __name__ == '__main__':
    app.run(debug=True)