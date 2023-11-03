function surface_para(funx,funy,funz,varargin)
%SURFACE_PARA   ø��H�ѼƤ�{����ܪ������ΥH�ѼƤ�{����ܪ����u¶z�b����ұo�����঱��
% SURFACE_PARA(FUNX,FUNY,FUNZ,T)  ø��ѼƤ�{���T�w�����u¶z�b���઺���঱��
% SURFACE_PARA(FUNX,FUNY,FUNZ,U,V)  ø��ѼƤ�{���T�w������
%
% ��ɤJ�ѼƼơG
%     ---FUNX,FUNY,FUNZ�G�ѼƤ�{���A�i�H�O���u�Φ���
%     ---T�G���u�ѼƤ�{�����ܼ�
%     ---U,V�G�����ѼƤ�{�������ܼ�
%
% See also surf

s=unique([symvar(funx),symvar(funy),symvar(funz)]);
if length(s)==1
    theta=linspace(0,2*pi);
    t=varargin{1};
    [T,Th]=meshgrid(t,theta);
    X=subs(sqrt(funx^2+funy^2),s,T).*cos(Th);
    Y=subs(sqrt(funx^2+funy^2),s,T).*sin(Th);
    Z=subs(funz,s,T);
elseif length(s)==2
    [u,v]=deal(varargin{:});
    [U,V]=meshgrid(u,v);
    X=subs(funx,num2cell(s),{U,V});
    Y=subs(funy,num2cell(s),{U,V});
    Z=subs(funz,num2cell(s),{U,V});
else
    error('�ѼƤ�{�����ѼƭӼƦ��~.')
end
surf(X,Y,Z)