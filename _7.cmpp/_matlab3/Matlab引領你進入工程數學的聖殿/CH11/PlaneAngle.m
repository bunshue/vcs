function theta=PlaneAngle(PI1,PI2)
%PLANEANGLE   ―ㄢキЖà
% T=PLANEANGLE(PI1,PI2)  ―キPI1㎝PI2Жà
%
% 块旧把计计
%     ---PI1,PI2ㄢキ╰计秖
% 块把计
%     ---T肚キЖà
%
% See also subspace

if isa([PI1;PI2],'sym')
    PI1=[diff(PI1,'x'),diff(PI1,'y'),diff(PI1,'z')];
    PI2=[diff(PI2,'x'),diff(PI2,'y'),diff(PI2,'z')];
end
if isvector(PI1) && isvector(PI2)
    if length(PI1)==3 && length(PI2)==3
        theta=subspace(PI1(:),PI2(:));
    else
        error('块秖ゲ斗3D秖.')
    end
else
    error('Illegal Input arguments.')
end