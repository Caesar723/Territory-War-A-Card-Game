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
