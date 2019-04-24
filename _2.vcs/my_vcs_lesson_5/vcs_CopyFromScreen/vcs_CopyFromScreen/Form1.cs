using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_CopyFromScreen
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //全螢幕截圖
            Bitmap myImage = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            Graphics g = Graphics.FromImage(myImage);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);

            String file = Application.StartupPath + "\\image_full_" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            myImage.Save(file);
            richTextBox1.Text += "全螢幕截圖，存檔檔名：" + file + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //本程式截圖
            Bitmap myImage = new Bitmap(this.Width, this.Height);
            Graphics g = Graphics.FromImage(myImage);
            //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(this.Width, this.Height));
            richTextBox1.Text += "W = " + this.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + this.Height.ToString() + "\n";
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            String file = Application.StartupPath + "\\image_my_" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            myImage.Save(file);
            richTextBox1.Text += "本程式截圖，存檔檔名：" + file + "\n";

        }
    }
}
