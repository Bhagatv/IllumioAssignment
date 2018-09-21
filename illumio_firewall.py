class IP_Interval:
    '''
    Class that stores IP intervals for ease of access when checking allowed IP addresses
    '''
    def __init__(self, ip_range):
        #Stores the IPs in a tuple so that they can be compared easily
        self.lower = tuple([int(i) for i in ip_range.split('-')[0].split('.')])
        self.upper = tuple([int(i) for i in ip_range.split('-')[1].split('.')])
        
    def contains(self, ip_address):
        '''
        Checks whether an ip address in the form of a string is within the range of this object
        '''

        
        ip_tuple = tuple([int(i) for i in ip_address.split('.')])

        if ip_tuple >= self.lower and ip_tuple <= self.upper:
            return True
        else:
            return False
        


class Firewall:
    def __init__(self, path):
        '''
        Schema of the dictionary map:
            {
                {'inbound' : {'tcp' : {port : [IP_Intervals]}}, 'udp' : {port : [IP_Intervals]}}, 
                {'outbound' : {'tcp' : {port : [IP_Intervals]}}, 'udp' : {port : [IP_Intervals]}}
            }
        self.rules = { 'inbound' : {'tcp' : dict(), 'udp' : dict()},
                       'outbound' : {'tcp' : dict(), 'udp' : dict()}
                     }

        file = open(path)

        for line in file:
            direction,protocol,port,ip = line.split(',')
            
            if direction == 'direction': #If the line is the header of the csv then skip the line
                continue
            
            if '-' in port: #If the port is a range
                port_lower = int(port.split('-')[0]) 
                port_upper = int(port.split('-')[1])
                for i in range(port_lower, port_upper + 1): #Iterate through the range and add the ports to the map
                    if i not in self.rules[direction][protocol]:
                        self.rules[direction][protocol][i] = []
                    if '-' in ip:
                        self.rules[direction][protocol][i].append(IP_Interval(ip)) #Add the IP Interval
                    else:
                        self.rules[direction][protocol][i].append(IP_Interval(ip + '-' + ip)) #Create an IP Interval of one IP to standardize searching
            else:
                if int(port) not in self.rules[direction][protocol]:
                    self.rules[direction][protocol][int(port)] = []
                if '-' in ip:
                    self.rules[direction][protocol][int(port)].append(IP_Interval(ip)) #Add the IP Interval
                else:
                    self.rules[direction][protocol][int(port)].append(IP_Interval(ip + '-' + ip)) #Create an IP Interval of one IP to standardize searching
                
                            
        file.close()           
            
            
            

        
        
    def accept_packet(self, direction, protocol, port, ip_address) -> bool:
        '''
        References the input rules of the object to determine whether to accept a packet
        '''
        try:
            if any([i.contains(ip_address) for i in self.rules[direction][protocol][port]]): #If any of the intervals contains the IP, then return True
                return True
            else:
                return False
        except KeyError: #If a port doesn't exist, then it is False
            return False
    
        
