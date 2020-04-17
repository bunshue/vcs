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
    public partial class CallByRef : Form
    {
        public CallByRef()
        {
            InitializeComponent();
        }
        
        void swap(int a, int b)
        {
            int t = a;
            a = b;
            b = t;
        }
        
        void swap(ref int a, ref int b)
        {
            int t = a;
            a = b;
            b = t;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = 10, b = 5;

            lblBeforeSwap.Text = "交換前: a = " + a + ", b = " + b;
            swap(a, b);
            lblAfterSwap.Text = "交換後: a = " + a + ", b = " + b;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int a = 10, b = 5;

            lblBeforeSwap.Text = "交換前: a = " + a + ", b = " + b;
            swap(ref a, ref b);
            lblAfterSwap.Text = "交換後: a = " + a + ", b = " + b;
        }
    }
}
