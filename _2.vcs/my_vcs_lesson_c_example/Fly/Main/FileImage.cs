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
    /// <summary>
    /// 从文件中读取图数据
    /// </summary> 
    public class FileImage : IImage
    {
        /// <summary>
        /// 获取图片
        /// </summary>
        /// <returns>
        /// 生成的图片
        /// </returns>
        public Bitmap GetBitmap()
        {
            return new Bitmap(this.GetType(), "3.bmp");
        }
    }
}
