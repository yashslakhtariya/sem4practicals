clc;
clear all;
close all;

n = input("Enter the number for calculating nPr : ");

nPr = zeros(1, n+1);
r = 0:n;

for i = 0:n
    nPr(i+1) = factfn(n)/factfn(n-i);
    printf("\n%dP%d = %d\n", n, i, nPr(i+1));
endfor

plot(r, nPr, "r.", "Markersize", 30)
title("YSL Graph for r versus nPr", "fontsize", 30)
xlabel("r variable", "fontsize", 25)
ylabel("nPr", "fontsize", 25)

