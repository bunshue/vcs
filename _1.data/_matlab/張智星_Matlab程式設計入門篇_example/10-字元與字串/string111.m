clear all		                   % �M���Ҧ��ܼ�
for i = 3:6    
	eval(['x', int2str(i) , '= magic(' , int2str(i) , ') ; ']);  
end  
whos x*