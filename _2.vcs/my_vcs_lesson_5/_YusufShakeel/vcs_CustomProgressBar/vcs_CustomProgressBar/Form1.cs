using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_CustomProgressBar
{
    public partial class Form1 : Form
    {
        double pbUnit;
        int pbWIDTH, pbHEIGHT, pbComplete;

        Bitmap bmp;
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //get picboxPB dimension
            pbWIDTH = pictureBox1.Width;
            pbHEIGHT = pictureBox1.Height;

            pbUnit = pbWIDTH / 100.0;

            //pbComplete - This is equal to work completed in % [min = 0 max = 100]
            pbComplete = 0;

            //create bitmap
            bmp = new Bitmap(pbWIDTH, pbHEIGHT);

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //graphics
            g = Graphics.FromImage(bmp);	// 取得繪圖區物件

            //clear graphics
            g.Clear(Color.LightSkyBlue);

            //draw progressbar
            g.FillRectangle(Brushes.CornflowerBlue, new Rectangle(0, 0, (int)(pbComplete * pbUnit), pbHEIGHT));

            //draw % complete
            g.DrawString(pbComplete + "%", new Font("Arial", pbHEIGHT / 2), Brushes.Black, new PointF(pbWIDTH / 2 - pbHEIGHT, pbHEIGHT / 10));

            //load bitmap in picturebox picboxPB
            pictureBox1.Image = bmp;

            //update pbComplete
            //Note!
            //To keep things simple I am adding +1 to pbComplete every 50ms
            //You can change this as per your requirement :)
            pbComplete++;
            if (pbComplete > 100)
            {
                //dispose
                g.Dispose();
                timer1.Stop();
            }

        }
    }
}
