from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

net.setLogLevel('info')

net.addP4Switch('s1')
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')

net.setP4Source('s1','./p4_src/l2_forwarding.p4')

net.addLink('s1', 'h1')
net.addLink('s1', 'h2')
net.addLink('s1', 'h3')
net.addLink('s1', 'h4')

net.setBwAll(5)

net.enableLogAll()

net.enableCli()
net.startNetwork()
