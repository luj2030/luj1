from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

# Get the current time
current_date = datetime.datetime.now().date()
current_time = str(datetime.datetime.now().time().strftime("%H:%M"))


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's prediction from the form
        morocco = request.form.get('morocco')
        if not morocco:
            morocco = "None"
        print(morocco)

        france = request.form.get('france')
        # If no prediction was made, default to "None"
        if not france:
            france = "None"
        print(france)# Print the prediction

        extra = request.form.get('extra')
        if not extra:
            extra = "None"
        print(extra)

        name = request.form.get('name')
        if not name:
            name = "None"
        print(name)



        # Connect to the database
        conn = sqlite3.connect('predictions.db')
        c = conn.cursor()
        # Save the prediction to the database
        c.execute("INSERT INTO predictions (date, time, morocco, france, extra, name) VALUES (?,?,?,?,?,?)",
                  (current_date, current_time, morocco, france, extra, name))
        conn.commit()
        conn.close()
        return redirect('/results')
    return render_template('index.html')


@app.route('/results')
def results():
    # Connect to the database
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    # Fetch the predictions from the database
    c.execute("SELECT * FROM predictions")
    predictions = c.fetchall()
    # Close the database connection
    conn.close()
    # Format the predictions for display in the template
    formatted_predictions = []
    for prediction in predictions:
        formatted_predictions.append({
            'id': prediction[0],
            'date': prediction[1],
            'time': prediction[2],
            'name': prediction[3],
            'morocco': prediction[4],
            'france': prediction[5],
            'extra': prediction[6]
        })

    return render_template('results.html', predictions=formatted_predictions)







if __name__ == '__main__':
    app.run()



