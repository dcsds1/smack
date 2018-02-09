from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run()
