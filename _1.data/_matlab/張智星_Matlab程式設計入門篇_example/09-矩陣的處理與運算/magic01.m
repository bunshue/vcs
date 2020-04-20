M = magic(5)      
fprintf('直行總和：'); sum(M)			% M 的每一個直行總和
fprintf('橫列總和：'); sum(M, 2)			% M 的每一個橫列總和
fprintf('對角線總和：'); sum(diag(M))		% M 的對角線總和
fprintf('反對角線總和：'); sum(diag(fliplr(M)))	% M 的反對角線總和