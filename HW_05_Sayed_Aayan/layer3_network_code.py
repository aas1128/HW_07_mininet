try:
    from mininet.net import Mininet
    from mininet.topo import Topo
    from mininet.log import setLogLevel, info
    from mininet.cli import CLI
except ImportError:
    pass 
class Layer3Topo( Topo ):
  #Task 2 
    def build( self ):
        """
        Function that congifures the network to represent the 3 Lans created previously. 
        """
        sA = self.addSwitch('sA')  # LAN A (0/63)
        sB = self.addSwitch('sB')  # LAN B (64/191)
        sC = self.addSwitch('sC')  # LAN C (192/223)


        #LAN A
        hA1 = self.addHost('hA1', ip='20.10.172.1/26') #Set to the smallest IP for Lan A 
        hA2 = self.addHost('hA2', ip='20.10.172.63/26') #Set to the largest IP for Lan A

        #LAN B
        hB1 = self.addHost('hB1', ip='20.10.172.65/25') #Set to the smallest IP for Lan B
        hB2 = self.addHost('hB2', ip='20.10.172.191/25') #Set to the largest IP for Lan B

       
        #Lan C (Need to make sure right ranges later aayan)
        hC1 = self.addHost('hC1', ip='20.10.172.192/27') #Set to the smallest IP for Lan C
        hC2 = self.addHost('hC2', ip='20.10.172.223/27') #Set to the largest IP for Lan C

        #connect each host to its switch 
        for host, switch in [
            (hB1, sB), (hB2, sB),
            (hA1, sA), (hA2, sA),
            (hC1, sC), (hC2, sC)
        ]:
            self.addLink(host, switch)

def runTest():
    """
    Function that initializes the network and then sends pings to each host
    in the network to verify connectivity.
    """
    topo = Layer3Topo()
    net = Mininet(topo=topo, controller=None)
    net.start()

    # Ping between hB1 and hB2
    net.ping([ net.get('hB1'), net.get('hB2') ])
    # Ping between hA1 and hA2
    net.ping([ net.get('hA1'), net.get('hA2') ])
    # Ping between hC1 and hC2
    net.ping([ net.get('hC1'), net.get('hC2') ])
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    runTest()