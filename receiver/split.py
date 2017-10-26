rfc3399 = '2017-10-24T23:41:29.524Z'
date = rfc3399.split('T')

year = date[0].split('-')[0]
month = date[0].split('-')[1]
day = date[0].split('-')[2]

hour = date[1].split(':')[0]
minute = date[1].split(':')[1]
second = date[1].split(':')[2].split('.')[0]

new = year + "/" + month + "/" + day + " " + date[1].split(".")[0]
print (new)
