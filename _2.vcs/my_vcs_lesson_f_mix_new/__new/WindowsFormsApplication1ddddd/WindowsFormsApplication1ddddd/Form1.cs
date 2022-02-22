using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace WindowsFormsApplication1ddddd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //畫曲線圖

            Curve2D cuv2D = new Curve2D();

            cuv2D.Fit();
            Bitmap bitmap1 = cuv2D.CreateImage();
            pictureBox1.Image = bitmap1;
        }
    }

    public class Curve2D
    {
        private Graphics objGraphics; //Graphics 類提供將對象繪制到顯示設備的方法
        private Bitmap objBitmap; //位圖對象
        private float fltWidth = 480; //圖像寬度
        private float fltHeight = 248; //圖像高度
        private float fltXSlice = 50; //X軸刻度寬度
        private float fltYSlice = 50; //Y軸刻度寬度
        private float fltYSliceValue = 20; //Y軸刻度的數值寬度
        private float fltYSliceBegin = 0; //Y軸刻度開始值
        private float fltTension = 0.5f;
        private string strTitle = "曲線圖"; //標題
        private string strXAxisText = "月份"; //X軸說明文字
        private string strYAxisText = "萬元"; //Y軸說明文字
        private string[] strsKeys = new string[] { "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月" }; //鍵
        private float[] fltsValues = new float[] { 20.0f, 30.0f, 50.0f, 55.4f, 21.6f, 12.8f, 99.5f, 36.4f, 78.2f, 56.4f, 45.8f, 66.5f, 99.5f, 36.4f, 78.2f, 56.4f, 45.8f, 66.5f, 20.0f, 30.0f, 50.0f, 55.4f, 21.6f, 12.8f }; //值
        private Color clrBgColor = Color.Snow; //背景色
        private Color clrTextColor = Color.Black; //文字顏色
        private Color clrBorderColor = Color.Black; //整體邊框顏色
        private Color clrAxisColor = Color.Black; //軸線顏色
        private Color clrAxisTextColor = Color.Black; //軸說明文字顏色
        private Color clrSliceTextColor = Color.Black; //刻度文字顏色
        private Color clrSliceColor = Color.Black; //刻度顏色
        private Color[] clrsCurveColors = new Color[] { Color.Red, Color.Blue }; //曲線顏色
        private float fltXSpace = 100f; //圖像左右距離邊緣距離
        private float fltYSpace = 100f; //圖像上下距離邊緣距離
        private int intFontSize = 9; //字體大小號數
        private float fltXRotateAngle = 30f; //X軸文字旋轉角度
        private float fltYRotateAngle = 0f; //Y軸文字旋轉角度
        private int intCurveSize = 2; //曲線線條大小
        private int intFontSpace = 0; //intFontSpace 是字體大小和距離調整出來的一個比較適合的數字
        #region 公共屬性
        /// <summary>

        /// 圖像的寬度
        /// </summary>
        public float Width
        {
            set
            {
                if (value < 100)
                {
                    fltWidth = 100;
                }
                else
                {
                    fltWidth = value;
                }
            }
            get
            {
                if (fltWidth <= 100)
                {
                    return 100;
                }
                else
                {
                    return fltWidth;
                }
            }
        }
        /// <summary>
        /// 圖像的高度
        /// </summary>
        public float Height
        {
            set
            {
                if (value < 100)
                {
                    fltHeight = 100;
                }
                else
                {
                    fltHeight = value;
                }
            }
            get
            {
                if (fltHeight <= 100)
                {
                    return 100;
                }
                else
                {
                    return fltHeight;
                }
            }
        }

        /// <summary>
        /// X軸刻度寬度
        /// </summary>
        public float XSlice
        {
            set { fltXSlice = value; }
            get { return fltXSlice; }
        }
        /// <summary>
        /// Y軸刻度寬度
        /// </summary>
        public float YSlice
        {
            set { fltYSlice = value; }
            get { return fltYSlice; }
        }

        /// <summary>
        /// Y軸刻度的數值寬度
        /// </summary>


        public float YSliceValue
        {
            set { fltYSliceValue = value; }
            get { return fltYSliceValue; }
        }
        /// <summary>
        /// Y軸刻度開始值
        /// </summary>
        public float YSliceBegin
        {
            set { fltYSliceBegin = value; }
            get { return fltYSliceBegin; }
        }
        /// <summary>
        /// 張力系數
        /// </summary>
        public float Tension
        {
            set
            {
                if (value < 0.0f && value > 1.0f)
                {
                    fltTension = 0.5f;
                }
                else
                {
                    fltTension = value;
                }
            }
            get
            {
                return fltTension;
            }
        }
        /// <summary>
        /// 標題
        /// </summary>
        public string Title
        {
            set { strTitle = value; }
            get { return strTitle; }
        }
        /// <summary>
        /// 鍵，X軸數據
        /// </summary>
        public string[] Keys
        {
            set
            {
                strsKeys = value;
            }
            get { return strsKeys; }
        }
        /// <summary>
        /// 值，Y軸數據
        /// </summary>
        public float[] Values
        {
            set { fltsValues = value; }
            get
            {
                return fltsValues;
            }
        }
        /// <summary>
        /// 背景色
        /// </summary>
        public Color BgColor
        {
            set
            {
                clrBgColor = value;
            }
            get { return clrBgColor; }
        }
        /// <summary>
        /// 文字顏色
        /// </summary>
        public Color TextColor
        {
            set { clrTextColor = value; }
            get { return clrTextColor; }
        }
        /// <summary>
        /// 整體邊框顏色
        /// </summary>
        public Color BorderColor
        {
            set { clrBorderColor = value; }
            get { return clrBorderColor; }
        }
        /// <summary>
        /// 軸線顏色
        /// </summary>
        public Color AxisColor
        {
            set
            {
                clrAxisColor = value;
            }
            get { return clrAxisColor; }
        }

        /// <summary>
        /// X軸說明文字
        /// </summary>
        public string XAxisText
        {
            set { strXAxisText = value; }
            get { return strXAxisText; }
        }
        /// <summary>
        /// Y軸說明文字
        /// </summary>
        public string YAxisText
        {
            set { strYAxisText = value; }
            get { return strYAxisText; }
        }
        /// <summary>
        /// 軸說明文字顏色
        /// </summary>
        public Color AxisTextColor
        {
            set
            {
                clrAxisTextColor = value;
            }
            get { return clrAxisTextColor; }
        }
        /// <summary>
        /// 刻度文字顏色
        /// </summary>
        public Color SliceTextColor
        {
            set
            {
                clrSliceTextColor = value;
            }
            get { return clrSliceTextColor; }
        }
        /// <summary>
        /// 刻度顏色
        /// </summary>
        public Color SliceColor
        {
            set { clrSliceColor = value; }
            get { return clrSliceColor; }
        }
        /// <summary>
        /// 曲線顏色
        /// </summary>
        public Color[] CurveColors
        {
            set { clrsCurveColors = value; }
            get
            {
                return clrsCurveColors;
            }
        }
        /// <summary>
        /// X軸文字旋轉角度
        /// </summary>
        public float XRotateAngle
        {
            get { return fltXRotateAngle; }
            set { fltXRotateAngle = value; }
        }
        /// <summary>
        /// Y軸文字旋轉角度
        /// </summary>
        public float YRotateAngle
        {
            get
            {
                return fltYRotateAngle;
            }
            set { fltYRotateAngle = value; }
        }

        /// <summary>
        /// 圖像左右距離邊緣距離
        /// </summary>
        public float XSpace
        {
            get
            {
                return fltXSpace;
            }
            set { fltXSpace = value; }
        }

        /// <summary>
        /// 圖像上下距離邊緣距離
        /// </summary>
        public float YSpace
        {
            get { return fltYSpace; }
            set { fltYSpace = value; }
        }
        /// <summary>
        /// 字體大小號數
        /// </summary>
        public int FontSize
        {
            get { return intFontSize; }
            set { intFontSize = value; }
        }

        /// <summary>
        /// 曲線線條大小
        /// </summary>
        public int CurveSize
        {
            get
            {
                return intCurveSize;
            }
            set { intCurveSize = value; }
        }

        #endregion
        /// <summary>
        /// 自動根據參數調整圖像大小
        /// </summary>
        public void Fit()
        {
            //計算字體距離
            intFontSpace = FontSize + 5;
            //計算圖像邊距

            float fltSpace = Math.Min(Width / 6, Height / 6);
            XSpace = fltSpace;
            YSpace = fltSpace;
            //計算X軸刻度寬度
            XSlice = (Width - 2 * XSpace) / (Keys.Length - 1);
            //計算Y軸刻度寬度和Y軸刻度開始值
            float fltMinValue = 0;
            float fltMaxValue = 0;
            for (int i = 0; i < Values.Length; i++)
            {
                if (Values[i] < fltMinValue)
                {
                    fltMinValue = Values[i];
                }
                else if (Values[i] > fltMaxValue)
                {
                    fltMaxValue = Values[i];
                }
            }

            if (YSliceBegin > fltMinValue)
            {
                YSliceBegin = fltMinValue;
            }
            int intYSliceCount = (int)(fltMaxValue / YSliceValue);
            if (fltMaxValue % YSliceValue != 0)
            {
                intYSliceCount++;
            }
            YSlice = (Height - 2 * YSpace) / intYSliceCount;
        }

        /// <summary>
        /// 生成圖像並返回bmp圖像對象
        /// </summary>
        /// <returns></returns>
        public Bitmap CreateImage()
        {
            InitializeGraph();

            int intKeysCount = Keys.Length;
            int intValuesCount = Values.Length;

            if (intValuesCount % intKeysCount == 0)
            {
                int intCurvesCount = intValuesCount / intKeysCount;
                for (int i = 0; i < intCurvesCount; i++)
                {
                    float[] fltCurrentValues = new float[intKeysCount];
                    for (int j = 0; j < intKeysCount; j++)
                    {
                        fltCurrentValues[j] = Values[i * intKeysCount + j];
                    }
                    DrawContent(ref objGraphics, fltCurrentValues, clrsCurveColors[i]);
                }
            }
            else
            {
                objGraphics.DrawString("發生錯誤，Values的長度必須是Keys的整數倍!", new Font("宋體", FontSize + 5), new SolidBrush(TextColor), new Point((int)XSpace, (int)(Height / 2)));
            }
            return objBitmap;
        }

        /// <summary>
        /// 初始化和填充圖像區域，畫出邊框，初始標題
        /// </summary>
        private void InitializeGraph()
        {
            //根據給定的高度和寬度創建一個位圖圖像
            objBitmap = new Bitmap((int)Width, (int)Height);
            //從指定的 objBitmap 對象創建 objGraphics 對象 (即在objBitmap對象中畫圖)
            objGraphics = Graphics.FromImage(objBitmap);
            //根據給定顏色(LightGray)填充圖像的矩形區域 (背景)
            objGraphics.DrawRectangle(new Pen(BorderColor, 1), 0, 0, Width - 1, Height - 1); //畫邊框
            objGraphics.FillRectangle(new SolidBrush(BgColor), 1, 1, Width - 2, Height - 2); //填充邊框
            //畫X軸,注意圖像的原始X軸和Y軸計算是以左上角為原點，向右和向下計算的
            float fltX1 = XSpace;
            float fltY1 = Height - YSpace;
            float fltX2 = Width - XSpace + XSlice / 2;
            float fltY2 = fltY1;
            objGraphics.DrawLine(new Pen(new SolidBrush(AxisColor), 1), fltX1, fltY1, fltX2, fltY2);
            //畫Y軸
            fltX1 = XSpace;
            fltY1 = Height - YSpace;
            fltX2 = XSpace;

            fltY2 = YSpace - YSlice / 2;
            objGraphics.DrawLine(new Pen(new SolidBrush(AxisColor), 1), fltX1, fltY1, fltX2, fltY2);
            //初始化軸線說明文字

            SetAxisText(ref objGraphics);
            //初始化X軸上的刻度和文字

            SetXAxis(ref objGraphics);
            //初始化Y軸上的刻度和文字
            SetYAxis(ref objGraphics);
            //初始化標題
            CreateTitle(ref objGraphics);
        }

        /// <summary>
        /// 初始化軸線說明文字
        /// </summary>
        /// <param name="objGraphics"></param>
        private void SetAxisText(ref Graphics objGraphics)
        {
            float fltX = Width - XSpace + XSlice / 2 - (XAxisText.Length - 1) * intFontSpace;
            float fltY = Height - YSpace - intFontSpace;
            objGraphics.DrawString(XAxisText, new Font("宋體", FontSize), new SolidBrush(AxisTextColor), fltX, fltY);
            fltX = XSpace + 5;
            fltY = YSpace - YSlice / 2 - intFontSpace;
            for (int i = 0; i < YAxisText.Length; i++)
            {
                objGraphics.DrawString(YAxisText[i].ToString(), new Font("宋體", FontSize), new SolidBrush(AxisTextColor), fltX, fltY);
                fltY += intFontSpace; //字體上下距離
            }
        }

        /// <summary>
        /// 初始化X軸上的刻度和文字
        /// </summary>
        /// <param name="objGraphics"></param>

        private void SetXAxis(ref Graphics objGraphics)
        {
            float fltX1 = XSpace;
            float fltY1 = Height - YSpace;
            float fltX2 = XSpace;
            float fltY2 = Height - YSpace;
            int iCount = 0;
            int iSliceCount = 1;
            float Scale = 0;
            float iWidth = ((Width - 2 * XSpace) / XSlice) * 50; //將要畫刻度的長度分段，並乘以50，以10為單位畫刻度線。
            float fltSliceHeight = XSlice / 10; //刻度線的高度
            objGraphics.TranslateTransform(fltX1, fltY1); //平移圖像(原點)
            objGraphics.RotateTransform(XRotateAngle, MatrixOrder.Prepend); //旋轉圖像
            objGraphics.DrawString(Keys[0].ToString(), new Font("宋體", FontSize), new
            SolidBrush(SliceTextColor), 0, 0);
            objGraphics.ResetTransform(); //重置圖像

            for (int i = 0; i <= iWidth; i += 10) //以10為單位
            {
                Scale = i * XSlice / 50;//即(i / 10) * (XSlice / 5)，將每個刻度分五部分畫，但因為i以10為單位，得除以10
                if (iCount == 5)
                {
                    objGraphics.DrawLine(new Pen(new SolidBrush(AxisColor)), fltX1 + Scale, fltY1 + fltSliceHeight * 1.5f, fltX2 + Scale, fltY2 - fltSliceHeight * 1.5f);

                    //畫網格虛線
                    Pen penDashed = new Pen(new SolidBrush(AxisColor));

                    penDashed.DashStyle = DashStyle.Dash;


                    objGraphics.DrawLine(penDashed, fltX1 + Scale, fltY1, fltX2 + Scale, YSpace - YSlice / 2);
                    //這裡顯示X軸刻度
                    if (iSliceCount <= Keys.Length - 1)
                    {
                        objGraphics.TranslateTransform(fltX1 + Scale, fltY1);
                        objGraphics.RotateTransform(XRotateAngle, MatrixOrder.Prepend);
                        objGraphics.DrawString(Keys[iSliceCount].ToString(), new Font("宋體", FontSize), new SolidBrush(SliceTextColor), 0, 0);
                        objGraphics.ResetTransform();
                    }
                    else
                    {
                        //超過范圍，不畫任何刻度文字
                    }
                    iCount = 0;
                    iSliceCount++;

                    if (fltX1 + Scale > Width - XSpace)
                    {
                        break;
                    }
                }
                else
                {
                    objGraphics.DrawLine(new Pen(new SolidBrush(SliceColor)), fltX1 + Scale, fltY1 + fltSliceHeight, fltX2 + Scale, fltY2 - fltSliceHeight);
                }
                iCount++;
            }
        }
        /// <summary>
        /// 初始化Y軸上的刻度和文字
        /// </summary>
        /// <param name="objGraphics"></param>
        private void SetYAxis(ref Graphics objGraphics)
        {
            float fltX1 = XSpace;
            float fltY1 = Height - YSpace;
            float fltX2 = XSpace;
            float fltY2 = Height - YSpace;
            int iCount = 0;
            float Scale = 0;
            int iSliceCount = 1;
            float iHeight = ((Height - 2 * YSpace) / YSlice) * 50; //將要畫刻度的長度分段，並乘以50，以10為單位畫刻度線。
            float fltSliceWidth = YSlice / 10; //刻度線的寬度
            string strSliceText = string.Empty;
            objGraphics.TranslateTransform(XSpace - intFontSpace * YSliceBegin.ToString().Length, Height - YSpace); //平移圖像(原點)
            objGraphics.RotateTransform(YRotateAngle, MatrixOrder.Prepend); //旋轉圖像
            objGraphics.DrawString(YSliceBegin.ToString(), new Font("宋體", FontSize), new SolidBrush(SliceTextColor), 0, 0);
            objGraphics.ResetTransform(); //重置圖像

            for (int i = 0; i < iHeight; i += 10)
            {
                Scale = i * YSlice / 50; //即(i / 10) * (YSlice / 5)，將每個刻度分五部分畫，但因為i以10為單位，得除以10
                if (iCount == 5)
                {
                    objGraphics.DrawLine(new Pen(new SolidBrush(AxisColor)), fltX1 - fltSliceWidth * 1.5f, fltY1 - Scale, fltX2 + fltSliceWidth * 1.5f, fltY2 - Scale);
                    //畫網格虛線

                    Pen penDashed = new Pen(new SolidBrush(AxisColor));

                    penDashed.DashStyle = DashStyle.Dash;
                    objGraphics.DrawLine(penDashed, XSpace, fltY1 - Scale, Width - XSpace + XSlice / 2, fltY2 - Scale);

                    //這裡顯示Y軸刻度
                    strSliceText = Convert.ToString(YSliceValue * iSliceCount + YSliceBegin);

                    objGraphics.TranslateTransform(XSpace - intFontSize * strSliceText.Length, fltY1 - Scale);

                    //平移圖像(原點)
                    objGraphics.RotateTransform(YRotateAngle, MatrixOrder.Prepend); //旋轉圖像
                    objGraphics.DrawString(strSliceText, new Font("宋體", FontSize), new SolidBrush(SliceTextColor), 0, 0);

                    objGraphics.ResetTransform(); //重置圖像
                    iCount = 0;
                    iSliceCount++;
                }
                else
                {
                    objGraphics.DrawLine(new Pen(new SolidBrush(SliceColor)), fltX1 - fltSliceWidth, fltY1 - Scale, fltX2 + fltSliceWidth, fltY2 - Scale);
                }
                iCount++;
            }
        }

        /// <summary>
        /// 畫曲線
        /// </summary>
        /// <param name="objGraphics"></param>
        private void DrawContent(ref Graphics objGraphics, float[] fltCurrentValues, Color clrCurrentColor)
        {
            Pen CurvePen = new Pen(clrCurrentColor, CurveSize);
            PointF[] CurvePointF = new PointF[Keys.Length];
            float keys = 0;
            float values = 0;
            for (int i = 0; i < Keys.Length; i++)
            {
                keys = XSlice * i + XSpace;
                values = (Height - YSpace) + YSliceBegin - YSlice * (fltCurrentValues[i] / YSliceValue);
                CurvePointF[i] = new PointF(keys, values);
            }
            objGraphics.DrawCurve(CurvePen, CurvePointF, Tension);
        }
        /// <summary>
        /// 初始化標題
        /// </summary>
        /// <param name="objGraphics"></param>
        private void CreateTitle(ref Graphics objGraphics)
        {
            objGraphics.DrawString(Title, new Font("宋體", FontSize), new SolidBrush(TextColor), new Point((int)(Width - XSpace) - intFontSize * Title.Length, (int)(YSpace - YSlice / 2 - intFontSpace)));

        }
    }
}

