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
    public partial class DateForm : Form
    {
        public DateForm()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            lblOutput.Text = "";
            txtYear.Text = "";
            txtMonth.Text = "";
            txtDay.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int y = Convert.ToInt32(txtYear.Text);
            int m = Convert.ToInt32(txtMonth.Text);
            int d = Convert.ToInt32(txtDay.Text);

            Date date = new Date();
            date.setDate(d, m, y);
            
            //Date date = new Date(d, m, y);

            lblOutput.Text = date.show();

        }

        private void DateForm_Load(object sender, EventArgs e)
        {

        }
    }
}
