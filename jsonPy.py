import pandas as pd
import sys

if __name__ == '__main__':
        entr = sys.argv
        df = pd.read_json(entr[1])
        arquivo = open(entr[2], "a", encoding="utf-8")
        lisTimeSt = []
        lisDdHash = []
        #lisNumBloc = []
        peerEnd = []
        lisPeerEnd = []
        lisStats = []
        ordener = ''
        numBloc = ''

        for i in df.data.data:
            lisTimeSt.append(i['payload']['header']['channel_header']['timestamp'])
            #lisNumBloc.append(i['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload']['extension']['results']['ns_rwset'][0]['rwset']['reads'][0]['version']['block_num'])
            lisDdHash.append(i['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload']['extension']['results']['ns_rwset'][1]['rwset']['writes'][0]['value'])  
            peerEnd = []
            for j in i['payload']['data']['actions'][0]['payload']['action']['endorsements']:
                peerEnd.append(j['endorser'])
            lisPeerEnd.append(peerEnd)
            lisStats.append(i['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload']['extension']['response']['status'])

        ordener = df.metadata.metadata[0]
        numBloc = df.header.number
        for i in range(len(lisTimeSt)):
            arquivo.writelines('{} {} {} {} {} {}\n'.format(lisTimeSt[i],lisDdHash[i],numBloc,lisPeerEnd[i],ordener,lisStats[i]))
            #print('{} {} {} {} {} {}\n'.format(lisTimeSt[i],lisDdHash[i],numBloc,lisPeerEnd[i],ordener,lisStats[i]))