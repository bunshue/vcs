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
    public partial class tForm : Form
    {
        public tForm()
        {
            InitializeComponent();
        }

        internal Teacher tObj; //讓主選單可以取得此Teacher物件
                
        private void btnOK_Click(object sender, EventArgs e)
        {
            string name = txtName.Text;
            int age = Convert.ToInt32(txtAge.Text);

            char gender = '男';

            if (rdbMale.Checked) gender = '男';
            if (rdbFemale.Checked) gender = '女';

            int y = Convert.ToInt32(txtYear.Text);
            int m = Convert.ToInt32(txtMonth.Text);
            int d = Convert.ToInt32(txtDay.Text);

            Date date = new Date(d, m, y);

            string r = txtRank.Text;

            tObj = new Teacher(name, age, gender, date, r);
                       
        }
       
    }
}
