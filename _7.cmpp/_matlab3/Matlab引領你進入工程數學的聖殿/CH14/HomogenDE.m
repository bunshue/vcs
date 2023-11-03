function varargout=HomogenDE(fun,coef,t)
%HOMOGENDE   �����Υi�Ƭ�������{�����D��
% L=HOMOGENDE(FUN,COEF)  �D�L����{��dY/dX=FUN((a*x+b*y+c)/(a1*x+b1*y+c1))���q��
% L=HOMOGENDE(FUN,COEF,T)  �D�i�Ƭ�������{�����q�ѡA�ë��wFUN�����ܼƬ�T
% [L,S]=L=HOMOGENDE(...)  �D�i�Ƭ�������{�����q�ѨöǦ^��Ѫ��r��Φ�
%
% ��ɤJ�ѼƼơG
%     ---FUN�G����(a*x+b*y+c)/(a1*x+b1*y+c1)�����
%     ---COEF�G�t�Ưx�}[a,b,c;a1,b1,c1]
%     ---T�G���FUN�����ܼ�
% ��X�ѼơG
%     ---L�G�L����{�����q��
%     ---S�G�L����{���Ѫ��r����
%
% See also SeparableVarsDE

if nargin==2
    t=symvar(fun);
end
if length(t)>1
    error('�Ÿ��ܼƭӼƦ��~.')
end
syms x y
D=det(coef(:,1:2));
if D==0
    v=sym('v','real');
    L=coef(2,1)/coef(1,1);
    fun=subs(fun,t,(v+coef(1,3))/(L*v+coef(2,3)));
    I=SeparableVarsDE(sym(coef(1,2)),1/(fun+coef(1,1)/coef(1,2)),x,v);
    yy=subs(I,v,coef(1,1)*x+coef(1,2)*y);
else
    u=sym('u','real');
    X=sym('X','real');
    Y=sym('Y','real');
    x0=-coef(:,1:2)\coef(:,3);
    fun=subs(fun,t,(coef(1,1)+coef(1,2)*u)/(coef(2,1)+coef(2,2)*u));
    I=SeparableVarsDE(1/X,1/(fun-u),X,u);
    I=subs(I,u,Y/X);
    yy=subs(I,{X,Y},{x-x0(1),y-x0(2)});
end
varargout{1}=yy;
if nargout==2
    varargout{2}=['Solution:',char(yy)];
end