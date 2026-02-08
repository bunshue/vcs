using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinPrint
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //  === 表單載入時會執行
        private void Form1_Load(object sender, EventArgs e)
        {
            printPreviewDialog1.Document = printDocument1;
            printDialog1.Document = printDocument1;
            pageSetupDialog1.Document = printDocument1;
            textBox1.ScrollBars = ScrollBars.Both;
            textBox1.Font = new Font("標楷體", 12, FontStyle.Regular);
        }

        //  ===  版面設定按鈕被按時會執行
        private void btnSetup_Click(object sender, EventArgs e)
        {
            if (pageSetupDialog1.ShowDialog() == DialogResult.OK)
            {
                printDocument1.DefaultPageSettings =
                    pageSetupDialog1.PageSettings;
            }
        }

        //  ===  預覽列印按鈕被按時會執行
        private void btnPreview_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.ShowDialog();
        }

        //  ===  列印按鈕被按時會執行
        private void btnPrint_Click(object sender, EventArgs e)
        {
            if (printDialog1.ShowDialog() == DialogResult.OK)
            {
                //Print()方法會觸動PrintDocument控制項的PrintPage事件
                printDocument1.Print();
            }
        }

        //  ===  當printDocument.Print()方法被執行時會被觸發
        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            Graphics prnGraph = e.Graphics;
            Font prnFont = new Font(textBox1.Font.Name, textBox1.Font.Size, textBox1.Font.Style);
            SolidBrush prnBrush = new SolidBrush(textBox1.ForeColor);
            Single left = printDocument1.DefaultPageSettings.Margins.Left - 10;
            Single top = printDocument1.DefaultPageSettings.Margins.Top - 20;
            prnGraph.DrawString(textBox1.Text, prnFont, prnBrush, left, top);
        }

        //  ===  結束按鈕被按時會執行
        private void btnEnd_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
