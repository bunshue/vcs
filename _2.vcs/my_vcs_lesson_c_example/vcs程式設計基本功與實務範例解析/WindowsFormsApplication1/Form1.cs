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

        private void button1_Click(object sender, EventArgs e)
        {
            MyTime now = new MyTime();
            //now.Hour = 30;
            //now.Minute = 30;
            //now.Second = 30;

            // encapsulation
            now.setTime(30, 30, 30);

            label1.Text = now.getTime();

            // property: get and set
            now.mHour = 30;
            now.mMinute = 30;
            now.mSecond = 30;

            label1.Text += "\r\nHour = " + now.mHour + ", "
                         + "Minute = " + now.mMinute + ", "
                         + "Second = " + now.mSecond + "\r\n";
            
            // method overloading
            MyTime obj2 = new MyTime();
            obj2.setTime(21, 40);

            label1.Text += obj2.getTime() + "\r\n";

            // constructors
            MyTime t1 = new MyTime(9, 30, 50);
            MyTime t2 = new MyTime(21, 40);
            label1.Text += t1.getTime() + "\r\n";
            label1.Text += t2.getTime() + "\r\n";
            
            // 物件陣列

            MyTime[] tArray = new MyTime[3];
            tArray[0] = new MyTime();
            tArray[0].setTime(21, 40);
            tArray[1] = new MyTime(9, 30, 50);
            tArray[2] = new MyTime(10, 30, 30);

            for(int i = 0; i < 3; i++)
                label1.Text += "物件" + i + ": " + tArray[i].getTime() + "\r\n";


            //System.GC.Collect();
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
      
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        
    }
}
