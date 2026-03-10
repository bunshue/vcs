using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_tmp_all1
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

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_tmp_all1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //設定檔案的路徑
            string path = @"../../data/Program.cs";
            string append = @"tmp_final.txt";
            string str;
            int index = 1;

            StreamReader sr = File.OpenText(path);
            StreamWriter sw = File.AppendText(append);

            while ((str = sr.ReadLine()) != null)
            {
                richTextBox1.Text += str + "\n";
                //WriteLine($"{index:D5} {str}");
                //sw.WriteLine($"{index++:D5} {str}");
            }
            sr.Close();
            sw.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string path2 = @"../../data";
            string fnShow = "檔案清單---<*.TXT>";
            try
            {
                //取得檔案路徑訊息
                DirectoryInfo currentDir = new
                   DirectoryInfo(path2);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = currentDir.GetFiles("*.txt");
                //設定檔案的標題
                //string header = fnShow + "\n" + $"{"檔名",-16}{"檔案長度",-12}{"修改日期"}" + "\n";
                string header = fnShow + "\n" + "檔名" + "檔案長度" + "修改日期" + "\n";
                richTextBox1.Text = header;

                /* 讀取資料夾中有關於 --檔名(Name)、長度(Length)
                   和修改日期(LastWriteTime)*/
                foreach (FileInfo getInfo in listFile)
                {
                    /*
                    richTextBox1.Text += $"{getInfo.Name,-15}" +
                       $"{getInfo.Length.ToString(),-11}" +
                       $"{getInfo.LastWriteTime.ToShortDateString(),15}" + "\n";
                    */
                    richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + getInfo.LastWriteTime.ToShortDateString() + "\n";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //新增檔案
            //指定路徑建立檔案
            string path = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\Sample\Demo.txt";
            FileInfo createFile = new FileInfo(path);
            //以Create方法新增一個檔案
            FileStream fs = createFile.Create();
            fs.Close();//關閉檔案

            //複製檔案
            path = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\Sample\Demo.txt";
            //目的檔案「Text.txttmp」
            String tagPath = path + "tmp";
            FileInfo copyFile = new FileInfo(path);
            try
            {
                //以CopyTo方法複製檔案
                copyFile.CopyTo(tagPath);
                richTextBox1.Text = path + " 已複製";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //刪除檔案
            path = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\Sample\Demo.txttmp";
            copyFile = new FileInfo(path);
            if (copyFile.Exists == false)//查看檔案是否存在
            {
                MessageBox.Show("無此檔案");
            }
            else
            {
                copyFile.Delete();//刪除檔案
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string path = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\Sample\Demo.txt";
            string str;
            FileStream fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.Unicode);

            //想儲存的文字
            str = "aaaaaaaaa";
            sw.WriteLine(str);  //將資料寫入檔案
            sw.Close();   //關閉sw資料流

            //檔案內所輸入的文字為
            FileStream f = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read);
            StreamReader sr = new StreamReader(f, Encoding.Unicode);
            sr.BaseStream.Seek(0, SeekOrigin.Begin);
            while (sr.Peek() > -1)
            {
                richTextBox1.Text += sr.ReadLine() + "\n";//讀出檔案
            }
            sr.Close();  //關閉資料流
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                string path = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\Sample\Icon\";
                //取得資料夾最後一次被存取的時間
                DateTime dt = Directory.GetLastWriteTime(path);
                //如果資料夾不存在就建立資料夾
                if (!Directory.Exists(path))
                {
                    Directory.CreateDirectory(path);
                }
                else
                {
                    richTextBox1.Text += "資料夾建立的時間 : " + dt + "\n";
                }
                //更新時間
                Directory.SetLastWriteTime(path, DateTime.Now);
                dt = Directory.GetLastWriteTime(path);
                richTextBox1.Text += "最後存取時間 : " + dt + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無法建立 : " + e.ToString() + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //儲存要回傳的檔案路徑和檔案類型
            string path2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\Sample";
            string fnShow = "檔案清單---<*.jpg>\n\n";

            //判斷資料夾是否存在，若是不存在會擲出例外情形
            try
            {    //取得檔案路徑訊息
                DirectoryInfo currentDir = new DirectoryInfo(path2);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = currentDir.GetFiles("*.jpg");
                //設定檔案的標題
                string sign = new string('-', 37);
                string fnName = "檔名", fnLength = "檔案長度";
                string fnDate = "修改日期";
                string header = fnShow + "\t" + fnName + "\t" + fnLength + "\t" + fnDate + "\n";
                richTextBox1.Text += header + "\n";
                richTextBox1.Text += sign + "\n";

                foreach (FileInfo getInfo in listFile)
                {
                    string dt = getInfo.LastWriteTime.ToShortDateString();
                    richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + dt + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無此資料夾 : " + ex.Message + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            BinaryReader readBit;
            FileStream objStream;
            //設定欲讀取檔案的路徑
            string path = @"D:\_git\vcs\_1.data\______test_files1\__RW\_bin\vcs_ReadWrite_BIN.bin";

            int count = 0;
            try
            {
                objStream = new FileStream(path, FileMode.Open, FileAccess.Read);

                //使用using陳述詞，確保資源的釋放
                using (readBit = new BinaryReader(objStream))
                {
                    do
                    {
                        //以位元組為單位讀取檔案內容，16進位方式顯示
                        richTextBox1.Text += readBit.ReadByte().ToString() + " ";
                        count += 1;
                        //'** 換行
                        if (count == 10)
                        {
                            richTextBox1.Text += "\n";
                            count = 0;
                        }
                    } while (true);
                }
            }
            catch (IndexOutOfRangeException ex)
            {
                richTextBox1.Text += "沒有指定檔案\n";
            }

            catch (EndOfStreamException ex)
            {
                richTextBox1.Text += "檔案讀取完畢\n";
            }

            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            BinaryWriter objWriter;
            FileStream objStream;
            string path = @"tmp_BinaryWriter.txt";
            try
            {
                objStream = new FileStream(path, FileMode.Append, FileAccess.Write);
                //使用using敘詞，寫入完墓會自動釋放資源
                using (objWriter = new BinaryWriter(objStream))
                {
                    // 寫入字串
                    objWriter.Write("空山不見人");
                    objWriter.Write("Visual C# 7.0");
                    // 寫入數值
                    objWriter.Write(640526);
                }
            }
            catch (IndexOutOfRangeException ex)
            {
                richTextBox1.Text += "沒有指定檔案\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            BinaryReader objReader;
            //FileStream objStream;
            path = @"tmp_Demo03aa.txt";
            try
            {
                objStream = new FileStream(path, FileMode.Open, FileAccess.Read);
                objReader = new BinaryReader(objStream);
                richTextBox1.Text += objReader.ReadString() + "\n";
                richTextBox1.Text += objReader.ReadInt32() + "\n";
                objReader.Close();
            }
            catch (IndexOutOfRangeException ex)
            {
                richTextBox1.Text += "沒有指定檔案\n";
            }

            catch (EndOfStreamException ex)
            {
                richTextBox1.Text += "檔案讀取完畢\n";
            }

            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //openFileDialog1
            //建立處理資料流的物件note
            Stream note = null;
            //設定OpenFileDialog的屬性-InitialDirectory設預設路徑
            //openFileDialog1.InitialDirectory = "../../data/";
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\Visual C# 2019-程式設計16堂課\vcs_tmp_all1\vcs_tmp_all1\data";
            //篩選檔案，只顯示文字檔
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|所有檔案(*.*)|*.*";
            //檔案類型會顯示-所有檔案
            openFileDialog1.FilterIndex = 2;
            //對話方塊關閉前還原目前取得的路徑
            openFileDialog1.RestoreDirectory = true;
            //以一般的訊息方塊來確認使用者按OK鈕 
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //攔截例外狀況
                try
                {
                    if ((note = openFileDialog1.OpenFile()) != null)
                    {
                        using (note)
                        {
                            //PlainText-代表OLE物件的純文字資料流，文字中允許有空格
                            richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);
                        }
                    }
                }
                catch (Exception ex)
                {
                    //MessageBox.Show($"檔案有誤：{ex.Message}");
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //openFileDialog1

            //開啟檔案項目

            openFileDialog1.InitialDirectory = Application.StartupPath; //從目前目錄開始尋找檔案

            openFileDialog1.FileName = null;

            //開啟RTF格式檔案
            openFileDialog1.DefaultExt = "rtf";
            openFileDialog1.Filter = "RTF格式(*.rtf)|*.rtf|所有檔案(*.*)|*.*";

            //顯示開啟檔案對話方塊
            DialogResult result = openFileDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                string openFileName = openFileDialog1.FileName;
                try
                {
                    //以RichTextBox的LoadFile()方法載入檔案
                    Stream sr = openFileDialog1.OpenFile();
                    richTextBox1.LoadFile(sr, RichTextBoxStreamType.RichText);
                    sr.Close();
                }
                catch (Exception exp)
                {
                    //MessageBox.Show("發生錯誤. 訊息: " +
                    //   $"{System.Environment.NewLine}" +
                    //   $"{exp.ToString()}, {Environment.NewLine}");
                }
            }
            // 按了「取消」按鈕就回到原來的表單畫面
            else if (result == DialogResult.Cancel)
            {
                return;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //saveFileDialog1
            richTextBox1.Lines = new string[]
            {
                "Irish poets learn your trade ",
                "Sing whatever is well made ",
                "Scorn the sort now growing up"
            };

            //設定預設目錄, 預設欲儲存的檔案類型
            saveFileDialog1.InitialDirectory = Application.StartupPath; //從目前目錄開始尋找檔案
            saveFileDialog1.Filter = "文字檔(*.txt)|*.txt|RTF格式|*.rtf";
            //設定對話方塊的標題
            saveFileDialog1.Title = "儲存檔案";
            //設定是否在關閉之前要還原至目前的目錄
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.CreatePrompt = true;
            saveFileDialog1.OverwritePrompt = true;
            //假如按下儲存按鈕時
            DialogResult result = saveFileDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                StreamWriter writer;
                //設定檔案名稱
                string filename = saveFileDialog1.FileName;
                writer = new StreamWriter(filename, false, Encoding.Default);
                //將文字方塊內容寫入指定的檔案中
                writer.Write(richTextBox1.Text);
                writer.Close(); //關閉檔案
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //folderBrowserDialog1
            //瀏覽資料夾

            //設定瀏覽資料夾對話方塊-從虛擬「桌面」為開始的資料夾
            folderBrowserDialog1.RootFolder = Environment.SpecialFolder.Desktop;

            //指定要瀏覽的資料夾
            folderBrowserDialog1.SelectedPath = Application.StartupPath; //從目前目錄開始尋找檔案

            //瀏覽資料夾的提示文字
            folderBrowserDialog1.Description = "選取要瀏覽的資料夾";

            //進入FloderBrowserDialog並按確定鈕
            DialogResult result = folderBrowserDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                //取得瀏覽資料夾對話方塊所選取的路徑
                string folderName = folderBrowserDialog1.SelectedPath;
                //確認沒有開啟的檔案，依預設的資料夾來開啟
                openFileDialog1.InitialDirectory = folderName;
                openFileDialog1.FileName = null;
            }
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

//saveFileDialog1.InitialDirectory = Application.StartupPath; //從目前目錄開始尋找檔案
