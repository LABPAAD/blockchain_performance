import sys
import threading
import time
import subprocess
import timeit
from hashlib import sha256
import datetime
import concurrent.futures


list = []

def insertionTx(id_str, cmd):
    
    inicioTx = timeit.default_timer()
    return_code = subprocess.call(cmd,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    
    fimTx = timeit.default_timer()
    temp = fimTx-inicioTx
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

    listHashes = []
    for i in range(T*N):
        id_str = sha256(str(time.time() + i).encode('utf-8')).hexdigest()
        listHashes.append(id_str)

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=200)
    timeIntern = []
    inicioScript = timeit.default_timer()
    for i in range(T):
        initThread = timeit.default_timer()
        for t in range(N):
            hash = listHashes.pop(0)
            cmd2 = '{"Args":["issue","Pedro","accessinfo","' + hash + '"]}'
            cmd = "docker exec cli peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emrcontract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{}'".format(cmd2)
            pool.submit(insertionTx,hash, cmd)
        endThread = timeit.default_timer()
        timeIntern.append( (initThread, endThread) )
        time.sleep(1)
        
    pool.shutdown(wait=True)
    
    fimScript = timeit.default_timer()

    txSucc = 0
    for i in list:
        if (i[1] == 0):
            txSucc += 1

    timeScript = fimScript - inicioScript
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

    for i in range(T):
        print(timeIntern[i])
    
    print(len(timeIntern))