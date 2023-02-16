clear all;
close all;
clc;

h = 0.01;
x = 0:h:1;

##for i = 1:length(x)
##  y(i) = 3 * x(i) * x(i);
##endfor
##
##plot(x,y,'Color','#bf616c','.','Markersize',16);

k = 6432;

a = min(x);
b = max(x);

xrgen = (b-a) * rand(1,k) + a;

for i = 1:length(xrgen)
  y(i) = 3 * xrgen(i) * xrgen(i);
endfor

plot(xrgen,y,'Color','#a347ba','.');
hold on


c = min(y);
d = max(y);

yrgen = (d-c) * rand(1,k) + c;

plot(xrgen(find(yrgen > y)),yrgen(find(yrgen > y)),'Color','#bf616c','.','Markersize',10);
plot(xrgen(find(yrgen < y)),yrgen(find(yrgen < y)),'Color','#5e81cc','.','Markersize',10);

prbblty = length(find(yrgen < y))/k;
area = prbblty * (max(x)-min(x)) * (max(y)-min(y));

hold off
