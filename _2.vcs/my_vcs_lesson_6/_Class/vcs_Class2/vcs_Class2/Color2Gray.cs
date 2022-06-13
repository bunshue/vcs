using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_Class2
{
    class Color2Gray
    {
        public Bitmap bitmap1; // 原圖形
        public Bitmap bitmap2; // 新圖形

        public Color2Gray(Bitmap bmp)
        {
            this.bitmap1 = bmp;
            bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);
        }

        public void do_Color2Gray()
        {
            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap2.SetPixel(xx, yy, zz);
                }
            }
        }

        public void Draw()
        {
            Graphics g = Graphics.FromImage(bitmap2);
            g.DrawRectangle(Pens.Red, 10, 10, 100, 100);
        }
    }
}

