using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Printing;

/*
printDocument2
改DocumentName

printDialog2
改Document為printDocument2
*/

namespace CH1406
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnPrint_Click(object sender, EventArgs e)
        {
            //對話方塊啟用頁數核取方塊
            dlgPrint.AllowSomePages = true;
            //對話方塊啟用說明按鈕
            dlgPrint.ShowHelp = true;
            //列印對話方塊中，按下確定鈕的話
            DialogResult result = dlgPrint.ShowDialog();
            if (result == DialogResult.OK)
            {
                OnPaper.Print();
            }
        }

        private void OnPaper_PrintPage(object sender, PrintPageEventArgs e)
        {
            string text = "千江有水千月，萬里晴空萬里晴";
            Font oneFont = new Font("標楷體", 35, FontStyle.Bold);
            e.Graphics.DrawString(text, oneFont, Brushes.Blue, 10, 10);
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
