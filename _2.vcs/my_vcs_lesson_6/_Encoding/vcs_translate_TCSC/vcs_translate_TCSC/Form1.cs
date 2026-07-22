using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for File, FileAccess
using System.Runtime.InteropServices;  // for DllImport

namespace vcs_translate_TCSC
{
    public partial class Form1 : Form
    {
        //使用系統 kernel32.dll LCMapString進行轉換
        internal const int LOCALE_SYSTEM_DEFAULT = 0x0800;
        internal const int LCMAP_SIMPLIFIED_CHINESE = 0x02000000;
        internal const int LCMAP_TRADITIONAL_CHINESE = 0x04000000;
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        internal static extern int LCMapString(int Locale, int dwMapFlags, string lpSrcStr, int cchSrc, [Out] string lpDestStr, int cchDest);

        // 將簡體中文字元轉換成繁體中文
        private string GB2312ToBig5(string strGB2312)
        {
            String tTarget = new String(' ', strGB2312.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_TRADITIONAL_CHINESE, strGB2312, strGB2312.Length, tTarget, strGB2312.Length);
            return tTarget;
        }

        // 將繁體中文字元轉換成簡體中文
        private string Big5ToGB2312(string strBig5)
        {
            String tTarget = new String(' ', strBig5.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_SIMPLIFIED_CHINESE, strBig5, strBig5.Length, tTarget, strBig5.Length);
            return tTarget;
        }

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
            //int dy;
            int border = 10;

            int W = 600;
            int H = 800;

            richTextBox_tc.Size = new Size(W, H);
            richTextBox_sc.Size = new Size(W, H);

            x_st = border;
            y_st = border;
            dx = border + 80 + border;   // border + 80 + border

            richTextBox_tc.Location = new Point(x_st, y_st);
            richTextBox_sc.Location = new Point(x_st + W + dx, y_st);

            bt_tc_sc.Location = new Point(x_st + W + 10, y_st + H * 1 / 3 - bt_tc_sc.Height);
            bt_sc_tc.Location = new Point(x_st + W + 10, y_st + H * 2 / 3 - bt_sc_tc.Height);
            bt_file_sc_tc.Location = new Point(x_st + W + 10, y_st + H - bt_file_sc_tc.Height);

            lb_tc.Location = new Point(richTextBox_tc.Location.X + richTextBox_tc.Size.Width - lb_tc.Size.Width, y_st);
            lb_sc.Location = new Point(richTextBox_sc.Location.X + richTextBox_sc.Size.Width - lb_sc.Size.Width, y_st);

            bt_open_tc.Location = new Point(richTextBox_tc.Location.X, richTextBox_tc.Location.Y + richTextBox_tc.Size.Height - bt_open_tc.Size.Height);
            bt_save_tc.Location = new Point(richTextBox_tc.Location.X + bt_open_tc.Size.Width, richTextBox_tc.Location.Y + richTextBox_tc.Size.Height - bt_open_tc.Size.Height);

            bt_clear_tc.Location = new Point(richTextBox_tc.Location.X + richTextBox_tc.Size.Width - bt_clear_tc.Size.Width, richTextBox_tc.Location.Y + richTextBox_tc.Size.Height - bt_clear_tc.Size.Height);
            bt_copy_tc.Location = new Point(richTextBox_tc.Location.X + richTextBox_tc.Size.Width - bt_clear_tc.Size.Width - bt_copy_tc.Size.Width, richTextBox_tc.Location.Y + richTextBox_tc.Size.Height - bt_copy_tc.Size.Height);

            bt_open_sc.Location = new Point(richTextBox_sc.Location.X, richTextBox_sc.Location.Y + richTextBox_sc.Size.Height - bt_open_sc.Size.Height);
            bt_save_sc.Location = new Point(richTextBox_sc.Location.X + bt_open_sc.Size.Width, richTextBox_sc.Location.Y + richTextBox_sc.Size.Height - bt_open_sc.Size.Height);

            bt_clear_sc.Location = new Point(richTextBox_sc.Location.X + richTextBox_sc.Size.Width - bt_clear_sc.Size.Width, richTextBox_sc.Location.Y + richTextBox_sc.Size.Height - bt_clear_sc.Size.Height);
            bt_copy_sc.Location = new Point(richTextBox_sc.Location.X + richTextBox_sc.Size.Width - bt_clear_sc.Size.Width - bt_copy_sc.Size.Width, richTextBox_sc.Location.Y + richTextBox_sc.Size.Height - bt_copy_sc.Size.Height);

            this.ClientSize = new Size(border + W + dx + W + border, border + H + border);
            this.Text = "正中簡中轉換程式";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        //------------------------------------------------------------  # 60個

        private void bt_tc_sc_Click(object sender, EventArgs e)
        {
            // 正中轉簡中
            richTextBox_sc.Text = Big5ToGB2312(this.richTextBox_tc.Text);
        }

        private void bt_sc_tc_Click(object sender, EventArgs e)
        {
            // 簡中轉正中
            richTextBox_tc.Text = GB2312ToBig5(this.richTextBox_sc.Text);
        }

        private void bt_copy_tc_Click(object sender, EventArgs e)
        {
            // 複製資料到剪貼簿
            // Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox_tc.Text + "\n");      //建議用此
            richTextBox_tc.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_copy_sc_Click(object sender, EventArgs e)
        {
            // 複製資料到剪貼簿
            // Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox_sc.Text + "\n");      //建議用此
            richTextBox_sc.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_clear_tc_Click(object sender, EventArgs e)
        {
            richTextBox_tc.Clear();
        }

        private void bt_clear_sc_Click(object sender, EventArgs e)
        {
            richTextBox_sc.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void bt_open_tc_Click(object sender, EventArgs e)
        {
            //正中開啟檔案
        }

        private void bt_save_tc_Click(object sender, EventArgs e)
        {
            //正中儲存檔案

        }

        private void bt_open_sc_Click(object sender, EventArgs e)
        {
            //簡中開啟檔案
        }

        private void bt_save_sc_Click(object sender, EventArgs e)
        {
            //簡中儲存檔案

        }

        //------------------------------------------------------------  # 60個

        void convert_sc_to_tc(string filename)
        {
            //richTextBox1.Text += "\n檔案 : " + filename + "\n\n";

            if (System.IO.File.Exists(filename) == true)  //確認檔案是否存在
            {
                /*
                richTextBox1.Text += "檔名(包含副檔名)： " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名)： " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名： " + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "根目錄： " + Path.GetPathRoot(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetDirectoryName(filename) + "\n";
                */

                string fore_filename = Path.GetFileNameWithoutExtension(filename);
                string ext_filename = Path.GetExtension(filename);
                string foldername = Path.GetDirectoryName(filename);
                string backup_filename = Path.Combine(foldername, fore_filename + "_old" + ext_filename);

                //richTextBox1.Text += "新檔名： " + backup_filename + "\n";

                if (System.IO.File.Exists(backup_filename) == false)
                {
                    System.IO.File.Copy(filename, backup_filename);     //若檔案已存在, 會出現IOException
                }
                else
                {
                    MessageBox.Show("備份檔案已存在, 跳過");
                    return;
                }
            }
            else
            {
                //richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                return;
            }

            try
            {
                string all_text = System.IO.File.ReadAllText(filename, Encoding.UTF8);

                //簡中轉正中
                string all_tc_text = GB2312ToBig5(all_text);

                //string filename_new = @"D:\_git\vcs\_4.python\test10_new08_test_sc_tc_ccccc.py";
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

        private void bt_file_sc_tc_Click(object sender, EventArgs e)
        {
            //檔案 簡中轉正中
            //簡中轉正中
            //TBD
            //convert_sc_to_tc(filename);

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

