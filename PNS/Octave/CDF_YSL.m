function[cdf] = CDF_YSL(x,pdf)
  cdf = ones(1,length(x));
  cdf(1) = pdf(1);
  for i=2:length(x)
    cdf(i) = cdf(i-1) + pdf(i);
  endfor
endfunction
