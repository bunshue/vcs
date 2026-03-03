using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

namespace vcs_test_all_05_Print2
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

            printPreviewDialog0.Document = printDocument0;
            printDialog0.Document = printDocument0;
            pageSetupDialog0.Document = printDocument0;
            textBox1.ScrollBars = ScrollBars.Both;
            textBox1.Font = new Font("標楷體", 24, FontStyle.Regular);
            textBox1.Text =
                "老來多驚夢，" + Environment.NewLine +
                "似有獻刀人，" + Environment.NewLine +
                "醒來懼銅鏡，" + Environment.NewLine +
                "怕顯董賊身。";

        }

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 4);

            textBox1.Size = new Size(400, 300);
            textBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1300, 910);
            this.Text = "vcs_test_all_05_Print2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        private void printDocument0_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            Graphics g = e.Graphics;
            Font prnFont = new Font(textBox1.Font.Name, textBox1.Font.Size, textBox1.Font.Style);
            SolidBrush prnBrush = new SolidBrush(textBox1.ForeColor);
            Single left = printDocument0.DefaultPageSettings.Margins.Left - 10;
            Single top = printDocument0.DefaultPageSettings.Margins.Top - 20;
            g.DrawString(textBox1.Text, prnFont, prnBrush, left, top);
            g.DrawRectangle(Pens.Red, 50, 50, 300, 200);
            int W = printDocument0.DefaultPageSettings.Bounds.Width;
            int H = printDocument0.DefaultPageSettings.Bounds.Height;
            g.DrawRectangle(Pens.Red, 20, 20, W - 40, H - 40);
        }

        private void button00_Click(object sender, EventArgs e)
        {
            //版面設定
            //版面設定
            if (pageSetupDialog0.ShowDialog() == DialogResult.OK)
            {
                printDocument0.DefaultPageSettings = pageSetupDialog0.PageSettings;
            }

        }

        private void button01_Click(object sender, EventArgs e)
        {

        }

        private void button02_Click(object sender, EventArgs e)
        {
            //預覽列印
            //預覽列印
            printPreviewDialog0.ShowDialog();

        }

        private void button03_Click(object sender, EventArgs e)
        {
            //列印
            //列印
            if (printDialog0.ShowDialog() == DialogResult.OK)
            {
                //Print()方法會觸動PrintDocument控制項的PrintPage事件
                printDocument0.Print();
            }


        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }


    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */
