using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace CH1613
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender,
              PaintEventArgs pe)
        {
            HatchBrush brush;
            Font myFont;
            Graphics gs = pe.Graphics;//宣告Graphics物件
            brush = new HatchBrush(
               HatchStyle.DashedDownwardDiagonal,
               Color.Black, Color.Red);
            myFont = new Font("Arial", 25, FontStyle.Bold);
            gs.DrawString("Visual Studio", myFont,
               brush, new PointF(20, 10));
            brush = new HatchBrush(
               HatchStyle.DarkUpwardDiagonal,
               Color.Black, Color.Blue);
            myFont = new Font("Garamond", 16,
               FontStyle.Strikeout);
            gs.DrawString("Visual Studio I love it.",
               myFont, brush, new PointF(10, 60));
            brush = new HatchBrush(
               HatchStyle.DashedDownwardDiagonal,
               Color.Black, Color.Green);
            myFont = new Font("Broadway", 22,
               FontStyle.Underline);
            gs.DrawString(".NET Framework", myFont,
               brush, new PointF(30, 100));
        }
    }
}
