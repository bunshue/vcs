input_string = 'ee cs econ stat me';  
remainder = input_string;  
parsed = '';		% �إߤ@�Ŧr���}�C  
while (any(remainder))  
	[chopped, remainder] = strtok(remainder);  
	parsed = strvcat(parsed, chopped);  
end  
parsed