function V=SolidVolume(fun,x,a,b,type)
%SOLIDVOLUME   �Q�Ωw�n���D������n
% V=SOLIDVOLUME(FUN,X,A,B,TYPE)  �p����w���A�������骺��n�A�Y���u��{�����]�A
%                                      �ߤ@�Ÿ����ܼƮɡA�hø�������������ϧ�
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���u����ƴy�z
%     ---X�G�Ÿ����ܼ�
%     ---A,B�G�S���n���U���M�W��
%     ---TYPE�G�����髬�A�ATYPE���H�U���ȡG
%               1.'c'��0�G�w�������I���n��������n
%               2.'x'��1�G¶x�b���઺������
%               3.'y'��2�G¶y�b���઺������
% ��X�ѼơG
%     ---V�G�Ǧ^���ϧέ��n�α�������n
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
            title('����b�Gx�b')
            axis([z_Lim,y_Lim,x_Lim])
        elseif isequal(direction,[1,0,0])
            title('����b�Gy�b')
            axis([x_Lim,z_Lim,y_Lim])
        end
        xlabel('x'); ylabel('y')
        h_legend=legend('������','���঱�u');
        set(h_legend,'Position',[0.13 0.87 0.22 0.1]);
    end
end