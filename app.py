from flask import Flask, render_template, send_from_directory
app = Flask(__name__, static_url_path='')


@app.route("/")
def run():
    return render_template('index.html')

@app.route('/monthly_reports/<path:path>')
def send_pdf(path):
    return send_from_directory('monthly_reports', path)