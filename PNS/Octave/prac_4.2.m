clc;
clear all;
close all;

y = audioread("good_morning.wav");
ysl = audioread("Sample_Audio.wav");

for i = 1:(length(ysl) - length(y) + 1)
  r(i) = sum(ysl(i:i+length(y)-1) .* y);
endfor

MaxIndex = find(r == max(r))

figure
subplot(3,1,1);
plot(ysl,'Color','#BF616C');
xlabel("Sample Audio waves",'fontsize',22);
title("YSL Graph of Audio File",'fontsize',32);
subplot(3,1,2);
plot(y,'Color','#5E81CC','LineWidth',3);
xlabel("Test Audio part waves",'fontsize',22);
subplot(3,1,3);
plot(r,'Color','#d18677');
xlabel("Correlation graph",'fontsize',22);
