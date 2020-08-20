using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality

using System.Drawing.Imaging;   //for ImageFormat


namespace vcs_Draw9_Example
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.Red);             //useless??
            pictureBox1.BackColor = Color.Pink;
            show_item_location();

            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.BackColor = Color.Pink;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 850;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            cb_manual.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            cb_snake.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            cb_magnifying.Location = new Point(x_st + dx * 2, y_st + dy * 7 + dy / 2);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            button22.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
        }

        void show_item_location2()
        {
            pictureBox2.Visible = false;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            this.Size = new Size(1700, 900);
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1250;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            cb_manual.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            cb_snake.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            cb_magnifying.Location = new Point(x_st + dx * 2, y_st + dy * 7 + dy / 2);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            button22.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //Bitmap bmp;
            //SolidBrush brush;
            //Pen p;

            float ratio_x, ratio_y;
            float w, h;
            float x0, x1, y0, y1;

            //----畫筆顏色----
            p = new Pen(Color.Black);
            sb = new SolidBrush(p.Color);
            //----取得picturebox寬度與高度----
            w = pictureBox1.Width;
            h = pictureBox1.Height;
            //----是否有上一次的圖片，如果有就清除----
            if (pictureBox1.Image != null)
                pictureBox1.Image = null;
            //if (bitmap1 != null)
            //  bitmap1.Dispose();
            //----轉換使用者輸入的資料----
            x0 = (float)10;
            y0 = (float)10;
            x1 = (float)-5;
            y1 = (float)-9;
            //----計算放大倍率----
            ratio_x = (w - 50) / 20;
            ratio_y = (h - 50) / 20;
            //----開新的Bitmap----
            bitmap1 = new Bitmap((int)w, (int)h);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);
            //----清除Bitmap為某顏色----
            g.Clear(Color.White);
            //----更改原點位置----
            g.TranslateTransform(pictureBox1.Width / 2, pictureBox1.Height / 2);
            //----畫坐標軸----
            g.DrawLine(p, -1000, 0, 1000, 0);//x軸
            g.DrawLine(p, 0, -1000, 0, 1000);//y軸
            g.DrawString("X", this.Font, sb, w / 2 - 20, 20);
            g.DrawString("Y", this.Font, sb, 20, -h / 2);
            g.DrawLine(p, w / 2, 0, w / 2 - 10, 5);//x軸箭頭
            g.DrawLine(p, w / 2, 0, w / 2 - 10, -5);
            g.DrawLine(p, 0, -h / 2, 5, -h / 2 + 10);//y軸箭頭
            g.DrawLine(p, 0, -h / 2, -5, -h / 2 + 10);
            for (int i = -10; i <= 10; i++)//畫X Y軸座標位置
            {
                g.DrawLine(p, i * ratio_x, -5, i * ratio_x, 5);
                g.DrawString(i.ToString().PadLeft(2, ' '), this.Font, sb, i * ratio_x - 9, 10);
                g.DrawLine(p, -5, i * ratio_y, 5, i * ratio_y);
                if (i != 0)
                    g.DrawString(i.ToString(), this.Font, sb, 15, i * ratio_y - 8);
            }
            //----換顏色----
            p = new Pen(Color.Red);
            sb = new SolidBrush(p.Color);
            //----畫線----
            g.DrawLine(p, x0 * ratio_x, -y0 * ratio_y, x1 * ratio_x, -y1 * ratio_y);
            //----畫兩點----
            g.FillEllipse(sb, new RectangleF(x0 * ratio_x - 2.5f, -y0 * ratio_y - 2.5f, 5, 5));
            g.FillEllipse(sb, new RectangleF(x1 * ratio_x - 2.5f, -y1 * ratio_y - 2.5f, 5, 5));
            //----釋放Graphics資源----
            //g.Dispose();
            //----將Bitmap顯示在Picture上
            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int center_x = 300;
            int center_y = 300;
            int radius = 200;
            DrawPacman(center_x, center_y, radius);
        }

        private void DrawPacman(int center_x, int center_y, int radius)
        {
            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();

            // Create a new brush.
            Brush brush = new SolidBrush(Color.Blue);

            try
            {
                g.FillPie(brush, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2), 320, -280);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

            //Dispose of the brush.
            brush.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //同心圓
            g.DrawString("這是一組同心圓", this.Font, Brushes.Black, 10, 20);
            Pen p1 = new Pen(Color.Red);
            Pen p2 = new Pen(Color.Purple);
            Pen p3 = new Pen(Color.Blue);
            Pen p4 = new Pen(Color.Green);
            g.DrawEllipse(p1, 120 - 80, 120 - 80, 80 * 2, 80 * 2);
            g.DrawEllipse(p2, 120 - 60, 120 - 60, 60 * 2, 60 * 2);
            g.DrawEllipse(p3, 120 - 40, 120 - 40, 40 * 2, 40 * 2);
            g.DrawEllipse(p4, 120 - 20, 120 - 20, 20 * 2, 20 * 2);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 50 + i, 500, 50 + i);
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Pen p = new Pen(Color.Black, 8);
            p.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(p, 50, 400, 50, 100);  //畫出X軸及y軸
            g.DrawLine(p, 50, 400, 350, 400);

            p = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            //pp.DashStyle = DashStyle.Dot; //DashStyle設定線條 點
            //pp.StartCap = LineCap.RoundAnchor; //設定為圓頭

            p.EndCap = LineCap.ArrowAnchor;

            //gg.DrawLine(pp, 50, 50, 250, 250);//只畫一條
            g.DrawLines(p, new Point[]
            {//一次畫好多條
            new Point(70,350),
            new Point(100,280),
            new Point(120,300),
            new Point(200,220),
            new Point(250,260),
            new Point(340,150)
            }
            );
        }

        private void button5_Click(object sender, EventArgs e)
        {
            draw_grid();
        }

        public void draw_grid()
        {
            int i;
            p = new Pen(Color.Navy, 1);
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Brush bb = new SolidBrush(Color.Orange);
            g.FillRectangle(bb, 70, 70, 200, 100);  //畫出一個填滿的方框

            Pen p = new Pen(Color.Black, 4);
            g.DrawRectangle(p, 70, 70, 200, 100);
            //在同樣起點畫出黑色的長方型線，即實現加外框            

            Random rr = new Random();
            Brush db;
            for (int i = 1; i <= 7; i++)
            {
                db = new SolidBrush(Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256)));
                //Color.FromArgb() 可以設定3原色，這裡3原色的代碼是亂數產生的

                g.FillRectangle(db, 70 + (i * 40), 70 + (i * 40), 200, 100);
                //畫布上畫出方框，每次位置的X及Y值都加70，以實現往右下角移動
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            int[,] gray = new int[31, 23];

            gray[0, 0] = 8;
            gray[1, 0] = 7;
            gray[2, 0] = 8;
            gray[3, 0] = 10;
            gray[4, 0] = 27;
            gray[5, 0] = 85;
            gray[6, 0] = 126;
            gray[7, 0] = 134;
            gray[8, 0] = 138;
            gray[9, 0] = 140;
            gray[10, 0] = 142;
            gray[11, 0] = 143;
            gray[12, 0] = 144;
            gray[13, 0] = 144;
            gray[14, 0] = 146;
            gray[15, 0] = 146;
            gray[16, 0] = 146;
            gray[17, 0] = 146;
            gray[18, 0] = 145;
            gray[19, 0] = 144;
            gray[20, 0] = 141;
            gray[21, 0] = 140;
            gray[22, 0] = 138;
            gray[23, 0] = 135;
            gray[24, 0] = 130;
            gray[25, 0] = 98;
            gray[26, 0] = 28;
            gray[27, 0] = 9;
            gray[28, 0] = 7;
            gray[29, 0] = 8;
            gray[30, 0] = 9;
            gray[0, 1] = 7;
            gray[1, 1] = 8;
            gray[2, 1] = 11;
            gray[3, 1] = 36;
            gray[4, 1] = 105;
            gray[5, 1] = 130;
            gray[6, 1] = 135;
            gray[7, 1] = 139;
            gray[8, 1] = 142;
            gray[9, 1] = 144;
            gray[10, 1] = 146;
            gray[11, 1] = 147;
            gray[12, 1] = 149;
            gray[13, 1] = 150;
            gray[14, 1] = 151;
            gray[15, 1] = 151;
            gray[16, 1] = 151;
            gray[17, 1] = 150;
            gray[18, 1] = 149;
            gray[19, 1] = 148;
            gray[20, 1] = 146;
            gray[21, 1] = 144;
            gray[22, 1] = 142;
            gray[23, 1] = 139;
            gray[24, 1] = 136;
            gray[25, 1] = 131;
            gray[26, 1] = 96;
            gray[27, 1] = 25;
            gray[28, 1] = 9;
            gray[29, 1] = 7;
            gray[30, 1] = 8;
            gray[0, 2] = 7;
            gray[1, 2] = 9;
            gray[2, 2] = 31;
            gray[3, 2] = 107;
            gray[4, 2] = 130;
            gray[5, 2] = 135;
            gray[6, 2] = 139;
            gray[7, 2] = 143;
            gray[8, 2] = 145;
            gray[9, 2] = 148;
            gray[10, 2] = 150;
            gray[11, 2] = 151;
            gray[12, 2] = 153;
            gray[13, 2] = 154;
            gray[14, 2] = 155;
            gray[15, 2] = 155;
            gray[16, 2] = 155;
            gray[17, 2] = 154;
            gray[18, 2] = 154;
            gray[19, 2] = 152;
            gray[20, 2] = 150;
            gray[21, 2] = 149;
            gray[22, 2] = 147;
            gray[23, 2] = 144;
            gray[24, 2] = 140;
            gray[25, 2] = 136;
            gray[26, 2] = 130;
            gray[27, 2] = 92;
            gray[28, 2] = 26;
            gray[29, 2] = 9;
            gray[30, 2] = 7;
            gray[0, 3] = 8;
            gray[1, 3] = 18;
            gray[2, 3] = 91;
            gray[3, 3] = 127;
            gray[4, 3] = 134;
            gray[5, 3] = 139;
            gray[6, 3] = 142;
            gray[7, 3] = 145;
            gray[8, 3] = 148;
            gray[9, 3] = 151;
            gray[10, 3] = 153;
            gray[11, 3] = 154;
            gray[12, 3] = 156;
            gray[13, 3] = 157;
            gray[14, 3] = 158;
            gray[15, 3] = 157;
            gray[16, 3] = 158;
            gray[17, 3] = 157;
            gray[18, 3] = 157;
            gray[19, 3] = 156;
            gray[20, 3] = 154;
            gray[21, 3] = 152;
            gray[22, 3] = 150;
            gray[23, 3] = 147;
            gray[24, 3] = 143;
            gray[25, 3] = 139;
            gray[26, 3] = 134;
            gray[27, 3] = 128;
            gray[28, 3] = 97;
            gray[29, 3] = 22;
            gray[30, 3] = 7;
            gray[0, 4] = 11;
            gray[1, 4] = 59;
            gray[2, 4] = 122;
            gray[3, 4] = 131;
            gray[4, 4] = 136;
            gray[5, 4] = 141;
            gray[6, 4] = 145;
            gray[7, 4] = 148;
            gray[8, 4] = 151;
            gray[9, 4] = 153;
            gray[10, 4] = 155;
            gray[11, 4] = 156;
            gray[12, 4] = 158;
            gray[13, 4] = 159;
            gray[14, 4] = 159;
            gray[15, 4] = 159;
            gray[16, 4] = 159;
            gray[17, 4] = 159;
            gray[18, 4] = 159;
            gray[19, 4] = 158;
            gray[20, 4] = 157;
            gray[21, 4] = 155;
            gray[22, 4] = 152;
            gray[23, 4] = 149;
            gray[24, 4] = 146;
            gray[25, 4] = 142;
            gray[26, 4] = 138;
            gray[27, 4] = 132;
            gray[28, 4] = 125;
            gray[29, 4] = 66;
            gray[30, 4] = 10;
            gray[0, 5] = 26;
            gray[1, 5] = 105;
            gray[2, 5] = 126;
            gray[3, 5] = 133;
            gray[4, 5] = 138;
            gray[5, 5] = 143;
            gray[6, 5] = 146;
            gray[7, 5] = 150;
            gray[8, 5] = 152;
            gray[9, 5] = 155;
            gray[10, 5] = 156;
            gray[11, 5] = 158;
            gray[12, 5] = 159;
            gray[13, 5] = 160;
            gray[14, 5] = 161;
            gray[15, 5] = 161;
            gray[16, 5] = 161;
            gray[17, 5] = 161;
            gray[18, 5] = 160;
            gray[19, 5] = 160;
            gray[20, 5] = 158;
            gray[21, 5] = 156;
            gray[22, 5] = 154;
            gray[23, 5] = 152;
            gray[24, 5] = 148;
            gray[25, 5] = 143;
            gray[26, 5] = 139;
            gray[27, 5] = 133;
            gray[28, 5] = 127;
            gray[29, 5] = 107;
            gray[30, 5] = 22;
            gray[0, 6] = 62;
            gray[1, 6] = 119;
            gray[2, 6] = 127;
            gray[3, 6] = 134;
            gray[4, 6] = 139;
            gray[5, 6] = 144;
            gray[6, 6] = 147;
            gray[7, 6] = 151;
            gray[8, 6] = 154;
            gray[9, 6] = 156;
            gray[10, 6] = 157;
            gray[11, 6] = 159;
            gray[12, 6] = 160;
            gray[13, 6] = 161;
            gray[14, 6] = 162;
            gray[15, 6] = 162;
            gray[16, 6] = 162;
            gray[17, 6] = 162;
            gray[18, 6] = 162;
            gray[19, 6] = 161;
            gray[20, 6] = 159;
            gray[21, 6] = 157;
            gray[22, 6] = 156;
            gray[23, 6] = 153;
            gray[24, 6] = 149;
            gray[25, 6] = 145;
            gray[26, 6] = 141;
            gray[27, 6] = 135;
            gray[28, 6] = 129;
            gray[29, 6] = 122;
            gray[30, 6] = 51;
            gray[0, 7] = 94;
            gray[1, 7] = 120;
            gray[2, 7] = 128;
            gray[3, 7] = 135;
            gray[4, 7] = 140;
            gray[5, 7] = 145;
            gray[6, 7] = 148;
            gray[7, 7] = 152;
            gray[8, 7] = 154;
            gray[9, 7] = 156;
            gray[10, 7] = 158;
            gray[11, 7] = 159;
            gray[12, 7] = 161;
            gray[13, 7] = 162;
            gray[14, 7] = 164;
            gray[15, 7] = 166;
            gray[16, 7] = 166;
            gray[17, 7] = 165;
            gray[18, 7] = 164;
            gray[19, 7] = 162;
            gray[20, 7] = 161;
            gray[21, 7] = 159;
            gray[22, 7] = 155;
            gray[23, 7] = 153;
            gray[24, 7] = 149;
            gray[25, 7] = 147;
            gray[26, 7] = 141;
            gray[27, 7] = 135;
            gray[28, 7] = 130;
            gray[29, 7] = 123;
            gray[30, 7] = 80;
            gray[0, 8] = 108;
            gray[1, 8] = 121;
            gray[2, 8] = 129;
            gray[3, 8] = 136;
            gray[4, 8] = 141;
            gray[5, 8] = 146;
            gray[6, 8] = 149;
            gray[7, 8] = 153;
            gray[8, 8] = 155;
            gray[9, 8] = 156;
            gray[10, 8] = 158;
            gray[11, 8] = 160;
            gray[12, 8] = 162;
            gray[13, 8] = 165;
            gray[14, 8] = 168;
            gray[15, 8] = 169;
            gray[16, 8] = 168;
            gray[17, 8] = 168;
            gray[18, 8] = 167;
            gray[19, 8] = 164;
            gray[20, 8] = 161;
            gray[21, 8] = 160;
            gray[22, 8] = 157;
            gray[23, 8] = 153;
            gray[24, 8] = 149;
            gray[25, 8] = 145;
            gray[26, 8] = 140;
            gray[27, 8] = 135;
            gray[28, 8] = 129;
            gray[29, 8] = 124;
            gray[30, 8] = 100;
            gray[0, 9] = 111;
            gray[1, 9] = 121;
            gray[2, 9] = 130;
            gray[3, 9] = 136;
            gray[4, 9] = 142;
            gray[5, 9] = 146;
            gray[6, 9] = 150;
            gray[7, 9] = 153;
            gray[8, 9] = 155;
            gray[9, 9] = 157;
            gray[10, 9] = 158;
            gray[11, 9] = 160;
            gray[12, 9] = 163;
            gray[13, 9] = 168;
            gray[14, 9] = 169;
            gray[15, 9] = 171;
            gray[16, 9] = 170;
            gray[17, 9] = 169;
            gray[18, 9] = 168;
            gray[19, 9] = 166;
            gray[20, 9] = 162;
            gray[21, 9] = 160;
            gray[22, 9] = 158;
            gray[23, 9] = 154;
            gray[24, 9] = 150;
            gray[25, 9] = 147;
            gray[26, 9] = 143;
            gray[27, 9] = 137;
            gray[28, 9] = 132;
            gray[29, 9] = 126;
            gray[30, 9] = 114;
            gray[0, 10] = 112;
            gray[1, 10] = 121;
            gray[2, 10] = 129;
            gray[3, 10] = 136;
            gray[4, 10] = 142;
            gray[5, 10] = 146;
            gray[6, 10] = 150;
            gray[7, 10] = 152;
            gray[8, 10] = 155;
            gray[9, 10] = 157;
            gray[10, 10] = 158;
            gray[11, 10] = 160;
            gray[12, 10] = 164;
            gray[13, 10] = 168;
            gray[14, 10] = 171;
            gray[15, 10] = 172;
            gray[16, 10] = 172;
            gray[17, 10] = 169;
            gray[18, 10] = 167;
            gray[19, 10] = 166;
            gray[20, 10] = 163;
            gray[21, 10] = 160;
            gray[22, 10] = 158;
            gray[23, 10] = 154;
            gray[24, 10] = 152;
            gray[25, 10] = 148;
            gray[26, 10] = 143;
            gray[27, 10] = 139;
            gray[28, 10] = 133;
            gray[29, 10] = 126;
            gray[30, 10] = 118;
            gray[0, 11] = 111;
            gray[1, 11] = 121;
            gray[2, 11] = 129;
            gray[3, 11] = 135;
            gray[4, 11] = 141;
            gray[5, 11] = 145;
            gray[6, 11] = 149;
            gray[7, 11] = 151;
            gray[8, 11] = 154;
            gray[9, 11] = 156;
            gray[10, 11] = 158;
            gray[11, 11] = 159;
            gray[12, 11] = 164;
            gray[13, 11] = 168;
            gray[14, 11] = 170;
            gray[15, 11] = 172;
            gray[16, 11] = 171;
            gray[17, 11] = 169;
            gray[18, 11] = 167;
            gray[19, 11] = 166;
            gray[20, 11] = 162;
            gray[21, 11] = 160;
            gray[22, 11] = 158;
            gray[23, 11] = 155;
            gray[24, 11] = 152;
            gray[25, 11] = 148;
            gray[26, 11] = 144;
            gray[27, 11] = 138;
            gray[28, 11] = 132;
            gray[29, 11] = 126;
            gray[30, 11] = 118;
            gray[0, 12] = 111;
            gray[1, 12] = 120;
            gray[2, 12] = 128;
            gray[3, 12] = 135;
            gray[4, 12] = 140;
            gray[5, 12] = 145;
            gray[6, 12] = 148;
            gray[7, 12] = 150;
            gray[8, 12] = 153;
            gray[9, 12] = 155;
            gray[10, 12] = 157;
            gray[11, 12] = 158;
            gray[12, 12] = 162;
            gray[13, 12] = 166;
            gray[14, 12] = 168;
            gray[15, 12] = 170;
            gray[16, 12] = 170;
            gray[17, 12] = 167;
            gray[18, 12] = 166;
            gray[19, 12] = 165;
            gray[20, 12] = 161;
            gray[21, 12] = 159;
            gray[22, 12] = 157;
            gray[23, 12] = 155;
            gray[24, 12] = 151;
            gray[25, 12] = 148;
            gray[26, 12] = 144;
            gray[27, 12] = 138;
            gray[28, 12] = 131;
            gray[29, 12] = 124;
            gray[30, 12] = 117;
            gray[0, 13] = 110;
            gray[1, 13] = 120;
            gray[2, 13] = 127;
            gray[3, 13] = 134;
            gray[4, 13] = 139;
            gray[5, 13] = 144;
            gray[6, 13] = 147;
            gray[7, 13] = 150;
            gray[8, 13] = 152;
            gray[9, 13] = 155;
            gray[10, 13] = 156;
            gray[11, 13] = 157;
            gray[12, 13] = 158;
            gray[13, 13] = 163;
            gray[14, 13] = 165;
            gray[15, 13] = 166;
            gray[16, 13] = 166;
            gray[17, 13] = 166;
            gray[18, 13] = 165;
            gray[19, 13] = 162;
            gray[20, 13] = 159;
            gray[21, 13] = 158;
            gray[22, 13] = 156;
            gray[23, 13] = 151;
            gray[24, 13] = 148;
            gray[25, 13] = 145;
            gray[26, 13] = 142;
            gray[27, 13] = 138;
            gray[28, 13] = 131;
            gray[29, 13] = 124;
            gray[30, 13] = 116;
            gray[0, 14] = 110;
            gray[1, 14] = 119;
            gray[2, 14] = 127;
            gray[3, 14] = 133;
            gray[4, 14] = 139;
            gray[5, 14] = 143;
            gray[6, 14] = 147;
            gray[7, 14] = 149;
            gray[8, 14] = 151;
            gray[9, 14] = 153;
            gray[10, 14] = 154;
            gray[11, 14] = 155;
            gray[12, 14] = 156;
            gray[13, 14] = 159;
            gray[14, 14] = 162;
            gray[15, 14] = 163;
            gray[16, 14] = 164;
            gray[17, 14] = 163;
            gray[18, 14] = 161;
            gray[19, 14] = 159;
            gray[20, 14] = 157;
            gray[21, 14] = 156;
            gray[22, 14] = 153;
            gray[23, 14] = 150;
            gray[24, 14] = 147;
            gray[25, 14] = 144;
            gray[26, 14] = 141;
            gray[27, 14] = 136;
            gray[28, 14] = 130;
            gray[29, 14] = 123;
            gray[30, 14] = 115;
            gray[0, 15] = 109;
            gray[1, 15] = 118;
            gray[2, 15] = 125;
            gray[3, 15] = 132;
            gray[4, 15] = 138;
            gray[5, 15] = 142;
            gray[6, 15] = 145;
            gray[7, 15] = 148;
            gray[8, 15] = 150;
            gray[9, 15] = 152;
            gray[10, 15] = 153;
            gray[11, 15] = 154;
            gray[12, 15] = 155;
            gray[13, 15] = 156;
            gray[14, 15] = 157;
            gray[15, 15] = 158;
            gray[16, 15] = 158;
            gray[17, 15] = 158;
            gray[18, 15] = 158;
            gray[19, 15] = 157;
            gray[20, 15] = 156;
            gray[21, 15] = 153;
            gray[22, 15] = 151;
            gray[23, 15] = 149;
            gray[24, 15] = 146;
            gray[25, 15] = 143;
            gray[26, 15] = 139;
            gray[27, 15] = 134;
            gray[28, 15] = 129;
            gray[29, 15] = 122;
            gray[30, 15] = 113;
            gray[0, 16] = 107;
            gray[1, 16] = 116;
            gray[2, 16] = 124;
            gray[3, 16] = 131;
            gray[4, 16] = 136;
            gray[5, 16] = 140;
            gray[6, 16] = 144;
            gray[7, 16] = 146;
            gray[8, 16] = 148;
            gray[9, 16] = 150;
            gray[10, 16] = 152;
            gray[11, 16] = 153;
            gray[12, 16] = 154;
            gray[13, 16] = 154;
            gray[14, 16] = 154;
            gray[15, 16] = 155;
            gray[16, 16] = 156;
            gray[17, 16] = 156;
            gray[18, 16] = 156;
            gray[19, 16] = 155;
            gray[20, 16] = 154;
            gray[21, 16] = 152;
            gray[22, 16] = 149;
            gray[23, 16] = 148;
            gray[24, 16] = 145;
            gray[25, 16] = 141;
            gray[26, 16] = 138;
            gray[27, 16] = 133;
            gray[28, 16] = 127;
            gray[29, 16] = 119;
            gray[30, 16] = 106;
            gray[0, 17] = 104;
            gray[1, 17] = 114;
            gray[2, 17] = 122;
            gray[3, 17] = 128;
            gray[4, 17] = 134;
            gray[5, 17] = 138;
            gray[6, 17] = 142;
            gray[7, 17] = 144;
            gray[8, 17] = 147;
            gray[9, 17] = 148;
            gray[10, 17] = 150;
            gray[11, 17] = 151;
            gray[12, 17] = 152;
            gray[13, 17] = 153;
            gray[14, 17] = 153;
            gray[15, 17] = 153;
            gray[16, 17] = 153;
            gray[17, 17] = 153;
            gray[18, 17] = 153;
            gray[19, 17] = 152;
            gray[20, 17] = 151;
            gray[21, 17] = 150;
            gray[22, 17] = 148;
            gray[23, 17] = 146;
            gray[24, 17] = 143;
            gray[25, 17] = 140;
            gray[26, 17] = 136;
            gray[27, 17] = 131;
            gray[28, 17] = 124;
            gray[29, 17] = 116;
            gray[30, 17] = 95;
            gray[0, 18] = 97;
            gray[1, 18] = 111;
            gray[2, 18] = 119;
            gray[3, 18] = 126;
            gray[4, 18] = 131;
            gray[5, 18] = 136;
            gray[6, 18] = 139;
            gray[7, 18] = 142;
            gray[8, 18] = 144;
            gray[9, 18] = 146;
            gray[10, 18] = 148;
            gray[11, 18] = 148;
            gray[12, 18] = 150;
            gray[13, 18] = 150;
            gray[14, 18] = 151;
            gray[15, 18] = 151;
            gray[16, 18] = 151;
            gray[17, 18] = 151;
            gray[18, 18] = 151;
            gray[19, 18] = 150;
            gray[20, 18] = 149;
            gray[21, 18] = 147;
            gray[22, 18] = 146;
            gray[23, 18] = 143;
            gray[24, 18] = 140;
            gray[25, 18] = 136;
            gray[26, 18] = 133;
            gray[27, 18] = 129;
            gray[28, 18] = 122;
            gray[29, 18] = 114;
            gray[30, 18] = 77;
            gray[0, 19] = 74;
            gray[1, 19] = 107;
            gray[2, 19] = 115;
            gray[3, 19] = 122;
            gray[4, 19] = 128;
            gray[5, 19] = 132;
            gray[6, 19] = 136;
            gray[7, 19] = 140;
            gray[8, 19] = 141;
            gray[9, 19] = 143;
            gray[10, 19] = 144;
            gray[11, 19] = 145;
            gray[12, 19] = 147;
            gray[13, 19] = 148;
            gray[14, 19] = 148;
            gray[15, 19] = 148;
            gray[16, 19] = 149;
            gray[17, 19] = 148;
            gray[18, 19] = 148;
            gray[19, 19] = 147;
            gray[20, 19] = 146;
            gray[21, 19] = 145;
            gray[22, 19] = 143;
            gray[23, 19] = 141;
            gray[24, 19] = 137;
            gray[25, 19] = 134;
            gray[26, 19] = 130;
            gray[27, 19] = 125;
            gray[28, 19] = 119;
            gray[29, 19] = 110;
            gray[30, 19] = 43;
            gray[0, 20] = 34;
            gray[1, 20] = 99;
            gray[2, 20] = 111;
            gray[3, 20] = 118;
            gray[4, 20] = 123;
            gray[5, 20] = 129;
            gray[6, 20] = 133;
            gray[7, 20] = 136;
            gray[8, 20] = 139;
            gray[9, 20] = 139;
            gray[10, 20] = 140;
            gray[11, 20] = 141;
            gray[12, 20] = 143;
            gray[13, 20] = 145;
            gray[14, 20] = 145;
            gray[15, 20] = 146;
            gray[16, 20] = 145;
            gray[17, 20] = 145;
            gray[18, 20] = 145;
            gray[19, 20] = 144;
            gray[20, 20] = 143;
            gray[21, 20] = 141;
            gray[22, 20] = 140;
            gray[23, 20] = 137;
            gray[24, 20] = 134;
            gray[25, 20] = 131;
            gray[26, 20] = 127;
            gray[27, 20] = 121;
            gray[28, 20] = 115;
            gray[29, 20] = 89;
            gray[30, 20] = 15;
            gray[0, 21] = 11;
            gray[1, 21] = 69;
            gray[2, 21] = 104;
            gray[3, 21] = 112;
            gray[4, 21] = 119;
            gray[5, 21] = 124;
            gray[6, 21] = 129;
            gray[7, 21] = 132;
            gray[8, 21] = 134;
            gray[9, 21] = 135;
            gray[10, 21] = 136;
            gray[11, 21] = 137;
            gray[12, 21] = 139;
            gray[13, 21] = 140;
            gray[14, 21] = 141;
            gray[15, 21] = 142;
            gray[16, 21] = 142;
            gray[17, 21] = 142;
            gray[18, 21] = 142;
            gray[19, 21] = 140;
            gray[20, 21] = 139;
            gray[21, 21] = 138;
            gray[22, 21] = 136;
            gray[23, 21] = 134;
            gray[24, 21] = 131;
            gray[25, 21] = 127;
            gray[26, 21] = 122;
            gray[27, 21] = 116;
            gray[28, 21] = 109;
            gray[29, 21] = 42;
            gray[30, 21] = 8;
            gray[0, 22] = 6;
            gray[1, 22] = 22;
            gray[2, 22] = 87;
            gray[3, 22] = 106;
            gray[4, 22] = 113;
            gray[5, 22] = 118;
            gray[6, 22] = 123;
            gray[7, 22] = 127;
            gray[8, 22] = 130;
            gray[9, 22] = 130;
            gray[10, 22] = 132;
            gray[11, 22] = 133;
            gray[12, 22] = 135;
            gray[13, 22] = 136;
            gray[14, 22] = 137;
            gray[15, 22] = 137;
            gray[16, 22] = 137;
            gray[17, 22] = 138;
            gray[18, 22] = 137;
            gray[19, 22] = 137;
            gray[20, 22] = 135;
            gray[21, 22] = 134;
            gray[22, 22] = 131;
            gray[23, 22] = 129;
            gray[24, 22] = 126;
            gray[25, 22] = 122;
            gray[26, 22] = 117;
            gray[27, 22] = 111;
            gray[28, 22] = 74;
            gray[29, 22] = 12;
            gray[30, 22] = 5;

            /*
            for (j = 0; j < 11; j++)
            {
                for (i = 0; i < 15; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
            */

            pictureBox1.Size = new Size(600, 500);
            //pictureBox1.Location = new Point(10, 10);

            int xx;
            int yy;
            int width = 620;
            int height = 460;
            //byte[,] rgb = new byte[30, 3];

            pictureBox1.Size = new Size(width, height);
            bitmap1 = new Bitmap(width, height);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;
            int dd = 20;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */


                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)gray[xx / dd, yy / dd];
                    gg = (byte)gray[xx / dd, yy / dd];
                    bb = (byte)gray[xx / dd, yy / dd];
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;


        }

        private const int COLUMNS = 32;
        private const int ROWS = 16;
        private void button8_Click(object sender, EventArgs e)
        {
            int max = 0;
            int min = 255;
            int total = 0;
            int average = 0;
            int rms = 0;

            int xx;
            int yy;
            int width;
            int height;

            int i;
            int j;

            //brightness = new int[,] { { 1, 2, 3, 4, 5 }, { 1 + 2, 2 + 2, 3 + 2, 4 + 2, 5 + 2 }, { 1 + 4, 2 + 4, 3 + 4, 4 + 4, 5 + 4 } };
            //brightness = new int[,] { { 182, 183, 182, 184, 183, 185, 185, 185, 184, 184, 185, 186, 186, 187, 188, 186, 186, 185, 184, 184, 185, 187, 187, 187, 187, 187, 187, 186 }, { 181, 182, 182, 181, 183, 183, 181, 182, 182, 182, 185, 185, 185, 185, 185, 186, 183, 182, 181, 181, 181, 181, 184, 184, 186, 186, 186, 187 }, { 182, 180, 179, 180, 179, 180, 180, 179, 180, 180, 179, 181, 181, 184, 185, 182, 180, 179, 178, 180, 180, 180, 180, 180, 181, 184, 186, 187 }, { 180, 180, 179, 179, 178, 179, 179, 180, 179, 179, 180, 180, 183, 182, 182, 181, 178, 178, 176, 175, 178, 178, 181, 181, 183, 182, 186, 185 }, { 174, 180, 178, 176, 176, 176, 178, 176, 176, 176, 178, 179, 179, 179, 179, 176, 176, 175, 175, 176, 174, 175, 175, 176, 178, 181, 182, 188 }, { 173, 173, 174, 174, 173, 173, 173, 174, 175, 175, 176, 176, 178, 178, 176, 175, 174, 174, 174, 174, 174, 174, 175, 175, 177, 177, 180, 181 }, { 168, 174, 174, 172, 172, 173, 174, 174, 174, 174, 174, 173, 173, 175, 174, 174, 173, 173, 173, 173, 172, 173, 172, 174, 175, 179, 178, 181 }, { 157, 176, 174, 174, 174, 173, 170, 170, 170, 170, 172, 172, 171, 170, 172, 172, 172, 173, 173, 173, 173, 173, 174, 174, 176, 175, 175, 175 }, { 174, 173, 173, 174, 174, 174, 174, 173, 172, 172, 172, 169, 168, 171, 168, 172, 172, 171, 173, 173, 173, 173, 172, 172, 173, 174, 174, 175 }, { 160, 175, 174, 175, 174, 173, 171, 169, 168, 168, 168, 170, 169, 169, 168, 169, 171, 171, 172, 172, 172, 172, 172, 172, 172, 172, 173, 172 }, { 172, 171, 171, 173, 173, 173, 172, 169, 169, 169, 169, 169, 168, 167, 166, 168, 168, 171, 173, 173, 173, 173, 170, 170, 170, 171, 173, 173 }, { 167, 167, 169, 171, 173, 173, 171, 171, 169, 169, 169, 169, 167, 167, 166, 166, 171, 171, 172, 172, 169, 169, 168, 168, 168, 168, 171, 171 }, { 164, 164, 165, 166, 169, 169, 169, 169, 168, 168, 168, 167, 166, 164, 164, 166, 166, 167, 167, 167, 168, 168, 166, 166, 165, 167, 168, 169 }, { 162, 161, 164, 164, 169, 169, 169, 169, 169, 168, 168, 168, 165, 166, 166, 166, 169, 168, 167, 167, 167, 167, 167, 167, 166, 165, 167, 167 }, { 160, 159, 161, 164, 162, 166, 165, 166, 168, 167, 167, 164, 165, 162, 161, 163, 163, 161, 161, 163, 165, 165, 164, 162, 160, 161, 164, 164 }, { 158, 158, 159, 159, 162, 162, 166, 167, 168, 168, 167, 167, 165, 165, 165, 166, 165, 165, 164, 164, 164, 162, 161, 161, 159, 159, 160, 160 }, { 158, 157, 158, 157, 159, 160, 160, 165, 165, 166, 166, 165, 164, 164, 161, 162, 162, 160, 160, 160, 161, 163, 161, 160, 160, 160, 160, 160 }, { 157, 155, 157, 157, 159, 159, 164, 164, 165, 164, 164, 165, 161, 161, 160, 160, 159, 160, 159, 161, 160, 160, 160, 160, 159, 159, 158, 158 }, { 158, 155, 155, 155, 158, 159, 159, 162, 161, 163, 164, 161, 161, 159, 159, 160, 161, 159, 160, 158, 158, 157, 157, 157, 156, 158, 159, 159 }, { 154, 154, 155, 155, 161, 161, 162, 162, 160, 161, 160, 160, 159, 159, 159, 158, 159, 159, 159, 159, 158, 158, 158, 158, 159, 159, 158, 159 }, { 154, 155, 154, 155, 156, 156, 158, 161, 160, 159, 158, 157, 156, 156, 157, 157, 158, 158, 154, 154, 157, 158, 158, 154, 155, 155, 155, 157 }, { 152, 152, 152, 153, 159, 159, 159, 159, 157, 157, 155, 157, 158, 157, 158, 157, 157, 155, 154, 154, 155, 155, 155, 157, 155, 155, 153, 153 }, { 150, 150, 151, 152, 152, 155, 157, 157, 155, 153, 152, 152, 153, 158, 157, 157, 154, 151, 152, 152, 152, 154, 158, 157, 155, 152, 151, 152 }, { 146, 147, 150, 151, 155, 155, 157, 157, 154, 153, 152, 152, 154, 154, 155, 155, 152, 152, 151, 150, 152, 151, 154, 155, 153, 152, 148, 148 }, { 147, 148, 148, 152, 152, 153, 154, 154, 152, 151, 150, 151, 150, 152, 153, 153, 152, 150, 150, 151, 151, 152, 152, 152, 152, 150, 148, 150 }, { 147, 147, 151, 151, 155, 154, 154, 154, 150, 150, 150, 150, 151, 151, 151, 151, 147, 147, 147, 147, 151, 150, 152, 151, 150, 148, 146, 147 }, { 143, 146, 146, 148, 149, 149, 150, 150, 150, 151, 150, 149, 148, 148, 147, 147, 148, 147, 146, 146, 147, 149, 150, 150, 150, 146, 147, 148 }, { 146, 146, 150, 149, 148, 150, 148, 147, 145, 145, 145, 145, 144, 144, 146, 146, 147, 149, 148, 150, 152, 151, 151, 151, 147, 148, 150, 150 } };
            //brightness = new int[,] { { 178, 179, 179, 185, 185, 190, 191, 196, 199, 203, 208, 215, 215, 225, 229, 236, 238, 244, 248, 251, 252, 254, 255, 255, 255, 255, 255, 255 }, { 179, 179, 182, 182, 188, 187, 193, 193, 199, 201, 207, 208, 216, 223, 231, 232, 241, 243, 250, 251, 253, 253, 255, 255, 255, 255, 255, 255 }, { 176, 176, 179, 181, 182, 187, 189, 194, 195, 200, 203, 211, 213, 223, 228, 235, 237, 243, 247, 249, 251, 253, 255, 255, 255, 255, 255, 255 }, { 176, 178, 181, 180, 183, 185, 190, 190, 197, 199, 203, 204, 212, 217, 225, 230, 237, 239, 249, 249, 253, 253, 255, 255, 255, 255, 255, 255 }, { 173, 174, 177, 180, 182, 186, 187, 190, 192, 196, 199, 207, 210, 218, 222, 230, 232, 238, 241, 248, 249, 251, 253, 255, 255, 255, 255, 255 }, { 174, 174, 179, 179, 183, 183, 188, 188, 193, 194, 199, 201, 209, 215, 222, 226, 233, 236, 244, 244, 250, 250, 255, 255, 255, 255, 255, 255 }, { 171, 174, 174, 179, 180, 182, 186, 188, 188, 193, 192, 200, 206, 214, 218, 225, 228, 234, 238, 246, 247, 250, 251, 255, 255, 255, 255, 255 }, { 173, 173, 176, 178, 182, 182, 186, 185, 188, 189, 195, 194, 203, 205, 216, 218, 229, 231, 241, 244, 248, 249, 252, 255, 255, 255, 255, 255 }, { 171, 173, 173, 175, 175, 180, 182, 187, 187, 189, 190, 195, 198, 205, 209, 217, 222, 230, 233, 239, 242, 248, 250, 253, 255, 255, 255, 255 }, { 171, 171, 174, 174, 179, 180, 186, 185, 187, 187, 192, 193, 201, 201, 209, 209, 218, 223, 233, 235, 245, 245, 252, 253, 255, 255, 255, 255 }, { 170, 170, 173, 174, 172, 177, 180, 185, 186, 188, 190, 194, 194, 201, 202, 208, 213, 222, 227, 234, 238, 244, 247, 249, 252, 253, 255, 255 }, { 170, 171, 175, 174, 178, 179, 181, 182, 186, 187, 189, 191, 195, 196, 201, 201, 212, 214, 226, 230, 238, 240, 248, 248, 252, 252, 255, 255 }, { 172, 172, 174, 174, 174, 179, 180, 183, 185, 187, 188, 193, 194, 199, 199, 206, 207, 216, 220, 229, 231, 239, 243, 246, 247, 249, 253, 255 }, { 171, 171, 173, 174, 173, 174, 178, 180, 181, 184, 189, 189, 193, 194, 199, 199, 207, 209, 214, 221, 232, 233, 243, 244, 250, 251, 255, 255 }, { 169, 172, 171, 174, 174, 177, 178, 180, 180, 182, 184, 189, 191, 195, 197, 202, 203, 208, 211, 217, 222, 230, 235, 240, 243, 248, 251, 253 }, { 168, 168, 172, 171, 173, 173, 175, 177, 181, 181, 187, 186, 193, 194, 200, 201, 203, 204, 213, 215, 223, 225, 235, 236, 244, 244, 252, 252 }, { 164, 166, 166, 170, 170, 172, 173, 175, 177, 180, 181, 187, 188, 193, 193, 198, 199, 203, 206, 213, 216, 222, 225, 233, 237, 244, 246, 249 }, { 166, 165, 168, 168, 171, 171, 175, 176, 180, 180, 186, 186, 193, 193, 196, 197, 199, 200, 209, 210, 218, 219, 228, 229, 238, 239, 248, 248 }, { 164, 164, 164, 166, 166, 171, 171, 173, 174, 178, 179, 185, 183, 190, 189, 194, 196, 200, 201, 208, 210, 217, 221, 228, 230, 236, 238, 243 }, { 163, 163, 166, 166, 168, 168, 173, 173, 175, 175, 180, 180, 185, 185, 187, 190, 192, 193, 202, 203, 212, 212, 220, 221, 230, 231, 237, 241 }, { 159, 160, 161, 165, 165, 169, 169, 171, 174, 175, 176, 181, 182, 185, 186, 189, 190, 195, 196, 201, 203, 210, 214, 222, 224, 230, 230, 236 }, { 162, 162, 166, 165, 167, 166, 170, 170, 173, 173, 176, 175, 180, 180, 186, 185, 189, 189, 196, 197, 203, 206, 213, 216, 223, 224, 233, 232 }, { 160, 161, 161, 164, 162, 167, 167, 169, 172, 173, 174, 177, 179, 182, 182, 186, 186, 189, 189, 193, 195, 202, 204, 213, 216, 222, 223, 227 }, { 161, 163, 162, 164, 166, 165, 168, 167, 171, 171, 173, 174, 177, 177, 182, 181, 187, 188, 194, 194, 199, 199, 204, 207, 214, 215, 219, 219 }, { 165, 163, 163, 161, 164, 165, 165, 167, 169, 171, 171, 174, 174, 179, 179, 182, 182, 186, 187, 190, 192, 196, 196, 202, 207, 214, 215, 220 }, { 164, 164, 161, 161, 164, 163, 166, 166, 168, 168, 172, 171, 175, 175, 179, 179, 183, 183, 188, 187, 192, 192, 196, 198, 206, 207, 212, 214 }, { 161, 161, 161, 161, 164, 166, 166, 167, 167, 169, 168, 174, 174, 176, 178, 179, 179, 182, 183, 186, 188, 190, 193, 196, 197, 202, 203, 210 }, { 161, 160, 161, 161, 164, 164, 166, 166, 168, 167, 172, 172, 176, 176, 178, 178, 181, 181, 184, 185, 186, 188, 191, 192, 198, 199, 205, 205 } };


            //brightness = new int[,] { { 255, 255, 255, 222, 209, 214, 212, 209, 195, 218, 231, 244, 246, 239, 242, 245, 247, 241, 239, 224 }, { 254, 255, 255, 222, 210, 221, 214, 215, 211, 222, 231, 237, 242, 246, 249, 249, 249, 236, 237, 239 }, { 255, 255, 252, 228, 229, 221, 209, 214, 207, 222, 228, 240, 243, 248, 249, 252, 252, 236, 231, 238 }, { 253, 253, 246, 235, 230, 238, 222, 218, 221, 223, 233, 246, 249, 253, 253, 255, 253, 253, 253, 253 }, { 253, 252, 248, 236, 236, 229, 226, 220, 220, 226, 231, 243, 249, 252, 252, 254, 253, 254, 254, 253 }, { 252, 254, 248, 239, 234, 231, 227, 227, 225, 227, 234, 240, 250, 252, 252, 253, 252, 254, 254, 255 }, { 252, 255, 249, 235, 235, 228, 228, 225, 224, 229, 229, 241, 246, 255, 253, 255, 255, 255, 255, 254 }, { 250, 251, 240, 240, 232, 233, 230, 232, 232, 234, 232, 219, 225, 240, 239, 242, 247, 252, 253, 252 }, { 251, 249, 240, 235, 235, 232, 232, 223, 231, 227, 229, 226, 222, 238, 238, 241, 235, 246, 251, 250 }, { 252, 249, 234, 241, 236, 236, 236, 240, 247, 242, 253, 221, 213, 236, 236, 238, 245, 248, 251, 251 }, { 252, 248, 230, 235, 234, 236, 238, 241, 244, 246, 249, 239, 237, 250, 242, 245, 246, 250, 250, 250 }, { 252, 248, 229, 238, 240, 240, 241, 240, 245, 247, 250, 241, 239, 252, 250, 252, 251, 251, 251, 251 }, { 254, 246, 236, 235, 236, 238, 239, 241, 240, 246, 249, 244, 242, 248, 249, 250, 250, 251, 251, 250 }, { 248, 245, 239, 238, 236, 234, 234, 234, 238, 239, 245, 247, 247, 248, 249, 249, 251, 250, 249, 251 }, { 245, 240, 239, 236, 236, 233, 233, 231, 234, 238, 241, 247, 247, 247, 249, 249, 249, 250, 253, 250 }, { 228, 234, 235, 236, 235, 233, 230, 229, 233, 236, 246, 248, 248, 246, 244, 246, 248, 249, 249, 250 }, { 230, 237, 237, 236, 236, 230, 229, 229, 227, 239, 241, 247, 248, 246, 246, 246, 246, 244, 239, 236 }, { 230, 231, 235, 235, 234, 233, 229, 230, 227, 243, 253, 252, 252, 250, 246, 244, 237, 237, 229, 234 }, { 233, 236, 236, 236, 235, 232, 230, 231, 228, 242, 247, 249, 249, 249, 247, 241, 241, 237, 236, 235 }, { 237, 239, 236, 236, 235, 234, 230, 226, 224, 255, 255, 255, 255, 252, 231, 236, 240, 238, 235, 236 } };
            /*
            brightness = new int[,] { { 166, 169, 174, 173, 173, 172, 171, 173, 176, 178, 179, 177, 177, 179, 179, 179, 178, 179, 181, 181, 183, 184, 182, 184, 186, 187, 185, 187 }, { 172, 174, 173, 173, 173, 168, 171, 173, 174, 181, 181, 182, 181, 179, 179, 178, 179, 180, 180, 183, 185, 186, 186, 187, 186, 187, 186, 187 }, { 166, 166, 168, 166, 168, 171, 171, 174, 176, 176, 178, 177, 178, 178, 175, 176, 176, 178, 180, 180, 182, 183, 186, 187, 188, 188, 185, 184 }, { 168, 168, 167, 169, 169, 173, 173, 175, 177, 179, 179, 180, 179, 177, 177, 175, 177, 177, 178, 180, 179, 181, 182, 186, 185, 186, 185, 187 }, { 167, 166, 166, 166, 172, 174, 178, 181, 179, 177, 175, 174, 175, 177, 175, 176, 179, 180, 180, 180, 181, 181, 183, 183, 185, 185, 186, 186 }, { 171, 170, 171, 171, 171, 173, 174, 179, 176, 176, 176, 176, 175, 176, 178, 178, 178, 181, 180, 182, 181, 185, 183, 185, 185, 185, 185, 186 }, { 167, 168, 169, 172, 174, 175, 178, 179, 179, 176, 176, 174, 174, 174, 174, 174, 176, 178, 180, 180, 181, 182, 181, 182, 180, 179, 180, 180 }, { 169, 172, 172, 172, 173, 173, 173, 173, 173, 174, 174, 174, 175, 178, 179, 181, 181, 183, 183, 183, 183, 186, 186, 185, 185, 183, 183, 185 }, { 163, 167, 172, 174, 173, 172, 172, 171, 171, 172, 172, 173, 174, 174, 176, 175, 174, 174, 180, 180, 182, 181, 181, 181, 183, 181, 182, 185 }, { 165, 169, 169, 172, 173, 171, 171, 169, 169, 172, 171, 175, 175, 176, 176, 179, 179, 182, 182, 181, 181, 180, 180, 178, 180, 180, 180, 183 }, { 160, 166, 172, 173, 174, 171, 168, 166, 167, 171, 173, 174, 175, 176, 178, 174, 175, 175, 176, 179, 178, 178, 176, 175, 179, 180, 185, 184 }, { 164, 168, 168, 170, 171, 169, 168, 168, 167, 169, 168, 172, 173, 175, 175, 175, 175, 178, 178, 179, 179, 178, 178, 178, 179, 178, 178, 181 }, { 161, 161, 168, 168, 171, 167, 164, 164, 165, 166, 168, 170, 172, 173, 173, 173, 173, 175, 174, 174, 171, 172, 171, 171, 174, 173, 178, 177 }, { 165, 167, 167, 166, 167, 164, 165, 166, 166, 167, 166, 167, 168, 172, 172, 173, 172, 173, 173, 173, 174, 174, 174, 179, 180, 179, 178, 178 }, { 154, 155, 160, 161, 164, 164, 162, 163, 160, 163, 164, 161, 168, 171, 171, 172, 169, 168, 168, 171, 171, 170, 172, 172, 175, 174, 173, 173 }, { 155, 159, 159, 159, 160, 159, 160, 164, 164, 165, 162, 164, 163, 170, 168, 168, 168, 168, 169, 167, 167, 172, 171, 175, 175, 175, 175, 174 }, { 154, 154, 158, 159, 159, 159, 162, 162, 166, 167, 165, 166, 166, 165, 164, 164, 166, 167, 168, 171, 169, 171, 173, 172, 172, 173, 172, 171 }, { 152, 155, 158, 159, 159, 159, 158, 161, 160, 164, 164, 164, 164, 168, 168, 168, 169, 166, 167, 169, 168, 170, 170, 167, 168, 170, 170, 171 }, { 159, 160, 160, 158, 156, 154, 159, 160, 162, 163, 160, 161, 159, 160, 164, 166, 169, 172, 171, 171, 168, 168, 171, 168, 171, 170, 168, 171 }, { 157, 161, 162, 160, 161, 154, 157, 158, 157, 161, 159, 165, 165, 167, 165, 165, 164, 168, 166, 170, 168, 168, 168, 164, 165, 167, 166, 171 }, { 160, 160, 159, 160, 159, 157, 158, 158, 158, 159, 160, 160, 161, 163, 166, 167, 168, 168, 168, 168, 167, 168, 169, 169, 169, 167, 168, 170 }, { 158, 161, 161, 161, 163, 157, 159, 157, 154, 158, 157, 165, 165, 167, 166, 161, 161, 166, 165, 166, 166, 170, 170, 168, 169, 167, 168, 171 }, { 154, 157, 153, 155, 161, 161, 161, 158, 158, 161, 162, 163, 159, 159, 163, 163, 163, 165, 164, 164, 167, 170, 170, 171, 169, 168, 168, 168 }, { 151, 154, 154, 160, 160, 161, 161, 158, 157, 159, 159, 165, 164, 162, 162, 160, 161, 164, 164, 166, 165, 170, 171, 172, 174, 171, 171, 171 }, { 149, 152, 152, 152, 155, 152, 156, 156, 159, 161, 160, 160, 158, 157, 162, 161, 164, 166, 162, 164, 164, 165, 166, 168, 165, 167, 167, 167 }, { 147, 150, 150, 157, 157, 157, 156, 159, 158, 160, 160, 160, 160, 158, 159, 160, 161, 165, 162, 166, 165, 167, 168, 171, 171, 167, 167, 170 }, { 148, 151, 153, 157, 153, 154, 155, 157, 159, 158, 158, 157, 159, 160, 162, 160, 162, 162, 165, 166, 165, 165, 162, 161, 160, 161, 164, 164 }, { 147, 151, 150, 154, 156, 151, 152, 157, 159, 163, 161, 155, 155, 156, 158, 161, 163, 167, 167, 167, 167, 166, 167, 169, 169, 171, 169, 171 } };
            */

            int[,] brightness = new int[COLUMNS, ROWS];

            Random r = new Random();

            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    brightness[i, j] = r.Next(1, 160);
                }
            }

            //brightness = new int[,] { { 166, 158, 154, 151, 150, 150, 152, 145, 143, 136, 131, 131, 131, 129, 128, 124, 123, 118, 119, 119 }, { 159, 159, 153, 153, 152, 153, 146, 146, 137, 146, 129, 116, 115, 114, 117, 116, 122, 122, 122, 122 }, { 159, 153, 152, 147, 148, 145, 143, 134, 132, 127, 123, 114, 116, 117, 117, 122, 123, 130, 132, 130 }, { 153, 153, 150, 148, 145, 144, 136, 133, 127, 127, 124, 121, 115, 115, 115, 115, 121, 123, 125, 125 }, { 138, 140, 140, 143, 143, 139, 137, 129, 126, 121, 122, 118, 118, 118, 121, 121, 118, 124, 125, 124 }, { 140, 142, 145, 144, 144, 142, 131, 129, 123, 123, 123, 123, 123, 123, 118, 117, 116, 116, 117, 118 }, { 139, 140, 139, 140, 139, 133, 130, 128, 126, 129, 130, 129, 126, 119, 118, 116, 115, 114, 114, 114 }, { 144, 144, 140, 142, 139, 139, 132, 131, 128, 128, 124, 125, 123, 123, 118, 117, 115, 115, 114, 114 }, { 145, 140, 139, 136, 135, 130, 128, 126, 128, 130, 130, 127, 123, 118, 117, 116, 117, 116, 112, 109 }, { 148, 147, 137, 124, 128, 128, 130, 130, 131, 132, 129, 130, 122, 121, 118, 118, 107, 122, 116, 121 }, { 153, 146, 139, 132, 129, 125, 124, 126, 128, 131, 131, 128, 125, 123, 123, 116, 125, 132, 148, 166 }, { 152, 152, 142, 129, 128, 128, 130, 130, 134, 135, 136, 136, 132, 129, 126, 126, 136, 147, 151, 154 }, { 152, 150, 150, 140, 136, 130, 129, 130, 132, 135, 138, 132, 137, 136, 136, 137, 136, 142, 139, 139 }, { 149, 150, 145, 144, 137, 137, 138, 138, 143, 144, 146, 145, 142, 143, 139, 142, 141, 141, 143, 143 }, { 145, 144, 147, 142, 144, 139, 138, 140, 144, 150, 152, 153, 153, 150, 147, 142, 138, 142, 139, 138 }, { 140, 139, 140, 142, 145, 145, 145, 146, 152, 152, 156, 154, 157, 156, 154, 154, 147, 147, 143, 142 }, { 144, 140, 140, 142, 145, 147, 147, 151, 153, 159, 160, 164, 163, 160, 158, 158, 158, 152, 143, 136 }, { 137, 136, 138, 138, 146, 145, 150, 150, 156, 157, 164, 162, 161, 160, 160, 160, 161, 159, 151, 151 }, { 124, 129, 144, 148, 150, 152, 151, 152, 154, 159, 158, 163, 161, 159, 158, 158, 161, 162, 166, 179 }, { 141, 144, 151, 151, 151, 151, 154, 154, 158, 158, 161, 160, 158, 157, 155, 153, 168, 165, 167, 169 } };

            richTextBox1.Text += "brightness rank" + brightness.Rank.ToString() + "\n";

            for (i = 0; i < brightness.Rank; i++)
            {
                richTextBox1.Text += "aaaa = " + brightness.GetLength(i) + "\n";
            }

            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    brightness[i, j] = r.Next(1, 160);

                    //richTextBox1.Text += brightness[j, i].ToString() + " ";
                    if (max < brightness[i, j])
                        max = brightness[i, j];
                    else if (min > brightness[i, j])
                        min = brightness[i, j];
                    total += brightness[i, j];
                }
                //richTextBox1.Text += "\n";
            }

            richTextBox1.Text += "max = " + max.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            average = total / (COLUMNS * ROWS);
            richTextBox1.Text += "average = " + average.ToString() + "\n";

            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    rms += (brightness[i, j] - average) * (brightness[i, j] - average);
                }
            }

            rms /= COLUMNS * ROWS;

            richTextBox1.Text += "rms = " + Math.Sqrt((double)rms).ToString() + "\n";

            pictureBox1.Size = new Size(600, 500);
            width = 20 * COLUMNS;
            height = 20 * ROWS;

            pictureBox1.Size = new Size(width, height);
            bitmap1 = new Bitmap(width, height);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;
            int dd = 20;
            int diff;
            if (max == min)
                diff = 1;
            else
                diff = max - min;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)((brightness[xx / dd, yy / dd] - min) * 255 / diff);
                    gg = (byte)((brightness[xx / dd, yy / dd] - min) * 255 / diff);
                    bb = (byte)((brightness[xx / dd, yy / dd] - min) * 255 / diff);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(640, 480);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);
            sb = new SolidBrush(Color.Navy);

            int i;
            var random = new Random();

            /*
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[10];
            var stringChars2 = new char[11];
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if (i < 2)
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            richTextBox1.Text += "相機序號1：" + finalString1 + "\n";

            for (int i = 0; i < stringChars2.Length; i++)
            {
                stringChars2[i] = chars2[random.Next(chars2.Length)];
            }
            var finalString2 = new String(stringChars2);
            richTextBox1.Text += "相機序號2：" + finalString2 + "\n";
            */

            int N = 10;
            int[] x = new int[N];
            int[] y = new int[N];

            int[,] position = new int[N, 2];	//建立一個二維陣列

            int w = pictureBox1.Width;
            int h = pictureBox1.Height;

            int cx = 100;
            int cy = 100;
            int r = 30;

            for (i = 0; i < N; i++)
            {
                position[i, 0] = random.Next(w - 2 * r) + r;  //x1, x2, x3.....
                position[i, 1] = random.Next(h - 2 * r) + r;  //y1, y2, y3.....
            }
            richTextBox1.Text += "每個點的位置\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += position[i, 0].ToString() + "\t" + position[i, 1].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < N; i++)
            {
                x[i] = i;
                y[i] = random.Next(N);
                /*
                do
                {
                    y[i] = random.Next(N);
                }
                while (x[i] == y[i]);
                */
            }
            richTextBox1.Text += "\n";


            richTextBox1.Text += "x array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += x[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "y array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";


            Point pointa;
            Point pointb;
            for (i = 0; i < N; i++)
            {
                pointa = new Point(position[x[i], 0], position[x[i], 1]);
                pointb = new Point(position[y[i], 0], position[y[i], 1]);
                g.DrawLine(p, pointa, pointb);     // Draw line to screen.
            }

            for (i = 0; i < N; i++)
            {
                cx = position[i, 0];
                cy = position[i, 1];

                //richTextBox1.Text += position[i, 0].ToString() + "\t" + position[i, 1].ToString() + "\n";
                //richTextBox1.Text += "(" + (cx - r).ToString() + ", " + (cy - r).ToString() + ") - (" + (cx + r).ToString() + ", " + (cy + r).ToString() + ")\n";
                //g.FillEllipse(sb, cx - r, cy - r, r * 2, r * 2);
                FillCircle(g, sb, cx, cy, r);

                //g.DrawEllipse(new Pen(Color.Red, 3), cx - r, cy - r, r * 2, r * 2);
                DrawCircle(g, p, cx, cy, r);
            }
            pictureBox1.Image = bitmap1;
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        void FillCircle(Graphics g, SolidBrush sb, int cx, int cy, int r)
        {
            g.FillEllipse(sb, cx - r, cy - r, r * 2, r * 2);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //畫各種編碼的區間
            int xx;
            int yy;
            int dd = 20;
            int allow = 0;

            richTextBox1.Text += "W = " + this.pictureBox1.Width.ToString() + " H = " + this.pictureBox1.Height.ToString() + "\n";

            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            //DrawXY();

            Point[] pt1 = new Point[656];    //一維陣列內有360個Point
            yy = 200;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt1[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0xA1) && ((xx / 256) <= 0xE7)) && (((xx % 256) >= 0xA1) && ((xx % 256) <= 0xFE)))
                {
                    pt1[xx / 100].Y = yy - 100 + dd;
                    allow++;
                }
                else
                    //pt1[xx / 100].Y = 300 - 100;
                    pt1[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt1);
            g.DrawString("GB2313", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(20, yy - 80));
            richTextBox1.Text += "e1 allow = " + allow.ToString() + "\n";



            Point[] pt2 = new Point[656];    //一維陣列內有360個Point
            yy = 300;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt2[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0x81) && ((xx / 256) <= 0xFE)) && ((((xx % 256) >= 0x40) && ((xx % 256) <= 0x7E)) || (((xx % 256) >= 0x80) && ((xx % 256) <= 0xFE))))
                {
                    pt2[xx / 100].Y = yy - 100 + dd;
                    allow++;
                    //pt1[xx / 100].Y = 300 - 100;
                }
                else
                    //pt1[xx / 100].Y = 300 - 100;
                    pt2[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Green, 3), pt2);
            g.DrawString("GBK", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(20, yy - 80));
            richTextBox1.Text += "e2 allow = " + allow.ToString() + "\n";

            Point[] pt3 = new Point[656];    //一維陣列內有360個Point
            yy = 400;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt3[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0x81) && ((xx / 256) <= 0xFE)) && ((((xx % 256) >= 0x40) && ((xx % 256) <= 0x7E)) || (((xx % 256) >= 0xA1) && ((xx % 256) <= 0xFE))))
                {
                    pt3[xx / 100].Y = yy - 100 + dd;
                    allow++;
                    //pt1[xx / 100].Y = 300 - 100;
                }
                else
                    //pt1[xx / 100].Y = 300 - 100;
                    pt3[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Blue, 3), pt3);
            g.DrawString("GB2313", new Font("Big5", 30), new SolidBrush(Color.Blue), new PointF(20, yy - 80));
            richTextBox1.Text += "e3 allow = " + allow.ToString() + "\n";


            Point[] pt4 = new Point[656];    //一維陣列內有360個Point
            yy = 500;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt4[xx / 100].X = xx / 100;
                if ((xx > 0x4e00) && (xx < 0x9fbf))
                {
                    pt4[xx / 100].Y = yy - 100 + dd;
                    allow++;
                }
                else
                    pt4[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Yellow, 3), pt4);
            g.DrawString("Unicode", new Font("標楷體", 30), new SolidBrush(Color.Yellow), new PointF(20, yy - 80));
            richTextBox1.Text += "e4 allow = " + allow.ToString() + "\n";

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            int W = 340;
            int H = 543;
            int x_st;
            int y_st;
            int w;
            int h;
            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(W + 50, H + 50);  //改變圖框大小
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            sb = new SolidBrush(Color.Red);
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, H - h, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, H - h, w, h));

            x_st = 0; y_st = 6 + 205; w = 10; h = 88; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));
            x_st = W - 10; y_st = 6 + 66; w = 10; h = 205; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            Font f;
            f = new Font("Times New Roman", 14);
            sb = new SolidBrush(Color.Black);
            g.DrawString("205", f, sb, new PointF(0, 205 / 2));
            g.DrawString("268", f, sb, new PointF(0, 573 - 6 - 268 + 268 / 2));
            g.DrawString("66", f, sb, new PointF(W - 30, 66 / 2));
            g.DrawString("290", f, sb, new PointF(W - 40, 573 - 6 - 290 + 290 / 2));

            Pen p = new Pen(Color.Black, 5);
            p.StartCap = LineCap.ArrowAnchor;
            p.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(p, 0, H + 10, W, H + 10);
            g.DrawLine(p, W + 10, 0, W + 10, H);
            g.DrawString("340", f, sb, new PointF(W / 2, H + 15));
            g.DrawString("573", f, sb, new PointF(W + 15, H / 2));


            int dw;
            int dh;

            //draw desk
            dw = 152;
            dh = 78;
            x_st = (W - dw) / 2;
            y_st = (H - dh) / 2;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));


            //draw sofa
            dw = 180;
            dh = 86;
            x_st = 0;
            y_st = H - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, W, H));
            p = new Pen(Color.Black, 1);
            g.DrawLine(p, 0, 0, W, H);
            g.DrawLine(p, W, 0, 0, H);

            pictureBox1.Image = bitmap1;

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {
            draw_audit_picture(1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            draw_audit_picture(2);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            draw_audit_picture(3);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            draw_audit_picture(4);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            draw_audit_picture(5);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            draw_audit_picture(6);
        }

        void draw_audit_picture(int draw_case)
        {
            int title_size1 = 50;
            int title_size2 = 40;
            int title_size3 = 40;
            int H = 100;
            int h = 10;
            int width = 440;
            int height = h + title_size1 + title_size2 + h + H + h + title_size3 + h + H + h;

            Pen ArrowPen;
            Pen redPen = new Pen(Color.Red, 3);
            Pen greenPen = new Pen(Color.Green, 3);
            Pen blackPen = new Pen(Color.Black, 3);

            pictureBox1.Width = width;
            pictureBox1.Height = height;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.White);

            /*
            //debug
            Pen debug = new Pen(Color.Green, 1);
            g.DrawRectangle(debug, 0, 0, width - 1, h - 1); //h
            g.DrawRectangle(debug, 0, h, width - 1, title_size1 - 1);   //title_size1
            g.DrawRectangle(debug, 0, h + title_size1, width - 1, title_size2 - 1);   //title_size2
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h, width - 1, H - 1);   //H
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h, width - 1, title_size3 - 1); //title_size3
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3 + h, width - 1, H - 1);   //H
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3 + h + H, width - 1, h - 1);   //h
            */

            g.DrawRectangle(p, 0, 0, width - 1, height - 1);

            int x_st = 0;
            int y_st = 0;
            int x_sp = 0;
            int y_sp = 0;
            int offset = 10;

            int h_st = height;

            int[] x_data = new int[21];
            int[] y_data = new int[21];
            Point point0;
            Point point1;
            Point point2;
            Point point3;
            Point point4;
            Point point5;
            Point point6;
            Point point7;
            Point point8;
            Point point9;
            Point point10;
            Point point11;
            Point point12;
            Point point13;
            Point point14;
            Point point15;
            Point point16;
            Point point17;
            Point point18;
            Point point19;
            Point point20;

            int dx = 22;
            y_st = h + H + h + title_size3 + h;

            if ((draw_case == 1) || (draw_case == 2))
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;
                x_data[5] = dx * 5; y_data[5] = y_st;
                x_data[6] = dx * 6; y_data[6] = y_st;
                x_data[7] = dx * 7; y_data[7] = y_st;
                x_data[8] = dx * 8; y_data[8] = y_st;
                x_data[9] = dx * 9; y_data[9] = y_st;

                x_data[10] = dx * 10; y_data[10] = y_st;
                y_st += H;
                x_data[11] = dx * 10; y_data[11] = y_st;

                x_data[12] = dx * 11; y_data[12] = y_st;
                y_st -= H;
                x_data[13] = dx * 11; y_data[13] = y_st;

                x_data[14] = dx * 12; y_data[14] = y_st;
                y_st += H;
                x_data[15] = dx * 12; y_data[15] = y_st;

                x_data[16] = dx * 13; y_data[16] = y_st;
                y_st -= H;
                x_data[17] = dx * 13; y_data[17] = y_st;

                x_data[18] = dx * 14; y_data[18] = y_st;
                y_st += H;
                x_data[19] = dx * 14; y_data[19] = y_st;

                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線

                y_st = h;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;
                x_data[5] = dx * 5; y_data[5] = y_st;
                x_data[6] = dx * 6; y_data[6] = y_st;
                x_data[7] = dx * 7; y_data[7] = y_st;
                x_data[8] = dx * 8; y_data[8] = y_st;
                x_data[9] = dx * 9; y_data[9] = y_st;

                x_data[10] = dx * 10; y_data[10] = y_st;
                y_st += H;
                x_data[11] = dx * 10; y_data[11] = y_st;

                x_data[12] = dx * 11; y_data[12] = y_st;
                y_st -= H;
                x_data[13] = dx * 11; y_data[13] = y_st;

                x_data[14] = dx * 12; y_data[14] = y_st;
                y_st += H;
                x_data[15] = dx * 12; y_data[15] = y_st;

                x_data[16] = dx * 13; y_data[16] = y_st;
                y_st -= H;
                x_data[17] = dx * 13; y_data[17] = y_st;

                x_data[18] = dx * 14; y_data[18] = y_st;
                y_st += H;
                x_data[19] = dx * 14; y_data[19] = y_st;

                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints2 = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(redPen, curvePoints2);   //畫直線
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 8; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 8; y_data[8] = y_st;

                x_data[9] = dx * 8; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 18; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線




                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線
            }
            else if (draw_case == 5)
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 7; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 7; y_data[8] = y_st;

                x_data[9] = dx * 7; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 17; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 17; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線


                y_st = h;


                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 8; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 8; y_data[8] = y_st;

                x_data[9] = dx * 8; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 18; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints2 = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(redPen, curvePoints2);   //畫直線






                /*
                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線
                */


            }
            else if (draw_case == 6)
            {

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 6; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 6; y_data[8] = y_st;

                x_data[9] = dx * 7; y_data[9] = y_st;
                y_st += H;
                x_data[10] = dx * 7; y_data[10] = y_st;

                x_data[11] = dx * 8; y_data[11] = y_st;
                y_st -= H;
                x_data[12] = dx * 8; y_data[12] = y_st;

                x_data[13] = dx * 9; y_data[13] = y_st;
                y_st += H;
                x_data[14] = dx * 9; y_data[14] = y_st;

                x_data[15] = dx * 10; y_data[15] = y_st;
                y_st -= H;
                x_data[16] = dx * 10; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                x_data[18] = dx * 18; y_data[18] = y_st;
                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線




                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線



            }


            ArrowPen = new Pen(Color.Red, 6);   //重新設定pp的線條樣式
            ArrowPen.EndCap = LineCap.ArrowAnchor;

            if ((draw_case == 1) || (draw_case == 2))
            {
                x_st = dx * 10;
                y_st = h_st - (h + H + h + title_size3 + h + offset);

                x_sp = dx * 10;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
            }
            else if (draw_case == 3)
            {

            }
            else if (draw_case == 4)
            {
                x_st = dx * 8 + 3;
                y_st = h_st - (h + H + h + title_size3 + h + offset);
                x_sp = dx * 8 + 3;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                g.DrawString("Initialize OK", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st, y_st - H / 2));

                x_st = dx * 18 + 3;
                y_st = h_st - (h + H + h + title_size3 + h + offset);
                x_sp = dx * 18 + 3;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

            }
            else if (draw_case == 5)
            {

            }
            else if (draw_case == 6)
            {
                x_st = dx * 5;
                y_st = h_st - (h + H + h + title_size3 + h + offset);

                x_sp = dx * 5;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

            }

            ArrowPen = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            ArrowPen.EndCap = LineCap.ArrowAnchor;

            if (draw_case == 1)
            {
                x_st = dx * 10;
                y_st = h_st - (h + offset);

                x_sp = dx * 10;
                y_sp = h_st - (h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 11;
                x_sp = dx * 11;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 12;
                x_sp = dx * 12;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 13;
                x_sp = dx * 13;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 14;
                x_sp = dx * 14;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
            }
            else if (draw_case == 2)
            {

                y_st = h_st - (h + offset);
                y_sp = h_st - (h + offset + (H - offset * 2));

                for (int i = 1; i < 13; i++)
                {
                    x_st = dx * i * 3 / 2 + 5;
                    x_sp = dx * i * 3 / 2 + 5;
                    if (i == 12)
                    {
                        ArrowPen = new Pen(Color.Red, 10);   //重新設定pp的線條樣式
                        ArrowPen.EndCap = LineCap.ArrowAnchor;
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                    else
                    {
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                }
            }
            else if (draw_case == 3)
            {
                y_st = h_st - (h + offset);
                y_sp = h_st - (h + offset + (H - offset * 2));

                int x_st2 = 0;
                int y_st2 = h_st - (h + 60);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + 60);

                for (int i = 1; i < 4; i++)
                {
                    x_st = dx * i * 13 / 2 - 70;
                    x_sp = dx * i * 13 / 2 - 70;
                    richTextBox1.Text += "x = " + x_st.ToString() + "\n";
                    if (i == 3)
                    {
                        ArrowPen = new Pen(Color.Red, 10);   //重新設定pp的線條樣式
                        ArrowPen.EndCap = LineCap.ArrowAnchor;
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                        //int height = h + title_size1 + title_size2 + h + H + h + title_size3 + h + H + h;
                        Pen p2 = new Pen(Color.Black, 2);
                        p2.DashStyle = DashStyle.Dash;
                        g.DrawLine(p2, x_st, h + title_size1 + 30, x_sp, height);
                    }
                    else
                    {
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                    if (i == 1)
                        x_st2 = x_st;
                    if (i == 2)
                        x_sp2 = x_st;
                }

                ArrowPen = new Pen(Color.Red, 5);   //重新設定pp的線條樣式
                ArrowPen.StartCap = LineCap.ArrowAnchor;
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                richTextBox1.Text += "x_st2 = " + x_st2.ToString() + "x_sp2 = " + x_sp2.ToString() + "\n";

                g.DrawString("1 sec", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 40, y_st2 + 5));
                g.DrawString("Conflict!", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(315, y_st2 - 55));

            }
            else if (draw_case == 4)
            {
                int x_st2 = 0;
                int y_st2 = h_st - (h + offset);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + offset + (H - offset * 2));

                x_st2 = dx * 8 + 6;
                x_sp2 = dx * 8 + 6;
                ArrowPen = new Pen(Color.Red, 8);   //重新設定pp的線條樣式
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";

                g.DrawString("Detect OK Signal", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2, y_st2 - H / 2));

                x_st2 = dx * 18 + 6;
                x_sp2 = dx * 18 + 6;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";
            }
            else if (draw_case == 5)
            {



            }
            else if (draw_case == 6)
            {
                int x_st2 = 0;
                int y_st2 = h_st - (h + offset);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + offset + (H - offset * 2));

                x_st2 = dx * 5;
                x_sp2 = dx * 5;
                ArrowPen = new Pen(Color.Red, 8);   //重新設定pp的線條樣式
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";

                g.DrawString("Detect OK Signal", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 10, y_st2 - H / 2 - 30));



                ArrowPen = new Pen(Color.Black, 5);   //重新設定pp的線條樣式
                ArrowPen.StartCap = LineCap.ArrowAnchor;
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2 - H / 2 + 20, x_st2 + 300, y_st2 - H / 2 + 20);
                richTextBox1.Text += "x_st2 = " + x_st2.ToString() + "x_sp2 = " + x_sp2.ToString() + "\n";

                g.DrawString("0.2 sec", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 120, y_st2 - H / 2 + 25));



            }

            int offset2 = 15;
            SolidBrush sb;
            Font f;
            f = new Font("Times New Roman", 17);
            sb = new SolidBrush(Color.Purple);
            if ((draw_case == 1) || (draw_case == 2))
            {
                g.DrawString("IE Insert Bouncing", f, sb, new PointF(0, h + offset2));
                //g.DrawString("Push Button Bouncing", f, sb, new PointF(0, h + offset2));
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                g.DrawString("IE initialization fails", f, sb, new PointF(0, h + offset2));
            }
            else if (draw_case == 5)
            {
                g.DrawString("Send Command to IE Error", f, sb, new PointF(0, h + offset2));
            }
            else if (draw_case == 6)
            {
                g.DrawString("Pedal Bouncing", f, sb, new PointF(0, h + offset2));
            }

            if ((draw_case == 1) || (draw_case == 2))
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("IE Insert", f, sb, new PointF(0, h + title_size1 + offset2));
                //g.DrawString("User Push Button", f, sb, new PointF(0, h + title_size1 + offset2));
                if (draw_case == 1)
                {
                    sb = new SolidBrush(Color.Green);
                    f = new Font("Times New Roman", 11);
                    g.DrawString("Hardware Response", f, sb, new PointF(310, h + title_size1 + title_size2 + h + 10));
                }
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("IE Plug-in & initialize", f, sb, new PointF(0, h + title_size1 + offset2));
            }
            else if (draw_case == 5)
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("Send Data without Check-Sum", f, sb, new PointF(0, h + title_size1 + offset2));
            }
            else if (draw_case == 6)
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("Real Pedal Bouncing", f, sb, new PointF(0, h + title_size1 + offset2));
            }


            f = new Font("Times New Roman", 17);
            sb = new SolidBrush(Color.Blue);
            if (draw_case == 1)
                g.DrawString("Software Response", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 2)
                g.DrawString("Software Detect Stable IE Signal", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 3)
                g.DrawString("Software Detect IE", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 4)
                g.DrawString("Software Detect IE OK Signal", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 5)
                g.DrawString("Send Data with Check-Sum", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 6)
                g.DrawString("Software Catthes First One", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));

            pictureBox1.Image = bitmap1;



        }


        private void button24_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_item_location2();
            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(887, 636);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            gamma = 2.2;
            //畫出真正的Gamma 2.2曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            gammaPen = new Pen(Color.Green, 2);
            gamma = 2.3;
            //畫出真正的Gamma 2.3曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            gammaPen = new Pen(Color.Blue, 2);
            gamma = 2.4;
            //畫出真正的Gamma 2.4曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線




            int YST0 = 0x00;
            int YST1 = 0x14;
            int YST2 = 0x22;
            int YST3 = 0x37;
            int YST4 = 0x4B;
            int YST5 = 0x5E;
            int YST6 = 0x6B;
            int YST7 = 0x76;
            int YST8 = 0x82;
            int YST9 = 0x8C;
            int YST10 = 0x9F;
            int YST11 = 0xAB;
            int YST12 = 0xB5;
            int YST13 = 0xCF;
            int YST14 = 0xDE;
            int YST15 = 0xED;

            int YSLP15 = 0x1B;

            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;

                if (data_in[i] <= 4)
                    data_out[i] = YST0 + (YST1 - YST0) * (data_in[i] - 0) / 4;
                else if (data_in[i] <= 8)
                    data_out[i] = YST1 + (YST2 - YST1) * (data_in[i] - 4) / 4;
                else if (data_in[i] <= 16)
                    data_out[i] = YST2 + (YST3 - YST2) * (data_in[i] - 8) / 8;
                else if (data_in[i] <= 32)
                    data_out[i] = YST4 + (YST4 - YST3) * (data_in[i] - 16) / 16;
                else if (data_in[i] <= 40)
                    data_out[i] = YST5 + (YST5 - YST4) * (data_in[i] - 32) / 8;
                else if (data_in[i] <= 48)
                    data_out[i] = YST6 + (YST6 - YST5) * (data_in[i] - 40) / 8;
                else if (data_in[i] <= 56)
                    data_out[i] = YST7 + (YST7 - YST6) * (data_in[i] - 48) / 8;
                else if (data_in[i] <= 64)
                    data_out[i] = YST8 + (YST8 - YST7) * (data_in[i] - 56) / 8;
                else if (data_in[i] <= 72)
                    data_out[i] = YST9 + (YST9 - YST8) * (data_in[i] - 64) / 8;
                else if (data_in[i] <= 80)
                    data_out[i] = YST10 + (YST10 - YST9) * (data_in[i] - 72) / 8;
                else if (data_in[i] <= 96)
                    data_out[i] = YST11 + (YST11 - YST10) * (data_in[i] - 80) / 16;
                else if (data_in[i] <= 112)
                    data_out[i] = YST12 + (YST12 - YST11) * (data_in[i] - 96) / 16;
                else if (data_in[i] <= 144)
                    data_out[i] = YST13 + (YST13 - YST12) * (data_in[i] - 112) / 32;
                else if (data_in[i] <= 176)
                    data_out[i] = YST14 + (YST14 - YST13) * (data_in[i] - 144) / 32;
                else if (data_in[i] <= 208)
                    data_out[i] = YST15 + (YST15 - YST14) * (data_in[i] - 176) / 32;
                else
                {
                    if (cb_manual.Checked == false)
                    {
                        data_out[i] = YST15 + YSLP15 * (data_in[i] - 208) / 64;


                    }
                    else
                    {

                        data_out[i] = YST15 + YSLP15 * (data_in[i] - 208) / 64;
                    }
                }
            }

            //int YSLP15 = 0x1B;
            //Yst15 + Yslp15 × (data - 208) / 64


            richTextBox1.Text += "In:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_in[i].ToString() + " ";
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Out:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_out[i].ToString() + " ";
            richTextBox1.Text += "\n";

            pictureBox1.Size = new Size(256 * 3, 256 * 2);   //改變圖框大小

            Pen redPen = new Pen(Color.Red, 3);

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;


                //curvePoints[i].X = i;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                //curvePoints[i].Y = 100;

            }

            // Draw lines between original points to screen.
            g.DrawLines(redPen, curvePoints);   //畫直線

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            pictureBox1.Image = bitmap1;
        }

        bool isDrawing = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;

            pictureBox1_MouseMove(sender, e);
        }

        bool isDoingMagnifying = false;
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            int region = 30;
            if (isMagnifying == true)
            {
                //pictureBox1擷取一小部分貼到pictureBox2上, 達到放大功能
                if (isDoingMagnifying == false)
                {
                    isDoingMagnifying = true;

                    if (((e.X - region * 2) < 0) || ((e.X + region * 2) > pictureBox1.Width))
                    {
                        isDoingMagnifying = false;
                        return;
                    }

                    if (((e.Y - region * 2) < 0) || ((e.Y + region * 2) > pictureBox1.Height))
                    {
                        isDoingMagnifying = false;
                        return;
                    }

                    RectangleF rect = new RectangleF(e.X, e.Y, 50, 50);

                    try
                    {
                        // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標, 起點y座標, 寬度, 高度)
                        // 將處理之後的圖片貼出來
                        pictureBox2.Image = bitmap1.Clone(rect, PixelFormat.Format32bppArgb);
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\t";
                        //richTextBox1.Text += "e.X = " + e.X.ToString() + ", e.Y = " + e.Y.ToString() + "\n";
                        //richTextBox1.Text += "t1 = " + (e.X - region).ToString() + ", t2 = " + (e.X + region).ToString() + "\n";
                        //richTextBox1.Text += "t3 = " + (e.Y - region).ToString() + ", t4 = " + (e.Y + region).ToString() + "\n";
                        //richTextBox1.Text += "W = " + pictureBox1.Width.ToString() + ", H = " + pictureBox1.Height.ToString() + "\n";
                    }
                    GC.Collect();       //回收資源
                    isDoingMagnifying = false;
                }
                return;
            }

            if (isDrawing == false)
                return;

            if (cb_snake.Checked == false)
                return;

            this.Text = e.X.ToString() + ", " + e.Y.ToString();
            int w = pictureBox1.Width;
            int h = pictureBox1.Height;
            int i;
            int j;
            int r;
            //g.Clear(Color.White);
            for (j = 0; j < h; j++)
            {
                if ((j > (e.Y - region)) && (j < (e.Y + region)))
                {
                    for (i = 0; i < w; i++)
                    {
                        if ((i > (e.X - region)) && (i < (e.X + region)))
                        {
                            r = (int)Math.Sqrt((e.X - i) * (e.X - i) + (e.Y - j) * (e.Y - j));
                            if (r < region)
                                bitmap1.SetPixel(i, j, Color.FromArgb(255 - r * (256 / region), 0xff, 0x0, 0x0));
                        }



                    }


                }

            }

            pictureBox1.Image = bitmap1;

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }

        private void cb_snake_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            //指定畫布大小
            pictureBox1.Width = 600;
            pictureBox1.Height = 600;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            p = new Pen(Color.Red, 3);     // 設定畫筆為紅色、粗細為 3 點。

            if (cb_snake.Checked == true)
            {
                g.Clear(Color.Lime);
            }
            else
            {
                g.Clear(Color.Pink);
            }
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            int width = pictureBox1.Width;
            int height = pictureBox1.Height;

            //把PictureBox上的東西匯出至檔案
            Bitmap bm = new Bitmap(width, height);
            pictureBox1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));   //匯出全部, 可以在此選擇匯出區域

            string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
            string filename1 = filename + ".jpg";
            string filename2 = filename + ".bmp";
            string filename3 = filename + ".png";

            try
            {
                bm.Save(@filename1, ImageFormat.Jpeg);
                bm.Save(@filename2, ImageFormat.Bmp);
                bm.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        bool isMagnifying = false;
        private void cb_magnifying_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_magnifying.Checked == true)
                isMagnifying = true;
            else
                isMagnifying = false;
        }

    }
}
