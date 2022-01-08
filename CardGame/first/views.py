from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import mysql.connector
import re
import csv
import first.consumers as concumer
type=0
if type==0:
    import first.father as father
    import first.Database as database
    import first.cardServent as S
    import first.cardMagic as M
    import first.cardGround as G
    import first.cardShelter as J
pw='20040723caesar'
conect = mysql.connector.connect(user='root', password=pw, host='localhost', database='CardGame',auth_plugin='mysql_native_password')
hom='<a href=http://127.0.0.1:8000/ >返回登陆</a>'
def getalluser(conect):
    con = conect.cursor()
    con.execute('SELECT Name FROM PlayerPassword ')
    get = list(set(con.fetchall()))
    arr=[]
    for i in get:
        arr.append(i[0])
    return list(arr)
def home(request,name,cardsName):
    #conect = mysql.connector.connect(user='root', password=pw, host='localhost', database='CardGame',auth_plugin='mysql_native_password')

    return render(request,'homeP.html',{'nam':name,'CardsName':database.getCardListByNameADCN(name,cardsName)[0]})
def load(request):
    conect = mysql.connector.connect(user='root', password=pw, host='localhost', database='CardGame',auth_plugin='mysql_native_password')

    lo="AS3-Caesar<br><td><font size=8><center>Territory War</center></td></font>"
    tit="<td><font size=6><center>输入账号密码</center></td>"
    fail="<td><font size=6><center>输入账号密码(fail)</center></td>"
    body="<td><form name='input' action='' method='post'><center>账号：<input name='name' size=30 ></center></td>" \
       "<td><center>密码：<input type='password' name='secret' size=30 ></center></td>" \
       "<td><center><input type='submit' value='提交' name='create' style='width:200px; height:50px;background-color:#FFFFFF'></form><form name='in' action='' method='post'><input type='submit' value='注册' name='create' style='width:200px; height:50px;background-color:#FFFFFF'></form></center></font></td>"

    if request.method=='GET':

        return HttpResponse(lo+tit+body)
    if request.method=='POST':
        print(request.POST)
        try:
            if request.POST['cla']!='':
                print(request.POST)
                return home(request,request.POST['cla'])
        except :
            pass
        if request.POST['create']=='注册':
            return HttpResponseRedirect('register/')
        if request.POST['create']=='提交':
            con = conect.cursor()
            con.execute('SELECT Name FROM PlayerPassword WHERE Name="%s" AND Password="%s"' %(str(request.POST['name']),str(request.POST['secret'])))
            try:
                get=[con.fetchone()[0],request.POST['secret']]
                print(get)
                #print('ok')
                if get!=None:
                    #print('ok')
                    try:
                        if request.POST['match']=='匹配':
                            return hall(request,get[0],get[1])
                        elif request.POST['match']=='新建套牌':
                            return creatCard(request,get[0],get[1])
                        elif request.POST['match']=='返回':
                            request.method='GET'
                            return hall(request,get[0],get[1])
                        elif request.POST['match']=='确认创建':
                            database.addCard(request.POST['name'],request.POST['coverName'],concumer.encodeCard(request.POST['cards']))
                            request.method='GET'
                            return hall(request,get[0],get[1])
                        elif request.POST['match']=='删除套牌':
                            database.deleteCardList(get[0],request.POST['cln'])
                            request.method='GET'
                            return hall(request,get[0],get[1])
                        elif request.POST['match']=='更改套牌':
                            return creatCard(request,get[0],get[1],concumer.decode(database.getCardListByNameADCN(get[0],request.POST['cln'])[0]))
                    except Exception as re:
                        request.method='GET'
                        print(re)
                        return hall(request,get[0],get[1])
                    #return  redirect(primary,Pass="pass",data=get[0])
                else:
                    return HttpResponse(lo+fail+body)
            except Exception as e:
                print(str(e))
                return HttpResponse(lo+fail+body)

def reg(request):
    conect = mysql.connector.connect(user='root', password=pw, host='localhost', database='CardGame',auth_plugin='mysql_native_password')

    tit="<td><font size=6><center>注册</center></td>"
    fail="<td><font size=6><center>注册失败</center></td>"
    success="<td><font size=6><center>注册(Success)</center></td>"
    lo = "<td><form name='input' action='' method='post'><center>账号：<input name='name' size=30 ></center></td>" \
         "<td><center>密码：<input type='password' name='secret' size=30 ></center></td>" \
         "<td><center>密码确认：<input type='password' name='Dsecret' size=30 ></center></td>" \

    send="<center><input type='submit' value='提交' name='create' style='width:200px; height:50px;background-color:#FFFFFF'></form></center></font></td>"
    lo+="<center>"

    lo+="</center>"+send
    if request.method == 'GET':
        return HttpResponse(hom+tit+lo)
    if request.method == 'POST':
        print(request.POST)
        alluser=getalluser(conect)
        print(alluser)
        alluser=[] if alluser==None else alluser
        print(request.POST['secret']!='' and request.POST['secret']==request.POST['Dsecret'] and not(request.POST['name'] in alluser))
        if request.POST['secret']!='' and request.POST['secret']==request.POST['Dsecret'] and not(request.POST['name'] in alluser):

            #try:
                #addUser(request.POST['name'],request.POST['secret'],request.POST['choose'],conect)
            concumer.addPlayerOnce(request.POST['name'],request.POST['secret'])
            return HttpResponse(hom+success+lo)
            #except:

        #if request.POST[]
                #return HttpResponse(hom+fail+lo)
        else:
            return HttpResponse(hom+fail+lo)
def hall(request,name,sec):
    
    conect = mysql.connector.connect(user='root', password=pw, host='localhost', database='CardGame',auth_plugin='mysql_native_password')
    conect.commit()
    getlistCard=database.getCardListByName(name)
    CardListName=[i[1] for i in getlistCard]#[newcomerCard]
    CardList=[[ii.name for ii in i] for i in ([concumer.getCardList(iii[0]) for iii in getlistCard])]#一个卡套的卡牌的名字
    if request.method=='POST':
        if request.POST['match']=='匹配':
            return home(request,name,request.POST['cln'])
    else:
        return render(request,'hall.html',{'nam':name,'CDN':CardListName,'CD':CardList,'secrete':sec,'score':database.GetScore(name)})
def creatCard(request,name,sec,decode=''):
    inde=['S','M','G']
    getNC=re.compile(r"\.\w+'")
    AllCards=[father.servent.__subclasses__(),father.magic.__subclasses__(),father.ground.__subclasses__()]
    narrateCard=''
    for category in AllCards:
        firs=''
        for i in range(len(category)):
            object=eval(inde[AllCards.index(category)]+"."+(getNC.findall(str(category[i]))[0].replace(".","").replace("'",""))+'()')
            text=''
            for tex in range(len(object.cost)):
                text+=str(object.cost[tex])+('-' if tex!=len(object.cost)-1 else '')
            
            firs+=object.typeCard+'_'+object.name+'_'+object.narrate+'_'+((str(object.power)+'_'+str(object.live)) if object.typeCard=='servent' else'_')+'_'+text+'_'+str(object.allCost)+'/'
        narrateCard+=firs+'|'
    return render(request,'createCover.html',{'nam':name,'secrete':sec,'allCards':narrateCard,'haveHad':decode})