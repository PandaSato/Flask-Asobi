from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route('/')
def hello():
    _text = 'Welcome to Flask!\n Do you know 21*37?\n if you know the answer, please input that in URL!'
    return render_template('testPage.html',subject = 'Hello World', text = _text.split('\n'))

@application.route("/<answer>")
def helloWorld(answer):
    if answer == '777':
        return render_template('testPage.html',subject='Welcome to 777 World!',text=['Now you started your journey!'])
    return 'There is nothing but you. Please go to the first!'


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
