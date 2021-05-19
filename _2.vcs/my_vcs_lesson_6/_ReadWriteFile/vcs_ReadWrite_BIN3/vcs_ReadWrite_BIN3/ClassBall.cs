using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // for Point, Color

namespace vcs_ReadWrite_BIN3
{
    class ClassBall
    {
        public Point pt; // �y����m
        public Color color; // �y���C��
        int D = 10; // �y���b�|
        int dx, dy; // �ƹ��M�y�����ߦ�m �� ������

        // �غc��
        public ClassBall(Point pt, Color color)
        {
            this.pt = pt;
            this.color = color;
        }

        // �ˬd�O�_���o���I
        public bool CheckSelected(int x, int y)  // �ƹ�����m (�����y��)
        {
            // �ƹ���� �M �y�� �Z��
            double dist = Math.Sqrt((pt.X - x) * (pt.X - x) + (pt.Y - y) * (pt.Y - y));
            if (dist <= D)
            {
                dx = x - pt.X; 
                dy = y - pt.Y;
                return true;
            }
            else return false;
        }

        // ��s �y����m
        public void Move(int x, int y)  // �ѼƬO �ƹ�����m
        {
            pt.X = x - dx;
            pt.Y = y - dy;
        }
    }
}
