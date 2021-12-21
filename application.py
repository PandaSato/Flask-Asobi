from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route('/')
def hello():
    return render_template('testPage.html',test=['Nice','Welcome to Flask!'])

@application.route("/<user>")
def helloWorld(user):
    return "Hello goorm! "+user


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
