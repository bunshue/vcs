using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Text;  //for InstalledFontCollection, PrivateFontCollection

namespace vcs_ShowFont
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "瀏覽資料夾內的字型檔";
            label2.Text = "唐 王昌齡 出塞\n秦時明月漢時關\n萬里長征人未還\n但使龍城飛將在\n不教胡馬度陰山。";
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();

            folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            folderBrowserDialog1.SelectedPath = @"C:\_git\vcs\_1.data\______test_files5";
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                richTextBox1.Text += "RootFolder: " + folderBrowserDialog1.RootFolder + "\n";
                richTextBox1.Text += "Container: " + folderBrowserDialog1.Container + "\n";
                richTextBox1.Text += "Description: " + folderBrowserDialog1.Description + "\n";
                richTextBox1.Text += "ShowNewFolderButton: " + folderBrowserDialog1.ShowNewFolderButton + "\n";
                richTextBox1.Text += "Site: " + folderBrowserDialog1.Site + "\n";
                richTextBox1.Text += "Tag: " + folderBrowserDialog1.Tag + "\n";

                comboBox1.Items.Clear();

                string foldername = folderBrowserDialog1.SelectedPath;

                richTextBox1.Text += "撈出資料夾 " + foldername + " 內所有圖片檔案合併\n";

                // Get the picture files in the source directory.
                List<string> files = new List<string>();
                foreach (string filename in Directory.GetFiles(foldername))
                {
                    int pos = filename.LastIndexOf('.');
                    string extension = filename.Substring(pos).ToLower();
                    if ((extension == ".ttf") ||
                        (extension == ".otf"))
                    {
                        files.Add(filename);
                        comboBox1.Items.Add(filename);
                    }
                }

                int num_images = files.Count;
                if (num_images == 0)
                {
                    richTextBox1.Text += "無字型檔\n";
                    return;
                }

                for (int i = 0; i < num_images; i++)
                {
                    richTextBox1.Text += "第 " + (i + 1).ToString() + " 個檔案\t" + files[i] + "\n";
                }
                comboBox1.SelectedIndex = 0;
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "你選擇了 : " + comboBox1.SelectedItem.ToString() + "\n";
            string font_filename = comboBox1.SelectedItem.ToString();

            apply_selected_font(font_filename);
        }

        void apply_selected_font(string font_filename)
        {
            //指明使用特定字型檔

            //string font_filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_4\vcs_test_all_04_Font\vcs_test_all_04_Font\font\金梅重黑浮體白字.ttf";

            //讀取字體文件
            PrivateFontCollection pfc = new PrivateFontCollection();
            pfc.AddFontFile(font_filename);

            //實例化字體
            Font f = new Font(pfc.Families[0], label2.Font.Size);

            //設置字體
            label2.Font = f;
        }
    }
}
