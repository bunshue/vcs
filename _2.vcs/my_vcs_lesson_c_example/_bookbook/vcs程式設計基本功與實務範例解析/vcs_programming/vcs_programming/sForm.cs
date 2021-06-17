using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class sForm : Form
    {
        internal Student sObj; //讓主選單可以取得此Student物件

        public sForm()
        {
            InitializeComponent();
        }

        private void sForm_Load(object sender, EventArgs e)
        {

        }

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

            int c = Convert.ToInt32(txtChinese.Text);
            int ma = Convert.ToInt32(txtMath.Text);

            sObj = new Student(name, age, gender, date, c, ma);
        }

    }
}
