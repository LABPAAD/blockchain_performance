## Blockchain Performance
### Avaliação de Desempenho e Custo de Redes Blockchain

Segue uma breve descrição deste repositório que contém os códigos e arquivos csv de experimentos para análise de custo e desempenho de nós em redes Ethereum e Hyperledger Fabric.

Na pasta raiz desse repositório temos o código Python `monitor.py` utilizado para obter as medições de recursos computacionais utilizados pelo nó.

Na pasta `gráficos` temos o notebook `sinais.ipynb` utilizado para gerar os gráficos das medições das redes. Além disso, temos pastas correspondentes a cada configuração de do tipo de nó avaliado para as redes: `small`, `medium` e `xlarge`. Cada pasta contém o respectivo arquivo de log da ferramenta Caliper e arquivos csv com os resultados das medições de desempenho.

Finalmente, na pasta `Hosts docker` encontram-se os arquivos de configuração de imagens docker para hosts na rede Hyperledger Fabric.
