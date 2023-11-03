function S=LineConvert(PI1,PI2)
%LINECONVERT   盢絬よ祘Α锣て把计よ祘Α
% S=LINECONVERT(PI1,PI2)  ―キPI1㎝PI2ユ絬把计よ祘Α
%
% 块旧把计计
%     ---PI1,PI2キ╰计秖
% 块把计
%     ---S把计よ祘Α笷Α
%
% See also \, cross

if ~isvector(PI1) && ~isvector(PI2)
    error('PI1 and PI2 must be vectors.')
end
if length(PI1)==4 && length(PI2)==4
    A=[PI1(1:3);PI2(1:3)];
    b=-[PI1(4);PI2(4)];
    x0=A\b;
    s=cross(A(1,:),A(2,:));
    syms t
    S=x0(:)+s(:)*t;
else
    error('块秖ゲ斗4蝴秖.')
end