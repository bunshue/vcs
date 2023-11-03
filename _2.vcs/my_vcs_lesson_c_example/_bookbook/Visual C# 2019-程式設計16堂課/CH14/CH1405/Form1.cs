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
using System.IO;

namespace CH1405
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnPrint_Click(object sender, EventArgs e)
        {
            try
            {
                OnPaper.Print();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        //PrintDocument的事件
        private void OnPaper_PrintPage(object sender,
           PrintPageEventArgs ev)
        {
            //1.建立繪圖物件gs和參數ev的關聯
            Graphics gs = ev.Graphics;
            //設定列印字型
            Font fontPrint = new Font("Segoe Print", 14);
            int morePages = 0; //計算每份文件頁數
            int OnPageChars = 0;//計算每頁字元數
                                //2.測量要繪製的字串
            gs.MeasureString(rtxtShow.Text,
               fontPrint, ev.MarginBounds.Size,
               StringFormat.GenericTypographic,
               out OnPageChars, out morePages);
            //3.繪製邊界內的字型
            gs.DrawString(rtxtShow.Text, fontPrint,
               Brushes.Black, ev.MarginBounds,
               new StringFormat());
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            rtxtShow.LoadFile("D:\\C#Lab\\Demo01.rtf");
            OnPaper.DocumentName = "CH1405";
        }
    }
}
