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

        private void convertButton_Click(object sender, EventArgs e)
        {
            int month;
            month = int.Parse(monthText.Text);

            if (month > 12 || month < 1)
                seasonText.Text = "無法判斷";
            else { 

                switch(month%3){
                    case 1:
                        seasonText.Text = "孟";
                        break;
                    case 2:
                        seasonText.Text = "仲";
                        break;
                    case 0:
                        seasonText.Text = "季";
                        break;
                }

                switch ((month-1)/3)
                {
                    case 0:
                        seasonText.Text += "春";
                        break;
                    case 1:
                        seasonText.Text += "夏";
                        break;
                    case 2:
                        seasonText.Text += "秋";
                        break;
                    case 3:
                        seasonText.Text += "冬";
                        break;
                }

            }
        }

    }
}
