using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Continue
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int num = 0;
            string msg = "1到20中不是3的倍數的整數：\n";
            do    //do...while迴圈
            {
                num++;  //num加1
                if (num % 3 == 0)   //若num能被3整除
                    continue;   //跳到while
                msg += num.ToString() + ",";    //將num加到msg字串中
            } while (num <= 20);    //當num <= 20就繼續迴圈
            MessageBox.Show(msg);   //顯示msg字串
            Application.Exit();
        }
    }
}
