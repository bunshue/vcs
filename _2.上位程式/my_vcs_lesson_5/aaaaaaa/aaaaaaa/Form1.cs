using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;   //for ImageFormat

namespace aaaaaaa
{
    public partial class Form1 : Form
    {
        Graphics g;                 // 繪圖區
        Pen pen;                    // 畫筆
        bool isMouseDown = false;   // 紀錄滑鼠是否被按下
        List<Point> points = new List<Point>(); // 紀錄滑鼠軌跡的陣列。        
        
        public Form1()
        {
            InitializeComponent();

            /*
            //測試沒有標題沒有邊框的Form
            this.Text = string.Empty;
            this.ControlBox = false;
            */
            g = this.CreateGraphics(); // 取得繪圖區物件
            pen = new Pen(Color.Black, 3); // 設定畫筆為黑色、粗細為 3 點。
        }

        private void panel1_MouseHover(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.VSplit;
            //label2.Text = "(" + MousePosition.X.ToString() + ", " + MousePosition.Y.ToString();
            //label2.Text = "(" + System.Windows.Forms.Cursor.Position.X.ToString() + ", " + System.Windows.Forms.Cursor.Position.Y.ToString() + ")";

        }

        private void panel1_MouseLeave(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.Default;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Bitmap Thepic;
            //Thepic = new Bitmap(panel1.ClientRectangle.Width, this.ClientRectangle.Height);

            richTextBox1.Text += "image W = " + this.panel1.BackgroundImage.Size.Width.ToString() + "\n";
            richTextBox1.Text += "image H = " + this.panel1.BackgroundImage.Size.Height.ToString() + "\n";

            //this.panel1.Size.Width = this.panel1.BackgroundImage.Size.Width + 10;
            //this.panel1.Size.Height = this.panel1.BackgroundImage.Size.Height + 10;

            this.panel1.Width = this.panel1.BackgroundImage.Size.Width + 0;
            this.panel1.Height = this.panel1.BackgroundImage.Size.Height + 0;

            richTextBox1.Text += "image W = " + this.panel1.BackgroundImage.Size.Width.ToString() + "\n";
            richTextBox1.Text += "image H = " + this.panel1.BackgroundImage.Size.Height.ToString() + "\n";
            
            int width = panel1.Size.Width;
            int height = panel1.Size.Height;


            richTextBox1.Text += "panel W = " + width.ToString() + "\n";
            richTextBox1.Text += "panel H = " + height.ToString() + "\n";

            Graphics g = panel1.CreateGraphics();
            pen = new Pen(Color.Black, 3); // 設定畫筆為黑色、粗細為 3 點。
            g.DrawRectangle(pen, 50, 50, 100, 100);  //繪製100×100矩形
            
            Bitmap bm = new Bitmap(width, height);
            panel1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));
            bm.Save(@"D:\aaaaaaa.jpg", ImageFormat.Jpeg);
            bm.Save(@"D:\aaaaaaa.bmp", ImageFormat.Bmp);
            bm.Save(@"D:\aaaaaaa.png", ImageFormat.Png);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "there are " + FontFamily.Families.Length.ToString() + " fonts\n";
            for (int i = 0; i < FontFamily.Families.Length; i++)
            //for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + FontFamily.Families[i].Name + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.panel1.BackgroundImage = null;

            this.panel1.Width = 100;
            this.panel1.Height = 100;
            this.panel1.BackColor = Color.Green;

            int width = panel1.Size.Width;
            int height = panel1.Size.Height;


            richTextBox1.Text += "panel W = " + width.ToString() + "\n";
            richTextBox1.Text += "panel H = " + height.ToString() + "\n";

            Bitmap bm = new Bitmap(width, height);
            panel1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));
            bm.Save(@"D:\aaaaaaa.jpg", ImageFormat.Jpeg);
            bm.Save(@"D:\aaaaaaa.bmp", ImageFormat.Bmp);
            bm.Save(@"D:\aaaaaaa.png", ImageFormat.Png);
        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox2.Text += "you pressed" + Keys.F3
            if (e.KeyCode == Keys.F3)
            {
                richTextBox2.Text += "F3\n";


                // 使用System.Text.RegularExpressions來搜尋指定字串

                string strTxt = richTextBox1.Text;   // 準備要搜尋的來源字串
                string strKey = "範圍";              // 指定字串

                richTextBox2.Text += "strKey = " + strKey + "\tLength = " + strKey.Length.ToString() + "\n";

                //richTextBox2.Text += "strTxt = " + strTxt + "\n";
                //richTextBox2.Text += "strKey = " + strKey + "\n";


                System.Text.RegularExpressions.MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(strTxt, strKey);
                foreach (System.Text.RegularExpressions.Match m in matches)
                {
                    //lstIndex.Items.Add(m.Index);  // 將搜尋結果index顯示於ListBox中
                    richTextBox2.Text += "aaa" + m.Index.ToString() + "\n";
                    richTextBox1.SelectionStart = m.Index;
                    richTextBox1.SelectionLength = strKey.Length;
                }

            }
        }

        private void richTextBox1_SelectionChanged(object sender, EventArgs e)
        {
            // 將RichTextBox中選取的文字，透過 FontFamily 類別 
            // 同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic 
            Font MyFont = new Font(new FontFamily("標楷體"), 18, FontStyle.Bold | FontStyle.Italic);
            //this.richTextBox1.Font = DefaultFont; fail
            this.richTextBox1.SelectionFont = MyFont;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            richTextBox2.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 原始影像，顯示於pictureBox1
            Bitmap bmpOrg = new Bitmap("D:\\bear.jpg");
            this.panel1.BackgroundImage = bmpOrg;
            // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標20, 起點y座標20, 寬度50, 高度50)
            Bitmap bmpClone = bmpOrg.Clone(new Rectangle(200, 100, 50, 50), bmpOrg.PixelFormat);
            this.panel2.BackgroundImage = bmpClone;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {

        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            label2.Text = "(" + System.Windows.Forms.Cursor.Position.X.ToString() + ", " + System.Windows.Forms.Cursor.Position.Y.ToString() + ")";
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDown = true; // 滑鼠被按下後設定旗標值。
            points.Add(e.Location); // 將點加入到 points 陣列當中。
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown) // 如果滑鼠被按下
            {
                points.Add(e.Location); // 將點加入到 points 陣列當中。
                // 畫出上一點到此點的線段。
                //g.DrawLine(pen, points[points.Count - 2], points[points.Count - 1]);
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            points.Add(new Point(-1, -1)); // 滑鼠放開時，插入一個斷點 (-1,-1)，以代表前後兩點之間有斷開。
            isMouseDown = false; // 滑鼠已經沒有被按下了。
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            for (int i = 0; i < points.Count - 1; i++)
            {
                if (points[i].X >= 0 && points[i + 1].X >= 0)
                    g.DrawLine(pen, points[i], points[i + 1]);
            }

        }
        

        /*
        private void button6_Click(object sender, EventArgs e)
        {
            Graphics m_graphics = pictureBox1.CreateGraphics();
            m_graphics.Clear(Color.Purple);

            Pen pen = new Pen(Color.Red, 5); //畫筆

            m_graphics.DrawRectangle(pen, 50, 50, 100, 100);  //繪製100×100矩形
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Graphics m_graphics = this.CreateGraphics();
            m_graphics.Clear(Color.Red);
        }
        */

  
    }
}
