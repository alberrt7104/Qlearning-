import random
s=1
count=0
state=[0]
nexts=0
nextq=0
r=0
rm=0
rd=0
t=0
compare=[1,1,1,1]

for num in range (100):
    state.append(1)
maxs=0
state[22]=0
state[23]=0
state[24]=0
state[27]=0
state[28]=0
state[29]=0
for num in range (25,85,10):
    state[num]=0

'''for num in range (100):
    print(num,":",state[num])'''
action=[ [1] * 4 for i in range(101) ]
##up0 down1 left2 right3 
for num in range (1,11):
    action[num][0]=0
for num in range (1,100,10):
    action[num][2]=0
for num in range (91,101):
    action[num][1]=0
for num in range (10,101,10):
    action[num][3]=0
for num in range (12,16):
    action[num][1]=0
for num in range (17,20):
    action[num][1]=0
action[26][2]=0
action[26][3]=0
for num in range (32,36):
    action[num][0]=0
for num in range (37,40):
    action[num][0]=0
for num in range (34,84,10):
    action[num][3]=0
action[85][0]=0
for num in range (36,86,10):
    action[num][2]=0
for num in range (37,40):
    action[num][0]=0
action[30][2]=0
reward=[0]
for num in range(100):
    reward.append(0)
reward[34]=-1
reward[46]=-1
reward[47]=-1
reward[56]=1
reward[57]=-1
reward[59]=-1
reward[69]=-1
reward[74]=-1
reward[76]=-1
reward[77]=-1
qvalue=[ [0] * 4 for i in range(1) ]


for g in range(1):
    while s!=56:
        a=random.random()
        if a>0.3:    
            for num in range(4):
                if action[s][num]==1:
                    if num==0:
                        for i in range(4):
                            if action[s-10][i]==1:
                                temp=qvalue[s-10][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp                        
                            count=0
                    if num==1:
                        for i in range(4):
                            if action[s+10][i]==1:
                                temp=qvalue[s+10][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp
                            count=0
                    if num==2:
                        for i in range(4):
                            if action[s-1][i]==1:
                                temp=qvalue[s-1][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp
                            count=0
                    if num==3:
                        for i in range(4):
                            if action[s+1][i]==1:
                                temp=qvalue[s+1][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp
                            count=0                
                qvalue[s][num]=qvalue[s][num]+0.01*(reward[s]+0.9*maxs-qvalue[s][num])
            for m in range(4):
                if action[s][m]==1:
                    if count==0:
                        nextq=qvalue[s][m]
                        nexts=m
                        count=count+1
                    else:                        
                        if qvalue[s][m]==nextq:
                            rm=rm+1
                            compare[rm]=m
                            rd=random.randint(0,rm)
                            nextq=qvalue[s][m]
                            nexts=compare[rd]
                        if qvalue[s][m]>nextq:
                            nextq=qvalue[s][m]
                            nexts=m
                            compare[0]=m
            count=0
            rm=0
            if nexts==0:
                s=s-10
            if nexts==1:
                s=s+10
            if nexts==2:
                s=s-1
            if nexts==3:
                s=s+1
            print(s)
            for f in range(4):
                print(qvalue[s][f])
        else:
            for num in range(4):
                if action[s][num]==1:
                    if num==0:
                        for i in range(4):
                            if action[s-10][i]==1:
                                temp=qvalue[s-10][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp
                            count=0
                    if num==1:
                        for i in range(4):
                            if action[s+10][i]==1:
                                temp=qvalue[s+10][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp                       
                            count=0
                    if num==2:
                        for i in range(4):
                            if action[s-1][i]==1:
                                temp=qvalue[s-1][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp
                            count=0
                    if num==3:
                        for i in range(4):
                            if action[s+1][i]==1:
                                temp=qvalue[s+1][i]
                                if count==0:
                                    maxs=temp
                                    count=1
                                if maxs<temp:
                                    maxs=temp
                            count=0                
                qvalue[s][num]=qvalue[s][num]+0.01*(reward[s]+0.9*maxs-qvalue[s][num])
            for b in range(4):
                if action[s][b]==1:
                    compare[rm]=b
                    rm=rm+1
                    compare[rm]=m
                    rd=random.randint(0,rm)
                    nexts=compare[rd]
            rm=0
            if nexts==0:
                s=s-10
            if nexts==1:
                s=s+10
            if nexts==2:
                s=s-1
            if nexts==3:
                s=s+1
            print(s)
            print(qvalue[s][num])
    ##print(qvalue)
    s=1
print(qvalue)
    
            
            
                    
            
            




