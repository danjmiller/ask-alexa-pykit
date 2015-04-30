import cherrypy
import json
import dialog

server_config_path = "config/server_config.json"
class BasicResponse(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        input_json = cherrypy.request.json
        print ("Request", input_json)
        output_str = dialog.route_intent(input_json)
        return output_str
   
if __name__ == "__main__":
    
    with open(server_config_path, 'r') as server_conf_file:
        server_config = json.load(server_conf_file)
    
    print ("Loaded server config file")
    print (json.dumps(server_config, indent=4))
    """
    server_config = { 
        "server.ssl_module" : "builtin",
        "server.ssl_certificate" : "keys/new_cert.pem",
        "server.ssl_private_key": "keys/privkey.pem",
        "server.socket_host": '0.0.0.0',
        "server.socket_port": 443
    }
    """
    
    config = {"global": server_config}
    
    cherrypy.config.update(server_config)
    cherrypy.quickstart(BasicResponse(), config=config)