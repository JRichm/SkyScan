from flask import Flask, render_template
import jinja2

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined # for debugging purposes
app.secret_key = 'dummdumm'

        ##  Flask Routes  ##
@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True, port=8565, host='localhost')