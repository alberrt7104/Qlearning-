import random
import copy
s=1
iteration=0
sumq=0
sumnq=0
count=0
state=[0]
nexts=0
nextq=0
r=0
rm=0
t=0
sumt=0
s6=0
end=0
converge=0
compare=[10,10,10,10]
for num in range (100):
    state.append(1)
maxs=0
flag=0
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
'''up0 down1 left2 right3 '''
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
for num in range(5000):
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
qvalue=[ [0] * 4 for i in range(101) ]


while end==0:
    while s!=56:
        a=random.random()
        if a>0.1:    
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
                if (num==0):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s-10]+0.9*maxs-qvalue[s][num])
                if (num==1):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s+10]+0.9*maxs-qvalue[s][num])
                if (num==2):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s-1]+0.9*maxs-qvalue[s][num])
                if (num==3):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s+1]+0.9*maxs-qvalue[s][num])

            for m in range(4):
                if action[s][m]==1:
                    if count==0:
                        nextq=qvalue[s][m]
                        compare[0]=m
                        count=count+1
                        nexts=m                        
                    else:                        
                        if qvalue[s][m]==nextq:
                            rm=rm+1
                            compare[rm]=m
                            rd=random.randint(0,rm)
                            nextq=qvalue[s][m]
                            nexts=compare[rd]                          
                        if qvalue[s][m]>nextq:
                            nextq=qvalue[s][m]                            
                            rm=0
                            compare[0]=m
                            nexts=m                
            rm=0
            count=0
            if nexts==0:
                s=s-10
            if nexts==1:
                s=s+10
            if nexts==2:
                s=s-1
            if nexts==3:
                s=s+1
            #print(s)
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
                if (num==0):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s-10]+0.9*maxs-qvalue[s][num])
                if (num==1):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s+10]+0.9*maxs-qvalue[s][num])
                if (num==2):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s-1]+0.9*maxs-qvalue[s][num])
                if (num==3):
                    qvalue[s][num]=qvalue[s][num]+0.01*(reward[s+1]+0.9*maxs-qvalue[s][num])

            for b in range(4):
                if action[s][b]==1:
                    compare[rm]=b
                                        
                    rd=random.randint(0,rm)
                    nexts=compare[rd]
                    rm=rm+1
            rm=0
            if nexts==0:
                s=s-10
            if nexts==1:
                s=s+10
            if nexts==2:
                s=s-1
            if nexts==3:
                s=s+1
            #print(s)
    
    ##print(qvalue)
    s=1
    iteration=iteration+1
    if flag==0:
        qvcopy=copy.deepcopy(qvalue)
        flag=1        
    if sumt==1:
        for e in range(1,101):
            for f in range(4):
                if qvcopy[e][f]-qvalue[e][f]<0.0000001:
                    #print(qvcopy[e][f]-qvalue[e][f])
                    
                    #print(len(qvalue))
                    converge=converge+1
                    
       
        qvcopy=copy.deepcopy(qvalue)
        if converge>399:
            end=1
    converge=0            
    sumt=1
print(qvalue)

print(iteration)
            
            
                    
            
            




