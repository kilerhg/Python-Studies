from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from functools import wraps
import datetime


def check_auth(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        # try:
        decoded = jwt
        # except:
        #     return jsonify({'message': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorator 
    # Foda que to meio pa, pq minha mãe ta fazendo um montão de comida tbm ;/


app = Flask(__name__)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'super-secret'


@app.route('/unprotected')
def unprotected():
    return 'Unprotected'


@app.route('/protected')
@check_auth
def protected():
    return 'Protected'

@app.route('/login')
def login():
    auth = request.authorization
    
    if auth and auth.password == 'secret':
        token = create_access_token(identity=auth.username, expires_delta=datetime.timedelta(minutes=30))
        
        return jsonify({'token': token})
    else:
        return make_response('Login failed', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

@app.route('/logout')
def logout():
    pass


if __name__ == '__main__':
    app.run(debug=True)