using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.IO;

/*
saveFileDialog1 使用 saveFileDialog1_FileOk
*/

namespace xCh7_3_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            openFileDialog1.Title = "客製化的「開啟檔案」對話方塊";
            openFileDialog1.Filter = "圖檔 (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" + "所有檔案 (*.*)|*.*";
            openFileDialog1.FilterIndex = 2;
            openFileDialog1.ValidateNames = false;
            openFileDialog1.CheckFileExists = false;

            saveFileDialog1.Title = "客製化的「另存新檔」對話方塊";
            saveFileDialog1.RestoreDirectory = false;
            saveFileDialog1.Filter = "圖檔 (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" + "所有檔案 (*.*)|*.*";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //預覽
            //多重選取
            //openFileDialog1.Multiselect = true;//false

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 在TextBox中寫入已選取的檔案名稱及安全名稱
                textBox1.Text = "檔名->" + openFileDialog1.FileName;
                textBox1.AppendText("\n");
                textBox1.AppendText("安全檔名->" + openFileDialog1.SafeFileName);

                // CheckBox4是設定Multiselect，如果有被勾選
                // 就將已選取的檔案，分別依是否含路徑名稱寫入
                if (checkBox4.Checked)
                {
                    listBox1.Items.Clear();
                    foreach (String file in openFileDialog1.FileNames)
                    {
                        listBox1.Items.Add(file);
                    }
                    listBox2.Items.Clear();
                    foreach (String file in openFileDialog1.SafeFileNames)
                    {
                        listBox2.Items.Add(file);
                    }
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //開啟檔案
            Stream myStream = null;
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            // 也可以使用FileOK事件處理程序，就如saveFileDialog1
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    if ((myStream = openFileDialog1.OpenFile()) != null)
                    {
                        using (myStream)
                        {
                            StreamReader sr = new StreamReader(myStream);

                            // ReadToEnd()方法，會從整個資料流或從目前的位
                            // 置至資料流的結尾，並將讀取到的資料流以字串的
                            // 方式來處理。
                            string whole = sr.ReadToEnd();
                            textBox1.Text = whole;
                        }
                    }
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "發生錯誤 " + ex.Message + "\n";
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //另存新檔
            saveFileDialog1.ShowDialog();
        }

        private void saveFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            string myFile = null;
            myFile = saveFileDialog1.FileName;
            try
            {
                if (myFile != null)
                {
                    if (File.Exists(myFile))
                    {
                        SaveFile(myFile);
                    }
                    else
                    {
                        SaveFile(myFile);
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "發生錯誤 " + ex.Message + "\n";
            }
        }

        private void SaveFile(string fileName)
        {
            StreamWriter sw = new StreamWriter(fileName);

            sw.WriteLine(textBox1.Text);
            sw.Write("存檔日期：");
            sw.Write(DateTime.Now);

            sw.Flush();
            sw.Close();

            richTextBox1.Text += "存檔完成 !\n";
        }
    }
}


/*屬性設定
openFileDialog1.ShowHelp = checkBox1.Checked;
openFileDialog1.ShowReadOnly = checkBox2.Checked;
openFileDialog1.ReadOnlyChecked = checkBox3.Checked;
openFileDialog1.ValidateNames = checkBox5.Checked;
openFileDialog1.CheckFileExists = checkBox6.Checked;
openFileDialog1.CheckPathExists = checkBox7.Checked;

saveFileDialog1.RestoreDirectory = checkBox8.Checked;
*/

