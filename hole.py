def end_odd(radi,sr_no,num):
    a=[]
    if num%2==0:
        nu1,nu2=0,0
    else:
        nu1,nu2=1,1
    middle=int((sr_no[num]+sr_no[num-1])/2)+nu1
    for num1 in range(middle-radi+1,middle+radi-1):
        if num1%2==nu2:
            a.append(num1)
    return a
def serial_no(radi,h,vert,dist_row):
    defect=2*radi-1
    sr_no=[]
    sub=radi+int(vert/2)-radi
    for num1 in range(vert+1):
        if num1 not in dist_row:
            if num1==0:
                sr_no.append(2*h+4)
            else:
                sr_no.append(2*h+2+sr_no[-1])
        elif num1<(vert/2):
            sr_no.append(2*h+2-defect+sr_no[-1])
            defect+=2
        else:
            defect-=2
            sr_no.append(2*h+2-defect+sr_no[-1])
    return sr_no
def data_refine(h,v,r):
    if h%2==1:
        h-=1
    if v%2==1:
        v-=1
    if (h/2)%2==0:
        h+=2
    if (v/2)%2==0:
        v+=2
    if r%2==0:
        r+=1
    if r>=((min(v,h)-4)/2):
        raise ValueError
    else:
        pass
    return h,v,r
print('Every input value has to be in unit of hexagon')
hori=int(input('Enter the horizontal width:'))
vert=int(input('Enter the vertical height:'))
radi=int(input('Enter radius of hole:'))
hori,vert,radi=data_refine(hori,vert,radi)
dist_row=range(int(vert/2)-radi+1,int(vert/2)+radi-1)
sr_no=serial_no(radi,hori,vert,dist_row)
r=[2,3]
l=[sr_no[1],1]
Xco=[0,0]
constant=0.705
constant_2=1.22109
bond=1.41
tem=0
distorted=[0]*(int(vert/2)-radi+1)
Yco=[round((constant+bond),6),round(constant,6)]
def yc(tem,constant,n1,n2):
    a=[]
    if n1%2==n2:
        a.append(round((tem+constant),6))
    else:
        a.append(round(tem,6))
    return a
for num in range(vert+1):
    if num==0:
        for num1 in range(2,sr_no[0]):
            r.append(num1+2)
            l.append(num1)
            Xco.append(round((Xco[-1]+constant_2),6))
            Yco.extend(yc(tem,constant,num1,1))
    elif num not in dist_row:
        Xco.append(Xco[-1])
        Yco.append(round(tem,6))
        for num1 in range(sr_no[num-1]+1,sr_no[num]):
            r.append(num1+1)
            l.append(num1-1)
            if num%2==1:
                Xco.append(round((Xco[-1]-constant_2),6))
            else:
                Xco.append(round((Xco[-1]+constant_2),6))
            Yco.extend(yc(tem,constant,num1,1))
        r.append(sr_no[num]+1)
        l.append(sr_no[num]-1)
    else:
        Xco.append(Xco[-1])
        Yco.append(round(tem,6))
        difference_atom=2*(hori+1)-(sr_no[num]-sr_no[num-1]+1)
        distorted_atom=int((sr_no[num]+sr_no[num-1]+1)/2)
        distorted.append(distorted_atom)
        if num%2==0:
            for nu in range(sr_no[num-1]+1,sr_no[num]):
                if nu!=distorted_atom:
                    Xco.append(round((Xco[-1]+constant_2),6))
                    if nu!=(distorted_atom-1):
                        r.append(nu+1)
                        l.append(nu-1)
                    else:
                        r.append(nu-1)
                        l.append(' ')
                else:
                    Xco.append(round((Xco[-1]+constant_2*(2+difference_atom)),6))
                    r.append(nu+1)
                    l.append(' ')
                if nu<distorted_atom:
                    if nu%2==1:
                        Yco.append(round(tem,6))
                    else:
                        Yco.append(round(tem+constant,6))
                else:
                    if nu%2==0:
                        Yco.append(round(tem,6))
                    else:
                        Yco.append(round(tem+constant,6))
        else:
            for nu in range(sr_no[num-1]+1,sr_no[num]):
                if nu!=distorted_atom:
                    Xco.append(round(Xco[-1]-constant_2,6))
                    if nu!=(distorted_atom+1):
                        r.append(nu+1)
                        l.append(nu-1)
                    else:
                        r.append(nu+1)
                        l.append(' ')
                else:
                    Xco.append(round((Xco[-1]-constant_2*(2+difference_atom)),6))
                    r.append(nu-1)
                    l.append(' ')
                if nu<=distorted_atom:
                    if nu%2==0:
                        Yco.append(round(tem,6))
                    else:
                        Yco.append(round(tem+constant,6))
                else:
                    if nu%2==1:
                        Yco.append(round(tem,6))
                    else:
                        Yco.append(round(tem+constant,6))
        r.append(sr_no[num]+1)
        l.append(sr_no[num]-1)
    tem+=round((bond+constant),6)
myfile=open('./hole.xyz','w')
myfile.write('{}\t \n'.format(sr_no[-1]))
m=[' ',' ',' ']
def m_ext(sr_no,num,num1,nu1,nu2,nu3):
    a=[]
    if num1%2==nu1:
        a.append(2*sr_no[num]-num1+nu2)
    else:
        a.append(2*sr_no[num-1]-num1+nu3)
    return a
for num in range(vert+1):
    if num==0:
        for num1 in range(4,sr_no[0]):
            if num1%2==0:
                m.append(sr_no[0]*2-num1+1)
            else:
                m.append(' ')
        m.append(' ')
    elif num==dist_row[0]-1:
        m.append(' ')
        temp_diff=sr_no[num+1]-2*sr_no[num]+sr_no[num-1]
        if radi%2==1:
            leave=end_odd(radi,sr_no,num)
        else:
            leave=end_even(radi,sr_no,num)
        for num1 in range(2+sr_no[num-1],sr_no[num]):
            if num1%2==1:
                m.append(sr_no[num-1]*2-num1+1)
            else:
                if num1>max(leave):
                    m.append(2*sr_no[num]-num1+1)
                elif num1 in leave:
                    m.append(' ')
                else:
                    m.append(2*sr_no[num]-num1+1+temp_diff)
        m.append(' ')
    elif num==dist_row[-1]+1:
        m.append(' ')
        temp_diff=sr_no[num]-2*sr_no[num-1]+sr_no[num-2]
        leave=end_odd(radi,sr_no,num)
        for num1 in range(2+sr_no[num-1],sr_no[num]):
            if num1%2==0:
                m.append(sr_no[num]*2-num1+1)
            else:
                if num1<min(leave):
                    m.append(2*sr_no[num-1]-num1+1)
                elif num1 in leave:
                    m.append(' ')
                else:
                    m.append(2*sr_no[num-1]-num1+1+temp_diff)
        m.append(' ')
    elif num not in dist_row:
        m.append(' ')
        for num1 in range(2+sr_no[num-1],sr_no[num]):
            m.extend(m_ext(sr_no,num,num1,0,1,1))
        m.append(' ')
        if num==1:
            m[-1]=1
    else:
        m.append(' ')
        down=sr_no[num]-2*sr_no[num-1]+sr_no[num-2]
        up=sr_no[num+1]-2*sr_no[num]+sr_no[num-1]
        for num1 in range(2+sr_no[num-1],sr_no[num]):
            if num%2==0 and num1<distorted[num]:
                if num1%2==1:
                    m.append(2*sr_no[num]-num1+1+up)
                else:
                    m.append(2*sr_no[num-1]-num1+1)
            elif num%2==0 and num1>=distorted[num]:
                if num1%2==0:
                    m.append(2*sr_no[num]-num1+1)
                else:
                    m.append(2*sr_no[num-1]-num1+1+down)
            elif num%2==1 and num1<=distorted[num]:
                if num1%2==1:
                    m.append(2*sr_no[num-1]-num1+1)
                else:
                    m.append(2*sr_no[num]-num1+1+up)
            else:
                if num1%2==1:
                    m.append(2*sr_no[num]-num1+1)
                else:
                    m.append(2*sr_no[num-1]-num1+1+down)
        m.append(' ')
for num in range(sr_no[-1]):
    if m[num]!=' ':
        if m[num]>sr_no[-1]:
            m[num]=' '
    if r[num]>sr_no[-1]:
        r[num],l[num]=l[num],' '
    if l[num]==' ' and m[num]!=' ':
        l[num],m[num]=m[num],''
    if l[num]==' ' and m[num]==' ':
        l[num],m[num]='',''
    if m[num]==' ':
        m[num]=''
for num in range(sr_no[-1]):
    sr=num+1
    myfile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t \n'.format(sr, 'C', Xco[num], Yco[num], 0, 2, r[num], l[num], m[num]))
myfile.close()
