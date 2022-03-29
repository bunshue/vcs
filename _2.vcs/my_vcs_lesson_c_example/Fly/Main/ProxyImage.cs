#region 版权
/*
 * 版权归Lawson所有
 * QQ：313769823
 * Blog:lawson.cnblogs.com
 */
#endregion

using System;
using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace Main
{
    /// <summary>
    /// 负责桌面飘动的图片处理
    /// </summary>
    public class ProxyImage
    {
        private static Hashtable imageList = new Hashtable();

        /// <summary>
        /// 默认构造函数
        /// </summary>
        public ProxyImage()
        {
            //无操作
        }

        /// <summary>
        /// 添加图片种类
        /// </summary>
        /// <param name="image">图片类型</param>
        public static void AddImage(IImage image)
        {
            imageList.Add(imageList.Count + 1, image);
        }

        /// <summary>
        /// 获取图片
        /// </summary>
        /// <returns>图片</returns>
        public static Image GetImage()
        {
            object obj = null;
            Image result = null;
            if (imageList.Count == 1)
            {
                obj = imageList[1];
            }
            else
            {
                Random random = new Random();
                obj = imageList[random.Next(1, imageList.Count)];
            }
            if (obj == null)
            {
                //防止扩展图片时，引用生成图片类而没先实例化它
                throw new Exception("添加生成图片类时请先实例化该类");
            }

            obj = obj as IImage;
            if (obj != null)
            {
                result = ((IImage)obj).GetBitmap();
            }
            else
            {
                throw new Exception("GetImage时出错误了，您可以把给错误发送给我：）");
            }

            return result;
        }
    }
}
