function r=irrFind(cashFlowVec, x0)
r=fzero(@npvCompute, x0);

	function npv=npvCompute(x)
	n=length(cashFlowVec);
	npv=sum(cashFlowVec./((1+x).^(0:n-1)));		% Yearly compounding
	end
end