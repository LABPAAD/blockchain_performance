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
ntrans = 0
cont = True
def timeout():
    global cont
    time.sleep(T)
    cont = False
    print("Tempo esgotado")

def funcao(j):
    text1 = "\nexecução: {} \n".format(j)
    list.append(text1)
    list.append("id return_code tempo   \n")
        #print(text)
    for i in range(N):
        #if (cont == False):
            #print(txCount)
        #    break
        id_str = sha256(str(time.time()).encode('utf-8')).hexdigest()
        cmd2 = '{"Args":["issue","Pedro","accessinfo","' + id_str + '"]}'
        cmd = "docker exec cli2 peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emrcontract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{}'".format(cmd2)

        #cmd = "sleep 2"
        inicio = timeit.default_timer()
        return_code = subprocess.call(cmd,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        #return_code = subprocess.call("sleep 2", shell=True)
        fim = timeit.default_timer()
        temp = fim-inicio
        text = [id_str, return_code, temp]
        #text = "{}     {}        {} \n".format(i,return_code,fim - inicio)
        #print(text)
        list.append(text)
        global ntrans
        ntrans +=1
    #list.append("\n{} Transações!\n".format(i+1))


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
    inicio = timeit.default_timer()

    #threading.Thread(target=timeout).start()
    #listThreads = []

    for i in range(T):
        thread = threading.Thread(target=funcao, args=(i,))
        thread.start()
        time.sleep(1)
        
    fim = timeit.default_timer()
    temtot = "Tempo total: {}".format(fim-inicio)
    prtntrans = "Numero total de transferencias: {}".format(ntrans)
    list.append(temtot)
    list.append(prtntrans)
    #arquivo.writelines(list)
    for i in list:
        arquivo.writelines("{}\n".format(i))
    print("Fim!!")
    print(temtot)
    print(prtntrans)
    
