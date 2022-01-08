from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import random
llist=[]
BigList=[]
ready=[]
losepeople=[]
locat=['rest','wushu','wuqi']
peoplelist=[]
class people:
    live=5
    hitv=1
    feature='sleep'
    hand='p'
    location=''
    name=''
    def __init__(self,num):
        self.location='home'+str(num)
        self.name='people'+str(num)

def check(arr):
    arr2=[]
    c=checkhand(arr)
    if ('p' in arr and 's' in arr and 'r' in arr )or(c):
        return False
    else:
        if ('r' in arr and 'p' in arr):
            getwin='p'
        elif ('s' in arr and 'p' in arr):
            getwin='s'
        else:
            getwin='r'
        return getindex(arr,getwin)

def gethand(arr):
    arr2=[]
    for i in arr:
        arr2.append(i.hand)
        #print(i.hand)
    return arr2
def checkhand(arr):
    c='p'
    count=0
    for i in arr:
        if i==c:
            count+=1
        else:
            c=i
            count=1
    if count==len(arr):
        return True
    else:
        return False
def sendToAll(str):
    for i in llist:
        i.send(str)
def getindex(arr,thing):
    arr2=[]
    for i in range(len(arr)):
        if arr[i]==thing:
            arr2.append(i)
    return arr2
#coun=0
def sendPeople():
    text='P'
    for ii in peoplelist:
        text+=ii.name+"-生命"+str(ii.live)+"-伤害"+str(ii.hitv)+"-"+ii.feature+" "
    for i in llist:
        i.send(text)

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self,message):
        global coun
        self.accept()
        llist.append(self)
        peoplelist.append(people(random.randint(0,100),))
        ready.append(False)
        for i in llist:
            text=''
            for ii in llist:
                #if ii!=i:
                text+=peoplelist[llist.index(ii)].name+'-'+peoplelist[llist.index(ii)].location+((' ') if llist.index(ii)!=len(llist)-1 else '')

        #coun+=1
            i.send("A"+text)#peoplelist[llist.index(self)].name+'-'+peoplelist[llist.index(self)].location)
            i.send("C" + text)
        self.send(peoplelist[llist.index(self)].name)
        sendPeople()
    def websocket_receive(self,message):
        #print(ready)
        if (message['text'][0]=='R'):
            get=message['text'][1:]
            if get[0]=='p':
                get=int(get[1:])-1
                get='home'+(peoplelist[get].name)[6:]
            peoplelist[llist.index(self)].location=get
        elif(message['text']=='S'):
            if peoplelist[llist.index(self)].location=='zx':
                peoplelist[llist.index(self)].live+=2
            elif peoplelist[llist.index(self)].location=='jg':
                peoplelist[llist.index(self)].hitv+=2
            elif peoplelist[llist.index(self)].location=='xb':
                for i in llist:
                    if i!=self:
                        peoplelist[llist.index(self)].feature='sleep'
        elif (message['text'][0]=='H'):
            get = message['text'][1:]
            for i in peoplelist:
                if i.name==get:
                    i.live-=peoplelist[llist.index(self)].hitv
        else:
            ready[llist.index(self)]=True
            peoplelist[llist.index(self)].hand=message['text']
            print(ready)
            #print(ready)
            if not(False in ready):
                winlist=check(gethand(peoplelist))
                print(winlist)
                text=''
                for ii in range(len(ready)):
                    ready[ii]=False
                if winlist!=False:
                    for iii in winlist:
                        #text+=str(peoplelist[iii].name)+'  '
                    #for i in llist:
                        if peoplelist[iii].feature=='sleep':
                            peoplelist[iii].feature ='up'
                            for iiii in llist:
                                iiii.send(peoplelist[iii].name+" awake")
                        else:
                            llist[iii].send('W')
                else:
                    for i in llist:

                        i.send('equil')

        for iiiii in llist:
            text=''
            for ii in llist:
                if ii!=iiiii:
                    text+=' '+peoplelist[llist.index(ii)].name+'-'+peoplelist[llist.index(ii)].location


            #print(peoplelist[llist.index(iiiii)])
            iiiii.send("C"+peoplelist[llist.index(iiiii)].name+'-'+peoplelist[llist.index(iiiii)].location+text)
        sendPeople()
    def websocket_disconnect(self,message):
        #print('dc')

        ready.pop(llist.index(self))
        #print(ready,'dc')
        peoplelist.pop(llist.index(self))
        llist.remove(self)
        for i in llist:
            text=''
            for ii in llist:
                #if ii!=i:
                peoplelist[llist.index(ii)].location='home'+(peoplelist[llist.index(ii)].name)[6:]
                text+=peoplelist[llist.index(ii)].name+'-'+peoplelist[llist.index(ii)].location+((' ') if llist.index(ii)!=len(llist)-1 else '')
            #i.send(peoplelist[llist.index(i)].name+'-'+peoplelist[llist.index(i)].location+text)
        #coun+=1
            i.send("A"+text)
        sendPeople()
        raise StopConsumer()