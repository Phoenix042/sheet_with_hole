file_o=str(int(input('Enter the file name of *.xyz_2:')))
myfile=open(file_o+'.xyz_2','r')
file=[]
x1=[]
y1=[]
z1=[]
for num1 in myfile:
    temp=list(num1)
    num2=5
    a=[]
    b=[]
    c=[]
    if len(temp)>10:
        while temp[num2]!='C':
            num2+=1
        num2+=1
        while temp[num2]==' ':
            num2+=1
        while temp[num2]!=' ':
            a.append(temp[num2])
            num2+=1
        while temp[num2]==' ':
            num2+=1
        while temp[num2]!=' ':
            b.append(temp[num2])
            num2+=1
        while temp[num2]==' ':
            num2+=1
        while temp[num2]!=' ':
            c.append(temp[num2])
            num2+=1
        x1.append(abs(float(''.join(a))))
        y1.append(abs(float(''.join(b))))
        z1.append(abs(float(''.join(c))))
file_1=str(int(input('Enter the file name of *.xyz_2:')))
myfile=open(file_1+'.xyz_2','r')
file=[]
x2=[]
y2=[]
z2=[]
for num1 in myfile:
    temp=list(num1)
    num2=5
    a=[]
    b=[]
    c=[]
    if len(temp)>10:
        while temp[num2]!='C':
            num2+=1
        num2+=1
        while temp[num2]==' ':
            num2+=1
        while temp[num2]!=' ':
            a.append(temp[num2])
            num2+=1
        while temp[num2]==' ':
            num2+=1
        while temp[num2]!=' ':
            b.append(temp[num2])
            num2+=1
        while temp[num2]==' ':
            num2+=1
        while temp[num2]!=' ':
            c.append(temp[num2])
            num2+=1
        x2.append(abs(float(''.join(a))))
        y2.append(abs(float(''.join(b))))
        z2.append(abs(float(''.join(c))))
X=[]
Y=[]
Z=[]
for num in range(min(len(x1),len(x2))):
    dx=x2[num]-x1[num]
    dy=y2[num]-y1[num]
    dz=z2[num]-z1[num]
    X.append(round(dx,6))
    Y.append(round(dy,6))
    Z.append(round(dz,6))
my1=open('x.txt','w')
my2=open('y.txt','w')
my3=open('z.txt','w')
for num in range(len(X)):
    my1.write('{}\t \n'.format(X[num]))
    my2.write('{}\t \n'.format(Y[num]))
    my3.write('{}\t \n'.format(Z[num]))
my1.close()
my2.close()
my3.close()
