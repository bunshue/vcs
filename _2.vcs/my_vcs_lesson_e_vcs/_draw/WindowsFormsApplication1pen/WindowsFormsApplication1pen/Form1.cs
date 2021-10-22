using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//Pen測試

namespace WindowsFormsApplication1pen
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

        private void button1_Click(object sender, EventArgs e)
        {
            System.Random r = new System.Random();
            Graphics g;
            g = this.CreateGraphics();
            /*         while(true)
                      {
                          int x1 = r.Next(0, 1366);
                          int y1 = r.Next(0, 200);
                          int x2 = x1;
                          int y2 = y1 + r.Next(0, 400);
                          for(int i=y1;i<=y2;i++)
                          {
                              Pen greenPen = new Pen(Color.Green, r.Next(1, 15));
                              g.DrawLine(greenPen, x1, y1, x2, y2);
                          }
                      }
           */
            for (int i = 0; i < 5000; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 8);
                int x1 = r.Next(100, 300);
                int y1 = r.Next(100, 500);
                int x2 = r.Next(100, 300);
                int y2 = r.Next(100, 500);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }
            for (int i = 0; i < 5000; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 9);
                int x1 = 500; //650-900
                int y1 = 300; //100-500
                int x2 = r.Next(400, 600);
                int y2 = r.Next(100, 500);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }
            for (int i = 0; i < 5000; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 10);
                int x1 = 900; //650-900
                int y1 = 100; //100-500
                int x2 = r.Next(700, 900);
                int y2 = r.Next(100, 500);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }
            for (int i = 0; i < 5000; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 11);
                int x1 = 1000; //650-900
                int y1 = 500; //100-500
                int x2 = r.Next(1000, 1200);
                int y2 = r.Next(100, 500);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }
            for (int i = 0; i < 5000; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 12);
                int x1 = r.Next(100, 1200); ; //650-900
                int y1 = r.Next(600, 700); ; //100-500
                int x2 = r.Next(100, 1200);
                int y2 = r.Next(600, 700);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }
            for (int i = 0; i < 5000; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), r.Next(1, 15));
                int x1 = r.Next(100, 1200); ; //650-900
                int y1 = r.Next(600, 700); ; //100-500
                int x2 = r.Next(100, 1200);
                int y2 = r.Next(600, 700);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }  

        }
    }
}
