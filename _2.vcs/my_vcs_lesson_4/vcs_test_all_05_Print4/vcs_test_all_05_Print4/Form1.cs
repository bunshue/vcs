using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Printing;

namespace vcs_test_all_05_Print4
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

            //------------------------------------------------------------  # 60個

            //列印設定
            printDialog0.Document = printDocument0;
            printDialog0.PrinterSettings = pageSetupDialog0.PrinterSettings;
            printPreviewDialog0.Document = printDocument0;            

            pageSetupDialog0.Document = printDocument0;

            textBox1.ScrollBars = ScrollBars.Both;
            textBox1.Font = new Font("標楷體", 64, FontStyle.Regular);
            textBox1.Text =
                "老來多驚夢，" + Environment.NewLine +
                "似有獻刀人，" + Environment.NewLine +
                "醒來懼銅鏡，" + Environment.NewLine +
                "怕顯董賊身。";
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 280 + 10;

            groupBox0.Size = new Size(200, 280);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            dy = 60 + 10;
            textBox1.Size = new Size(240, 180);
            textBox1.Location = new Point(x_st + dx * 3 - 50, y_st + dy * 4 + 20);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 180 + 10;
            dy = 55 + 10;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            this.Size = new Size(1300, 750);
            this.Text = "vcs_test_all_05_Print2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button00_Click(object sender, EventArgs e)
        {
            //版面設定
            if (pageSetupDialog0.ShowDialog() == DialogResult.OK)
            {
                printDocument0.DefaultPageSettings = pageSetupDialog0.PageSettings;
            }
        }

        private void button01_Click(object sender, EventArgs e)
        {
            //列印設定
        }

        private void button02_Click(object sender, EventArgs e)
        {
            //預覽列印
            //加入PrintDocument 和 PrintPreviewDialog
            //printPreviewDialog1屬性之Document選printDocument1
            //編輯 printDocument1_PrintPage

            printPreviewDialog0.ClientSize = new Size(500, 600);
            printPreviewDialog0.ShowDialog();  // 預覽列印
        }

        private void button03_Click(object sender, EventArgs e)
        {
            //列印
            if (printDialog0.ShowDialog() == DialogResult.OK)
            {
                //Print()方法會觸動PrintDocument控制項的PrintPage事件
                printDocument0.Print();
            }

        }

        private void printDocument0_PrintPage(object sender, PrintPageEventArgs e)
        {
            richTextBox1.Text += "可列印區間\n";

            richTextBox1.Text += e.MarginBounds.Left.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Right.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Top.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Bottom.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Width.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Height.ToString() + "\n";

            int x_st = e.MarginBounds.Left;
            int y_st = e.MarginBounds.Top;
            int W = e.MarginBounds.Width;
            int H = e.MarginBounds.Height;
            e.Graphics.DrawRectangle(Pens.Red, x_st, y_st, W, H);

            e.Graphics.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            e.Graphics.DrawRectangle(Pens.Red, 100, 200, 100, 100);
            e.Graphics.DrawRectangle(Pens.Red, 100, 300, 100, 100);

            /*
            Graphics g = e.Graphics;
            Font f = new Font(textBox1.Font.Name, textBox1.Font.Size, textBox1.Font.Style);
            SolidBrush sb = new SolidBrush(textBox1.ForeColor);
            Single left = printDocument0.DefaultPageSettings.Margins.Left - 10;
            Single top = printDocument0.DefaultPageSettings.Margins.Top - 20;
            g.DrawString(textBox1.Text, f, sb, left, top);
            g.DrawRectangle(Pens.Red, 50, 50, 300, 200);
            int W = printDocument0.DefaultPageSettings.Bounds.Width;
            int H = printDocument0.DefaultPageSettings.Bounds.Height;
            g.DrawRectangle(Pens.Red, 20, 20, W - 40, H - 40);

            int x_st = 100;
            int y_st = 550;
            int dy = 60;
            e.Graphics.DrawString("老來多驚夢，", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st);
            e.Graphics.DrawString("似有獻刀人，", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st + dy * 1);
            e.Graphics.DrawString("醒來懼銅鏡，", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st + dy * 2);
            e.Graphics.DrawString("怕顯董賊身。", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st + dy * 3);
            */

            // Convert mm to inches * 100.
            float diameter = 100;
            diameter = diameter / 25.4f * 100f;

            float cx = (e.MarginBounds.Left + e.MarginBounds.Right) / 2f;
            float cy = (e.MarginBounds.Top + e.MarginBounds.Bottom) / 2f;
            float x = cx - diameter / 2f;
            float y = cy - diameter / 2f;

            RectangleF rect = new RectangleF(x, y, diameter, diameter);

            e.Graphics.DrawEllipse(Pens.Red, rect);


            /*
// Draw the star.
*/

            // Draw axes in the middle of the page.
            DrawAxes(e);

            e.HasMorePages = false;
        }

        // Draw axes in the middle of the page.
        private void DrawAxes(PrintPageEventArgs e)
        {
            float cx = (e.MarginBounds.Left + e.MarginBounds.Right) / 2f;
            float cy = (e.MarginBounds.Top + e.MarginBounds.Bottom) / 2f;

            e.Graphics.DrawLine(Pens.Black,                e.MarginBounds.Left, cy,                e.MarginBounds.Right, cy);
            e.Graphics.DrawLine(Pens.Black,                cx, e.MarginBounds.Top,                cx, e.MarginBounds.Bottom);

            for (float x = cx; x <= e.MarginBounds.Right; x += 100)
            {
                e.Graphics.DrawLine(Pens.Black, x, cy - 25, x, cy + 25);
            }

            for (float x = cx; x >= e.MarginBounds.Left; x -= 100)
            {
                e.Graphics.DrawLine(Pens.Black, x, cy - 25, x, cy + 25);
            }

            for (float y = cy; y <= e.MarginBounds.Bottom; y += 100)
            {
                e.Graphics.DrawLine(Pens.Black, cx - 25, y, cx + 25, y);
            }

            for (float y = cy; y >= e.MarginBounds.Top; y -= 100)
            {
                e.Graphics.DrawLine(Pens.Black, cx - 25, y, cx + 25, y);
            }
        }

        //------------------------------------------------------------  # 60個

        private void printDocument_pascal_PrintPage(object sender, PrintPageEventArgs e)
        {
                        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            try
            {
                Bitmap bitmap = new Bitmap(filename);
                e.Graphics.DrawImage(bitmap, 150, 240, 350, 300);
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }


        }

        private void button0_Click(object sender, EventArgs e)
        {
            //1. 拉一個 PrintPreviewDialog 控件為 printPreviewDialog_pascal
            //2. 拉一個 PrintDocument      控件為 printDocument_pascal
            //3. printPreviewDialog_pascal 的屬性 Document  設定為 printDocument_pascal
            //4. printDocument_pascal      的方法 PrintPage 設定為 printDocument_pascal_PrintPage

            //5. 開啟預覽列印
            // printDocument_pascal.PrinterSettings.PrinterName = "Dell Photo AIO Printer 926";

            printDocument_pascal.DefaultPageSettings.Margins = new System.Drawing.Printing.Margins(50, 50, 50, 50);
            printDocument_pascal.DefaultPageSettings.Landscape = true;

            printPreviewDialog_pascal.ClientSize = new Size(1200, 600);
            printPreviewDialog_pascal.ShowDialog();
        }

        //6060

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個



/*

//預覽列印 Star
控件PrintPreviewDialog    printPreviewDialog_xxxx 內的參數 Document 設定為 printDocument_xxxx

//列印文件
控件PrintDocument         printDocument_xxxx

printDocument_xxxx 的PrintPage方法     printDocument_xxxx_PrintPage 設定要列印的內容

//預覽列印 Star
//            printPreviewDialog_star.ShowDialog();

*/




/*

            printPreviewDialog1.Document = this.printDocument_preview;
            printPreviewDialog1.ShowDialog();

            printDocument1.Print();



        private void printDocument0ddddddd_PrintPage(object sender, PrintPageEventArgs e)
        private void printDocument_preview_PrintPage(object sender, PrintPageEventArgs e)
        {
        }

            printPreviewDialog2.Document = this.printDocument2;
            printPreviewDialog2.ShowDialog();

*/
