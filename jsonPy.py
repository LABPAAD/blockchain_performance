import pandas as pd
import sys

if __name__ == '__main__':
        arq = sys.argv
        df = pd.read_json(arq[1])
            
        lisTimeSt = []
        lisDdHash = []
        lisNumBloc = []
        lisPeerEnd = []
        lisStats = []
        ordener = ''

        for i in df.data.data:
            lisTimeSt.append(i['payload']['header']['channel_header']['timestamp'])
            lisNumBloc.append(i['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload']['extension']['results']['ns_rwset'][0]['rwset']['reads'][0]['version']['block_num'])
            lisDdHash.append(i['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload']['extension']['results']['ns_rwset'][1]['rwset']['writes'][0]['value'])  
            lisPeerEnd.append(i['payload']['data']['actions'][0]['payload']['action']['endorsements'][0]['endorser'])
            lisStats.append(i['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload']['extension']['response']['status'])

        ordener = df.metadata.metadata[0]

        for i in range(len(lisTimeSt)):
            print('{} {} {} {} {} {} {}'.format(i,lisTimeSt[i],lisDdHash[i],lisNumBloc[i],lisPeerEnd[i],ordener,lisStats[i]))
            