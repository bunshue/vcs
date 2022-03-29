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
    /// 飘动的实体
    /// </summary>
    public class Flakes
    {
        #region 私有字段

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
        /// 默认构造函数
        /// </summary>
        public Flakes()
        {
            //无操作
        }

        /// <summary>
        /// 赋初值构造函数
        /// </summary>
        /// <param name="x">X位置</param>
        /// <param name="y">Y位置</param>
        /// <param name="xRate">X坐标速度</param>
        /// <param name="yRate">Y坐标速度</param>
        /// <param name="rottion">旋转度数</param>
        /// <param name="rotationRate">旋转速度</param>
        /// <param name="scale">缩放比例</param>
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

        #region 公有字段

        /// <summary>
        /// X位置
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
        /// Y位置
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
        /// X坐标速度
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
        /// Y坐标速度
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
        /// 旋转度数
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
        /// 旋转速度
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
        /// 缩放比例
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
        /// 飘动的图片
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
