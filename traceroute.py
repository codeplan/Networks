#!/usr/bin/env python
##A simple program in PYTHON to implement 'traceroute' and search the country name of the different hops from the GeoIp databade##
import socket
import sys
import csv

def main(dest_name,countries):
        dest_addr = socket.gethostbyname(dest_name)
        port = 33434
        max_hops = 30
        icmp = socket.getprotobyname('icmp')
        udp = socket.getprotobyname('udp')
        ttl = 1
        f=csv.reader(open('country.csv','rU'))
        data = []
        for row in f:
            data.append(row)
        while True:
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            recv_socket.bind(("", port))
            send_socket.sendto("", (dest_name, port))
            curr_addr = None
            curr_name = None
            try:
                _, curr_addr = recv_socket.recvfrom(512)
                curr_addr = curr_addr[0]
                try:
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except socket.error:
                    curr_name = curr_addr
            except socket.error:
                pass
            finally:
                send_socket.close()
                recv_socket.close()

            if curr_addr is not None:
                curr_host = "%s (%s)" % (curr_name, curr_addr)
            else:
                curr_host = "*"
            print "%d\t%s" % (ttl, curr_host)
            a=[]
            a=coun(curr_addr,data) ###
            countries.append(a)
            ttl += 1
            if curr_addr == dest_addr or ttl > max_hops:
                break
        return countries

def coun(curr_addr,data):
    countries=[]
    add=curr_addr.split('.')
    #print add
    var=0
    #while data[var] is not None:
    for row in data:
        #print "fdgjdfgdfkg"    
        uplimit=row[1]
        
        lwlimit=row[0]
        uplimit=uplimit.split('.')
        lwlimit=lwlimit.split('.')
        #print uplimit
        #print lwlimit
        

        if add[0] == uplimit[0]:
            #print "gnvkdfhgkfd"
            if add[1] == lwlimit[1] or add[1] == uplimit[1]:
                if add[2] == uplimit[2] or add[2] == lwlimit[2]:
                    if add[3] == uplimit[3] or add[3] == lwlimit[3]:
                        return row[5]
                elif add[2] < uplimit[2] and add[2] > lwlimit[2]:
                    return row[5] 
              
            elif add[1] < uplimit[1] and add[1] > lwlimit[1]:
                return row[5]
        #else:
                    
    return "country NA"    
            

if __name__ == "__main__":
    countries=[]
    countries = main(sys.argv[1],countries)
    print "The packets are routing through the following countries:"
    for value in countries:
        print value