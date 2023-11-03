function C=Direction_Cosine(r)
%DIRECTION_COSINE   �D�V�q����V�E��
% DIRECTION_COSINER(R)  ø��V�qR�P�U�y�жb����m���t
% C=DIRECTION_COSINE(R)  �D�V�qR����V�E��
%
% ��ɤJ�ѼƼơG
%     ---R�G���w�V�q
% ��X�ѼơG
%     ---C�G�V�q����V�E��
%
% See also Distance, drawvec

[m,n]=size(r);
if m~=1 && n~=1
    error('�V�q���y�Ъ�ܧΦ����~.')
end
L=Distance(r);
Cosine=r/L;
if nargout==0
    if isnumeric(Cosine) && (n==2 || n==3)
        drawvec(r)
        hold on
        drawvec([r(1),0,0])
        drawvec([0,r(2),0])
        drawvec([0,0,r(3)])
        title(['��V�E���G[',num2str(Cosine),']'])
    else
        C=Cosine;
    end
else
    C=Cosine;
end