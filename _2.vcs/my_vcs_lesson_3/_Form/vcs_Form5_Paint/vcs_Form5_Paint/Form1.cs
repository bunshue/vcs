using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form5_Paint
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //直接寫一個OnPaint在此, 取代Form1_Paint

        private const string MENU_CAPTION = "用 OnPaint 寫字";
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);

            // Create the font we will use to draw the text.
            Font f = new Font("標楷體", 20, FontStyle.Bold);

            // See how big the text will be.
            SizeF text_size = e.Graphics.MeasureString(MENU_CAPTION, f);

            e.Graphics.FillRectangle(Brushes.Pink, 700, 100, 100, 100);

            e.Graphics.DrawString(MENU_CAPTION, f, Brushes.AliceBlue, 900, 100);

            e.Graphics.FillRectangle(Brushes.LightGray, 900, 200, 100, 100);

            // Draw the text.
            e.Graphics.DrawString(MENU_CAPTION, f, Brushes.Black, 900, 200);
        }



        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(new Pen(Color.Green, 10), new Rectangle(00, 00, this.ClientSize.Width - 1, this.ClientSize.Height - 1));    //畫邊框

            int x_st = 100;
            int y_st = 100;
            e.Graphics.DrawString("用 Form1_Paint 寫字", new Font("標楷體", 20, FontStyle.Italic), new SolidBrush(Color.Red), new RectangleF(new PointF(x_st, y_st), this.Size));

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

