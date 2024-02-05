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
        string pdf_filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_7_free\vcs_MyPdfReader\vcs_MyPdfReader\bin\Debug\Python簡介.pdf";

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
            richTextBox1.Text += "無參數\n";
            webBrowser1.Navigate(pdf_filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int pdf_page = 3;   //從1開始

            richTextBox1.Text += "加頁數\n";
            webBrowser1.Navigate(pdf_filename + "?#page=" + pdf_page.ToString());
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "顯示比例, 15%\n";
            //webBrowser1.Navigate(pdf_filename + "?#page=1 & zoom = 15");

            //richTextBox1.Text += "顯示比例, 40%\n";
            //webBrowser1.Navigate(pdf_filename + "?#page=1 & zoom = 40");

            richTextBox1.Text += "顯示比例, 60%, 並指定顯示位置\n";
            webBrowser1.Navigate(pdf_filename + "?#page=1 & zoom = 60, 300, 300");


            /*
            zoom 可選
            zoom = scale
            zoom = scale, left, top
            */

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "顯示toolbar\n";
            //webBrowser1.Navigate(pdf_filename + "?#toolbar = 1");

            richTextBox1.Text += "不顯示toolbar\n";
            webBrowser1.Navigate(pdf_filename + "?#toolbar = 0");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "顯示navpanes\n";
            webBrowser1.Navigate(pdf_filename + "?#navpanes = 1");

            //richTextBox1.Text += "不顯示navpanes\n";
            //webBrowser1.Navigate(pdf_filename + "?#navpanes = 0");

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //initZoom
            webBrowser1.Navigate(pdf_filename + "?#initZoom = fitToPage");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //webBrowser1.Navigate(pdf_filename + "?#initZoom = fitToPage & view = fit & navpanes = 0 & toolbar = 0");
            int pdf_page = 3;

            webBrowser1.Navigate(pdf_filename + "?#initZoom = fitToPage & view = fit & navpanes = 0 & toolbar = 0 & page = " + pdf_page.ToString());

            /*            
            view 可選
            fit
            fitH / fitH,top
            fitV / fitV,left
            fitB
            fitBH / fitBH,top
            fitBV / fitBV,left
            */

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //其他 TBD

            /*
            filename.pdf#view=FitH
             <embed src="filename.pdf?zoom=50" width="575" height="500">


            webBrowser1.Navigate(pdf_filename + "?#initZoom = fitToPage & view = fit & navpanes = 0 & toolbar = 0 & page = " + pdf_page.ToString());

            viewrect = left, top, wd, ht	#測不出來

            & navpanes=0 & toolbar=0"

            #toolbar=1 & navpanes=0 & scrollbar=1 & 



            #zoom=scale', like this:


            <object data="/path/to/file.pdf#zoom=scale" type="application/pdf">
            </object>

            */





        }

    }
}
