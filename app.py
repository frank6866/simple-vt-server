from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import thread


from resources.server import ServerResource
from resources.server import ServerResourceList

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(ServerResourceList, '/proxy/servers')
api.add_resource(ServerResource, '/proxy/servers/<host>')


if __name__ == '__main__':
    # thread.start_new_thread(utils.scheduler.handle_task, ())
    app.run(host='0.0.0.0', port=5000, debug=True)




# api.add_resource(ExecutionList, '/executions')
# api.add_resource(Execution, '/executions/<execution_id>')
# api.add_resource(Master, '/master')
# api.add_resource(Agent, '/agent')
# api.add_resource(ServerDeploy, '/agent/deploy')
# api.add_resource(Docker, "/docker")
#
# # # cluster mapping
# # api.add_resource(ClusterResourceList, '/clusters')
# # api.add_resource(ClusterResource, '/clusters/<cluster_name>')
#
# # role mapping
# api.add_resource(RoleResourceList, '/roles')
# api.add_resource(RoleResource, '/roles/<role_id>')
#
# # server mapping
# api.add_resource(ServerResourceList, '/servers')
# api.add_resource(ServerResource, '/servers/<server_id>')
#
# # item mapping
# api.add_resource(ItemResourceList, '/items')
# api.add_resource(ItemResource, '/items/<item_id>')







