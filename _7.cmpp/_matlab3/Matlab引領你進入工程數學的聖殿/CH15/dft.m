function X=dft(x,dim)
%DFT   �����Ÿ̸��ܴ�
% Y=DFT(X)  �D��Ưx�}X�������Ÿ̸��ܴ�
% Y=DFT(X,DIM)  ��x�}X������ΦC���D�Ÿ̸��ܴ�
%
% ��ɤJ�ѼƼơG
%     ---X�G��Ưx�}
%     ---DIM�G���w������V
% ��X�ѼơG
%     ---Y�G�����Ÿ̸��ܴ����G
%
% See also fourier

if isvector(x)
    x=x(:).';
end
if nargin<2 || isvector(x)
    dim=1;
end
N=size(x,setdiff([1,2],dim));
n=0:N-1;
k=0:N-1;
WN=exp(-1j*2*pi/N);
nk=n'*k;
W=WN.^nk;
if dim==1
    X=x*W;
else
    X=(x.'*W).';
end