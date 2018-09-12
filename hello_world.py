from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image height="458" width="720" src="https://secure.meetupstatic.com/photos/theme_body/9/a/8/e/full_7599566.jpeg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'Hello DevOps DC Meetup!'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)