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

namespace CH1502
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //新增檔案
        private void msCreate_Click(object sender, EventArgs e)
        {
            //指定路徑建立檔案
            string path = @"D:\C#Lab\Sample\Demo.txt";
            FileInfo createFile = new FileInfo(path);
            //以Create方法新增一個檔案
            FileStream fs = createFile.Create();
            fs.Close();//關閉檔案
        }

        //複製檔案
        private void msCopy_Click(object sender, EventArgs e)
        {
            string path = @"D:\C#Lab\Sample\Demo.txt";
            //目的檔案「Text.txttmp」
            String tagPath = path + "tmp";
            FileInfo copyFile = new FileInfo(path);
            try
            {
                //以CopyTo方法複製檔案
                copyFile.CopyTo(tagPath);
                txtShow.Text = path + " 已複製";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        //刪除檔案
        private void msDelete_Click(object sender, EventArgs e)
        {
            string path = @"D:\C#Lab\Sample\Demo.txttmp";
            FileInfo copyFile = new FileInfo(path);
            if (copyFile.Exists == false)//查看檔案是否存在
            {
                MessageBox.Show("無此檔案");
            }
            else
                copyFile.Delete();//刪除檔案
        }

        //檢視檔案內容
        private void msView_Click(object sender, EventArgs e)
        {
            string path2 = @"D:\C#Lab\Sample";
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
                string header = fnShow + Environment.NewLine +
                   $"{"檔名",-16}{"檔案長度",-12}{"修改日期"}" +
                   Environment.NewLine;
                txtShow.Text = header;

                /* 讀取資料夾中有關於 --檔名(Name)、長度(Length)
                   和修改日期(LastWriteTime)*/
                foreach (FileInfo getInfo in listFile)
                {
                    txtShow.Text += $"{getInfo.Name,-15}" +
                       $"{getInfo.Length.ToString(),-11}" +
                       $"{getInfo.LastWriteTime.ToShortDateString(),15}"
                       + Environment.NewLine;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
