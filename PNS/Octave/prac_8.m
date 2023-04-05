clear all;
close all;
clc;

P = 0.4:-0.01:0.1;
n = 100;

for i = 1:length(P)
 p = P(i);
 q = 1-p;
 l = n*p;
 for r = 0:n
   B(r+1) = (factfn(n) / (factfn(n-r) * factfn(r))) * (p^r) * (q^(n-r));
   psn(r+1) = ((e^(-l)) * (l^r)) / factfn(r);
 endfor
endfor

figure
subplot(3,1,1);
plot(0:n, B, 'Color', '#a347ba', 'LineWidth', 2);
title('Binomial Distribution Graph', 'fontsize', 25);
xlabel('x = 0 to n', 'fontsize', 20);
ylabel('probability', 'fontsize', 20);
subplot(3,1,2);
plot(0:n, psn, 'Color', '#d18677', 'LineWidth', 2);
title('Poisson Distribution Graph', 'fontsize', 25);
xlabel('x = 0 to n', 'fontsize', 20);
ylabel('probability', 'fontsize', 20);
subplot(3,1,3);
hold on;
plot(0:n, B, 'Color', '#5e81cc', 'LineWidth', 6);
plot(0:n, psn, 'Color', '#b75969', 'LineWidth', 3);
title('Binomial and Poisson Distribution Graph', 'fontsize', 25);
xlabel('x = 0 to n', 'fontsize', 20);
ylabel('probability', 'fontsize', 20);
hold off;
