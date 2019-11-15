import pygal
piechart=pygal.Pie()
barchart=pygal.Bar()
str=' '
value=0
flag=0
num_lines=0
count=0
file=open('pets.txt','r')
with open('pets.txt', 'r') as f:
    for i in f:
        num_lines += 1
num_lines-=1
for line in file.read().splitlines():
  if line:
    str,value=line.split(' ')
    if str=='barchart':
      flag=1
      continue
    if flag==1:
      count+=1
      barchart.add(str,int(value))
      if num_lines-1==count:
        barchart.render()
    elif flag==0:
      count+=1
      piechart.add(str,int(value))
      if num_lines-1==count:
        piechart.render()
file.close()
