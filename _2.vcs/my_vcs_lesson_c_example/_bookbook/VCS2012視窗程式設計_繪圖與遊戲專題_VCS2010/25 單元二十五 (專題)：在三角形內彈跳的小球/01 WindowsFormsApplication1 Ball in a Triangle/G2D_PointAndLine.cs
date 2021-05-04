using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    static class G2D_PointAndLine  // �I�u���Y���O
    {
        // ���� �I �O ��� �V�q �� ���@�� 
        // �`�N�G�o�̬O �ϥ� Y �b�V�U ���y�Шt�� 
        public static short IsPointInVector(PointF p1, PointF p2, PointF q1)
        {
            PointF p1p2 = new PointF(p2.X - p1.X, p2.Y - p1.Y);
            PointF p1q1 = new PointF(q1.X - p1.X, q1.Y - p1.Y);

            double Product = p1p2.X * p1q1.Y - p1q1.X * p1p2.Y;

            if (Product > 0) return 1; // �k���A�b���`�� 2D �y�Шt�� �O���� return -1
            else if (Product < 0) return -1; // �����A�b���`�� 2D �y�Шt�� �O�k�� return 1
            else // Product == 0  �b �V�q�������u �W
            {
                float MaxX = (p1.X > p2.X ? p1.X : p2.X);
                float MinX = (p1.X < p2.X ? p1.X : p2.X);
                float MaxY = (p1.Y > p2.Y ? p1.Y : p2.Y);
                float MinY = (p1.Y < p2.Y ? p1.Y : p2.Y);
                if (q1.X <= MaxX && q1.X >= MinX && 
                    q1.Y <= MaxY && q1.Y >= MinY) // q1 �b �V�q�W
                    return 0; // q1 �b �V�q�W
                else
                    return -101; // q1 �b �V�q�������u �W
            }
        }

        // ���� �I �O�_ ��� �T���� ���� 
        // �u�n ���� �I �O�_ ��� �T���� �T���� ���P�@��(���� �� �k��) �Y�i
        // �`�N�G�o�̬O �ϥ� Y �b�V�U ���y�Шt�� 
        public static bool IsPointInTriangle(PointF p1, PointF p2, PointF p3, PointF q1)
        {
            PointF p1p2 = new PointF(p2.X - p1.X, p2.Y - p1.Y);
            PointF p1q1 = new PointF(q1.X - p1.X, q1.Y - p1.Y);
            double Product_p1p2p1q1 = p1p2.X * p1q1.Y - p1q1.X * p1p2.Y;

            PointF p2p3 = new PointF(p3.X - p2.X, p3.Y - p2.Y);
            PointF p2q1 = new PointF(q1.X - p2.X, q1.Y - p2.Y);
            double Product_p2p3p2q1 = p2p3.X * p2q1.Y - p2q1.X * p2p3.Y;

            PointF p3p1 = new PointF(p1.X - p3.X, p1.Y - p3.Y);
            PointF p3q1 = new PointF(q1.X - p3.X, q1.Y - p3.Y);
            double Product_p3p1p3q1 = p3p1.X * p3q1.Y - p3q1.X * p3p1.Y;

            if (Product_p1p2p1q1 <= 0 && Product_p2p3p2q1 <= 0 && Product_p3p1p3q1 <= 0)
                return true;
            else if (Product_p1p2p1q1 >= 0 && Product_p2p3p2q1 >= 0 && Product_p3p1p3q1 >= 0)
                return true;
            else
                return false;
        }

        // �p�� �I q1 �� ���u p1 p2 �� ���u�Z��D�B��e�IH�B�ιﰼ�I q2���y��
        // �`�N�G�o�̬O �ϥ� Y �b�V�U ���y�Шt�� 
        public static void PointToLine(PointF p1, PointF p2, PointF q1, ref double D, ref PointF H, ref PointF q2)
        {
            // �� p1 �M p2 ���I ��� ���u��{��  Ax + By + C = 0
            float A = p1.Y - p2.Y;
            float B = p2.X - p1.X;
            float C = p2.Y * (p1.X - p2.X) - p2.X * (p1.Y - p2.Y);

            double S = A * A + B * B;
            double L = A * q1.X + B * q1.Y + C;
            D = Math.Abs(L) / Math.Sqrt(S);
            H = new PointF((float)(q1.X - A * L / S), (float)(q1.Y - B * L / S));
            q2 = new PointF((float)(q1.X - 2*A * L / S), (float)(q1.Y - 2*B * L / S));
        }

        // �V�q���W��   �Ѥ@�ӦV�q => �@�Ӫ��׬� 1 ���V�q
        public static PointF VectorNormalize(PointF v)
        {
            double v_Length = Math.Sqrt(v.X * v.X + v.Y * v.Y);
            return new PointF((float)(v.X / v_Length), (float)(v.Y / v_Length));
        }

        // �V�q���W��  �Ѩ���I => p1 p2 �V�q => �@�Ӫ��׬� 1 ���V�q
        public static PointF VectorNormalize(PointF p1, PointF p2)
        {
            PointF v = new PointF(p2.X - p1.X, p2.Y - p1.Y);
            double v_Length = Math.Sqrt(v.X * v.X + v.Y * v.Y);
            return new PointF((float)(v.X / v_Length), (float)(v.Y / v_Length));
        }
    }
}
