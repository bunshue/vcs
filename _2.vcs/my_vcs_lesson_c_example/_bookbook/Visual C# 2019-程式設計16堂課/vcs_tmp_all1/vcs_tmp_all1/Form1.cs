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
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

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
                FileInfo[] listFile =
                   currentDir.GetFiles("*.txt");
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
            string path = @"D:\C#Lab\Sample\Demo.txt";
            FileInfo createFile = new FileInfo(path);
            //以Create方法新增一個檔案
            FileStream fs = createFile.Create();
            fs.Close();//關閉檔案



            //複製檔案
            path = @"D:\C#Lab\Sample\Demo.txt";
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
            path = @"D:\C#Lab\Sample\Demo.txttmp";
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
            string path = @"D:\C#Lab\Sample\Demo.txt";
            string str;
            FileStream fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.Unicode);

            //WriteLine("請輸入想儲存的文字");
            str = "aaaaaaaaa";
            sw.WriteLine(str);  //將資料寫入檔案
            sw.Close();   //關閉sw資料流
            //WriteLine("檔案內所輸入的文字為");

            FileStream f = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read);
            StreamReader sr = new StreamReader(f, Encoding.Unicode);
            sr.BaseStream.Seek(0, SeekOrigin.Begin);
            while (sr.Peek() > -1)
            {
                //WriteLine(sr.ReadLine());//讀出檔案
            }
            sr.Close();  //關閉資料流
            //ReadKey();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                string path = @"D:\C#Lab\Sample\Icon\";
                //取得資料夾最後一次被存取的時間
                DateTime dt = Directory.GetLastWriteTime(path);
                //如果資料夾不存在就建立資料夾
                if (!Directory.Exists(path))
                {
                    Directory.CreateDirectory(path);
                }
                else
                {
                    //WriteLine($"資料夾建立的時間：\n{dt}");
                }
                //更新時間
                Directory.SetLastWriteTime(path, DateTime.Now);
                dt = Directory.GetLastWriteTime(path);
                //WriteLine($"\n最後存取時間：\n{dt}");
            }
            catch (Exception ex)
            {
                //WriteLine($"無法建立:{e.ToString()}");
            }
            //ReadKey();


        }

        private void button5_Click(object sender, EventArgs e)
        {
            //儲存要回傳的檔案路徑和檔案類型
            string path2 = @"D:\C#Lab\Sample";
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
                //string header = fnShow + $"{fnName,-12}{fnLength,-8}{fnDate,-11}";

                //WriteLine(header);
                //WriteLine(sign);

                foreach (FileInfo getInfo in listFile)
                {
                    string dt = getInfo.LastWriteTime.ToShortDateString();
                    //WriteLine($"{getInfo.Name,-15}" + $"{getInfo.Length.ToString(),-10} {dt}");
                }
            }
            catch (Exception ex)
            {
                //WriteLine($"無此資料夾: {ex.Message}");
            }
            //ReadKey();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            BinaryReader readBit;
            FileStream objStream;
            //設定欲讀取檔案的路徑
            string path = @"D:\C#Lab\CH15\CH1506\005.jpg";
            //讀取範例CH1507寫入的二進位檔 Demo03.txt
            //string path = @"D:\C#Lab\Demo03.txt";
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
                        //Write($"{readBit.ReadByte(),2:X}");
                        count += 1;
                        //'** 換行
                        if (count == 10)
                        {
                            //WriteLine();
                            count = 0;
                        }
                    } while (true);
                }
            }
            catch (IndexOutOfRangeException ex)
            {
                //WriteLine("沒有指定檔案");
            }

            catch (EndOfStreamException ex)
            {
                //WriteLine("\n檔案讀取完畢");
            }

            catch (Exception ex)
            {
                //WriteLine(e.Message);
            }
            //ReadKey();

        }

        private void button7_Click(object sender, EventArgs e)
        {
            BinaryWriter objWriter;
            FileStream objStream;
            string path = @"tmp_Demo03.txt";
            try
            {
                objStream = new FileStream(path, FileMode.Append, FileAccess.Write);
                //使用using敘詞，寫入完墓會自動釋放資源
                using (objWriter = new BinaryWriter(objStream))
                {
                    //* 寫入字串
                    objWriter.Write("空山不見人");
                    objWriter.Write("Visual C# 7.0");
                    //* 寫入數值
                    objWriter.Write(640526);
                }
            }
            catch (IndexOutOfRangeException ex)
            {
                //WriteLine("沒有指定檔案");
            }
            catch (Exception ex)
            {
                //WriteLine(e.Message);
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            BinaryReader objReader;
            FileStream objStream;
            string path = @"tmp_Demo03aa.txt";
            try
            {
                objStream = new FileStream(path, FileMode.Open, FileAccess.Read);
                objReader = new BinaryReader(objStream);
                //WriteLine(objReader.ReadString());
                //WriteLine(objReader.ReadInt32());
                objReader.Close();
            }
            catch (IndexOutOfRangeException ex)
            {
                //WriteLine("沒有指定檔案");
            }

            catch (EndOfStreamException ex)
            {
                //WriteLine("檔案讀取完畢");
            }

            catch (Exception ex)
            {
                //WriteLine(e.Message);
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {
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

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
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

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
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


