# %%
import pandas as pd
import  numpy as np
import json
import os
# %%
l=[]
with open('dblp_v14/dblp_v14.json', 'r') as f:
    count=1000000
    for i in f:
        l.append(i)
        if(count==0):
            break
        count-=1
# %%
flag=l[0:100000]

# %%
flag2=[]

# %%
for i in flag:
    try:
        flag2.append(json.loads(i[0:len(i)-2]))
    except:
        print(i)
# %%
df=pd.DataFrame(flag2)
# %%
print(df.shape)

# %%
df.to_csv('test.csv')



# %%
for j in range(0,1000000,100000):
    flag=l[j:j+100000]
    flag2=[]
    for i in flag:
        try:
            flag2.append(json.loads(i[0:len(i)-2]))
        except:
            print(i)
    df=pd.DataFrame(flag2)
    df.to_csv('d'+str(j)+'.csv')
# %%
l=[]
with open('dblp_v14/dblp_v14.json', 'r') as f:
    start=1000000
    end=2000000
    a=0
    for i in f:
        if(a>=start):
            l.append(i)
        if(a==end):
            break
        a+=1
# %%
len(l)
# %%
l[len(l)-1]
# %%
for lol in range(0,5):
    start=1000000*lol
    end=1000000*(lol+1)
    l=[]
    with open('dblp_v14/dblp_v14.json', 'r') as f:
        a=0
        for i in f:
            if(a>=start):
                l.append(i)
            if(a==end):
                break
            a+=1
    for lo2 in range(0,10):
        s2=100000*lo2
        e2=100000*(lo2+1)
        flag=l[s2:e2]
        flag2=[]
        for i in flag:
            try:
                flag2.append(json.loads(i[0:len(i)-2]))
            except:
                print(i)
        df=pd.DataFrame(flag2)
        df.to_csv('data/'+str(start/1000000)+'d'+str(s2/100000)+'.csv')
# %%
dir='data'
for filename in os.listdir(dir):
    print(filename)
    df=pd.read_csv(dir+'/'+filename)

# %%
df=pd.read_csv('data/0.0d0.0.csv')

# %%
useless_attributes=['lang','volume','v12_id','v12_authors','venue','indexed_abstract']
# %%
column_names = df.columns
print(column_names)

# %%
df.drop(useless_attributes, axis=1, inplace=True)
# %%
df.head()
# %%
import pandas as pd
import  numpy as np
import os
dir='data'
for filename in os.listdir(dir):
    print(filename)
    df1=pd.DataFrame()
    df=pd.read_csv(dir+'/'+filename)
    condition = df['abstract'].apply(lambda x: isinstance(x, float))
    df1 = df[condition].copy()
    df=df[~condition].copy()
    df1.reset_index(drop=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df1.to_csv('split'+'/'+'without/'+filename)
    df.to_csv('split'+'/'+'with/'+filename)
# %%
for filename in os.listdir('data'):
    print(filename)
# %%
