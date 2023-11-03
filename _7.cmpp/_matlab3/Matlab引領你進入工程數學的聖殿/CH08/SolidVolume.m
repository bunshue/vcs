function V=SolidVolume(fun,x,a,b,type)
%SOLIDVOLUME   利用定積分求立體體積
% V=SOLIDVOLUME(FUN,X,A,B,TYPE)  計算指定型態的旋轉體的體積，若曲線方程式中包括
%                                      唯一符號自變數時，則繪制對應的旋轉體圖形
%
% 輸導入參數數：
%     ---FUN：曲線的函數描述
%     ---X：符號自變數
%     ---A,B：特殊的積分下限和上限
%     ---TYPE：旋轉體型態，TYPE有以下取值：
%               1.'c'或0：已知平面截面積的立體體積
%               2.'x'或1：繞x軸旋轉的旋轉體
%               3.'y'或2：繞y軸旋轉的旋轉體
% 輸出參數：
%     ---V：傳回的圖形面積或旋轉體體積
%
% See also int, GraphicArea

s=symvar(fun);
switch type
    case {0,'c'}
        V=simple(int(fun,x,a,b));
    case {1,'x'}
        V=simple(int(pi*fun^2,x,a,b));
        if length(s)==1
            DrawSolid([0,1,0])
        end
    case {2,'y'}
        V=simple(int(pi*fun^2,x,a,b));
        if length(s)==1
            DrawSolid([1,0,0])
        end
    otherwise
        error('Illegal options.')
end
    function DrawSolid(direction)
        t=linspace(a,b,50);
        [X,Y,Z]=cylinder(subs(fun,x,t),50);
        h1=mesh(X,Y,a+(b-a)*Z);
        hidden off
        hold on
        h2=plot3(t,zeros(size(t)),subs(fun,x,t),'k','LineWidth',2);
        x_Lim=get(gca,'xlim');
        y_Lim=get(gca,'ylim');
        z_Lim=get(gca,'zlim');
        axis([x_Lim,y_Lim,z_Lim])
        h3=arrow([0,0,a],[0,0,b],'Length',20,'BaseAngle',30,...
            'TipAngle',20,'Width',2);
        rotate([h1,h2,h3],direction,90,[0,0,0]);
        if isequal(direction,[0,1,0])
            title('旋轉軸：x軸')
            axis([z_Lim,y_Lim,x_Lim])
        elseif isequal(direction,[1,0,0])
            title('旋轉軸：y軸')
            axis([x_Lim,z_Lim,y_Lim])
        end
        xlabel('x'); ylabel('y')
        h_legend=legend('旋轉體','旋轉曲線');
        set(h_legend,'Position',[0.13 0.87 0.22 0.1]);
    end
end