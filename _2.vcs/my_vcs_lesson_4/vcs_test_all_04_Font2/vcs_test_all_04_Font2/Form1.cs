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

namespace vcs_test_all_04_Font2
{
    public partial class Form1 : Form
    {
        bool flag_debug_mode = false;
        FontFamily old_font_name;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "瀏覽資料夾內的字型檔";
            label2.Text = "唐 王昌齡 出塞\n秦時明月漢時關\n萬里長征人未還\n但使龍城飛將在\n不教胡馬度陰山。";
            tb_font_size.Text = label2.Font.Size.ToString();
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;
            bt_plus.BackgroundImage = Properties.Resources.plus;
            bt_plus.BackgroundImageLayout = ImageLayout.Zoom;
            bt_minus.BackgroundImage = Properties.Resources.minus;
            bt_minus.BackgroundImageLayout = ImageLayout.Zoom;
            bt_clear.BackgroundImage = Properties.Resources.clear;
            bt_clear.BackgroundImageLayout = ImageLayout.Zoom;
            bt_x.BackgroundImage = Properties.Resources.x;
            bt_x.BackgroundImageLayout = ImageLayout.Zoom;
            bt_x.Visible = false;

            show_item_location();
            old_font_name = label2.Font.FontFamily;

            if (flag_debug_mode == true)
            {
                comboBox1.Items.Clear();

                string foldername = @"D:\_git\整理字型";

                richTextBox1.Text += "撈出資料夾 " + foldername + " 內所有圖片檔案合併\n";

                // Get the picture files in the source directory.
                List<string> files = new List<string>();
                foreach (string filename in Directory.GetFiles(foldername))
                {
                    int pos = filename.LastIndexOf('.');
                    string extension = filename.Substring(pos).ToLower();
                    if ((extension == ".ttf") ||
                        (extension == ".ttc") ||
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int BORDER = 10;
            bt_plus.Location = new Point(this.ClientSize.Width - bt_plus.Size.Width - BORDER, 0 + BORDER);
            bt_minus.Location = new Point(this.ClientSize.Width - bt_minus.Size.Width - BORDER, 0 + BORDER + bt_plus.Height + BORDER);
            bt_x.Location = new Point(this.ClientSize.Width - bt_minus.Size.Width - BORDER, 0 + BORDER + bt_plus.Height + BORDER + bt_minus.Height + BORDER);

            tb_font_size.Location = new Point(this.ClientSize.Width - bt_plus.Size.Width - BORDER - tb_font_size.Width - BORDER, 0 + BORDER);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();

            folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            //folderBrowserDialog1.SelectedPath = @"D:\_git\整理字型";
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                /*
                richTextBox1.Text += "RootFolder: " + folderBrowserDialog1.RootFolder + "\n";
                richTextBox1.Text += "Container: " + folderBrowserDialog1.Container + "\n";
                richTextBox1.Text += "Description: " + folderBrowserDialog1.Description + "\n";
                richTextBox1.Text += "ShowNewFolderButton: " + folderBrowserDialog1.ShowNewFolderButton + "\n";
                richTextBox1.Text += "Site: " + folderBrowserDialog1.Site + "\n";
                richTextBox1.Text += "Tag: " + folderBrowserDialog1.Tag + "\n";
                */
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
                        (extension == ".ttc") ||
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

            //讀取字體文件
            PrivateFontCollection pfc = new PrivateFontCollection();
            pfc.AddFontFile(font_filename);

            //實例化字體
            Font f = new Font(pfc.Families[0], label2.Font.Size);

            //設置字體
            label2.Font = f;
            old_font_name = pfc.Families[0];
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            float old_font_size = label2.Font.Size;
            old_font_size += 4;

            //實例化字體
            Font f = new Font(old_font_name, old_font_size);

            //設置字體
            label2.Font = f;
            tb_font_size.Text = label2.Font.Size.ToString();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            float old_font_size = label2.Font.Size;
            old_font_size -= 4;
            if (old_font_size < 10)
                old_font_size = 10;

            //實例化字體
            Font f = new Font(old_font_name, old_font_size);

            //設置字體
            label2.Font = f;
            tb_font_size.Text = label2.Font.Size.ToString();
        }

        private void bt_x_Click(object sender, EventArgs e)
        {
            //顯示目前字型種類

            richTextBox1.Text += "fontname = " + label2.Font.Name + "\n";
        }

    }
}
