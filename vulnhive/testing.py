import sys

import vulnhive
from time import sleep
from pkg_resources import get_distribution

vulnhive.clean_all()
print("Version: ", get_distribution("vulnhive").version)
for server, cls in vulnhive.__dict__.items():
    if server.endswith("Server"):
        temp_server = cls(options="capture_commands")
        temp_server.run_server(process=True, auto=True)
        sleep(2)
        temp_server.test_server()
        sleep(2)
        temp_server.kill_server()
vulnhive.clean_all()
sys.exit()
