using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh8_6_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 這行程式碼會將資料載入 'NorthwindDataSet.員工' 資料表。您可以視需要進行移動或移除。
            this.員工TableAdapter.Fill(this.NorthwindDataSet.員工);

            this.reportViewer1.RefreshReport();
        }
    }
}
