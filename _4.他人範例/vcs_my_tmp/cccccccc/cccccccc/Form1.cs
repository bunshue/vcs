using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace cccccccc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.panel1.Width = 400;
            this.panel1.Height = 300;
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            int i;
            for (i = 0; i < this.panel1.Height; i++)
            { 
                //this.panel1.

            
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            Color cc = new Color();

            cc = Color.Red;
            panel1.BackColor = cc;
            richTextBox1.Text += cc.R.ToString() + "," + cc.G.ToString() + "," + cc.B.ToString() + "\n";
            
            byte Alpha = 0xff;
            byte Red = 0x00;
            byte Green = 0xff;
            byte Blue = 0x00;
            cc = Color.FromArgb(Alpha, Red, Green, Blue);
            panel1.BackColor = cc;
            richTextBox1.Text += cc.R.ToString() + "," + cc.G.ToString() + "," + cc.B.ToString() + "\n";

            for (i = 0; i < this.panel1.Height; i++)
            {
                SolidBrush sBrush = new SolidBrush(cc);
                Pen pen new Pen(sBrush, 1);
                
                
                //e.Graph
            
            }



            /*
            SolidBrush SBrush = new SolidBrush(color);//实例化一个单色画笔类对象SBrush
            Pen pen = new Pen(SBrush, 1);//实例化一个用于绘制直线和曲线的对象pen
            e.Graphics.DrawRectangle(pen, this.ClientRectangle.X, intLocation, this.Width, intLocation + intHeight);//绘制图形
            intLocation = intLocation + intHeight;//重新为变量intLocation赋值
            */




        /*
          public Color GetColor(Point screenPoint)   
          {   
              IntPtr displayDC = CreateDC("DISPLAY",null,null,IntPtr.Zero);   
              uint   colorref   =   GetPixel(displayDC,screenPoint.X,screenPoint.Y);   
              DeleteDC(displayDC);   
              byte   Red   =   GetRValue(colorref);   
              byte   Green   =   GetGValue(colorref);   
              byte   Blue   =   GetBValue(colorref);   
              return Color.FromArgb(Red,   Green,   Blue);   
          }   
         */




        }
    }
}
