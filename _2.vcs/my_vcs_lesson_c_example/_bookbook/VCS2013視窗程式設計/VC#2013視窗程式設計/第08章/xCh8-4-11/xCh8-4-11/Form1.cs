using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh8_4_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 這行程式碼會將資料載入 '北風DataSet.訂單詳細資料' 資料表。您可以視需要進行移動或移除。
            this.訂單詳細資料TableAdapter.Fill(this.北風DataSet.訂單詳細資料);
            // TODO: 這行程式碼會將資料載入 '北風DataSet.訂單' 資料表。您可以視需要進行移動或移除。
            this.訂單TableAdapter.Fill(this.北風DataSet.訂單);
            // TODO: 這行程式碼會將資料載入 '北風DataSet.訂單' 資料表。您可以視需要進行移動或移除。
            this.訂單TableAdapter.Fill(this.北風DataSet.訂單);

        }
    }
}
