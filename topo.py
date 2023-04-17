
from ryu.base import app_manager
from ryu.topology import event
from ryu.topology import switches
 
from ryu.base import app_manager
from ryu.topology import event
from ryu.topology import switches
import logging
 
class MyTopology(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(MyTopology, self).__init__(*args, **kwargs)
        self.topology_api_app = self
 
    def _register_switches(self):
        # Register switches
        self.topology_api_app.switch_map = switches.SwitchMap()
 
        for i in range(1, 4):
            switch = switches.Switch(i)
            self.topology_api_app.switch_map.register_switch(switch)
        # Example of print statement
        print("Registered switches in the topology")
 
    def _register_links(self):
        # Register links
        self.topology_api_app.link_list = []
 
        # Switches connected to controller
        for i in range(1, 4):
            link = event.EventLinkAdd(i, 0, 1, i)
            self.topology_api_app.link_list.append(link)
        # Example of logging statement
        logging.info("Registered links in the topology")
 
    def _register_hosts(self):
        # Register hosts
        self.topology_api_app.host_map = {}
 
        for i in range(1, 4):
            host = event.EventHostAdd(str(i), 0, i)
            self.topology_api_app.host_map[str(i)] = host
        # Example of logging statement
        logging.info("Registered hosts in the topology")
 
    def switch_features_handler(self, ev):
        self._register_switches()
        self._register_links()
        self._register_hosts()
 
if __name__ == '__main__':
    # Example of logging configuration
    logging.basicConfig(filename='my_topology.log', level=logging.DEBUG)
    MyTopology().run()