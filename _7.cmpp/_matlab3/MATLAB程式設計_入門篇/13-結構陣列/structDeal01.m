myStruct = struct('name', {'Tim', 'Annie'}, 'age', {10, 13});  
[myStruct.name] = deal('Roger', 'Jack');  
fprintf('myStruct(1).name = %s\n', myStruct(1).name);
fprintf('myStruct(2).name = %s\n', myStruct(2).name);