function dfdl=DirectionalDerivative(fun,vars,direction,M)
%DIRECTIONALDERIVATIVE   �p�����F��
% DFDL=DIRECTIONALDERIVATIVE(FUN,VARS,DIRECTION,M)  �p���Ʀb�IM�W������F��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�h����ƪ��Ÿ���F��
%     ---VARS�G�Ÿ����ܼ�
%     ---DIRECTION�G��V�V�q
%     ---M�G���w�I���y��
% ��X�ѼơG
%     ---DFDL�G�Ǧ^������F��
%
% See also Distance, dot

if ~isa(fun,'sym')
    error('FUN must be a Symbolic function.')
end
N=length(vars);
df=sym(zeros(1,N));
for k=1:N
    df(k)=subs(diff(fun,vars{k}),vars,num2cell(M));
end
C=Direction_Cosine(direction);
dfdl=dot(df,C);