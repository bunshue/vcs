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
using System.Text;

namespace Main
{
    /// <summary>
    /// ���ļ��ж�ȡͼ����
    /// </summary> 
    public class FileImage : IImage
    {
        /// <summary>
        /// ��ȡͼƬ
        /// </summary>
        /// <returns>
        /// ���ɵ�ͼƬ
        /// </returns>
        public Bitmap GetBitmap()
        {
            return new Bitmap(this.GetType(), "3.bmp");
        }
    }
}
