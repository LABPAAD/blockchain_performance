import sys
import threading
import time
import subprocess
import timeit
from hashlib import sha256


N = 5
T = 10
#cmd = 'docker exec cli peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emr_contract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"Args":["issue","Pedro","accessinfo","123"]}'

def funcao():
    for i in range(N):
        id_str = sha256(str(time.time()).encode('utf-8')).hexdigest()
        cmd = "sleep 2"
        inicio = timeit.default_timer()
        return_code = subprocess.call(cmd, shell=True)
        fim = timeit.default_timer()
        print(id_str, return_code, fim - inicio)
        


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
    print("experiment:",N, T, log_name)

    for i in range(T):
        threading.Thread(target=funcao).start()
        time.sleep(1)

