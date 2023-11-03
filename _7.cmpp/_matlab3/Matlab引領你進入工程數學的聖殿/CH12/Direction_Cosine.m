function C=Direction_Cosine(r)
%DIRECTION_COSINE   求向量的方向余弦
% DIRECTION_COSINER(R)  繪制向量R與各座標軸的位置關系
% C=DIRECTION_COSINE(R)  求向量R的方向余弦
%
% 輸導入參數數：
%     ---R：指定向量
% 輸出參數：
%     ---C：向量的方向余弦
%
% See also Distance, drawvec

[m,n]=size(r);
if m~=1 && n~=1
    error('向量的座標表示形式有誤.')
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
        title(['方向余弦：[',num2str(Cosine),']'])
    else
        C=Cosine;
    end
else
    C=Cosine;
end