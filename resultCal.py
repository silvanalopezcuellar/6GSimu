import numpy as np


def throughputCal(nodeNum, data):
    throughput_node = np.zeros(nodeNum)

    for n in range(nodeNum):

        # Select only data from node n and succesfull packets
        dataSucc = data[(data[:, 0] == n) & (data[:, 3] == 1), :]

        if dataSucc.shape[0] == 0:
            throughput_node[n] = 0;  
        else:
            throughput_node[n] = np.mean(dataSucc[:, 1] * 8 / dataSucc[:, 2])
               
    return throughput_node

if __name__ == "__main__":

    handshake_ways = 3
    nodeNum = 3
    Tia = 200

    filename = f'/home/silvana/ns3/ns-allinone-3.44/ns-3.44/contrib/thz-thz-1.2/results/result_{handshake_ways}way_{nodeNum}n_{Tia}us_1.txt'
    data = np.loadtxt(filename)

    #Throughput calculation
    throughput = np.mean(throughputCal(nodeNum,data)) # [Gbps] Average throughput
    print("Throughput =", throughput, " Gbps") #print Throughput

    #Discard rate
    discard_rate = sum(data[:,4])/data.shape[0] #Takes the total success packages and divided over the total packages
    print("Discard rate = ", discard_rate ,"") #print Throughput

    #[us] Average packet time
    dataSucc = data[(data[:, 3] == 1), :]
    end = dataSucc.shape[0]  #obtain the total of packages 
    average_packet_time = np.mean(dataSucc[round(end/10):-1,2])*1e-3 
    print("Average packet time = ", average_packet_time ,"us\n") #print Average packet time



