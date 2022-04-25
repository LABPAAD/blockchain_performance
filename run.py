import sys
import threading
import time
import subprocess
import timeit
from hashlib import sha256
import datetime


N = 5
T = 10
list = []
cmd = "docker exec cli2 peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emr_contract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{'Args':['issue','Pedro','accessinfo','123']}"
def funcao(j):
    text1 = "execução: {} \n".format(j)
    list.append(text1)
    list.append("id return_code tempo   \n")
        #print(text)
    for i in range(N):
        id_str = sha256(str(time.time()).encode('utf-8')).hexdigest()
        #cmd = "sleep 2"
        inicio = timeit.default_timer()
        return_code = subprocess.call("echo Hello World", shell=True)
        #return_code = subprocess.call("sleep 2", shell=True)
        fim = timeit.default_timer()
        text = [i, return_code, fim-inicio]
        #text = "{}     {}        {} \n".format(i,return_code,fim - inicio)
        #print(text)
        list.append(text)


#*******************************************************************************
# Main:
#*******************************************************************************
if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("run.py <tps> <seconds> <log_name>")
        sys.exit(1)

    N = int(sys.argv[1])
    T = int(sys.argv[2])
    log_name = sys.argv[3]
    prt = "experiment: {} {} {} {}\n\n\n".format(N, T, log_name, datetime.datetime.now())
    print(prt)
    list.append(prt)
    arquivo = open(log_name, "a")
    for i in range(T):
        threading.Thread(target=funcao(i)).start()
        time.sleep(1)
    
    #arquivo.writelines(list)
    for i in list:
        arquivo.writelines(str(i))
    print("Fim!!")
    
