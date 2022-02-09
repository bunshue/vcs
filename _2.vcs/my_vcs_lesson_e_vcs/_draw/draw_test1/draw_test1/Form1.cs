using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Reflection;    //PropertyInfo

namespace draw_test1
{
    public partial class Form1 : Form
    {
        public Point pt_st = new Point(0, 0);  //鼠標第一點 
        public Point pt_sp = new Point(0, 0);  //鼠標第二點 
        public bool flag_mouse_down = false;   //是否開始畫矩形 

        /// <summary>
        /// 在 picturebox1 上畫矩形
        /// </summary>
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = this.pictureBox1.CreateGraphics();
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0+50);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //餅圖
            Draw_PieDiagram();
        }

        //畫餅圖
        void Draw_PieDiagram()
        {
            Bitmap bmp = new Bitmap(400, 300);	//創建一個長度為400，寬帶為400的Bitmap實例
            Graphics g;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Snow);
            string[] sitem = { "很好", "好", "一般", "差" };
            int[] num = { 1000, 69, 90, 20 };
            int cnt, i, len;
            float s;
            float[] nflt;
            string header;
            header = "";
            cnt = 0;
            s = 0;
            len = num.Length;
            //nflt.Length = len;
            nflt = new float[len];
            for (i = 0; i < len; i++)
            {
                cnt += num[i];
            }
            //flt = cnt /len;
            for (i = 0; i < len; i++)
            {
                nflt[i] = 360 * num[i] / cnt;
            }

            header = "調查統計結果一覽圖";
            g.DrawString(header, new Font("宋體", 12, FontStyle.Bold), Brushes.Black, new Point(75, 10));
            g.DrawString("單位：次", new Font("宋體", 9), Brushes.Black, new Point(300, 25));

            Point myRec = new Point(300, 40);
            Point myDec = new Point(320, 40);


            for (i = 0; i < len; i++)
            {
                if (i == len - 1)
                {
                    //s = 360-s;
                    nflt[i] = 360 - s;
                }

                g.DrawRectangle(Pens.Black, myRec.X, myRec.Y, 20, 10);
                //繪制小方塊
                g.FillRectangle(new SolidBrush(Return_Color(i)), myRec.X, myRec.Y, 20, 10);
                //填充小方塊
                g.DrawString(" " + sitem[i] + " " + num[i], new Font("宋體", 9), Brushes.Black, myDec);
                //繪制小方塊右邊的文字
                myRec.Y += 15;
                myDec.Y += 15;

                g.FillPie(new SolidBrush(Return_Color(i)), 50, 50, 200, 200, s, nflt[i]);
                g.DrawPie(Pens.Black, 50, 50, 200, 200, s, nflt[i]);
                s = s + nflt[i];
            }
            Pen p = new Pen(Color.Black, 1);
            g.DrawRectangle(p, 1, 1, 398, 298);
            //bmp.Save ( Response.OutputStream , System.Drawing.Imaging.ImageFormat.Jpeg);

            pictureBox1.Image = bmp;
        }

        public Color Return_Color(int i)
        {
            switch (i)
            {
                case 0:
                    return Color.Red;
                //break;
                case 1:
                    return Color.Blue;
                //break;
                case 2:
                    return Color.Yellow;
                case 3:
                    return Color.Green;
                //break;
                case 4:
                    return Color.Pink;
                //break;
                case 5:
                    return Color.Plum;
                //break;
                case 6:
                    return Color.Gray;
                //break;
                case 7:
                    return Color.Salmon;
                //break;
                case 8:
                    return Color.RosyBrown;
                //break;
                case 9:
                    return Color.Teal;
                //break;
                case 10:
                    return Color.Orange;
                //break;
                case 11:
                    return Color.Thistle;
                //break;
                case 12:
                    return Color.Maroon;
                //break;
                default:
                    return Color.WhiteSmoke;
                //break;

            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //棒圖
            Draw_BarDiagram();
        }

        //畫棒圖
        void Draw_BarDiagram()
        {
            //創建一個長度為400，寬帶為400的Bitmap實例
            Bitmap bmp = new Bitmap(400, 300);
            Graphics g;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Snow);
            string[] sitem = { "很好", "好", "一般", "差" };
            int[] num = { 1000, 69, 90, 2000 };
            int cnt, i, len, iBarWidth;
            float scale;
            float[] nflt;
            string header;
            header = "";
            cnt = 0;
            iBarWidth = 40;
            scale = 1;
            len = num.Length;
            //nflt.Length = len;
            nflt = new float[len];
            for (i = 0; i < len; i++)
            {
                cnt += num[i];
            }
            //flt = cnt /len;
            for (i = 0; i < len; i++)
            {
                nflt[i] = 200 * num[i] / cnt;
                //nflt[i] = scale * num[i]/cnt;
            }

            header = "調查統計結果一覽圖";
            g.DrawString(header, new Font("宋體", 12, FontStyle.Bold), Brushes.Black, new Point(75, 10));
            Point myRec = new Point(300, 40);
            Point myDec = new Point(320, 40);

            for (i = 0; i < len; i++)
            {
                g.DrawRectangle(Pens.Black, myRec.X, myRec.Y, 20, 10);
                //繪制小方塊
                g.FillRectangle(new SolidBrush(Return_Color(i)), myRec.X, myRec.Y, 20, 10);
                //填充小方塊
                g.DrawString(" " + sitem[i], new Font("宋體", 9), Brushes.Black, myDec);
                //繪制小方塊右邊的文字
                myRec.Y += 15;
                myDec.Y += 15;

                g.DrawRectangle(Pens.Black, (i * iBarWidth) + 15, 290 - (nflt[i] * scale), 20, (nflt[i] * scale) + 5);
                //繪制Bar圖
                g.FillRectangle(new SolidBrush(Return_Color(i)), (i * iBarWidth) + 15, 290 - (nflt[i] * scale), 20, (nflt[i] * scale) + 5);
                //以指定的色彩填充Bar圖
                g.DrawString(num[i].ToString(), new Font("宋體", 9), Brushes.Black, (i * iBarWidth) + 20, 275 - (nflt[i] * scale));
                //顯示Bar圖代表的數據

                //s = s + nflt[i];   
            }
            Pen p = new Pen(Color.Black, 1);
            g.DrawRectangle(p, 1, 1, 398, 298);
            //bmp.Save ( Response.OutputStream , System.Drawing.Imaging.ImageFormat.Jpeg);
            //bmp.Dispose();

            pictureBox1.Image = bmp;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //太極圖
            int imgWidth = 400; //圖象尺寸
            int eyeRadius = imgWidth / 20; //魚眼半徑
            int headDiameter = imgWidth / 2; //魚頭直徑

            Bitmap image = new Bitmap(imgWidth, imgWidth);
            image.SetResolution(300, 300);

            Graphics g = Graphics.FromImage(image);

            //設置圖像質量
            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;


            //底色填充為白色
            Brush white = new SolidBrush(Color.White);
            g.FillRectangle(white, new Rectangle(0, 0, imgWidth, imgWidth));

            Brush blue = new SolidBrush(Color.Blue);//定義藍色筆刷
            Brush red = new SolidBrush(Color.Red);//定義紅色筆刷

            //整個圓形填充藍色
            g.FillPie(blue, 0, 0, imgWidth, imgWidth, 0, 360);

            //定義右邊的路徑（紅色部分）
            GraphicsPath redPath = new GraphicsPath();//初始化路徑
            redPath.AddArc(0, 0, imgWidth, imgWidth, 0, -180);
            redPath.AddArc(0, headDiameter / 2, headDiameter, headDiameter, 0, -180);
            redPath.AddArc(headDiameter, headDiameter / 2, headDiameter, headDiameter, 0, 180);
            //填充右邊部分
            g.FillPath(red, redPath);
            //填充紅色眼睛
            g.FillPie(red, new Rectangle(headDiameter / 2 - eyeRadius, headDiameter - eyeRadius, eyeRadius * 2, eyeRadius * 2), 0, 360);
            //填充藍色眼睛
            g.FillPie(blue, new Rectangle(headDiameter + headDiameter / 2 - eyeRadius, headDiameter - eyeRadius, eyeRadius * 2, eyeRadius * 2), 0, 360);

            g.Dispose();
            pictureBox1.Image = image;

            //使用指定參數輸出
            //image.Save(Response.OutputStream, myImageCodecInfo, myEncoderParameters);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //生成Color類所有static預定義成員的顏色表
            //生成Color類所有static預定義成員的顏色表
            const long CELLS_PER_LINE = 10;

            const float MARGIN = 12;
            const float CELL_WIDTH = 160;
            const float CELL_HEIGHT = 64;
            const float COLOR_LEFT_MARGIN = 8;
            const float COLOR_TOP_MARGIN = 8;
            const float COLOR_CELL_WIDTH = 48;
            const float COLOR_CELL_HEIGHT = 32;
            const float TEXT_TOP_MARGIN = COLOR_TOP_MARGIN + COLOR_CELL_HEIGHT + 2;

            List<Color> vColors = new List<Color>();
            Type t = typeof(Color);
            PropertyInfo[] vProps = t.GetProperties();
            foreach (PropertyInfo propInfo in vProps)
            {
                if (MemberTypes.Property == propInfo.MemberType &&
                    typeof(Color) == propInfo.PropertyType)
                {
                    Color tmpColor = (Color)propInfo.GetValue(null, null);
                    vColors.Add(tmpColor);
                }
            }

            Bitmap bmpColor = new Bitmap((int)(CELLS_PER_LINE * CELL_WIDTH + MARGIN * 2), (int)((vColors.Count / CELLS_PER_LINE + 1) * CELL_HEIGHT + MARGIN * 2));
            using (Graphics grp = Graphics.FromImage(bmpColor))
            {
                grp.Clear(Color.Black);

                for (int i = 0; i < vColors.Count; i++)
                {
                    float nLeftBase = MARGIN + i % CELLS_PER_LINE * CELL_WIDTH;
                    float nTopBase = MARGIN + i / CELLS_PER_LINE * CELL_HEIGHT;

                    grp.DrawRectangle(new Pen(Color.White), nLeftBase, nTopBase, CELL_WIDTH, CELL_HEIGHT);

                    grp.FillRectangle(new SolidBrush(vColors[i]),
                                      nLeftBase + COLOR_LEFT_MARGIN, nTopBase + COLOR_TOP_MARGIN,
                                      COLOR_CELL_WIDTH, COLOR_CELL_HEIGHT);

                    grp.DrawString(vColors[i].Name,
                                   new Font("宋體", 9, FontStyle.Regular),
                                   new SolidBrush(Color.White),
                                   nLeftBase + COLOR_LEFT_MARGIN, nTopBase + TEXT_TOP_MARGIN);
                }
            }
            bmpColor.Save("AllColor.bmp");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //顯示豎排文字1
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawString("顯示橫排", new Font("標楷體", 20, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline), Brushes.Red, 10, 200);
            //設置旋轉中心點
            g.TranslateTransform(W / 2, H / 2);
            //設置旋轉角度
            g.RotateTransform(90);
            //畫文字
            g.DrawString("顯示豎排文字", new Font("標楷體", 20), new SolidBrush(Color.Black), 0, 0);
            //平移
            g.TranslateTransform(100, 100);
            //畫文字
            g.DrawString("平移後顯示豎排文字", new Font("標楷體", 20), new SolidBrush(Color.Black), 0, 0);
            //恢復為默認場景
            g.ResetTransform();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //顯示豎排文字2
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawString("顯示豎排文字", new Font("標楷體", 20), new SolidBrush(Color.Black), 0, 0, new StringFormat(StringFormatFlags.DirectionVertical));
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //坐標系畫圖（C#）示例

            //數據初始化   
            string[] month = new string[12] { "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月" };
            float[] d = new float[12] { 20.5F, 60, 10.8F, 15.6F, 30, 70.9F, 50.3F, 30.7F, 70, 50.4F, 30.8F, 20 };
            //畫圖初始化   
            Bitmap bMap = new Bitmap(500, 500);
            Graphics gph = Graphics.FromImage(bMap);
            gph.Clear(Color.White);

            PointF cPt = new PointF(40, 420);//中心點
            PointF[] xPt = new PointF[3] { new PointF(cPt.Y + 15, cPt.Y), new PointF(cPt.Y, cPt.Y - 8), new PointF(cPt.Y, cPt.Y + 8) };//X軸三角形
            PointF[] yPt = new PointF[3] { new PointF(cPt.X, cPt.X - 15), new PointF(cPt.X - 8, cPt.X), new PointF(cPt.X + 8, cPt.X) };//Y軸三角形
            gph.DrawString("某工廠某產品月生產量圖表", new Font("宋體", 14), Brushes.Black, new PointF(cPt.X + 60, cPt.X));//圖表標題
            //畫X軸
            gph.DrawLine(Pens.Black, cPt.X, cPt.Y, cPt.Y, cPt.Y);
            gph.DrawPolygon(Pens.Black, xPt);
            gph.FillPolygon(new SolidBrush(Color.Black), xPt);
            gph.DrawString("月份", new Font("宋體", 12), Brushes.Black, new PointF(cPt.Y + 10, cPt.Y + 10));
            //畫Y軸
            gph.DrawLine(Pens.Black, cPt.X, cPt.Y, cPt.X, cPt.X);
            gph.DrawPolygon(Pens.Black, yPt);
            gph.FillPolygon(new SolidBrush(Color.Black), yPt);
            gph.DrawString("單位(萬)", new Font("宋體", 12), Brushes.Black, new PointF(0, 7));
            for (int i = 1; i <= 12; i++)
            {
                //畫Y軸刻度
                if (i < 11)
                {
                    gph.DrawString((i * 10).ToString(), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X - 30, cPt.Y - i * 30 - 6));
                    gph.DrawLine(Pens.Black, cPt.X - 3, cPt.Y - i * 30, cPt.X, cPt.Y - i * 30);
                }
                //畫X軸項目
                gph.DrawString(month[i - 1].Substring(0, 1), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30 - 5, cPt.Y + 5));
                gph.DrawString(month[i - 1].Substring(1, 1), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30 - 5, cPt.Y + 20));
                if (month[i - 1].Length > 2) gph.DrawString(month[i - 1].Substring(2, 1), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30 - 5, cPt.Y + 35));
                //畫點
                gph.DrawEllipse(Pens.Black, cPt.X + i * 30 - 1.5F, cPt.Y - d[i - 1] * 3 - 1.5F, 3, 3);
                gph.FillEllipse(new SolidBrush(Color.Black), cPt.X + i * 30 - 1.5F, cPt.Y - d[i - 1] * 3 - 1.5F, 3, 3);
                //畫數值
                gph.DrawString(d[i - 1].ToString(), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30, cPt.Y - d[i - 1] * 3));
                //畫折線
                if (i > 1) gph.DrawLine(Pens.Red, cPt.X + (i - 1) * 30, cPt.Y - d[i - 2] * 3, cPt.X + i * 30, cPt.Y - d[i - 1] * 3);
            }
            //儲存輸出圖片
            //bMap.Save(Response.OutputStream, ImageFormat.Gif);

            pictureBox1.Image = bMap;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //this.Hide();//隱藏當前窗體
            Thread.Sleep(50);//讓線程睡眠一段時間，窗體消失需要一點時間
            Catch CatchForm = new Catch();
            Bitmap CatchBmp = new Bitmap(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height);//新建一個和屏幕大小相同的圖片
            Graphics g = Graphics.FromImage(CatchBmp);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height));//保存全屏圖片
            CatchForm.BackgroundImage = CatchBmp;//將Catch窗體的背景設為全屏時的圖片
            if (CatchForm.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "CatchForm OK\n";
                //如果Catch窗體結束,就將剪貼板中的圖片放到信息發送框中
                IDataObject iData = Clipboard.GetDataObject();
                DataFormats.Format myFormat = DataFormats.GetFormat(DataFormats.Bitmap);
                if (iData.GetDataPresent(DataFormats.Bitmap))
                {
                    richTextBox1.Paste(myFormat);
                    Clipboard.Clear();//清除剪貼板中的對象
                }

                //this.Show();//重新顯示窗體
            }
            else
            {
                richTextBox1.Text += "CatchForm Cancel\n";
            }
        }

        /// <summary>
        /// 在 pictureBox1 上按下鼠標事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            pt_st = new Point(e.X, e.Y);
        }

        /// <summary>
        /// 在 pictureBox1 上鼠標移動開始繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                //清除 pictureBox1 繪圖面,相當於刷新了一次窗體界面然後重新繪制
                g.Clear(this.BackColor);
                //獲取新的右下角坐標 
                pt_sp = new Point(e.X, e.Y);
                //獲取兩個數中的大者或小者
                int minX = Math.Min(pt_st.X, pt_sp.X);
                int minY = Math.Min(pt_st.Y, pt_sp.Y);
                int maxX = Math.Max(pt_st.X, pt_sp.X);
                int maxY = Math.Max(pt_st.Y, pt_sp.Y);

                //畫矩形
                g.DrawRectangle(new Pen(Color.Red), minX, minY, maxX - minX, maxY - minY);
                //ControlPaint.DrawReversibleFrame(new Rectangle(minX, minY, maxX - minX, maxY - minY),this.BackColor,FrameStyle.Dashed);
            }
        }

        /// <summary>
        /// 鼠標放開停止繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }
    }
}

