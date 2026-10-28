from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel

def myTopology():

    net = Mininet(controller=None, switch=OVSBridge)

    # Add switchesA
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    h4 = net.addHost('h4', ip='10.0.0.4/24')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2)
    net.addLink(h3, s2)
    net.addLink(h4, s2)

    # Start network
    net.start()

    # Display topology information
    net.pingAll()

    # Open Mininet CLI
    CLI(net)

    # Stop network
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myTopology()