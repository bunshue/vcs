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
    /// 用GDI+绘制图片抽象类
    /// </summary>
    public abstract class GdiImage : IImage
    {
        private static Bitmap bitmap = null;
        private static readonly object obj = new object();
        private Color flyColor = Color.White;
        private float width = 2f;

        /// <summary>
        /// 获取图片
        /// </summary>
        /// <returns>
        /// 生成的图片
        /// </returns>
        public virtual Bitmap GetBitmap()
        {
            createBitmap();
            return bitmap;
        }

        /// <summary>
        /// 生成Bitmap
        /// </summary>
        /// <returns>
        /// 生成后的Bitmap
        /// </returns>
        protected virtual Bitmap createBitmap()
        {
            if (bitmap == null)
            {
                lock (obj)
                {
                    if (bitmap == null)
                    {
                        bitmap = new Bitmap(64, 64);
                        using (Graphics g = Graphics.FromImage(bitmap))
                        {
                            g.SmoothingMode = SmoothingMode.HighQuality;
                            g.Clear(Color.Transparent);

                            DrawImage(g, new SolidBrush(flyColor), new Pen(flyColor, width));

                            g.Save();
                        }
                    }
                }
            }

            return bitmap;
        }

        /// <summary>
        /// 绘制需要的图片
        /// </summary>
        /// <param name="g">Graphics</param>
        /// <param name="b">画刷</param>
        /// <param name="p">画笔</param>
        protected abstract void DrawImage(Graphics g, Brush b, Pen p);

        /// <summary>
        /// 颜色
        /// </summary>
        public virtual Color FlyColor
        {
            get
            {
                return flyColor;
            }
            set
            {
                flyColor = value;
            }
        }

        /// <summary>
        /// 宽度
        /// </summary>
        public virtual float Width
        {
            get
            {
                return width;
            }
            set
            {
                width = value;
            }
        }
    }
}
