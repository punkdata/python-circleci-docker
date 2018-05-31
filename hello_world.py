from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
            <div style='font-size:120px;'>
            <center>
                <image height="200" width="800" src="https://infosiftr.com/wp-content/uploads/2018/01/unnamed-2.png">
                <br>
                {0}<br>
            </center>
            </div>
        </html>
    """.format(message)
    return html

@app.route('/')
def hello_world():
    message = wrap_html('Hello DockerCon!')
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)