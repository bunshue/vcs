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

            string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
            string filename1 = filename + ".jpg";
            string filename2 = filename + ".bmp";
            string filename3 = filename + ".png";

            bm.Save(@filename1, ImageFormat.Jpeg);
            bm.Save(@filename2, ImageFormat.Bmp);
            bm.Save(@filename3, ImageFormat.Png);

            richTextBox1.Text += "存檔完成\n";
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
            /*  修改panel上的內容
            this.panel1.BackgroundImage = null;

            this.panel1.Width = 100;
            this.panel1.Height = 100;
            this.panel1.BackColor = Color.Red;
            */

            int width = panel1.Size.Width;
            int height = panel1.Size.Height;


            //richTextBox1.Text += "panel W = " + width.ToString() + "\n";
            //richTextBox1.Text += "panel H = " + height.ToString() + "\n";

            //把Panel上的東西匯出至檔案
            Bitmap bm = new Bitmap(width, height);
            panel1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));

            string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
            string filename1 = filename + ".jpg";
            string filename2 = filename + ".bmp";
            string filename3 = filename + ".png";

            bm.Save(@filename1, ImageFormat.Jpeg);
            bm.Save(@filename2, ImageFormat.Bmp);
            bm.Save(@filename3, ImageFormat.Png);

            richTextBox1.Text += "存檔完成\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //panel1擷取一小部分貼到panel2上
            // 原始影像，顯示於pictureBox1
            Bitmap bmpOrg = new Bitmap(@"C:\______test_files\bear.jpg");
            this.panel1.BackgroundImage = bmpOrg;

            // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標20, 起點y座標20, 寬度50, 高度50)
            Bitmap bmpClone = bmpOrg.Clone(new Rectangle(200, 100, 50, 50), bmpOrg.PixelFormat);
            this.panel2.BackgroundImage = bmpClone;
        }

    }
}
