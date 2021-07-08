from flask import Flask
from redis import Redis


app = Flask(__name__)
r = Redis(host="redis", port=6379)


@app.route('/hello')
def say_hello():
    try:
        if not r.exists('name'):
            r.set('name', 'mehdi')

        name = r.get('name').decode()
        return f'Hello {name} \n'

    except Exception as e:
        return f'Error Occured - {e} \n'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, Debug=True)

