from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':
        hrs = float(request.form['hrs'])
        marks_pred = m.marks_prediction(hrs)

        return render_template(
            'index.html',
            prediction=marks_pred
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)