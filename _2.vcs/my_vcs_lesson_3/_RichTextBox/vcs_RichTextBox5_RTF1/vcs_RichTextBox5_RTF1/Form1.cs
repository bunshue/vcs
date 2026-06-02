using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_RichTextBox5_RTF1
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

            groupBox1.Size = new Size(200, 130);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            richTextBox_rtf.Size = new Size(240, 400);
            richTextBox_rtf.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            //richTextBox1.Size = new Size(300, 680);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            //bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_justify_left.BackgroundImage = vcs_RichTextBox5_RTF1.Properties.Resources.align_left;
            bt_justify_center.BackgroundImage = vcs_RichTextBox5_RTF1.Properties.Resources.align_center;
            bt_justify_right.BackgroundImage = vcs_RichTextBox5_RTF1.Properties.Resources.align_right;

            this.Size = new Size(1360, 750);
            this.Text = "vcs_RichTextBox5_RTF1";

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
            //讀寫RTF檔

            //讀寫RTF檔

            //富文字格式（Rich Text Format）即RTF格式，又稱多文字格式

            string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";
            //string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\SAMPO(PA63)變頻分離式室外機功能規格書_2014.08.18doc.rtf";

            richTextBox_rtf.LoadFile(rtf_filename);

            //另存RTF檔
            rtf_filename = "tmp_rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";
            richTextBox_rtf.SaveFile(rtf_filename);
            //richTextBox_rtf.SaveFile(rtf_filename, RichTextBoxStreamType.RichText);
            richTextBox2.Text += "已存檔 : " + rtf_filename + "\n";

            /*
            //開啟 .rtf 檔 至 RTB
            rtxtShow.LoadFile("../../../Demo01.rtf");
            //取得載入檔案的總字串長度
            int result = rtxtShow.TextLength;
            richTextBox1.Text += "字串長度 : " + result.ToString() + "\n";

            //將 RTB 儲存至 .rtf 檔
            rtxtShow.SaveFile("../../../tmp_Change.rtf", RichTextBoxStreamType.RichText);
            int result = rtxtShow.TextLength;
            richTextBox1.Text += "字串長度 : " + result.ToString() + "\n";

            rtxtShow.LoadFile("../../../Demo01.rtf");
            rtxtShow.SaveFile("tmp_Demo02.rtf");
            */

            // 將test.rtf檔的內容載入到richTextBox1豐富文字方塊內
            // richTextBox1.LoadFile("../../../GOTOP.rtf", RichTextBoxStreamType.RichText);

            // 將test.rtf檔的內容載入到richTextBox1豐富文字方塊內
            richTextBox1.LoadFile("GOTOP.rtf", RichTextBoxStreamType.RichText);

            // 將richTextBox1豐富文字方塊內的資料儲存到test.rtf檔
            richTextBox1.SaveFile("GOTOP.rtf", RichTextBoxStreamType.RichText);

            // 將richTextBox1豐富文字方塊內的資料儲存到test.rtf檔
            // richTextBox1.SaveFile("tmp_GOTOP.rtf", RichTextBoxStreamType.RichText);

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_rtf\VS2013Express.rtf";

            /*
            RTB load rtf 檔
            openFileDialog1.DefaultExt = "*.rtf";
            openFileDialog1.Filter = "RTF檔|*.rtf";

            if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK && openFileDialog1.FileName.Length > 0)
            {
                richTextBox1.LoadFile(openFileDialog1.FileName);
            }

            saveFileDialog1.Filter = "RTF檔|*.rtf";

            if (saveFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK && saveFileDialog1.FileName.Length > 0)
            {
                richTextBox1.SaveFile(saveFileDialog1.FileName);
            }

            saveFileDialog1.Filter = "RTF檔|*.rtf";

            if (saveFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK && saveFileDialog1.FileName.Length > 0)
            {
                richTextBox1.LoadFile(saveFileDialog1.FileName, RichTextBoxStreamType.PlainText);
            }
            */
            //------------------------------------------------------------  # 60個

        }

        //------------------------------------------------------------  # 60個

        //設定RichTextBox的文字對齊方式

        string temp = "tomorrow.RTF";//保存文件的路徑

        private void bt_open_rtf_Click(object sender, EventArgs e)
        {
            OpenFileDialog TxTOpenDialog = new OpenFileDialog();//聲明一個用於打開文件對話框的對象
            TxTOpenDialog.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf";
            TxTOpenDialog.Filter = "RTF文件(*.RTF)|*.RTF";//定義打開文件對話框的過濾參數
            if (TxTOpenDialog.ShowDialog() == DialogResult.OK)//當在打開對話框中單擊「打開」按鈕時
            {
                temp = TxTOpenDialog.FileName;//保存打開文件的路徑
                richTextBox1.LoadFile(TxTOpenDialog.FileName, RichTextBoxStreamType.RichText);//從指定的位置加載RTF文件
                //MessageBox.Show("讀取成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出讀取成功時的提示信息
            }

            /*
            if (File.Exists(temp))//當在指定路徑下存在該文件時
            {
                this.richTextBox1.LoadFile(temp, RichTextBoxStreamType.RichText);//從指定的位置加載RTF文件
            }
            */

        }

        private void bt_save_rtf_Click(object sender, EventArgs e)
        {
            ConserveMeasure(temp);//在指定路徑下保存文件
        }

        private void ConserveMeasure(string path)
        {
            SaveFileDialog TxTSaveDialog = new SaveFileDialog();//定義一個用於保存文件的保存對話框
            TxTSaveDialog.Filter = "RTF文件（*.RTF)|*.RTF";//設置保存文件的過濾參數
            if (File.Exists(path))//當在指定路徑下存在該路徑時
            {
                this.richTextBox1.SaveFile(path, RichTextBoxStreamType.RichText);//保存指定文件到指定位置
                MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的提示信息
                this.richTextBox1.Clear();//清空RichTextBox控件中的所有內容
            }
            else
            {
                if (TxTSaveDialog.ShowDialog() == DialogResult.OK)//當在保存對話框中單擊「保存」按鈕時
                {
                    this.richTextBox1.SaveFile(TxTSaveDialog.FileName, RichTextBoxStreamType.RichText);//保存文件到指定的位置
                    MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的提示信息
                    this.richTextBox1.Clear();//清空RichTextBox控件中的所有內容
                }
            }
        }

        private void bt_justify_left_Click(object sender, EventArgs e)
        {
            this.richTextBox1.SelectionAlignment = HorizontalAlignment.Left;//設置選定的文本為左對齊
        }

        private void bt_justify_center_Click(object sender, EventArgs e)
        {
            this.richTextBox1.SelectionAlignment = HorizontalAlignment.Center;//設置選定的文本為居中對齊
        }

        private void bt_justify_right_Click(object sender, EventArgs e)
        {
            this.richTextBox1.SelectionAlignment = HorizontalAlignment.Right;//設置選定的文本為右對齊
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

