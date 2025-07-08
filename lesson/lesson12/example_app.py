from flask import Flask, url_for, redirect, request


MY_APP = Flask(__name__)


@MY_APP.route('/')
def hello_world():
    return 'Hello, World!'

@MY_APP.route('/name')
def hello_name():
    return 'Hello, name!'

@MY_APP.route('/name/<my_name>')
def hello_name_cust(my_name):
    try:
        n = int(my_name)
        print(n)
        return redirect(url_for("hello_name_cust_n", my_name="taras", count=n))
    except:
        pass
    return f'Hello, {my_name}!'


@MY_APP.route('/name/<my_name>/<int:count>')
def hello_name_cust_n(my_name, count):
    return f'Hello, {my_name*count}!'

@MY_APP.route('/test', methods=['GET', 'POST', "PUT"])
def test_url():
    if request.method == "GET":
        return "get"
    elif request.method == "POST":
        return "POST"
    elif request.method == "PUT":
        return "PUT"

if __name__ == '__main__':
    # with MY_APP.test_request_context():
    #     print(url_for("hello_world"))
    #     print(url_for("hello_name"))
    #     print(url_for("hello_name_cust", my_name="taras"))
    #     print(url_for("hello_name_cust_n", my_name="taras", count=5))

    MY_APP.run(host="0.0.0.0", port=3001, debug=True)