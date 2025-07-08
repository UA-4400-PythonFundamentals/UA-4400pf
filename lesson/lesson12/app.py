from flask import Flask, url_for, redirect, request, render_template
from user import User



app = Flask(__name__)
User.generate_dummy_users(10)



@app.route('/')
@app.route('/<int:pk>', methods=['GET', 'POST'])
def hello(pk=None):

    if pk is not None:
        if request.method == 'POST':
            user = User.get(pk)
            if not user:
                return render_template('user.html')
            else:
                username = request.form.get('username')
                if username:
                    user.username = username
                return render_template('index.html', users=User.get_all())

        elif request.method == 'GET':
            user = User.get(pk)
            return render_template('user.html', user=user)
    else:
        return render_template('index.html', users=User.get_all())




if __name__ == '__main__':

    
    app.run(host="0.0.0.0", port=3001, debug=True)