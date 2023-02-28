clear all;
close all;
clc;

h = 0.001;
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

count = 0;

for i = 1:length(x)
  c(i) = length(find(xrgen(find(yrgen < y)) <= x(i)));
  cdf(i) = c(i) / length(find(yrgen < y));
  count = count + 1;
  if(cdf(i) > 0.5)
    tmp1 = i - 1;
    break;
  endif
endfor

for i = 1:length(x)
  c(i) = length(find(xrgen(find(yrgen < y)) <= x(i)));
  cdf(i) = c(i) / length(find(yrgen < y));
  count = count + 1;
  if(cdf(i) > 0.95)
    tmp2 = i - 1;
    break;
  endif
endfor

p1 = x(tmp1);
p2 = x(tmp2);

printf("\n\tArea : %f\n\tProbability : %f\n\tThe point were CDF(X) is 0.5 : %f\n\tThe point where CDF(x) is 0.95 : %f\n", area, prbblty, p1, p2);

