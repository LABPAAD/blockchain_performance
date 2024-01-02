# PBFT-APM

Este repositório contém o software **PBFT-APM**, que é uma ferramenta para interagir com uma blockchain. Antes de começar, certifique-se de seguir as instruções abaixo para configurar corretamente o ambiente.

## Pré-requisitos

Para utilizar o **PBFT-APM**, é necessário ter o Node.js e o TypeScript instalados em seu ambiente.

### Instalando o Node.js com NVM (Node Version Manager)

O NVM é uma maneira conveniente de gerenciar as versões do Node.js. Siga os passos abaixo para instalá-lo:

1. Instale o wget, se ainda não estiver instalado:
   
   sudo apt install wget

2. Baixe e execute o script de instalação do NVM:

    wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

3. Carregue o NVM em seu perfil de usuário:

    source ~/.profile

4. Liste as versões do Node.js disponíveis para instalação:

    nvm ls-remote
5. Escolha a versão desejada (recomendamos a versão 18.17.1) e instale:

    nvm install 18.17.1

6. Verifique se a instalação foi bem-sucedida:

    node -v

### Instalando o TypeScript
Para instalar o TypeScript globalmente, execute o seguinte comando:

    npm install -g typescript

### Instalando e usando o PBFT-APM
Siga as etapas abaixo para clonar o repositório e configurar o PBFT-APM:

1. Clone este repositório dentro da pasta fabric-samples/test-network:

    git clone https://github.com/LABPAAD/blockchain_performance.git

2. Navegue até a pasta do projeto:

    cd PBFT-APM

3. Instale as dependências do projeto:

    npm install

4. Execute o processo de build:

    npm run build

Agora você está pronto para utilizar o PBFT-APM. Execute o seguinte comando para iniciar a ferramenta com argumentos específicos:

Para povoar a blockchain com assets pré-definidos:

    npm start initLedger

Para criar novos assets:

    npm start createAsset [n]

Para criar novos assets com operações de Endorse/Submit/CommitStatus:

    npm start createAssetEndorse [n]

Para visualizar todos os assets:

    npm start getAll

Para visualizar um asset pelo seu ID:

    npm start getByKey [id]

Para transferir a propriedade de um asset:

    npm start transferAsset [id] [newOwner]

Para atualizar um asset existente:

    npm start updateAsset [id]

# Lembre-se de substituir `[n]`, `[id]` e `[newOwner]` pelos valores apropriados.

## Executando com Python

Além do método padrão em Node.js, você também pode executar o cliente utilizando um script Python. O arquivo runBenchAle.py foi criado para essa finalidade. Certifique-se de ter as bibliotecas necessárias instaladas e ajuste os parâmetros conforme necessário antes de executar o script.

    python runBenchAle.py

Este script realiza uma série de transações no cliente PBFT-APM utilizando tempos aleatórios previamente gerados.

### Modificações no Script Python
1. Arquivo CSV de Tempos:

Substitua o nome do arquivo CSV (tempos_aleatorios_wei_dropbox.csv) pelo nome do arquivo contendo os tempos que você deseja utilizar.

2. Arquivo de Saída:

Modifique o nome do arquivo de saída (testeAleWei1kdb.csv) conforme necessário.

3. Comando Node.js:

A linha subprocess.Popen(["sudo", "node", "dist/client.js", "createAssetEndorse", "1", "B"], ... executa o cliente PBFT-APM com argumentos específicos. Certifique-se de que o caminho para o arquivo client.js está correto e ajuste os argumentos conforme necessário. Por exemplo, se você deseja criar novos ativos em vez de createAssetEndorse, altere para createAsset.
4. Tempo de Espera:

O script aguarda um tempo especificado entre as iterações, conforme definido por time.sleep(tempo). Certifique-se de que a unidade de tempo (segundos, milissegundos, etc.) esteja correta.

## Executando o Script Python
Após fazer as modificações necessárias, você pode executar o script no terminal:
    python runBenchAle.py

O script realizará uma série de transações no cliente PBFT-APM, usando os tempos aleatórios do arquivo CSV fornecido. Os resultados e gráficos associados serão gerados no arquivo de saída especificado.

Lembre-se de ajustar os parâmetros conforme necessário para atender às suas necessidades de teste.
Aproveite o uso do **PBFT-APM**! Se tiver alguma dúvida ou problema, não hesite em entrar em contato.


