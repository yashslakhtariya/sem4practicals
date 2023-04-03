clear all;
close all;
clc;

d = 64;
r = 6432;

for i = 1:d
  A = randi([1, 6], i, r);
  B = sum(A, 1); # 1 for vertical, 2 for horizontal sum

  for k = i:6*i
    p(k-(i-1)) = length(find(B==k)) / r;
  endfor
endfor

stem(p, 'k.', 'Color', '#5e81cc', 'Markersize', 10, 'LineWidth', 2)
figure
bar(d:6*d, p, 1, 'facecolor', '#b75969')

