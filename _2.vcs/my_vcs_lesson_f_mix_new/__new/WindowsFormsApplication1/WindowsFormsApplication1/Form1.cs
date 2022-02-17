using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        [System.Runtime.InteropServices.DllImportAttribute("gdi32.dll")]

private static extern bool BitBlt(

IntPtr hdcDest, //目的DC的句柄

int nXDest, //目的圖形的左上角的x坐標

int nYDest, //目的圖形的左上角的y坐標

int nWidth, //目的圖形的矩形寬度

int nHeight, //目的圖形的矩形高度

IntPtr hdcSrc, //源DC的句柄

int nXSrc, //源圖形的左上角的x坐標

int nYSrc, //源圖形的左上角的x坐標

System.Int32 dwRop //光柵操作代碼

);

 


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //

            // button1

            //

            this.button1.BackColor = System.Drawing.SystemColors.ActiveBorder;

            this.button1.ForeColor = System.Drawing.SystemColors.ControlDarkDark;

            this.button1.Location = new System.Drawing.Point(272, 19);

            this.button1.Name = "button1";

            this.button1.Size = new System.Drawing.Size(72, 27);

            this.button1.TabIndex = 4;

            this.button1.Text = "屏幕捕捉";

            this.button1.Click += new System.EventHandler(this.button1_Click);

            //

            // pictureBox1

            //

            //this.pictureBox1.Image = ((System.Drawing.Bitmap)(resources.GetObject("pictureBox1.Image")));

            this.pictureBox1.Location = new System.Drawing.Point(16, 16);

            this.pictureBox1.Name = "pictureBox1";

            this.pictureBox1.Size = new System.Drawing.Size(240, 224);

            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;

            this.pictureBox1.TabIndex = 0;

            this.pictureBox1.TabStop = false;

            //

            // Form1

            //

            this.AutoScaleBaseSize = new System.Drawing.Size(6, 14);

            this.ClientSize = new System.Drawing.Size(358, 255);

            this.Controls.AddRange(new System.Windows.Forms.Control[] {this.button1,this.pictureBox1});

            this.KeyPreview = true;

            this.Name = "Form1";

            this.Text = "屏幕捕捉程序";

            this.ResumeLayout(false);


        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g1 = this.CreateGraphics();//獲得窗體圖形對象

            Image MyImage = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height, g1);

            Graphics g2 = Graphics.FromImage(MyImage);//創建位圖圖形對象

            IntPtr dc1 = g1.GetHdc();//獲得窗體的上下文設備

            IntPtr dc2 = g2.GetHdc();//獲得位圖文件的上下文設備

            BitBlt(dc2, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height, dc1, 0, 0, 13369376);//寫入到位圖

            g1.ReleaseHdc(dc1);//釋放窗體的上下文設備

            g2.ReleaseHdc(dc2);//釋放位圖文件的上下文設備

            MyImage.Save("aaaa.jpg", ImageFormat.Jpeg);//保存為jpeg文件

            MessageBox.Show("保存圖片結束！");

        }
    }
}
