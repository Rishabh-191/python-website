from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return render_template('welcome.html', name=name)


app.run(debug=True)
