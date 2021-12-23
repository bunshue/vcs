using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PrintDialog
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

        private void button1_Click(object sender, EventArgs e)
        {
            printDialog1.AllowCurrentPage = true;       //顯示當前頁
            printDialog1.AllowPrintToFile = true;       //允許選擇打印到文件
            printDialog1.AllowSelection = true;         //啟用“選擇”單選按鈕
            printDialog1.AllowSomePages = true;         //啟用“頁”單選按鈕
            //printDialog1.Document = printDocument1;   //指定設置的PrintDocument對象
            //printDialog1.PrinterSettings = printDocument1.PrinterSettings;    //打印頁的默認設置
            printDialog1.PrintToFile = false;           //不選擇“打印到文件”
            printDialog1.ShowHelp = true;               //顯示“幫助”按鈕
            printDialog1.ShowNetwork = true;            //可以選擇網絡打印機
            if (printDialog1.ShowDialog() == DialogResult.OK)
            {
                //printDocument1.Print();    //打印
            }
            else
            {
            }
        }
    }
}
