k=0;
for i=0:2^16-1
	strRep=dec2hex(i);
	if length(strRep)<4
		strRep=['0'*ones(1,4-length(strRep)), strRep];
	end
	hb=hex2dec(strRep(1:2));
	lb =hex2dec(strRep(3:4));
	if ((lb<=126 & lb>=64) | (lb<=254 & lb>=161)) & ... 
		((i>=41281 & i<=41915) | (i>=41917 & i<=41919) | (i>=42048 & i<=50814) | (i>=50849 & i<=51411) | (i>=51520 & i<=63998))
		k=k+1;
		fprintf('%d. %s\n', k, char(i));
	end
end