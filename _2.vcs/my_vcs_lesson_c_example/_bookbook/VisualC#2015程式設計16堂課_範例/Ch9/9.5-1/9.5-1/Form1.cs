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

        private void startButton_Click(object sender, EventArgs e)
        {
            int length = int.Parse(listLength.Text);
            long[] fibonacci = new long[length];

            for(int i=0; i< length; i++){
                if(i == 0 || i ==1)
                    fibonacci[i] = 1;
                else
                    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];
            }

            finalList.Items.Clear();
            for (int i = 0; i < length; i++)
                finalList.Items.Add(fibonacci[i]);

        }

    }
}
