from flask import Flask
app = Flask(__name__)

def wrap_html(message):
    html = """
            <html>
                <div style="font_size:120px">
                    <center>
                        <img height=200 width=800 src='https://infosiftr.com/wp-content/uploads/2018/01/unnamed-2.png'>
                        {0}
                    </center>
                </div>
            </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'Hello DockerCon 2018!'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)