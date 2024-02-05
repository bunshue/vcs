using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser9_pdf
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 170 + 10;
            dy = 70 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);


            webBrowser1.Size = new Size(500, 500);
            webBrowser1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(250, 500);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            string pdf_filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_7_free\vcs_MyPdfReader\vcs_MyPdfReader\bin\Debug\Python簡介.pdf";

            richTextBox1.Text += "檔案 : " + pdf_filename + "\n";

            int pdf_page = 1;   //從1開始

            //1. 無參數
            //webBrowser1.Navigate(pdf_filename);

            //2.
            //webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0");

            //3. 加頁數
            //webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0&page=" + pdf_page.ToString());

            //webBrowser1.Navigate(pdf_filename + "?#initZoom = fitToPage & view = fit & navpanes = 0 & toolbar = 0 & page = " + pdf_page.ToString());


            //顯示比例 %
            //webBrowser1.Navigate(pdf_filename + "?#page=1 & zoom = 100");

            //webBrowser1.Navigate(pdf_filename + "?#page=1 & zoom = 100, 0, 200");


            //webBrowser1.Navigate(pdf_filename + "?#page=1 & zoom = 100, 0, 200");

            webBrowser1.Navigate(pdf_filename + "?#view = fitB");


            this.webBrowser1.Focus();



        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

    }
}
