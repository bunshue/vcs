using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport
using System.IO;                        //for FileAccess, File

namespace vcs_SendTo_Convert
{
    public partial class Form1 : Form
    {
        //使用系統 kernel32.dll LCMapString進行轉換
        internal const int LOCALE_SYSTEM_DEFAULT = 0x0800;
        internal const int LCMAP_SIMPLIFIED_CHINESE = 0x02000000;
        internal const int LCMAP_TRADITIONAL_CHINESE = 0x04000000;
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        internal static extern int LCMapString(int Locale, int dwMapFlags, string lpSrcStr, int cchSrc, [Out] string lpDestStr, int cchDest);

        /// <summary>
        /// 將簡體中文字元轉換成繁體中文
        /// </summary>
        /// <param name="strGB2312"></param>
        /// <returns></returns>
        private string GB2312translateBig5(string strGB2312)
        {
            String tTarget = new String(' ', strGB2312.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_TRADITIONAL_CHINESE, strGB2312, strGB2312.Length, tTarget, strGB2312.Length);
            return tTarget;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string sendto_folder = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
            //richTextBox1.Text += "[傳送到]資料夾位置:\n" + sendto_folder + "\n";

            //label1.Text = "檔案總管 右鍵 傳送到 XXX, 可用XXX開啟檔案\n\n拉一個捷徑到\n%APPDATA%\\Microsoft\\Windows\\SendTo\n或\n" + sendto_folder;

            int len = System.Environment.GetCommandLineArgs().Length;
            int i;
            //richTextBox1.Text += "參數長度\t" + len.ToString() + "\t分別是:\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "第 " + i.ToString() + " 項\t" + System.Environment.GetCommandLineArgs()[i] + "\n";
            }

            List<String> filenames = new List<String>();

            for (i = 1; i < len; i++)
                filenames.Add(System.Environment.GetCommandLineArgs()[i]);

            filenames.Sort();

            for (i = 0; i < (len - 1); i++)
            {
                string filename = filenames[i];
                convert_sc_to_tc(filename);
            }
        }

        void convert_sc_to_tc(string filename)
        {
            richTextBox1.Text += "\n#檔案 : " + filename + "\n\n";

            if (File.Exists(filename)==true)  //確認檔案是否存在
            {
                richTextBox1.Text += "檔名(包含副檔名)： " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名)： " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名： " + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "根目錄： " + Path.GetPathRoot(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetDirectoryName(filename) + "\n";

                string fore_filename = Path.GetFileNameWithoutExtension(filename);
                string ext_filename = Path.GetExtension(filename);
                string foldername = Path.GetDirectoryName(filename);
                string backup_filename = Path.Combine(foldername, fore_filename + "_old" + ext_filename);

                richTextBox1.Text += "新檔名： " + backup_filename + "\n";

                if (File.Exists(backup_filename) == false)
                {
                    File.Copy(filename, backup_filename);     //若檔案已存在, 會出現IOException
                }
                else
                {
                    MessageBox.Show("備份檔案已存在, 跳過");
                    return;
                }
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                return;
            }

            try
            {
                string all_text = File.ReadAllText(filename, Encoding.UTF8);

                //簡中轉正中
                string all_tc_text = GB2312translateBig5(all_text);

                //string filename_new = @"C:\_git\vcs\_4.python\test10_new08_test_sc_tc_ccccc.py";
                //覆蓋原檔
                FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
                StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);   //指名編碼格式            
                sw.Write(all_tc_text);
                sw.Close();

                MessageBox.Show("簡中轉正中完成, 檔名 : " + filename);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }


        }
    }
}
