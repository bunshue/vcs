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
using System.Text;

namespace Main
{
    public interface IImage : IShow
    {
        /// <summary>
        /// 获取图片
        /// </summary>
        /// <returns>
        /// 生成的图片
        /// </returns>
        Bitmap GetBitmap();
    }
}
