%duty=40;weight=1.4;step=2;duty_spwm=duty*weight;aa=0:step:60;bb=sind(aa*3);cc=floor(duty_spwm*bb);plot(cc);cc



%duty=40;weight=1.4;step=2;duty_spwm=duty*weight;aa=0:step:60;bb=sind(aa*3);cc=floor(duty_spwm*bb);plot(cc);cc

%每1度一點，M由0.01、0.02、0.03、、1，共100表格
clear,clc;

%duty=40;
weight=1.4
step=1;

disp('BYTE code spwm_duty_table[100][61] ={')
for duty=1:1:100
    duty_spwm=duty*weight;
    aa=0:step:60;
    bb=sind(aa*3);
    cc=floor(duty_spwm*bb);
	fprintf('{');
	for j=1:1:61
		if(cc(j)>=100)
            cc(j)=100;
			fprintf('%d',cc(j));
        elseif(cc(j)>=10)
			fprintf(' %d',cc(j));
		else
			fprintf('  %d',cc(j));
		end
		if(j==61)
			if(i==100)
				disp('}};');
			else
				disp('},');
			end
		else
			fprintf(',');
		end
	end
end


    
    