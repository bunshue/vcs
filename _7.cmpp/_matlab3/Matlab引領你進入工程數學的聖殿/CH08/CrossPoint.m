function r=CrossPoint(varargin)
%CROSSPOINT   �T�w�ϧΩҦb�������϶�
% R=CROSSPOINT(F1,F2)  �Ǧ^���uF1�MF2�����I�����y�СA�Ÿ����ܼƬ��ۥѦ��ܼ�
% R=CROSSPOINT(F1,F2,X)  �Ǧ^���uF1�MF2�����I�����y�СA�Ÿ����ܼƬ�X
% 
% ��ɤJ�ѼƼơG
%     ---F1,F2�G���u����ƴy�z
% ��X�ѼơG
%     ---R�G���I�����y�а϶�
%
% See also solve

[f1,f2]=deal(varargin{1:2});
s=unique([symvar(f1),symvar(f2)]);
if nargin==2 && length(s)==1
    x=s;
else
    x=varargin{3};
end
x0=solve(f1-f2,x);
N=length(x0);
r=zeros(N-1,2);
for k=1:N-1
    r(k,:)=[x0(k),x0(k+1)];
end