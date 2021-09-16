using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 修改滑鼠停留在Label時的滑鼠游標的長相
            label1.Cursor = Cursors.Hand;

            // 動態修改Label的文字，並設定成便捷鍵N
            label1.Text = "姓名(&N)";
        }
    }
}
