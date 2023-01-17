clc;
clear all;
close all;

n = input("Enter the number for calculating nCr : ");

nCr = zeros(1, n+1);
r = 0:n;

for i = 0:n
    nCr(i+1) = factfn(n)/(factfn(n-i)*factfn(i));
    printf("\n%dC%d = %d\n", n, i, nCr(i+1));
endfor

plot(r, nCr, "r.", "Markersize", 30)
title("YSL Graph for r versus nCr", "fontsize", 30)
xlabel("r variable", "fontsize", 25)
ylabel("nCr", "fontsize", 25)

