from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = """
            <html>
                <div style='font-size:120px;'>
                <center>
                    Hello World
                </center>
                </div>
            </html>
        """
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)