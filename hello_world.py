from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image height="191" width="642" src="http://www.geekadelphia.com/wp-content/uploads/2013/08/banner-642x191.png">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'Hello FOSSCON 2018!'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)