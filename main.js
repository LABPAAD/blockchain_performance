/*
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const { Gateway, Wallets } = require('fabric-network');
const fs = require('fs');
const path = require('path');

let parametersFile = fs.readFileSync('parameters.txt', 'utf8');
let [par1, par2, par3, par4] = parametersFile.split(',');
let data = fs.readFileSync('emrHASH.csv', 'utf8');   
data = data.split('\r\n');

let cont = 0;
let tps = parseInt(par1);
let position = parseInt(par2);
let tx = par3.toString();
let nLoads = parseInt(par4);

let date = new Date();



async function main(name, hash) {
    try {
        // load the network configuration
        const ccpPath = path.resolve(__dirname, '.', 'connection.json');
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join('/vars/profiles/vscode/wallets', 'org3.com.br');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the admin user.
        const identity = await wallet.get('Admin');
        if (! identity) {
            console.log('Admin identity can not be found in the wallet');
            return;
        }

        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'Admin', discovery: { enabled: true, asLocalhost: false } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');
        

        // Get the contract from the network.
        const contract = network.getContract('emr_contract');

        // Submit the specified transaction.

        
        let response;
        try {
            let initTime = Math.floor(Date.now() / 1000);
            const transaction = contract.createTransaction(tx);
            if (tx == "issue"){
                response = await transaction.submit(name, "access info", hash);
            }else if(tx == "read"){
                response = await transaction.evaluate(name, hash);
            }
            
            response = response.toString('hex');
            if(response){
                let endTime =  Math.floor(Date.now() / 1000);
                fs.appendFile('output.csv', initTime + "," + endTime + "," + transaction.getTransactionId() + "," + tx +'\n', function(error){
                    if (error) return console.log(error);
                    console.log('Appended!');
                });
            }
            
        } catch (txError) {
            console.error(txError);
            /* fs.appendFile('output.csv', "-" + "," + "-" + "," + transaction.getTransactionId() +'\n', function(error){
                if (error) return console.log(error);
                console.log('Appended!');
            }); */
        }

        //let issueResponse = await contract.submitTransaction('issue', name, 'access info9', hash);

        //let readResponse = await contract.evaluateTransaction('read', 'pedro', '123');
        
        console.log('Transaction has been submitted');

        // Disconnect from the gateway.
        await gateway.disconnect();

    } catch (txError) {
        /* fs.appendFile('outputErr.txt', "-" + "," + "-" + "," + txError +'\n', function(error){
            if (error) return console.error(error);
            console.log('Appended!');
        }); */
        //const response = await channel.sendTransaction(channel);
        console.error(`Failed to enroll admin user "admin": ${txError}`);
        process.exit(1);
    }
}

/* 
    Tx bem sucedidas
    Tempo de experimento
    Vazão
*/

async function execTx(position){
    for(let i=0; i<tps; i++){
        let [nome, hash] =  data[position].split(",");
        main(nome, hash);
        position++;
    }
}

async function execLoads(){
    for (let i = 0; i < nLoads; i++){
        await execTx(position);
        await sleep(1000);
        position+=tps+1;
    }
}

execLoads();


function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}








