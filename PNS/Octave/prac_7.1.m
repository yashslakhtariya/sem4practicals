clc;
clear all;
close all;

A = [1 2 3 4 5 6];
pA = [1/6 1/6 1/6 1/6 1/6 1/6];
d1 = bar(A, pA, 1);
set(d1, 'FaceColor', '#a347ba');
d = 4;

B = [];
for k = 2:d
  for i = 1:6
    tmp = A+i;
    B = [B tmp];
  endfor

  for j = k:(6*k)
    pB(j-(k-1)) = length(find(B==j)) / (6^k);
  endfor

  figure
  d2 = bar(k:(6*k), pB, 1);

  if mod(k,2) == 0
      set(d2, 'FaceColor', '#b75969');
  else
      set(d2, 'FaceColor', '#d18677');
  endif

  A = B;
  B = [];
endfor
