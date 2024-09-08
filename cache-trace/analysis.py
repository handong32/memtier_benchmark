import pandas as pd
import numpy as np
import threading

def tf(name, ndf, tsm):
    max_uniq_key = 0
    max_client_id = 0
    dfac = int(tsm/64)
    
    print(f"{name}: {dfac*name} {dfac}")
    for i in range(int(dfac*name), int(dfac*name)+dfac):
        max_uniq_key = max(max_uniq_key, len(ndf[ndf.timestamp == i]['key'].unique().tolist()))
        max_client_id = max(max_client_id, len(ndf[ndf.timestamp == i]['client_id'].unique().tolist()))
        if (i % 50) == 0:
            print(f"{i}: max_uniq_key={max_uniq_key}, max_client_id={max_client_id}")

df = pd.read_csv('/mydata/hand32/data/twitter/cluster10.sort', sep=',', 
        names=['timestamp', 'key', 'key_size', 'value_size', 'client_id', 'op', 'ttl'])
print("read_csv done")
    
print(df['timestamp'].max())
ncpus=64
threads = list()
for index in range(ncpus):
    x = threading.Thread(target=tf, args=(index,df,df['timestamp'].max()))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()
print("DONE")
