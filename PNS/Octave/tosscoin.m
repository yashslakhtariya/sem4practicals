function outpt = tosscoin(n)
  for i = 1:n
    rndm = randi(2,1);
    if rndm == 1
      outpt(1,i) = "H";
    else
      outpt(1,i) = "T";
    endif
  endfor
endfunction
