using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Struct
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
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);


            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // 定義Product產品結構資料型別
        struct Product
        {
            // Product產品結構內含No編號欄位、Name品名欄位、Price單價欄位
            public string No, Name;
            public int Price;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //struct用法
            // 宣告game結構變數為Product結構型別
            Product game;
            // 設定game.No編號欄位的值為 "G01"
            game.No = "G01";
            // 設定game.Name品名欄位的值為"XBox One"
            game.Name = "XBox One";
            // 設定game.Price單價欄位的值為10000
            game.Price = 10000;

            Product cookie;        // 宣告cookie結構變數為Product結構型別
            cookie.No = "A123";
            cookie.Name = "LION_MOUSE";
            cookie.Price = 1234;
            richTextBox1.Text += "====== 產品單價清單 ======\n";
            // 印出game及cookie結構的編號、品名及單價
            richTextBox1.Text += "產品編號： " + game.No + "\n";
            richTextBox1.Text += "產品名稱： " + game.Name + "\n";
            richTextBox1.Text += "產品單價： " + game.Price + "\n";
            richTextBox1.Text += "產品編號： " + cookie.No + "\n";
            richTextBox1.Text += "產品名稱： " + cookie.Name + "\n";
            richTextBox1.Text += "產品單價： " + cookie.Price + "\n";

        }

        struct circle
        {
            public float cRadius;
            public string cColor;
        }
        struct wheel
        {
            public circle circle1;
            public string usage;
        };

        private void button1_Click(object sender, EventArgs e)
        {
            //巢狀自訂型態
            wheel wheel1;
            wheel1.circle1.cRadius = 50;
            wheel1.circle1.cColor = "黑色";
            wheel1.usage = "汽車";
            richTextBox1.Text += "輪胎半徑：" + wheel1.circle1.cRadius + "\n";
            richTextBox1.Text += "輪胎顏色：" + wheel1.circle1.cColor + "\n";
            richTextBox1.Text += "輪胎用途：" + wheel1.usage + "\n";

        }

        //結構與結構陣列的用法 ST
        struct Ball  // 結構
        {
            public Point pt;
            public Color color;
        }
        Random rd = new Random(); // 亂數
        List<Ball> ballList = new List<Ball>(); // 動態陣列

        private void button2_Click(object sender, EventArgs e)
        {
            //結構與結構陣列的用法
            int i;
            //richTextBox1.Clear();
            richTextBox1.Text += "清除結構陣列\n";
            ballList.Clear();
            this.Invalidate();

            Ball aBall;

            richTextBox1.Text += "加入3個紅球\n";

            for (i = 0; i < 3; i++)
            {
                aBall.pt = new Point(rd.Next(20, this.ClientSize.Width - 20), rd.Next(40, this.ClientSize.Height - 20));
                aBall.color = Color.Red;
                ballList.Add(aBall);
                this.Invalidate();
            }

            richTextBox1.Text += "加入5個綠球\n";

            for (i = 0; i < 5; i++)
            {
                aBall.pt = new Point(rd.Next(20, this.ClientSize.Width - 20), rd.Next(40, this.ClientSize.Height - 20));
                aBall.color = Color.Green;
                ballList.Add(aBall);
                this.Invalidate();
            }

            richTextBox1.Text += "看結構陣列內所有資料\n";
            i = 0;
            foreach (Ball b in ballList)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 個, 位置 : " + b.pt.ToString() + ", 顏色 : " + b.color.ToString() + "\n";
                i++;

                //把圓球畫出來
                //e.Graphics.FillEllipse(new SolidBrush(b.color), b.pt.X - 10, b.pt.Y - 10, 20, 20);
                //e.Graphics.DrawEllipse(Pens.Black, b.pt.X - 10, b.pt.Y - 10, 20, 20);
            }
        }
        //結構與結構陣列的用法 SP

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
    }
}
