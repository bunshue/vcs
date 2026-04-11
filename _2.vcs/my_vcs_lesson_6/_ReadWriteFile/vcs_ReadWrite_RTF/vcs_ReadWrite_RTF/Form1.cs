using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_RTF
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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            //richTextBox1.Size = new Size(300, 680);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            //bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1273, 750);
            this.Text = "vcs_ReadWrite_RTF";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //RTF檔案讀取到RTB
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\VS2013Express.rtf";
            richTextBox1.LoadFile(filename, RichTextBoxStreamType.RichText);//從指定位置加載RTF文件
            richTextBox2.Text += "開啟檔案 : " + filename + "\n";


            /*
            //以RichTextBox的LoadFile()方法載入檔案
            Stream sr = openFileDialog1.OpenFile();
            richTextBox1.LoadFile(sr, RichTextBoxStreamType.RichText);
            sr.Close();
            */

            /*
            //開啟RTF檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";

            try
            {
                richTextBox1.LoadFile(filename);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("沒找到相關文件");
            }
            */

            /*
            rtxtShow.LoadFile("../../Demo01.rtf");
            // 將test.rtf檔的內容載入到richTextBox1豐富文字方塊內
            richTextBox1.LoadFile("Gotop.rtf", RichTextBoxStreamType.RichText);

            // 將test.rtf檔的內容載入到richTextBox1豐富文字方塊內
            richTextBox1.LoadFile("GOTOP.rtf", RichTextBoxStreamType.RichText);
            */


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //RTB寫入到RTF檔案
            string filename = Application.StartupPath + "\\rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";

            richTextBox1.SaveFile(filename, RichTextBoxStreamType.RichNoOleObjs);//在指定路徑下保存

            //same
            //richTextBox1.SaveFile(filename);//在指定位置下保存RTF文件

            richTextBox2.Text += "儲存檔案 : " + filename + " 完成\n";

            /*
            rtxtShow.SaveFile("tmp_change.rtf");

            // 將richTextBox1豐富文字方塊內的資料儲存到test.rtf檔
            richTextBox1.SaveFile("tmp_Gotop.rtf", RichTextBoxStreamType.RichText);


            // 將richTextBox1豐富文字方塊內的資料儲存到test.rtf檔
            richTextBox1.SaveFile("GOTOP.rtf", RichTextBoxStreamType.RichText);
            */

            /*
            //另存RTF檔案
            try
            {
                richTextBox1.SaveFile("tmp_aaaa.rtf");
            }
            catch (Exception err)
            {
                MessageBox.Show(err.Message);
            }
            */

        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Lines = new string[]
            {
                "Irish poets learn your trade ",
                "Sing whatever is well made ",
                "Scorn the sort now growing up"
            };

            StreamWriter writer;
            //設定檔案名稱
            string filename = "tmp_cccccc.rtf";
            writer = new StreamWriter(filename, false, Encoding.Default);
            //將文字方塊內容寫入指定的檔案中
            writer.Write(richTextBox1.Text);
            writer.Close(); //關閉檔案
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            CreateMyRichTextBox();
        }

        public void CreateMyRichTextBox()
        {
            RichTextBox richTextBox1 = new RichTextBox();
            //richTextBox1.Dock = DockStyle.Fill;
            richTextBox1.Size = new Size(300, 300);
            richTextBox1.Location = new Point(100, 100);

            try
            {
                richTextBox1.LoadFile(@"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\VS2013Express.rtf");
                richTextBox1.Find("Text", RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionFont = new Font("Verdana", 12, FontStyle.Bold);
                richTextBox1.SelectionColor = Color.Red;

                string filename = Application.StartupPath + "\\rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";
                richTextBox1.SaveFile(filename, RichTextBoxStreamType.RichText);
                richTextBox1.Text += "已存檔 : " + filename + "\n";

                this.Controls.Add(richTextBox1);
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
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

