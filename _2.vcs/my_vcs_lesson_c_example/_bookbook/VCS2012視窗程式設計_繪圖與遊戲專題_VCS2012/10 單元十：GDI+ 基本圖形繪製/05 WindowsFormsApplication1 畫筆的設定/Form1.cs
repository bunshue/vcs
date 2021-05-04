using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for DashStyle LineCap

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Pen myPen = new Pen(Color.Red, 1);
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawLine(myPen, 0, 0, this.ClientSize.Width - 20, this.ClientSize.Height - 20);
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            RadioButton radioButton = (RadioButton)sender;
            if (radioButton.Checked == false) return;

            // 顏色選項
            if (radioButton == radioButton1)
                myPen.Color = Color.Red;
            else if (radioButton == radioButton2)
                myPen.Color = Color.Green;
            else if (radioButton == radioButton3)
                myPen.Color = Color.Blue;

            // 粗細選項
            else if (radioButton == radioButton4)
                myPen.Width = 1;
            else if (radioButton == radioButton5)
                myPen.Width = 5;
            else if (radioButton == radioButton6)
                myPen.Width = 10;

            // 樣式選項
            else if (radioButton == radioButton7)
                myPen.DashStyle = DashStyle.Solid; //實線
            else if (radioButton == radioButton8)
                myPen.DashStyle = DashStyle.Dash; //虛線
            else if (radioButton == radioButton9)
                myPen.DashStyle = DashStyle.Dot; //點線

            // 端點樣式選項
            else if (radioButton == radioButton10)
                myPen.EndCap = LineCap.Flat; // 扁平線條端點
            else if (radioButton == radioButton11)
                myPen.EndCap = LineCap.RoundAnchor; //圓形錨點端點
            else if (radioButton == radioButton12)
                myPen.EndCap = LineCap.SquareAnchor; //方形錨點線條端點

            this.Invalidate();
        }
    }
}