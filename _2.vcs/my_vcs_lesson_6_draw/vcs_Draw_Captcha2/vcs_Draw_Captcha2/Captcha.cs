using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace vcs_Draw_Captcha2
{
    /// <summary>
    /// Captcha
    /// </summary>
    public class Captcha
    {
        #region Private Field
        /// <summary>
        /// 隨機種子
        /// </summary>
        private Random objRandom = new Random();
        #endregion

        #region Public Property

        #region 驗證碼長度
        /// <summary>
        /// 驗證碼長度
        /// </summary>
        private int length = 4;
        /// <summary>
        /// 驗證碼長度(默認為4)
        /// </summary>
        public int Length
        {
            get { return this.length; }
            set { this.length = value; }
        }
        #endregion

        #region 驗證碼字符串
        /// <summary>
        /// 驗證碼字符串
        /// </summary>
        private string verifyCodeText = null;

        /// <summary>
        /// 驗證碼字符串
        /// </summary>
        public string VerifyCodeText
        {
            get { return this.verifyCodeText; }
            set { this.verifyCodeText = value; }
        }
        #endregion

        #region 是否加入小寫字母
        /// <summary>
        /// 是否加入小寫字母
        /// </summary>
        private bool addLowerLetter = false;

        /// <summary>
        /// 是否加入小寫字母(不包括o)
        /// </summary>
        public bool AddLowerLetter
        {
            get { return this.addLowerLetter; }
            set { this.addLowerLetter = value; }
        }
        #endregion

        #region 是否加入大寫字母
        /// <summary>
        /// 是否加入大寫字母
        /// </summary>
        private bool addUpperLetter = false;

        /// <summary>
        /// 是否加入大寫字母(不包括O)
        /// </summary>
        public bool AddUpperLetter
        {
            get { return this.addUpperLetter; }
            set { this.addUpperLetter = value; }
        }
        #endregion

        #region 字體大小
        /// <summary>
        /// 字體大小
        /// </summary>
        private int fontSize = 18;

        /// <summary>
        /// 字體大小(默認為18)
        /// </summary>
        public int FontSize
        {
            get { return this.fontSize; }
            set { this.fontSize = value; }
        }
        #endregion

        #region 字體顏色
        /// <summary>
        /// 字體顏色
        /// </summary>
        private Color fontColor = Color.Blue;

        /// <summary>
        /// 字體顏色(默認為Blue)
        /// </summary>
        public Color FontColor
        {
            get { return this.fontColor; }
            set { this.fontColor = value; }
        }
        #endregion

        #region 字體類型
        /// <summary>
        /// 字體類型
        /// </summary>
        private string fontFamily = "Verdana";

        /// <summary>
        /// 字體類型(默認為Verdana)
        /// </summary>
        public string FontFamily
        {
            get { return this.fontFamily; }
            set { this.fontFamily = value; }
        }
        #endregion

        #region 背景色
        /// <summary>
        /// 背景色
        /// </summary>
        private Color backgroundColor = Color.AliceBlue;

        /// <summary>
        /// 背景色(默認為AliceBlue)
        /// </summary>
        public Color BackgroundColor
        {
            get { return this.backgroundColor; }
            set { this.backgroundColor = value; }
        }
        #endregion

        #region 前景噪點數量
        /// <summary>
        /// 前景噪點數量
        /// </summary>
        private int foreNoisePointCount = 2;

        /// <summary>
        /// 前景噪點數量(默認為2)
        /// </summary>
        public int ForeNoisePointCount
        {
            get { return this.foreNoisePointCount; }
            set { this.foreNoisePointCount = value; }
        }
        #endregion

        #region 隨機碼的旋轉角度
        /// <summary>
        /// 隨機碼的旋轉角度
        /// </summary>
        private int randomAngle = 45;

        /// <summary>
        /// 隨機碼的旋轉角度(默認為40度)
        /// </summary>
        public int RandomAngle
        {
            get { return this.randomAngle; }
            set { this.randomAngle = value; }
        }
        #endregion

        #endregion

        #region Constructor Method
        /// <summary>
        /// 構造方法
        /// </summary>
        public Captcha()
        {
            this.GetText();
        }
        #endregion

        #region Private Method
        /// <summary>
        /// 得到驗證碼字符串
        /// </summary>
        private void GetText()
        {
            //沒有外部輸入驗證碼時隨機生成
            if (String.IsNullOrEmpty(this.verifyCodeText))
            {
                StringBuilder objStringBuilder = new StringBuilder();

                //加入數字1-9
                for (int i = 1; i <= 9; i++)
                {
                    objStringBuilder.Append(i.ToString());
                }

                //加入大寫字母A-Z，不包括O
                if (this.addUpperLetter)
                {
                    char temp = ' ';

                    for (int i = 0; i < 26; i++)
                    {
                        temp = Convert.ToChar(i + 65);

                        //如果生成的字母不是'O'
                        if (!temp.Equals('O'))
                        {
                            objStringBuilder.Append(temp);
                        }
                    }
                }

                //加入小寫字母a-z，不包括o
                if (this.addLowerLetter)
                {
                    char temp = ' ';

                    for (int i = 0; i < 26; i++)
                    {
                        temp = Convert.ToChar(i + 97);

                        //如果生成的字母不是'o'
                        if (!temp.Equals('o'))
                        {
                            objStringBuilder.Append(temp);
                        }
                    }
                }

                //生成驗證碼字符串
                {
                    int index = 0;

                    for (int i = 0; i < length; i++)
                    {
                        index = objRandom.Next(0, objStringBuilder.Length);

                        this.verifyCodeText += objStringBuilder[index];

                        objStringBuilder.Remove(index, 1);
                    }
                }
            }
        }
        /// <summary>
        /// 得到驗證碼圖片
        /// </summary>
        public Bitmap GetImage()
        {
            Bitmap result = null;

            //創建繪圖
            result = new Bitmap(this.verifyCodeText.Length * 16, 25);

            using (Graphics objGraphics = Graphics.FromImage(result))
            {
                objGraphics.SmoothingMode = SmoothingMode.HighQuality;

                //清除整個繪圖面並以指定背景色填充
                objGraphics.Clear(this.backgroundColor);

                //創建畫筆
                using (SolidBrush objSolidBrush = new SolidBrush(this.fontColor))
                {
                    this.AddForeNoisePoint(result);

                    this.AddBackgroundNoisePoint(result, objGraphics);

                    //文字居中
                    StringFormat objStringFormat = new StringFormat(StringFormatFlags.NoClip);

                    objStringFormat.Alignment = StringAlignment.Center;
                    objStringFormat.LineAlignment = StringAlignment.Center;

                    //字體樣式
                    Font objFont = new Font(this.fontFamily, objRandom.Next(this.fontSize - 3, this.fontSize), FontStyle.Regular);

                    //驗證碼旋轉，防止機器識別
                    char[] chars = this.verifyCodeText.ToCharArray();

                    for (int i = 0; i < chars.Length; i++)
                    {
                        //轉動的度數
                        float angle = objRandom.Next(-this.randomAngle, this.randomAngle);

                        objGraphics.TranslateTransform(12, 12);
                        objGraphics.RotateTransform(angle);
                        objGraphics.DrawString(chars[i].ToString(), objFont, objSolidBrush, -2, 2, objStringFormat);
                        objGraphics.RotateTransform(-angle);
                        objGraphics.TranslateTransform(2, -12);
                    }
                }
            }

            return result;
        }
        /// <summary>
        /// 添加前景噪點
        /// </summary>
        /// <param name="objBitmap"></param>
        private void AddForeNoisePoint(Bitmap objBitmap)
        {
            for (int i = 0; i < objBitmap.Width * this.foreNoisePointCount; i++)
            {
                objBitmap.SetPixel(objRandom.Next(objBitmap.Width), objRandom.Next(objBitmap.Height), this.fontColor);
            }
        }
        /// <summary>
        /// 添加背景噪點
        /// </summary>
        /// <param name="objBitmap"></param>
        /// <param name="objGraphics"></param>
        private void AddBackgroundNoisePoint(Bitmap objBitmap, Graphics objGraphics)
        {
            using (Pen objPen = new Pen(Color.Azure, 0))
            {
                for (int i = 0; i < objBitmap.Width * 2; i++)
                {
                    objGraphics.DrawRectangle(objPen, objRandom.Next(objBitmap.Width), objRandom.Next(objBitmap.Height), 1, 1);
                }
            }
        }
        #endregion

        /*
        #region Public Method
        public void Output(HttpResponse objHttpResponse)
        {
            using (Bitmap objBitmap = this.GetImage())
            {
                if (objBitmap != null)
                {
                    using (MemoryStream objMS = new MemoryStream())
                    {
                        objBitmap.Save(objMS, ImageFormat.Jpeg);
 
                        HttpContext.Current.Response.ClearContent();
                        HttpContext.Current.Response.ContentType = "image/Jpeg";
                        HttpContext.Current.Response.BinaryWrite(objMS.ToArray());
                        HttpContext.Current.Response.Flush();
                        HttpContext.Current.Response.End();
                    }
                }
            }
        }
        #endregion
        */
    }
}
