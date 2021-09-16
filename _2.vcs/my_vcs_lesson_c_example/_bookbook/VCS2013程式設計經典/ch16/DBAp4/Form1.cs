using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DBAp4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO:  這行程式碼會將資料載入 'myDBDataSet.員工' 資料表。您可以視需要進行移動或移除。
            this.員工TableAdapter.Fill(this.myDBDataSet.員工);
            // TODO:  這行程式碼會將資料載入 'myDBDataSet.部門' 資料表。您可以視需要進行移動或移除。
            this.部門TableAdapter.Fill(this.myDBDataSet.部門);

        }
    }
}
