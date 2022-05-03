using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_UseConfigFile
{
    public partial class Form1 : Form
    {
        private String config_filename = "ConfigFile.cfg";
        static String RootPath;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadConfig();

            //檢查存圖的資料夾
            string Path = @"C:\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }
            RootPath = Path;
        }

        void LoadConfig()
        {
            richTextBox1.Text += "LoadConfig, config_filename : " + config_filename + "\n";

            if (!File.Exists(config_filename))
            {
                //設定檔不存在
                RootPath = @"C:\dddddddddd";
                SaveConfig();
                richTextBox1.Text += "LoadConfig 111 RootPath = " + RootPath + "\n";
            }
            else
            {
                StreamReader sr = new StreamReader(config_filename);

                String Line;
                while ((Line = sr.ReadLine()) != null)
                {
                    if (Line[0] == '#')
                    {
                        //skip comment line
                    }
                    else if (Line.Contains("RootPath="))
                    {
                        RootPath = Line.Substring("RootPath=".Length);
                    }
                    else if (Line.Contains("BalloonTips="))
                    {
                        checkBox2.Checked = Convert.ToBoolean(Line.Substring("BalloonTips=".Length));
                    }
                    else if (Line.Contains("Sound="))
                    {
                        checkBox1.Checked = Convert.ToBoolean(Line.Substring("Sound=".Length));
                    }
                }
                sr.Close();

                richTextBox1.Text += "LoadConfig 222 config_filename = " + config_filename + "\n";
            }
        }

        void SaveConfig()
        {
            StreamWriter sw = new StreamWriter(config_filename);

            sw.WriteLine("RootPath=" + RootPath);
            sw.WriteLine("BalloonTips=" + checkBox2.Checked);
            sw.WriteLine("Sound=" + checkBox1.Checked);

            sw.Close();

            richTextBox1.Text += "SaveConfig\nFilename = " + config_filename + "\n";
            richTextBox1.Text += "RootPath = " + RootPath + "\n";
            richTextBox1.Text += "BalloonTips = " + checkBox2.Checked + "\n";
            richTextBox1.Text += "Sound = " + checkBox1.Checked + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SaveConfig();
        }
    }
}
