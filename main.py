import csv
from selenium import webdriver

driver = webdriver.Firefox()
last_page = 11
#la url tiene que ser de esta forma de aqui abajo
link= 'https://www.forocoches.com/foro/showthread.php?t=8391188&page='
array_usr=[]
array_url=[]
file = open('users.txt','w')
for i in range (1,last_page+1): 
    driver.get(link+str(i)+'')
    user = driver.find_elements_by_class_name('bigusername')
    for i in range(0,len(user)):
        array_url.append(user[i].get_attribute('href'))
        array_usr.append(user[i].text)
array_usr = list(dict.fromkeys(array_usr))
# excluyendo el primer elemento del array para que no automencionarte
for i in range(1,len(array_usr)):
    file.write('@[URL="'+array_url[i]+'"]'+array_usr[i]+'[/URL], ')