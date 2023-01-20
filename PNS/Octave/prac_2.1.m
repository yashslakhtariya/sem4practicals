clc;
clear all;
close all;

n = input("Enter number of tosses : ");

outpt = tosscoin(n);
printf("\n\tOutcome : %s", outpt);
heads=0;
tails=0;
for i = 1:n
  heads = heads + (outpt(i)=="H");
  tails = tails + (outpt(i)=="T");
endfor

PofH = heads/n;
printf("\n\tProbability of Heads : %d", PofH);
PofT = tails/n;
printf("\n\tProbability of Tails : %d", PofT);
