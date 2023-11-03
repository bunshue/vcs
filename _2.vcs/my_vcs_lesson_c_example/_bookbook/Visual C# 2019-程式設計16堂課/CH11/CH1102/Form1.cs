using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1102
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            btnOpen.Enabled = false;   //開啟按鈕控制項無作用
                                       //文字方塊擴充表單上方
            rtxtShow.Dock = DockStyle.Top;
            //載入檔案
            rtxtShow.LoadFile("D:\\C#Lab\\CH11\\Demo01.rtf");
            //取得載入檔案的總字串長度
            int result = rtxtShow.TextLength;
            MessageBox.Show($"字串長度{result}");
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            //儲存檔案
            rtxtShow.SaveFile("D:\\C#CLab\\CH11\\Change.rtf",
               RichTextBoxStreamType.RichText);
            int result = rtxtShow.TextLength;
            MessageBox.Show($"字串長度{result}");
        }
    }
}
