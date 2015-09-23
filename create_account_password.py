#C:\Users\Administrator\Desktop
#-*- coding:utf-8 -*- 

import string
import random
import time



start = time.clock() 
a = string.letters +string.digits
c = string.letters


for i in range(10000):#数字10000是生成多少个
    mycount = ''
    mypassword = ''
    
    for j in range(8):#数字8 是账号密码的长度
        b = a[random.randint(0,61)]
        mycount += b
        e = a[random.randint(0,61)]
        mypassword += e
    if mycount[0] in string.digits:
        mycount = c[random.randint(0,51)] + mycount[0:]
    #print '%s\t%s' % (mycount , mypassword)
    fileHandle = open ('account.ini' , 'a')
    fileHandle.write('%s\t%s\n' % (mycount , mypassword))

end = time.clock()
fileHandle.close() 
print end - start


 
 
