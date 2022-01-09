# Territory War
## How to use it
use pip3 to install django and channels：
</br>
`pip3 install Django`
</br>
`pip3 install channels`

go to CardGame/first/consumers.py and go to Line 36
</br>
`change the path which contain “first” folder`
![example](http://tiebapic.baidu.com/forum/pic/item/f4aab864034f78f0fcd5c2ea24310a55b2191c97.jpg)

To create database , first , install mysql.connector
</br>
`pip3 install mysql-connector-python`
</br>
  go to CardGame/first/Database.py use function
  </br>
  *createDatabase()*
  </br>
  *createPasswordTable()*
  </br>
  *creatCardTable()*
  </br>
  
change the path which contain manage.py file
</br>
`python3.9 manage.py runserver`
</br>
</br>
</br>
</br>
</br>
## Game's content
![example](http://tiebapic.baidu.com/forum/pic/item/9d1fc209b3de9c82e973c55e2981800a18d84397.jpg)
</br>

When you in this game , you must register a account number , click '注册'.
</br>
![example](http://tiebapic.baidu.com/forum/pic/item/a959bbd3fd1f413450705f67781f95cad1c85e2f.jpg)
</br>

And then you can access this game.
</br>
![example](http://tiebapic.baidu.com/forum/pic/item/7f8828c79f3df8dc047ad5889011728b4710282f.jpg)

In this game you can click '新建套牌' to create a deck.
</br>
![example](http://tiebapic.baidu.com/forum/pic/item/0c086bf0f736afc3f01a03b4f619ebc4b6451297.jpg)

After creating a deck, you can click '匹配' to match a opponent, waiting for the opponent.
</br>
![example](http://tiebapic.baidu.com/forum/pic/item/a423104f78f0f736a5b816185755b319ebc4132f.jpg)
</br>
</br>
</br>
</br>
</br>
## How to diy a card
go to /CardGame/first/father.py 
</br>
you will see the **superclass**  of the card called **card**
</br>
It have and function, **Rcost()** is to output the the final cost
</br>
such as **['g','g','g','g','g']**
</br>
It means this card have **5 green** 
</br>
![example](http://tiebapic.baidu.com/forum/pic/item/8a72f6dde71190ef6d87ae0e8b1b9d16fcfa60ad.jpg)
</br>
This is the cost bar **5 green** means your cost bar must have a number greater than 5 in the last row
</br>
</br>
</br>
There are three subclass **servent** **magic** **ground** , ignore the shelter
</br>
you can see there are lots of function in **servent**
</br>
![example](http://tiebapic.baidu.com/forum/pic/item/f871bcc379310a553857e225f24543a9832610b2.jpg)
</br>
you can over override:
</br>
**ZhanHong(self,MyMaster,Master,selectIndex=None):# when use servent the function is used** 
</br>**WangYu(self,MyMaster,Master): # when servent is die function is uesd**
</br>**WhenBeAttack(self,MyMaster,Master,otherServent):# when serveny be attack use this function** 
</br>**whenSendData(self,MyMaster,Master):#used to make Aura**
</br>**whenTermFinish(self,MyMaster,Master):# when round finish use this function**
</br>
The class called **Master** is protagonist


</br>
Now start to make a card, go to /CardGame/first/cardServent.py


