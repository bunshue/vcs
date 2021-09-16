using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_2_51
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            maskedTextBox1.Mask = "00/00/0000";
            maskedTextBox1.ValidatingType = typeof(System.DateTime);
        }

        private void maskedTextBox1_TypeValidationCompleted(
            object sender, TypeValidationEventArgs e)
        {
            if (!e.IsValidInput)
                textBox1.Text = "資料格式錯誤 ！";
            else
            {
                DateTime userDate = (DateTime)e.ReturnValue;
                if (userDate < DateTime.Now)
                {
                    textBox1.Text = "資料格式正確，但值不對 ！";
                    e.Cancel = true;
                }
            }
        }
    }
}
