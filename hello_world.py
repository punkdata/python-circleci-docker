from flask import Flask

app = Flask(__name__)
def wrap_html(text):
    msg = """
        <html>
            <div style='font-size:120px;'>
            <center>
                {0}
            </center>
            </div>
        </html>
    """.format(text)
    return msg

@app.route('/')
def hello_world():
    msg = wrap_html('Hello World')
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)