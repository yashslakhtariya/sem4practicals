function[vrnce] = VRNCE_YSL(x,pdf,mean)
vrnce = sum(x.^2 .* pdf) - mean^2;
endfunction
