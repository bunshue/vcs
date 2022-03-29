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
    /// Ʈ����ʵ��
    /// </summary>
    public class Flakes
    {
        #region ˽���ֶ�

        private float x = 0.0f;
        private float y = 0.0f;
        private float xRate = 0.5f;
        private float yRate = 1.5f;
        private float rotation = 0.5f;
        private float rotationRate = 1.0f;
        private float scale = 1.0f;
        private Image showImage;

        #endregion

        /// <summary>
        /// Ĭ�Ϲ��캯��
        /// </summary>
        public Flakes()
        {
            //�޲���
        }

        /// <summary>
        /// ����ֵ���캯��
        /// </summary>
        /// <param name="x">Xλ��</param>
        /// <param name="y">Yλ��</param>
        /// <param name="xRate">X�����ٶ�</param>
        /// <param name="yRate">Y�����ٶ�</param>
        /// <param name="rottion">��ת����</param>
        /// <param name="rotationRate">��ת�ٶ�</param>
        /// <param name="scale">���ű���</param>
        public Flakes(float x, float y, float xRate, float yRate, float rotation, float rotationRate, float scale, Image showImage)
        {
            this.x = x;
            this.y = y;
            this.xRate = xRate;
            this.yRate = yRate;
            this.rotation = rotation;
            this.rotationRate = rotationRate;
            this.scale = scale;
            this.showImage = showImage;
        }

        #region �����ֶ�

        /// <summary>
        /// Xλ��
        /// </summary>
        public float X
        {
            get
            {
                return x;
            }
            set
            {
                x = value;
            }
        }

        /// <summary>
        /// Yλ��
        /// </summary>
        public float Y
        {
            get
            {
                return y;
            }
            set
            {
                y = value;
            }
        }

        /// <summary>
        /// X�����ٶ�
        /// </summary>
        public float XRate
        {
            get
            {
                return xRate;
            }
            set
            {
                xRate = value;
            }
        }

        /// <summary>
        /// Y�����ٶ�
        /// </summary>
        public float YRate
        {
            get
            {
                return yRate;
            }
            set
            {
                yRate = value;
            }
        }

        /// <summary>
        /// ��ת����
        /// </summary>
        public float Rotation
        {
            get
            {
                return rotation;
            }
            set
            {
                rotation = value;
            }
        }

        /// <summary>
        /// ��ת�ٶ�
        /// </summary>
        public float RotationRate
        {
            get
            {
                return rotationRate;
            }
            set
            {
                rotationRate = value;
            }
        }

        /// <summary>
        /// ���ű���
        /// </summary>
        public float Scale
        {
            get
            {
                return scale;
            }
            set
            {
                scale = value;
            }
        }

        /// <summary>
        /// Ʈ����ͼƬ
        /// </summary>
        public Image ShowImage
        {
            get
            {
                return showImage;
            }
            set
            {
                showImage = value;
            }
        }

        #endregion
    }
}
