clc;
clear all;
close all;

dx = 0.1;
x = -10:dx:10;
s = 2;
u = 0.5;

pdf = PDF_YSL(x,dx,s,u);
cdf = CDF_YSL(x,pdf);

figure
subplot(2,1,1);
plot(x,pdf,"r.","Markersize",16);
title("x versus pdf(x) graph","fontsize",22);
xlabel("value of 'x'","fontsize",22);
ylabel("pdf(x)","fontsize",22);

subplot(2,1,2);
plot(x,cdf,"r.","Markersize",16);
title("x versus cdf(x) graph","fontsize",22);
xlabel("value of 'x'","fontsize",22);
ylabel("cdf(x)","fontsize",22);

mean = MEAN_YSL(x,pdf)
vrnce = VRNCE_YSL(x,pdf,mean)


