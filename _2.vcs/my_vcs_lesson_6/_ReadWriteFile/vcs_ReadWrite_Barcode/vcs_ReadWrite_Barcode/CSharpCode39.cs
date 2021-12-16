using System;
using System.Collections.Generic;
using System.Collections;
using System.Text;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Text;
using System.Drawing.Imaging;

namespace vcs_ReadWrite_Barcode
{
    /// <summary>
    /// Code39一维码生成类
    /// http://www.cnblogs.com/bluescreen/p/4689351.html
    /// </summary>
    public class CSharpCode39
    {

        #region 数据码
        private byte[,] c39_bp = new byte[,] { 
            { 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x31, 0x30, 0x30 }, { 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31 }, { 0x32, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31 }, { 0x33, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30 }, { 0x34, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x31 }, { 0x35, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30 }, { 0x36, 0x30, 0x30, 0x31, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30 }, { 0x37, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31 }, { 0x38, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30 }, { 0x39, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30 }, { 0x41, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31 }, { 0x42, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31 }, { 0x43, 0x31, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30 }, { 0x44, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31 }, { 0x45, 0x31, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30 }, { 70, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30 }, 
            { 0x47, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x31 }, { 0x48, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30 }, { 0x49, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30 }, { 0x4a, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x31, 0x30, 0x30 }, { 0x4b, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31 }, { 0x4c, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31 }, { 0x4d, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30 }, { 0x4e, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x31 }, { 0x4f, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30 }, { 80, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30 }, { 0x51, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x31 }, { 0x52, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30 }, { 0x53, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30 }, { 0x54, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30 }, { 0x55, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31 }, { 0x56, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31 }, 
            { 0x57, 0x31, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30 }, { 0x58, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31 }, { 0x59, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30 }, { 90, 0x30, 0x31, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30 }, { 0x2d, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31 }, { 0x2e, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30 }, { 0x20, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30 }, { 0x2a, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30 }, { 0x24, 0x30, 0x31, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30 }, { 0x2f, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30 }, { 0x2b, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30 }, { 0x25, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x31, 0x30 }
         };
        //code39合法字符集 [0-9A-Z+-*/%. ] 共43个
        private byte[] c39_cw = new byte[] { 
            0x30, 0x31, 50, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x41, 0x42, 0x43, 0x44, 0x45, 70, 
            0x47, 0x48, 0x49, 0x4a, 0x4b, 0x4c, 0x4d, 0x4e, 0x4f, 80, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 
            0x57, 0x58, 0x59, 90, 0x2d, 0x2e, 0x20, 0x24, 0x2f, 0x2b, 0x25
         };
        private byte[,] c39_ex = new byte[,] { 
            { 1, 0x24, 0x41 }, { 2, 0x24, 0x42 }, { 3, 0x24, 0x43 }, { 4, 0x24, 0x44 }, { 5, 0x24, 0x45 }, { 6, 0x24, 70 }, { 7, 0x24, 0x47 }, { 8, 0x24, 0x48 }, { 9, 0x24, 0x49 }, { 10, 0x24, 0x4a }, { 11, 0x24, 0x4b }, { 12, 0x24, 0x4c }, { 13, 0x24, 0x4d }, { 14, 0x24, 0x4e }, { 15, 0x24, 0x4f }, { 0x10, 0x24, 80 }, 
            { 0x11, 0x24, 0x51 }, { 0x12, 0x24, 0x52 }, { 0x13, 0x24, 0x53 }, { 20, 0x24, 0x54 }, { 0x15, 0x24, 0x55 }, { 0x16, 0x24, 0x56 }, { 0x17, 0x24, 0x57 }, { 0x18, 0x24, 0x58 }, { 0x19, 0x24, 0x59 }, { 0x1a, 0x24, 90 }, { 0x1b, 0x25, 0x41 }, { 0x1c, 0x25, 0x42 }, { 0x1d, 0x25, 0x43 }, { 30, 0x25, 0x44 }, { 0x1f, 0x25, 0x45 }, { 0x3b, 0x25, 70 }, 
            { 60, 0x25, 0x47 }, { 0x3d, 0x25, 0x48 }, { 0x3e, 0x25, 0x49 }, { 0x3f, 0x25, 0x4a }, { 0x5b, 0x25, 0x4b }, { 0x5c, 0x25, 0x4c }, { 0x5d, 0x25, 0x4d }, { 0x5e, 0x25, 0x4e }, { 0x5f, 0x25, 0x4f }, { 0x7b, 0x25, 80 }, { 0x7c, 0x25, 0x51 }, { 0x7d, 0x25, 0x52 }, { 0x7e, 0x25, 0x53 }, { 0x7f, 0x25, 0x54 }, { 0, 0x25, 0x55 }, { 0x40, 0x25, 0x56 }, 
            { 0x60, 0x25, 0x57 }, { 0x21, 0x2f, 0x41 }, { 0x22, 0x2f, 0x42 }, { 0x23, 0x2f, 0x43 }, { 0x26, 0x2f, 70 }, { 0x27, 0x2f, 0x47 }, { 40, 0x2f, 0x48 }, { 0x29, 0x2f, 0x49 }, { 0x2a, 0x2f, 0x4a }, { 0x2c, 0x2f, 0x4c }, { 0x3a, 0x2f, 90 }, { 0x61, 0x2b, 0x41 }, { 0x62, 0x2b, 0x42 }, { 0x63, 0x2b, 0x43 }, { 100, 0x2b, 0x44 }, { 0x65, 0x2b, 0x45 }, 
            { 0x66, 0x2b, 70 }, { 0x67, 0x2b, 0x47 }, { 0x68, 0x2b, 0x48 }, { 0x69, 0x2b, 0x49 }, { 0x6a, 0x2b, 0x4a }, { 0x6b, 0x2b, 0x4b }, { 0x6c, 0x2b, 0x4c }, { 0x6d, 0x2b, 0x4d }, { 110, 0x2b, 0x4e }, { 0x6f, 0x2b, 0x4f }, { 0x70, 0x2b, 80 }, { 0x71, 0x2b, 0x51 }, { 0x72, 0x2b, 0x52 }, { 0x73, 0x2b, 0x53 }, { 0x74, 0x2b, 0x54 }, { 0x75, 0x2b, 0x55 }, 
            { 0x76, 0x2b, 0x56 }, { 0x77, 0x2b, 0x57 }, { 120, 0x2b, 0x58 }, { 0x79, 0x2b, 0x59 }, { 0x7a, 0x2b, 90 }
         };
        #endregion
        #region 字段和属性



        private bool _checksum;
        private string _dataToEncode;
        private bool _humanReadable;
        private string _humanReadableFont;
        private float _humanReadableSize;
        private float _marginX;
        private float _marginY;
        private float _moduleHeight;
        private float _moduleWidth;
        private float _ratio;
        private float _reduction;
        private Color _codeBarColor = Color.Black;
        private bool _isDisplayCheckCode;
        private string _checkData;
        private bool _isDisplayStartStopSign;
        /// <summary>
        /// 是否检查效验
        /// </summary>
        public bool Checksum
        {
            get
            {
                return _checksum;
            }
            set
            {
                _checksum = value;
            }
        }


        /// <summary>
        /// 要进行编码的数据
        /// </summary>
        public string DataToEncode
        {
            get
            {
                return _dataToEncode;
            }
            set
            {
                _dataToEncode = value;
            }
        }



        /// <summary>
        /// 是否显示文本内容
        /// </summary>
        public bool HumanReadable
        {
            get
            {
                return _humanReadable;
            }
            set
            {
                _humanReadable = value;
            }
        }
        /// <summary>
        /// 用于显示文本内容的字体
        /// </summary>
        public string HumanReadableFont
        {
            get
            {
                return _humanReadableFont;
            }
            set
            {
                _humanReadableFont = value;
            }
        }
        /// <summary>
        /// 用于显示文本内容文字的代大小 
        /// </summary>
        public float HumanReadableSize
        {
            get
            {
                return _humanReadableSize;
            }
            set
            {
                _humanReadableSize = value;
            }
        }

        /// <summary>
        /// 水平方向边距
        /// 水平方向建议尽量留白
        /// 如果没有留白同时模块宽度较小可能会造成无法识别
        /// </summary>
        public float MarginX
        {
            get
            {
                return _marginX;
            }
            set
            {
                _marginX = value;
            }
        }
        /// <summary>
        /// 垂直方向边距
        /// </summary>
        public float MarginY
        {
            get
            {
                return _marginY;
            }
            set
            {
                _marginY = value;
            }
        }

        /// <summary>
        /// 模块高度(mm)
        /// </summary>
        public float ModuleHeight
        {
            get
            {
                return _moduleHeight;
            }
            set
            {
                _moduleHeight = value;
            }
        }

        /// <summary>
        /// 模块宽度(mm)
        /// 模块宽度不应低于0.2646f
        /// 模块宽度过低会造成数据丢失因而读不出数据或者会误读
        /// </summary>
        public float ModuleWidth
        {
            get
            {
                return _moduleWidth;
            }
            set
            {
                _moduleWidth = value;
            }
        }


        /// <summary>
        /// 放大比率 
        /// </summary>
        public float Ratio
        {
            get
            {
                return _ratio;
            }
            set
            {
                _ratio = value;
            }
        }
        /// <summary>
        /// 缩小
        /// </summary>
        public float Reduction
        {
            get
            {
                return _reduction;
            }
            set
            {
                _reduction = value;
            }
        }
        /// <summary>
        /// 设置条形码的颜色
        /// </summary>
        public Color CodeBarColor
        {
            get
            {
                return _codeBarColor;
            }
            set
            {
                _codeBarColor = value;
            }
        }

        /// <summary>
        /// 是否显示效验码
        /// 此属性要在Checksum属性为true的情况下有用
        /// </summary>
        public bool IsDisplayCheckCode
        {
            get { return this._isDisplayCheckCode; }
            set { this._isDisplayCheckCode = value; }
        }
        /// <summary>
        /// 供人识别是否显示起止符
        /// </summary>
        public bool IsDisplayStartStopSign
        {
            get { return this._isDisplayStartStopSign; }
            set { this._isDisplayStartStopSign = value; }
        }
        #endregion
        /// <summary>
        /// 默认构造函数
        /// 初始化
        /// </summary>
        public CSharpCode39()
        {
            this.initData();
            
        }
        public CSharpCode39(string dataToEncode)
        {
            this.initData();
            this._dataToEncode = dataToEncode;
        }
        /// <summary>
        /// 默认构造函数
        /// 初始化数据
        /// </summary>
        private void initData()
        {
            this._humanReadableFont = "Arial";
            this._humanReadableSize = 10f;
            this._codeBarColor = Color.Black;
            this._moduleHeight = 15f;//模块高度毫米
            this._moduleWidth = 0.35f;//模块宽度毫米
            this._ratio = 3f;
            this._marginX =2;
            this._marginY =2;
            this._checksum = true;
            this._isDisplayCheckCode = false;
            this._isDisplayStartStopSign = false;
        }
        private char[] _bitpattern_c39(string rawdata, ref int finalLength)
        {
            //0x27  39  
            //0x50  80
            if ((rawdata.Length == 0) || (rawdata.Length > 0x50 /*0x27*/))
            {
                return null;
            }
            for (int i = 0; i < rawdata.Length; i++)
            {
                if ((rawdata[i] == '\0') || (rawdata[i] > '\x007f'))
                {
                    return null;
                }
            }
            byte[] data = processTilde(rawdata);
            if (data.Length == 0)
            {
                return null;
            }
            byte[] buffer2 = this.processExtended(data);
            if ((buffer2.Length == 0) || (buffer2.Length > /*40*/80))
            {
                return null;
            }
            finalLength = this._checksum ? ((buffer2.Length + 2) + 1) : (buffer2.Length + 2);
            return this.getPattern_c39(buffer2);
        }


        /// <summary>
        /// 计算效验值
        /// </summary>
        /// <param name="data"></param>
        /// <param name="len"></param>
        /// <returns></returns>
        private byte _checksum_c39(byte[] data, int len)
        {
            //0x2b 43
            //字符值的总和除以合法字符集的个数43 取余数   余数在合法字符数组中对应的数值就是效验值
            int num2 = 0;
            for (int i = 1; i < len; i++)
            {
                num2 += this.valueFromCharacter(data[i]);
            }
            return this.c39_cw[num2 % 0x2b];
        }

        private char[] Code39_bitpattern(string dataToEncode)
        {
            int finalLength = 0;
            return this._bitpattern_c39(dataToEncode, ref finalLength);
        }
        /// <summary>
        /// 获得Code39条码图片
        /// </summary>
        /// <param name="resolution">DPI</param>
        /// <returns></returns>
        public Bitmap getBitmapImage(float resolution)
        {
           return Code39_createCode(resolution);
        }
       
        private Bitmap Code39_createCode(float resolution)
        {
            int num6;
            int finalLength = 0;
            char[] chArray = this._bitpattern_c39(DataToEncode, ref finalLength);
            if (chArray == null)
            {
                return null;
            }
            float fontsize = this._humanReadable ? (0.3527778f * this._humanReadableSize) : 0f;
            // float num3 = (7f * ModuleWidth) + ((3f * Ratio) * ModuleWidth);
            float num3 = (7f * this._moduleWidth) + ((3f * this._ratio) * this._moduleWidth);
            float width = (finalLength * num3) + (2f * this._marginX);
            float height = (this._moduleHeight + (2f * this._marginY)) + fontsize;
            width *= resolution / 25.4f;
            height *= resolution / 25.4f;
            Bitmap image = new Bitmap((int)width, (int)height, PixelFormat.Format32bppPArgb);
            image.SetResolution(resolution, resolution);
            //image.SetResolution(300, 300);
            Graphics g = Graphics.FromImage(image);
            g.Clear(Color.White);
            g.PageUnit = GraphicsUnit.Millimeter; //以毫米为度量单位
            g.FillRectangle(new SolidBrush(Color.White), new Rectangle(0, 0, /*(int)width*/image.Width, /*(int)height*/image.Height));
            //new Pen(Color.Black, 2f);
            //new SolidBrush(Color.White);
            SolidBrush brush = new SolidBrush(Color.Black);
            if (resolution < 300f)
            {
                //g.TextRenderingHint = TextRenderingHint.AntiAlias;
                //g.SmoothingMode = SmoothingMode.AntiAlias;
                g.CompositingQuality = CompositingQuality.HighQuality;
                //g.SmoothingMode = SmoothingMode.HighQuality;
                g.InterpolationMode = InterpolationMode.HighQualityBicubic;
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            }
            float num7 = 0f;
            for (num6 = 0; num6 < chArray.Length; num6++)
            {
                if (chArray[num6] == '0')
                {
                    if ((num6 & 1) != 1)
                    {
                        RectangleF rect = new RectangleF(MarginX + num7, MarginY, ModuleWidth, ModuleHeight);
                        MakeBar(g, rect, Reduction);
                    }
                    num7 += 1f * ModuleWidth;
                }
                else
                {
                    if ((num6 & 1) != 1)
                    {
                        RectangleF ef2 = new RectangleF(MarginX + num7, MarginY, Ratio * ModuleWidth, ModuleHeight);
                        MakeBar(g, ef2, Reduction);
                    }
                    num7 += Ratio * ModuleWidth;
                }
            }

            #region  供人识别内容
            if (this._humanReadable)
            {
                #region 保留
                /*byte[] buffer2 = processTilde(this._dataToEncode);
                int index = 0;
                List<byte> arr = new List<byte>();
                for (num6 = 0; num6 < buffer2.Length; num6++)
                {
                    //0x20 32      0x7e  126
                    if ((buffer2[num6] >= 0x20) && (buffer2[num6] <= 0x7e))
                    {
                        arr.Add(buffer2[num6]);
                    }
                }
                byte[] bytes = new byte[arr.Count];
                for (int i = 0; i < arr.Count; i++)
                {
                    bytes[i] = arr[i];
                }
                index = arr.Count;
                
                //string text = new ASCIIEncoding().GetString(bytes, 0, index);
                 */ 
                #endregion
                string text = this._dataToEncode;
                if (this._isDisplayCheckCode&&!string.IsNullOrEmpty(this._checkData)) {
                    text += this._checkData;
                }
                if (this._isDisplayStartStopSign)
                {
                    text = "*" + text + "*";
                }
                Font font = new Font(this._humanReadableFont, this._humanReadableSize);
                //g.DrawString(text, font, brush, new PointF(MarginX, MarginY + ModuleHeight));
                //新增字符串格式
                var drawFormat = new StringFormat { Alignment = StringAlignment.Center };
                float inpix = image.Width / resolution;//根据DPi求出 英寸数
                float widthmm = inpix * 25.4f;   //有每英寸像素求出毫米
                //g.DrawString(text, font, Brushes.Black, width / 2, height - 14, drawFormat);
                g.DrawString(text, font, /*Brushes.Black*/brush, new PointF(/*MarginX*/(int)(widthmm / 2), MarginY + ModuleHeight + 1), drawFormat);

            }

            #endregion



            return image;
        }

        /// <summary>
        /// 进行图形填充
        /// </summary>
        /// <param name="g"></param>
        /// <param name="rect"></param>
        /// <param name="reduction"></param>
        private void MakeBar(Graphics g, RectangleF rect, float reduction)
        {
            MakeBar(g, rect, reduction,this._codeBarColor);
        }

        /// <summary>
        /// 进行图形填充
        /// </summary>
        /// <param name="g"></param>
        /// <param name="rect"></param>
        /// <param name="reduction"></param>
        /// <param name="brushColor"></param>
        private void MakeBar(Graphics g, RectangleF rect, float reduction, Color brushColor)
        {
            float num = rect.Width * (reduction / 200f);
            float num2 = rect.Width - (rect.Width * (reduction / 200f));

            RectangleF ef = new RectangleF
            {
                X = rect.X + num,
                Y = rect.Y,
                Width = num2,
                Height = rect.Height
            };
            SolidBrush brush = new SolidBrush(brushColor);
            g.FillRectangle(brush, ef);

        }

        private char[] getPattern_c39(byte[] data)
        {   //0x2a  42为*
            //int num = 0x27;
            int num = 80;
            byte[] buffer = new byte[num + 1];
            buffer[0] = 0x2a;
            int index = 1;
            for (int i = 0; i < data.Length; i++)
            {
                buffer[index] = data[i];
                index++;
            }
            if (Checksum)
            {
                buffer[index] = this._checksum_c39(buffer, index);
                if (_isDisplayCheckCode)
                {
                    this._checkData = ((char)buffer[index]).ToString();
                }
                index++;
            }
            buffer[index] = 0x2a;
            index++;
            char[] chArray = new char[index * 10];
            int num5 = 0;
            for (int j = 0; j < index; j++)
            {
                byte c = buffer[j];
                int num9 = this.indexFromCharacter(c);
                for (int k = 0; k < 9; k++)
                {
                    chArray[num5] = (char)this.c39_bp[num9, k + 1];
                    num5++;
                }
                chArray[num5] = '0';
                num5++;
            }
            return chArray;
        }

        private int indexFromCharacter(byte c)
        {
            //0x2c==44
            for (int i = 0; i < 0x2c; i++)
            {
                if (this.c39_bp[i, 0] == c)
                {
                    return i;
                }
            }
            return -1;
        }


        private byte[] processExtended(byte[] data)
        {
            //0x25  38
            //0x4F  79 0x4E 78
            //int num = 0x4F;
            int num = data.Length - 1;
            byte[] sourceArray = new byte[num + 1];
            int index = 0;
            for (int i = 0; i < data.Length; i++)
            {
                byte c = data[i];
                if (this.valueFromCharacter(c) != -1)
                {
                    sourceArray[index] = c;
                    index++;
                }
                else
                {
                    byte num5 = 0;
                    byte num6 = 0;
                    if (this.valuesFromExtended(c, ref num5, ref num6))
                    {
                        sourceArray[index] = num5;
                        sourceArray[index + 1] = num6;
                        index += 2;
                    }
                }
            }
            byte[] destinationArray = new byte[index];
            Array.Copy(sourceArray, destinationArray, index);
            return destinationArray;
        }

        /// <summary>
        /// 返回指定字符在code39合法字符数组中对应的索引
        /// </summary>
        /// <param name="c"></param>
        /// <returns></returns>
        private int valueFromCharacter(byte c)
        {
            //c39_cw为数组，保存的为合法的字符集信息[0-9A-Z+-*/%. ] 共43个
            //如果存在这个字符就返回c39_cw对应的索引
            for (int i = 0; i < /*0x2b*/this.c39_cw.Length; i++)
            {
                if (this.c39_cw[i] == c)
                {
                    return i;
                }
            }
            return -1;
        }

        /// <summary>
        /// 判断字符集是否存在Extended
        /// </summary>
        /// <param name="c"></param>
        /// <param name="v1"></param>
        /// <param name="v2"></param>
        /// <returns></returns>
        private bool valuesFromExtended(byte c, ref byte v1, ref byte v2)
        {
            //0x55  85
            for (int i = 0; i < 0x55; i++)
            {
                if (this.c39_ex[i, 0] == c)
                {
                    v1 = this.c39_ex[i, 1];
                    v2 = this.c39_ex[i, 2];
                    return true;
                }
            }
            return false;
        }

        private byte[] processTilde(string rawdata)
        {
            byte[] sourceArray = new byte[rawdata.Length];
            int index = 0;
            for (int i = 0; i < rawdata.Length; i++)
            {
                if (rawdata[i] != '~')
                {
                    sourceArray[index] = (byte)rawdata[i];
                    index++;
                }
                else if ((i + 3) < rawdata.Length)
                {
                    string str = new string(new char[] { rawdata[i + 1], rawdata[i + 2], rawdata[i + 3] });
                    int num3 = Convert.ToInt32(str, 10);
                    if ((num3 > 0) && (num3 <= 0xff))
                    {
                        sourceArray[index] = (byte)num3;
                        index++;
                    }
                    if (num3 == 0x3e7)
                    {
                        sourceArray[index] = 0x86;
                        index++;
                    }
                    i += 3;
                }
                else
                {
                    sourceArray[index] = (byte)rawdata[i];
                    index++;
                }
            }
            byte[] destinationArray = new byte[index];
            Array.Copy(sourceArray, destinationArray, index);
            return destinationArray;
        }
    }
}
