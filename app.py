from flask import Flask
from flask_cors import CORS
from flask_restful import Api


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(ServerResourceList, '/proxy/servers')
api.add_resource(ServerResource, '/proxy/servers/<host>')


if __name__ == '__main__':
    # thread.start_new_thread(utils.scheduler.handle_task, ())
    app.run(host='0.0.0.0', port=5000, debug=True)






