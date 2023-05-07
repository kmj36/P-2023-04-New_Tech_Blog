'''
 ## API 앱
 # 작성자 : kmj36
 # 작성일 : 2023-05-07
 # History
 # 
 
'''
import sys
import subprocess
from v1 import APIv1

try:
    from flask import Flask
    from flask_restx import Api
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'flask'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'flask_restx'])
    from flask import Flask
    from flask_restx import Api
    
app = Flask(__name__)
api = Api(app)

api.add_namespace(APIv1, '/v1')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)