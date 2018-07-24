from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:120px;'>
            <center>
                <image height="544" width="1042" src="https://cdn-1.wp.nginx.com/wp-content/uploads/2018/03/Google-Cloud-Next-18.jpg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = ''
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)