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
    public interface IImage : IShow
    {
        /// <summary>
        /// ��ȡͼƬ
        /// </summary>
        /// <returns>
        /// ���ɵ�ͼƬ
        /// </returns>
        Bitmap GetBitmap();
    }
}
