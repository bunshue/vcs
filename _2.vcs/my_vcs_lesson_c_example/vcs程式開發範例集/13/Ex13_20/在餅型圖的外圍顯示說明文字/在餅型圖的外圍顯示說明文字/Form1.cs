using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 在餅型圖的外圍顯示說明文字
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public static string[] XText = new string[7] { "商品1", "商品2", "商品3", "商品4", "商品5", "商品6", "商品7" };//儲存數據的名稱數組
        public static float[] SzData = new float[7] { 5F, 17F, 7F, 2F, 10F, 5F, 4F };//取得每列的和
        public static Color[] WearColor = new Color[] { Color.Red,Color.Gold,Color.Chartreuse,Color.Teal,Color.RoyalBlue,Color.Fuchsia,Color.Firebrick,
            Color.Goldenrod,Color.ForestGreen,Color.Aqua,Color.Blue,Color.PaleVioletRed,Color.Salmon,Color.Yellow,Color.LimeGreen,Color.LightBlue,Color.LightSteelBlue,Color.MediumPurple};
        public static string[] AreaText;//臨時儲存數據的名稱數組
        Pen mypen;
        float AreaAngle = 0F;
        public static float XSize = 50;//X軸的大小
        public static float YSize = 50;//Y軸的大小
        public static float ASum=50;//記錄餅形的總和
        public static float TemXSize = 0;//X軸的臨時大小
        public static float XLeft = 0;//X軸的左端點
        public static float XRight = 0;//X軸的右端點
        public static float YUp = 0;//Y軸的上端點
        public static float YDown = 50;//Y軸的下端點
        public static SolidBrush mybrush = new SolidBrush(Color.Red);
        public static float Aline = 20;//標識文字的前端線長
        public static float Asash = 3;//標識文字名邊框的寬度
        public static float temXLeft = 0;//X軸的左端點初始化

        #region 繪製餅形圖(Area)
        public static float AreaXMaxWidth = 0;//取得字串的寬度
        public static float AreaXMaxHeight = 0;//取得字串的高度
        //取得餅形圖的標識文字
        public void AreaValue()
        {
            string temTextSize = "";//儲存最長的名稱
            Font LSfont = new System.Drawing.Font("細明體", 8);//設定說明文字的字體
            AreaText = new string[XText.Length];//實例化一個臨時數組
            for (int i = 0; i < AreaText.Length; i++)//取得名稱
            {
                AreaText[i] = XText[i];
            }
            float AresF = 0;//記錄百分比
            for (int i = 0; i < AreaText.Length; i++)//透過名稱及百分比,組合說明文字
            {
                AresF = (SzData[i] / ASum) * 100;//取得目前記錄的百分比
                AresF = (float)Math.Round(AresF, 3);//對百分比進行四捨五入
                AreaText[i] = AreaText[i] + " " + AresF.ToString() + "%";//組合說明文字
                if (AreaText[i].Length > temTextSize.Length)//取得最長的說明文件
                    temTextSize = AreaText[i];
            }
            Graphics TitG = this.CreateGraphics();//建立Graphics類對像
            SizeF XMaxSize = TitG.MeasureString(temTextSize + Asash * 2, LSfont);//將繪製的字串進行格式化
            AreaXMaxWidth = XMaxSize.Width;//取得字串的寬度
            AreaXMaxHeight = XMaxSize.Height;//取得字串的高度
        }

        //繪製餅形圖表
        public void ProtractArea(Graphics g)
        {
            AreaValue();//計算最長說明文字的大小
            //初始化變數
            mypen = new Pen(Color.Black, 1);//設定畫筆的顏色及大小
            float f = 0;//記錄百分比
            float TimeNum = 0;//扇形的繪製度數
            float AXLeft = 0;//設定餅形圖的X座標
            float AYUp = 0;//設定餅形圖的Y座標
            float AXSize = 0;//設定餅形圖的寬度
            float AYSize = 0;//設定餅形圖的高度
            float Atop = 0;//記錄餅形的高度為長和寬的最小值
            float Aleft = 0;//記錄餅形的高度為長和寬的最小值
            TimeNum = AreaAngle;//設定餅形圖的起始度數
            //計算餅形圖的初始位置
            XLeft = panel1.Width - (panel1.Width - 5);//去了邊框後餅形圖的X位置
            XSize = panel1.Width - 10;//設定餅形圖的寬度
            temXLeft = AXLeft;//記錄餅形圖的X座標
            AXLeft = XLeft;//記錄餅形圖的X座標
            AXSize = XSize;//記錄餅形圖的寬度

            //透過說明文字的大小計算餅形圖的位置
            AXLeft = AXLeft + AreaXMaxWidth + Aline;//設定去除說明文字後的餅形圖X座標
            AYUp = AYUp + AreaXMaxHeight;//設定去除說明文字後的餅形圖Y座標
            AXSize = XSize - AreaXMaxWidth * 2 - Aline * 2;//設定去除說明文字後的餅形圖寬度
            AYSize = YSize - AreaXMaxHeight * 2;//設定去除說明文字後的餅形圖高度
            if (AXSize >= AYSize)//如果餅形圖的寬度大於等於高度
            {
                Aleft = AXSize - AYSize;//記錄餅形圖的X座標
                AXSize = AYSize;//將高度設為寬度
            }
            else
            {
                Atop = AYSize - AXSize;//記錄餅形圖的Y座標
                AYSize = AXSize;//將寬度設為高度
            }
            if (Aleft != 0)//如果寬大於高
            {
                AXLeft = AXLeft + Aleft / 2;//設定餅形圖橫向局中
            }
            if (Atop != 0)//如果高大於寬
            {
                AYUp = AYUp + Atop / 2;//設定餅形圖縱向局中
            }
            temXLeft = XLeft;
            //繪製餅形圖
            if (AXSize > 0 && AYSize > 0)//如果餅形圖的寬和高大於0
            {
                for (int i = 0; i < SzData.Length; i++)//搜尋數據
                {
                    f = SzData[i] / ASum;//取得目前數據的百分比
                    //設定目前扇形圖的填充顏色
                    if (i >= WearColor.Length)//如果沒有超出顏色數組
                        mybrush = new SolidBrush(WearColor[i - WearColor.Length]);
                    else
                        mybrush = new SolidBrush(WearColor[i]);
                    g.FillPie(mybrush, AXLeft, AYUp, AXSize, AYSize, TimeNum, f * 360);//繪製扇形圖
                    TimeNum += f * 360;//設定下一個扇形圖的度數
                }
                ProAreaSign(g);//繪製餅形圖的說明文字
            }
            else
                return;
        }
        #endregion

        #region 繪製餅形圖標識(Area)
        public void ProAreaSign(Graphics g)
        {
            AreaValue();//儲存最長的名稱
            mypen = new Pen(Color.Black, 1);//設定畫筆的顏色及大小
            Font LSfont = new System.Drawing.Font("細明體", 8);//設定說明文字的字體樣式
            SolidBrush Zbrush = new SolidBrush(Color.Black);//設定存放說明文字邊框的畫刷
            SolidBrush ATbrush = new SolidBrush(Color.Khaki);//設定存放說明文字方塊的背景畫刷
            //初始化變數
            float f = 0;//記錄百分比
            float TimeNum = 0;//扇形的繪製度數
            float AXLeft = 0;//設定餅形圖的X座標
            float AYUp = 0;//設定餅形圖的Y座標
            float AXSize = 0;//設定餅形圖的寬度
            float AYSize = 0;//設定餅形圖的高度
            float Atop = 0;//記錄餅形的高度為長和寬的最小值
            float Aleft = 0;//記錄餅形的高度為長和寬的最小值
            Graphics TitG = panel1.CreateGraphics();//建立Graphics類對像
            SizeF XMaxSize = TitG.MeasureString("", LSfont);//將繪製的字串進行格式化
            float SWidth = 0;//取得字串的寬度
            float SHeight = 0;//取得字串的高度
            //計算餅形圖的初始位置
            XLeft = panel1.Width - (panel1.Width - 5);//去了邊框後餅形圖的X位置
            XSize = panel1.Width - 10;//設定餅形圖的寬度
            temXLeft = AXLeft;//記錄餅形圖的X座標
            AXLeft = XLeft;//記錄餅形圖的X座標
            AXSize = XSize;//記錄餅形圖的寬度
            //透過說明文字的大小計算餅形圖的位置
            AXLeft = AXLeft + AreaXMaxWidth + Aline;//設定去除說明文字後的餅形圖X座標
            AYUp = AYUp + AreaXMaxHeight;//設定去除說明文字後的餅形圖Y座標
            AXSize = XSize - AreaXMaxWidth * 2 - Aline * 2;//設定去除說明文字後的餅形圖寬度
            AYSize = YSize - AreaXMaxHeight * 2;//設定去除說明文字後的餅形圖高度
            if (AXSize >= AYSize)//如果餅形圖的寬度大於等於高度
            {
                Aleft = AXSize - AYSize;//記錄餅形圖的X座標
                AXSize = AYSize;//將高度設為寬度
            }
            else
            {
                Atop = AYSize - AXSize;//記錄餅形圖的Y座標
                AYSize = AXSize;//將寬度設為高度
            }
            if (Aleft != 0)//如果寬大於高
            {
                AXLeft = AXLeft + Aleft / 2;//設定餅形圖橫向局中
            }
            if (Atop != 0)//如果高大於寬
            {
                AYUp = AYUp + Atop / 2;//設定餅形圖縱向局中
            }
            temXLeft = XLeft;
            //初始化說明文字前橫線的變數
            float X1 = 0;
            float Y1 = 0;
            float X2 = 0;
            float Y2 = 0;
            //初始化說明文字位置的變數
            float TX1 = 0;
            float TY1 = 0;
            float TX2 = 0;
            float TY2 = 0;
            float temf = 0;//記錄百分比
            double radians = 0;//記錄扇形的角度
            temf = (this.AreaAngle * (ASum / 360) / ASum);//記錄起始位置的度數
            TimeNum = this.AreaAngle;//記錄扇形的起始角度
            //繪製說明文字
            if (AXSize > 0 && AYSize > 0)
            {
                for (int i = 0; i < SzData.Length; i++)//搜尋所有說明文字
                {
                    f = SzData[i] / ASum;//取得目前記錄的百分比
                    if (f == 0)//如果目前值為0
                        continue;//執行下一次循環
                    radians = ((double)((temf + f / 2) * 360) * Math.PI) / (double)180;
                    X1 = Convert.ToSingle(AXLeft + (AXSize / 2.0 + (int)((float)(AXSize / 2.0) * Math.Cos(radians))));
                    Y1 = Convert.ToSingle(AYUp + (AYSize / 2.0 + (int)((float)(AYSize / 2.0) * Math.Sin(radians))));

                    XMaxSize = TitG.MeasureString(AreaText[i].Trim(), LSfont);//將繪製的字串進行格式化
                    SWidth = XMaxSize.Width;//取得字串的寬度
                    SHeight = XMaxSize.Height;//取得字串的高度
                    if ((temf + f / 2) * 360 > 90 && (temf + f / 2) * 360 <= 270)
                    {
                        X2 = X1 - Aline;

                        TX1 = X2 - 1 - SWidth;
                        TY1 = Y1 - SHeight / 2 - Asash;
                        TX2 = SWidth;
                        TY2 = SHeight + Asash * 2;
                        g.FillRectangle(ATbrush, TX1, TY1, TX2, TY2);//繪製內矩形
                        g.DrawRectangle(new Pen(Color.Black, 1), TX1, TY1, TX2, TY2);//繪製矩形
                        g.DrawString(AreaText[i].Trim(), LSfont, Zbrush, new PointF(X2 - SWidth + Asash - 1, Y1 - SHeight / 2));
                    }
                    else
                    {
                        X2 = X1 + Aline;

                        TX1 = X2 + 1;
                        TY1 = Y1 - SHeight / 2 - Asash;
                        TX2 = SWidth;
                        TY2 = SHeight + Asash * 2;
                        g.FillRectangle(ATbrush, TX1, TY1, TX2, TY2);//繪製內矩形
                        g.DrawRectangle(new Pen(Color.Black, 1), TX1, TY1, TX2, TY2);//繪製矩形
                        g.DrawString(AreaText[i].Trim(), LSfont, Zbrush, new PointF(X2 + Asash + 1, Y1 - SHeight / 2));
                    }
                    Y2 = Y1;
                    g.DrawLine(new Pen(new SolidBrush(Color.Black), 1), X1, Y1, X2, Y2);
                    TimeNum += f * 360;
                    temf = temf + f;
                }
            }
            else
                return;
        }
        #endregion

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            XSize = panel1.Width;//X軸的大小
            YSize = panel1.Height;//Y軸的大小
            YDown = panel1.Height;//Y軸的下端點
            ProtractArea(e.Graphics);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
