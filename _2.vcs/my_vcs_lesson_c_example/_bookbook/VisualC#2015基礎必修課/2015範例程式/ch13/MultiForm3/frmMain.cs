using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MultiForm3
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private void frmMain_Load(object sender, EventArgs e)
        {
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            int myMoney = 0, myYear = 0;
            double myRate = 0;
            try
            {
                myMoney = Convert.ToInt32(txtMoney.Text);
                myYear = Convert.ToInt32(txtYear.Text);
                myRate = Convert.ToDouble(txtRate.Text) / 100;
            }
            catch (Exception ex)
            {
                MessageBox.Show("請輸入正確的數值資料");
                return;
            }

            frmCal f = new frmCal(); //宣告並建立frmCal表單類別的f物件

            //使用ShowDialog()方法使 f 以強制回應形式顯示表單
            f.ShowDialog();

            //使用他表單的函數的寫法

            //呼叫frmCal的Cal方法以計算配息方式
            richTextBox1.Text += myYear.ToString() + " 年後領回本利和：" + f.Cal(myMoney, myYear, myRate).ToString() + "\n";
        }
    }
}
