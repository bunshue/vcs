#region 版权
/*
 * 版权归Lawson所有
 * QQ：313769823
 * Blog:lawson.cnblogs.com
 */
#endregion

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Text;

namespace Main
{
    /// <summary>
    /// 用GDI+绘制的图片
    /// </summary> 
    public class GDIPlusImage : GdiImage
    {
        /// <summary>
        /// 绘制Love字体图片
        /// </summary>
        /// <param name="g">Graphics</param>
        /// <param name="b">画刷</param>
        /// <param name="p">画笔</param>
        protected override void DrawImage(Graphics g, Brush b, Pen p)
        {
            //绘制Love字
            Pen smallPen = new Pen(Color.White, 1f);

            const int top = 15;
            const int length = 35;
            const int middle = 12;
            const int mmidlle = 6;
            const int one = 6;
            const int two = 12;
            const int three = 14;
            const int four = 17;
            const int five = 20;
            const int sixth = 24;
            const int seventh = 28;

            g.DrawLine(p, 0, top, 0, 0);
            g.DrawLine(p, 0, 0, length, 0);

            g.DrawLine(smallPen, one, middle, one, 0);
            g.DrawLine(smallPen, one, middle, two, middle);
            g.DrawLine(smallPen, two, middle, two, 0);

            g.DrawLine(smallPen, three, 0, four, middle);
            g.DrawLine(smallPen, four, middle, five, 0);

            g.DrawLine(smallPen, sixth, middle, sixth, 0);
            g.DrawLine(smallPen, sixth, middle, seventh, middle);
            g.DrawLine(smallPen, sixth, mmidlle, seventh, mmidlle);
        }
    }
}
