function S=GraphicArea(varargin)
%GRAPHICAREA   �ϥΩw�n���D�����ϧΪ����n
% S=GRAPHICAREA(F,G,A,B,'dicarl')  �p�⪽���y�Шt�U���uF�MG�P���uX=A�BX=B�ҳ�ϧ�
%                                         �����n�A�A�Ω���F�MG�u�]�A�@�ӲŸ��ܼƪ�����
% S=GRAPHICAREA(F,G,X,A,B,'dicarl')  �p�⪽���y�Шt�U���uF�MG�P���uX=A�BX=B�ҳ�
%                                           �ϧΪ����n�A�ë��w�Ÿ����ܼƬ�X
% S=GRAPHICAREA(R,ALPHA,BETA,'polar')  �p�ⷥ�y�Шt�U���uR�PT=ALPHA�BT=BETA�ҳ�ϧ�
%                                              �����n�A�䤤R�u�]�A�@�ӲŸ��ܼ�T
% S=GRAPHICAREA(R,T,ALPHA,BETA,'polar')  �p�ⷥ�y�Шt�U���uR�PT=ALPHA�BT=BETA�ҳ�
%                                                �ϧΪ����n�A�ë��w�Ÿ����ܼƬ�T
%
% ��ɤJ�ѼƼơG
%     ---F,G�G�����y�Шt�U���u����ƴy�z
%     ---R�G���y�Шt�U���u����ƴy�z
%     ---A,B�G�����y�Шt�U���n���U���P�W��
%     ---ALPHA,BETA�G���y�Шt�U���n���U���P�W��
%     ---TYPE�G�y�Шt���A�A��'dicarl'�M'polar'��ب���
% ��X�ѼơG
%     ---S�G�Ǧ^���ϧΪ����n
%
% See also int

args=varargin;
type=args{end};
switch lower(type)
    case 'dicarl'
        f1=args{1};
        f2=args{2};
        s=unique([symvar(f1),symvar(f2)]);
        if length(s)>1 || nargin==6
            x=args{3};
            a=args{4};
            b=args{5};
        else
            if nargin==5
                x=s;
                a=args{3};
                b=args{4};
            end
        end
        S=simple(int(f1-f2,x,a,b));
    case 'polar'
        r=args{1};
        s=symvar(r);
        if length(s)>1 || nargin==5
            t=args{2};
            alpha=args{3};
            beta=args{4};
        else
            if nargin==4
                t=s;
                alpha=args{2};
                beta=args{3};
            end
        end
        S=simple(1/2*int(r^2,t,alpha,beta));
    otherwise
        error('Illegal options.')
end
S=abs(S);