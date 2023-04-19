close all;
clear all;
clc;

pkg load io
C=xlsread('p9.xlsx','S11');
S=xlsread('p9.xlsx','K11');
[rows,cols]=size(C);

for i=1:rows
  A=C(i,:);
  counts(i)=length(find(A==S));
endfor
result=max(counts);
ind=find(counts==result);
stem(counts/cols, 'k.', 'Color', '#5e81cc', 'Markersize', 10, 'LineWidth', 2);
figure
bar(1:rows, counts/cols, 'facecolor', '#b75969');
title('Conditional Probability');
xlabel('Index');
ylabel('Probability');
set(gca, 'fontsize', 15);

printf('\nRows : %d\nColumns : %d\nResult : %d\nIndex : %d\n\n', rows, cols, result, ind);

