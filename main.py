import csv
from selenium import webdriver

driver = webdriver.Firefox()
last_page = 8
#la url tiene que ser de esta forma de aqui abajo
link= 'https://www.forocoches.com/foro/showthread.php?t=8391188&page='
array=[]
file = open('users.txt','w')
for i in range (1,last_page+1): 
    driver.get(link+str(i)+'')
    user = driver.find_elements_by_class_name('bigusername')
    for i in range(0,len(user)):
        array.append(user[i].text)
array = list(dict.fromkeys(array))
# excluyendo el primer elemento del array para que no automencionarte
for i in range(1,len(array)):
    file.write('@'+str(array[i])+', ')