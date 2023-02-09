function [r] = YSL_correlation(x,y)
  n = length(x);
  r = ((n * sum(x .* y)) - (sum(x) * sum(y))) / (((sqrt(n * sum(x .* x) - (sum(x))^2))) * ((sqrt(n * sum(y .* y) - (sum(y))^2))))
 endfunction
