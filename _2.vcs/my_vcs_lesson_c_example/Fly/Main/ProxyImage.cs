#region ��Ȩ
/*
 * ��Ȩ��Lawson����
 * QQ��313769823
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
    /// ��������Ʈ����ͼƬ����
    /// </summary>
    public class ProxyImage
    {
        private static Hashtable imageList = new Hashtable();

        /// <summary>
        /// Ĭ�Ϲ��캯��
        /// </summary>
        public ProxyImage()
        {
            //�޲���
        }

        /// <summary>
        /// ���ͼƬ����
        /// </summary>
        /// <param name="image">ͼƬ����</param>
        public static void AddImage(IImage image)
        {
            imageList.Add(imageList.Count + 1, image);
        }

        /// <summary>
        /// ��ȡͼƬ
        /// </summary>
        /// <returns>ͼƬ</returns>
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
                //��ֹ��չͼƬʱ����������ͼƬ���û��ʵ������
                throw new Exception("�������ͼƬ��ʱ����ʵ��������");
            }

            obj = obj as IImage;
            if (obj != null)
            {
                result = ((IImage)obj).GetBitmap();
            }
            else
            {
                throw new Exception("GetImageʱ�������ˣ������԰Ѹ������͸��ң���");
            }

            return result;
        }
    }
}
