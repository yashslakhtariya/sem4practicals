clc;
clear all;
close all;

n = input("Enter number of tosses : ");

outpt = tosscoin(n);
printf("\n\tOutcome : %s", outpt);

heads = length(find(outpt=="H"));
tails = length(find(outpt=="T"));

PofH = heads/n;
printf("\n\tProbability of Heads : %d", PofH);
PofT = tails/n;
printf("\n\tProbability of Tails : %d", PofT);
