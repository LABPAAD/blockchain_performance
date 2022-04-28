import sys
import threading
import time
import subprocess
import timeit
from hashlib import sha256
import datetime


list = []

cont = True
def timeout(T):
    global cont
    time.sleep(T)
    cont = False

def funcao(id_str):
    cmd2 = '{"Args":["issue","Pedro","accessinfo","' + id_str + '"]}'
    cmd = "docker exec cli2 peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emrcontract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{}'".format(cmd2)

    inicio = timeit.default_timer()
    return_code = subprocess.call(cmd,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    
    fim = timeit.default_timer()
    temp = fim-inicio
    text = [id_str, return_code, temp]
   
    list.append(text)
    
    


#*******************************************************************************
# Main:
#*******************************************************************************
if __name__ == '__main__':

    if len(sys.argv) != 4:
        sys.exit(1)

    N = int(sys.argv[1])
    T = int(sys.argv[2])
    log_name = sys.argv[3]
    prt = "experiment: {} {} {} {}\n\n\n".format(N, T, log_name, datetime.datetime.now())
    list.append(prt)
    arquivo = open(log_name, "a", encoding="utf-8")
    
    listThreads = []
    listHashes = []
    for i in range(T*N):
        id_str = sha256(str(time.time() + i).encode('utf-8')).hexdigest()
        listHashes.append(id_str)

    timeoutThread = threading.Thread(target=timeout, args=(T,))
    timeoutThread.start()
    inicio = timeit.default_timer()
    while(cont == True):
        for t in range(N):
            thread = threading.Thread(target=funcao, args=(listHashes.pop(0),))
            listThreads.append(thread)
            thread.start()
        time.sleep(1)
    
    
    for j in listThreads:
        j.join()
    
    fim = timeit.default_timer()
    
    
    

    txSucc = 0
    for i in list:
        if (i[1] == 0):
            txSucc += 1

    timeScript = fim - inicio
    temtot = "Tempo total: {}".format(timeScript)
    prtntrans = "Numero total de transferencias: {}".format(len(list) - 1)
    succ = "Transações bem sucedidas: {}".format(txSucc)
    throughput = "Vazão: {}".format(txSucc / timeScript)

    list.append(temtot)
    list.append(prtntrans)
    list.append(succ)
    list.append(throughput)
    for i in list:
        arquivo.writelines("{}\n".format(i))
    