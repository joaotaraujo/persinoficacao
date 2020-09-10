#import OSC
#c = OSC.OSCClient()
#c.connect(('127.0.0.1', 9001))   # connect to SuperCollider
#oscmsg = OSC.OSCMessage()
#oscmsg.setAddress("/adress")
#oscmsg.append('HELLO')
#c.send(oscmsg)




# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse

# Start the system.
osc_startup()

# Make client channels to send packets.
osc_udp_client("127.0.0.1", 9030, "aclientname")

# Build a simple message and send it.
msg = oscbuildparse.OSCMessage("/adress", ",sif", ["text", 672, 8.871])
osc_send(msg, "aclientname")
osc_process()
