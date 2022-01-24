using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

using System.Collections;   //for ArrayList
namespace draw_test4_romeo
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Bitmap sinImage = new Bitmap(360, 120);
            Graphics myGraphics = Graphics.FromImage(sinImage);
            myGraphics.Clear(Color.White);
            myGraphics.SmoothingMode = SmoothingMode.AntiAlias;
            Rectangle r1 = new Rectangle(0, 0, 360, 20);
            Rectangle r2 = new Rectangle(0, 20, 360, 40);
            Rectangle r3 = new Rectangle(0, 60, 360, 40);
            Rectangle r4 = new Rectangle(0, 100, 360, 20);

            Brush brush1 = new SolidBrush(Color.OrangeRed);
            Brush brush2 = new SolidBrush(Color.SkyBlue);
            Brush brush3 = new SolidBrush(Color.Pink);
            Brush brush4 = new SolidBrush(Color.YellowGreen);

            myGraphics.FillRectangle(brush1, r1);
            myGraphics.FillRectangle(brush2, r2);
            myGraphics.FillRectangle(brush2, r3);
            myGraphics.FillRectangle(brush1, r4);

            myGraphics.DrawString("0", new Font("宋體", 8), brush1, new PointF(3, 65));
            myGraphics.DrawString("90", new Font("宋體", 8), brush1, new PointF(85, 65));
            myGraphics.DrawString("180", new Font("宋體", 8), brush1, new PointF(170, 65));
            myGraphics.DrawString("360", new Font("宋體", 8), brush1, new PointF(336, 65));

            Point myPoint = new Point(0, 60);

            float sinValue = 0.0F;

            for (int i = 0; i < 360; i++)
            {
                sinValue = Convert.ToSingle(Math.Sin(Convert.ToSingle((i * Math.PI) / 180))) * 40;
                //事實上，這裡根本無需注意 sinValue 的正負
                //當其為負時，  60-sinValue 則會變大
                Point thisPoint = new Point(i, Convert.ToInt32(60 - sinValue));
                myGraphics.DrawLine(new Pen(brush3), thisPoint, myPoint);
                myPoint = thisPoint;
            }
            pictureBox1.Image = sinImage;
        }

        private void button1_Click(object sender, EventArgs e)
        {



            //第一步，定義一下各個結點的內容以及結點數量等初始信息
            string parentTree = "中國";
            ArrayList midTree = new ArrayList();
            midTree.Add("江蘇省");
            midTree.Add("山東省");
            int midTreeCount = midTree.Count;
            ArrayList subTree = new ArrayList();
            subTree.Add("南京市");
            subTree.Add("揚州市");
            subTree.Add("蘇州市");
            subTree.Add("青島市");
            subTree.Add("日照市");
            int subTreeCount = subTree.Count;
            ArrayList eachSubTreeCount = new ArrayList();
            eachSubTreeCount.Add(3);
            eachSubTreeCount.Add(2);

            //定義一些畫圖需要的初始變量

            int midCountFlag = 0;   //畫中間結點時用到的偏移量 
            int subCountFlag = 0;   //畫頂層結點時用到的偏移量 
            int x = 0;              //結點矩形圖左上角X坐標 
            int y = 0;              //結點矩形圖左上角Y坐標 
            int picX = pictureBox1.Width;   //繪圖區域水平長度 
            int picY = pictureBox1.Height;  //繪圖區域豎直長度 
            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Center;
            Rectangle rect;         //結點矩形圖 
            Point loc;              //結點矩形圖左上角坐標 
            Point startP;           //連接線起始坐標 
            Point endP;             //連接線終止坐標 
            Point tempP = new Point();   //坐標緩存量 
            SizeF sizeF;            //結點內容尺寸大小 
            Size s;
            Font font = new Font("宋體", 18);     //結點內容的字體 
            Pen redPen = new Pen(Color.Red, 2);   //連線需要的畫筆 
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);         //每次重繪先把繪圖區域清空 

            //OK，這時我們就可以開始畫了，先把根部畫出來。

            #region  畫樹根
            sizeF = g.MeasureString(parentTree, font);
            sizeF.Width += 10;
            s = sizeF.ToSize();

            x = Convert.ToInt32((picX - sizeF.Width) / 2);
            y = 30;
            startP = new Point(picX / 2, y + s.Height);
            loc = new Point(x, y);

            rect = new Rectangle(loc, s);
            g.DrawRectangle(Pens.Black, rect);
            g.DrawString(parentTree, font, Brushes.Black, rect, sf);
            #endregion

            //再把樹根的子樹畫出來。

            #region  畫子樹
            foreach (object o in midTree)
            {
                int picXMid = picX / midTreeCount;

                string strMidTree = o.ToString();
                sizeF = g.MeasureString(strMidTree, font);
                sizeF.Width += 10;
                s = sizeF.ToSize();

                x = Convert.ToInt32((picXMid - sizeF.Width) / 2 + picXMid * midCountFlag);
                y = 230;
                endP = new Point(picXMid / 2 + picXMid * midCountFlag, y);
                loc = new Point(x, y);

                rect = new Rectangle(loc, s);
                g.DrawRectangle(Pens.Black, rect);
                g.DrawString(strMidTree, font, Brushes.Black, rect, sf);
                g.DrawLine(redPen, startP, endP);

                midCountFlag++;
                if (midCountFlag == 1)
                    tempP = new Point(endP.X, endP.Y + s.Height);
            }
            #endregion

            //畫出子樹的樹枝。

            #region  畫子樹的樹枝

            startP = tempP;

            for (int i = 0; i != midTree.Count; ++i)
            {
                int picXMid = picX / midTreeCount;
                startP.X += picXMid * i;
                if (i >= 1)
                    subCountFlag += (int)eachSubTreeCount[i - 1];
                for (int j = 0; j != (int)eachSubTreeCount[i]; ++j)
                {

                    int picXSub = picX / (midTreeCount * (int)eachSubTreeCount[i]);

                    string strSubTree = subTree[j + subCountFlag].ToString();
                    sizeF = g.MeasureString(strSubTree, font);
                    sizeF.Width += 10;
                    s = sizeF.ToSize();

                    x = Convert.ToInt32(((picXSub - sizeF.Width) / 2 + picXSub * j) + picXMid * i);
                    y = 430;
                    endP = new Point(picXSub / 2 + picXSub * j + picXMid * i, y);
                    loc = new Point(x, y);

                    rect = new Rectangle(loc, s);
                    g.DrawRectangle(Pens.Black, rect);
                    g.DrawString(strSubTree, font, Brushes.Black, rect, sf);
                    g.DrawLine(redPen, startP, endP);
                }
            }
            #endregion 






        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

    }
}
