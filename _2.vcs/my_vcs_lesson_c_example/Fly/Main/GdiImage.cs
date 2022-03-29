#region ��Ȩ
/*
 * ��Ȩ��Lawson����
 * QQ��313769823
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
    /// ��GDI+����ͼƬ������
    /// </summary>
    public abstract class GdiImage : IImage
    {
        private static Bitmap bitmap = null;
        private static readonly object obj = new object();
        private Color flyColor = Color.White;
        private float width = 2f;

        /// <summary>
        /// ��ȡͼƬ
        /// </summary>
        /// <returns>
        /// ���ɵ�ͼƬ
        /// </returns>
        public virtual Bitmap GetBitmap()
        {
            createBitmap();
            return bitmap;
        }

        /// <summary>
        /// ����Bitmap
        /// </summary>
        /// <returns>
        /// ���ɺ��Bitmap
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
        /// ������Ҫ��ͼƬ
        /// </summary>
        /// <param name="g">Graphics</param>
        /// <param name="b">��ˢ</param>
        /// <param name="p">����</param>
        protected abstract void DrawImage(Graphics g, Brush b, Pen p);

        /// <summary>
        /// ��ɫ
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
        /// ���
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
