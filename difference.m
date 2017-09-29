clear all;
clf;
zz=[1:6991];
load x.txt
load y.txt
load z.txt
plot(zz,x,'r',zz,y,'b')
hold on
plot(zz,z,'g')
title('Difference in position coordinates','Color','r','FontSize',24)
xlabel('Atom number','FontSize',18,'Color','b')
ylabel('x,y,z','FontSize',18,'Color','b')
hold on
legend('Diff(x)','Diff(y)','Diff(z)')