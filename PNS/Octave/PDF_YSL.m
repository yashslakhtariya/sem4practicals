function[pdf]=PDF_YSL(x,dx,s,u)
  for i=1:length(x)
    p(i) = (1/(s*sqrt(2*pi)))* e^(-0.5*((x(i)-u)/s)^2);
    pdf(i) = p(i)*dx;
  endfor
endfunction
