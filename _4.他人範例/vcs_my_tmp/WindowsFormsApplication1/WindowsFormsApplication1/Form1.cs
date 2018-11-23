using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Width = this.ClientSize.Width - 20;
            pictureBox1.Height = this.ClientSize.Height - 20;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int index = comboBox1.SelectedIndex;
            richTextBox1.Text += "index = " + index.ToString() + "\n";
            switch (index)
            {
                case 0: pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 1: pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 2: pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 3: pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 4: pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;
                default: break;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.SelectedIndex = 4;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DrawCircle(200, 200, 100);

            Graphics g = pictureBox1.CreateGraphics();
            Pen pen;
            Font font;
            Brush brush;

            pen = new Pen(Color.Black, 3);	// 設定畫筆為黑色、粗細為 3 點。
            font = new Font("標楷體", 16);
            brush = new SolidBrush(Color.Black);

            g.DrawLine(pen, new Point(1, 1), new Point(300, 100));
            g.DrawRectangle(pen, new Rectangle(50, 50, 100, 100));
            g.DrawString("Hello! 你好！", font, brush, new PointF(150.0F, 150.0F));
            g.DrawString("Hello! 你好！", font, brush, 50.0F, 50.0F);



        }
    }
}
