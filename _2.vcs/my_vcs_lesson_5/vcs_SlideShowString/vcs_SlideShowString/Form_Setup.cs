using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport
using System.IO;

namespace vcs_SlideShowString
{
    public partial class Form_Setup : Form
    {
        private const int PLAYMODE_SEQUENCE = 0;
        private const int PLAYMODE_RANDOM = 1;
        private const int PLAYMODE_SEQUENCE_RANDOM = 2;

        string filename = "";//該變量保存INI文件所在的具体物理位置
        string strOne = "";

        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(
            string lpAppName,
            string lpKeyName,
            string lpDefault,
            StringBuilder lpReturnedString,
            int nSize,
            string lpFileName);

        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(
            string mpAppName,
            string mpKeyName,
            string mpDefault,
            string mpFileName);

        public string ContentReader(string area, string key, string def)
        {
            StringBuilder stringBuilder = new StringBuilder(1024); 				//定义一个最大长度为1024的可变字符串
            GetPrivateProfileString(area, key, def, stringBuilder, 1024, filename); 			//读取INI文件
            return stringBuilder.ToString();								//返回INI文件的内容
        }

        void load_poetry_ini()
        {
            filename = Application.StartupPath + "\\poetry.ini";		//INI文件的物理地址
            richTextBox1.Text += "filename = " + filename + "\n";
            strOne = System.IO.Path.GetFileNameWithoutExtension(filename); 		//獲取INI文件的文件名
            if (File.Exists(filename)) 						//判斷是否存在該INI文件
            {
                richTextBox1.Text += "Align: " + ContentReader(strOne, "Align", "") + "\n";			            //讀取INI文件中Align項
                richTextBox1.Text += "PlaySequence: " + ContentReader(strOne, "PlaySequence", "") + "\n";			    //讀取INI文件中PlaySequence項
                richTextBox1.Text += "FontType: " + ContentReader(strOne, "FontType", "") + "\n";				//讀取INI文件中FontType項
                richTextBox1.Text += "FontSize: " + ContentReader(strOne, "FontSize", "") + "\n";				//讀取INI文件中FontSize項

                richTextBox1.Text += "FontUserSize: " + ContentReader(strOne, "FontUserSize", "") + "\n";		//讀取INI文件中FontUserSize項
                richTextBox1.Text += "PlaySpeed: " + ContentReader(strOne, "PlaySpeed", "") + "\n";				//讀取INI文件中PlaySpeed項
                richTextBox1.Text += "TopMost: " + ContentReader(strOne, "TopMost", "") + "\n";				    //讀取INI文件中TopMost項
                richTextBox1.Text += "RatioWidth: " + ContentReader(strOne, "RatioWidth", "") + "\n";			//讀取INI文件中RatioWidth項
                richTextBox1.Text += "RatioHeight: " + ContentReader(strOne, "RatioHeight", "") + "\n";		//讀取INI文件中RatioHeight項

                int align_direction = 0;
                int play_sequence = 0;
                string font_type = String.Empty;
                int font_size_default = 0;
                int font_size_user = 0;
                float font_size_current;
                float font_size_current_max;
                int slide_show_interval = 0;
                int display_width = 0;      //percentage
                int display_height = 0;     //percentage
                bool flag_top_most = false;
                bool flag_pause = false;

                align_direction = int.Parse(ContentReader(strOne, "Align", ""));
                richTextBox1.Text += "value = " + align_direction.ToString() + "\n";
                richTextBox1.Text += "設定對齊方向" + "\t";
                if (align_direction == 0)
                    richTextBox1.Text += "靠右\n";
                else if (align_direction == 1)
                    richTextBox1.Text += "靠右\n";
                else
                    richTextBox1.Text += "正中\n";
                comboBox0.SelectedIndex = align_direction;

                play_sequence = int.Parse(ContentReader(strOne, "PlaySequence", ""));
                richTextBox1.Text += "value = " + play_sequence.ToString() + "\n";
                richTextBox1.Text += "設定播放順序" + "\t";
                if (play_sequence == PLAYMODE_SEQUENCE)
                {
                    play_sequence = PLAYMODE_SEQUENCE;
                    richTextBox1.Text += "依序\n";
                }
                else if (play_sequence == PLAYMODE_RANDOM)
                {
                    play_sequence = PLAYMODE_RANDOM;
                    richTextBox1.Text += "隨機\n";
                }
                else if (play_sequence == PLAYMODE_SEQUENCE_RANDOM)
                {
                    play_sequence = PLAYMODE_SEQUENCE_RANDOM;
                    richTextBox1.Text += "依序隨機啟動\n";
                }
                else
                {
                    play_sequence = PLAYMODE_SEQUENCE;
                    richTextBox1.Text += "依序\n";
                }
                comboBox1.SelectedIndex = play_sequence;

                font_size_user = int.Parse(ContentReader(strOne, "FontUserSize", ""));
                richTextBox1.Text += "自訂字型大小: " + font_size_user.ToString() + "\n";
                numericUpDown3.Value = font_size_user;

                slide_show_interval = int.Parse(ContentReader(strOne, "PlaySpeed", ""));
                richTextBox1.Text += "播放速度: " + slide_show_interval.ToString() + " 秒\n";
                numericUpDown4.Value = slide_show_interval;

                if (ContentReader(strOne, "TopMost", "") == "0")
                {
                    flag_top_most = false;
                    richTextBox1.Text += "設定非最上層顯示\n";
                    comboBox5.SelectedIndex = 0;
                }
                else if (ContentReader(strOne, "TopMost", "") == "1")
                {
                    flag_top_most = true;
                    richTextBox1.Text += "設定最上層顯示\n";
                    comboBox5.SelectedIndex = 1;
                }


                display_width = int.Parse(ContentReader(strOne, "RatioWidth", ""));
                richTextBox1.Text += "display width = " + display_width.ToString() + " %\n";
                numericUpDown6.Value = display_width;

                display_height = int.Parse(ContentReader(strOne, "RatioHeight", ""));
                richTextBox1.Text += "display height = " + display_height.ToString() + " %\n";
                numericUpDown7.Value = display_height;






            }


        }

        public Form_Setup()
        {
            InitializeComponent();


            int x_st = 50;
            int y_st = 100;
            int dy = 55;
            label0.Location = new Point(x_st, y_st + dy * 0);
            label1.Location = new Point(x_st, y_st + dy * 1);
            label2.Location = new Point(x_st, y_st + dy * 2);
            label3.Location = new Point(x_st, y_st + dy * 3);
            label4.Location = new Point(x_st, y_st + dy * 4);
            label5.Location = new Point(x_st, y_st + dy * 5);
            label6.Location = new Point(x_st, y_st + dy * 6);
            label7.Location = new Point(x_st, y_st + dy * 7);
            label0.Text = "對齊方向：";
            label1.Text = "播放順序：";
            label2.Text = "字型：";
            label3.Text = "自訂字型大小：";
            label4.Text = "播放速度：";
            label5.Text = "最上層顯示：";
            label6.Text = "螢幕佔寬比：";
            label7.Text = "螢幕佔高比：";

            int dx = 200;
            label22.Location = new Point(x_st + dx, y_st + dy * 2);
            button2.Location = new Point(x_st + dx + dx, y_st + dy * 2);
            comboBox0.Location = new Point(x_st + dx, y_st + dy * 0);
            comboBox1.Location = new Point(x_st + dx, y_st + dy * 1);
            comboBox5.Location = new Point(x_st + dx, y_st + dy * 5);

            numericUpDown3.Location = new Point(x_st + dx, y_st + dy * 3);
            numericUpDown4.Location = new Point(x_st + dx, y_st + dy * 4);
            numericUpDown6.Location = new Point(x_st + dx, y_st + dy * 6);
            numericUpDown7.Location = new Point(x_st + dx, y_st + dy * 7);

            load_poetry_ini();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;

            //fontDialog1.Font = label1.Font;
            //fontDialog1.Color = label1.ForeColor;

            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                label22.Font = fontDialog1.Font;
                label22.ForeColor = fontDialog1.Color;
                label22.Text = fontDialog1.Font.Name + " " + fontDialog1.Font.Size.ToString();
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            load_poetry_ini();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            save_poetry_ini();
        }

        void save_poetry_ini()
        {
            filename = Application.StartupPath + "\\poetry2.ini";		//INI文件的物理地址
            //if (File.Exists(filename))											//判断是否存在INI文件
            {
                WritePrivateProfileString(strOne, "Align", comboBox0.SelectedIndex.ToString(), filename); 		    //修改INI文件中的第1項
                WritePrivateProfileString(strOne, "PlaySequence", comboBox1.SelectedIndex.ToString(), filename); 		    //修改INI文件中的第1項
                //WritePrivateProfileString(strOne, "FontType", textBox1.Text, filename); 		    //修改INI文件中的第1項
                //WritePrivateProfileString(strOne, "FontSize", textBox1.Text, filename); 		    //修改INI文件中的第1項

                WritePrivateProfileString(strOne, "FontUserSize", numericUpDown3.Value.ToString(), filename); 		    //修改INI文件中的第1項
                WritePrivateProfileString(strOne, "PlaySpeed", numericUpDown4.Value.ToString(), filename); 		    //修改INI文件中的第1項
                WritePrivateProfileString(strOne, "TopMost", comboBox5.SelectedIndex.ToString(), filename); 		    //修改INI文件中的第1項
                WritePrivateProfileString(strOne, "RatioWidth", numericUpDown6.Value.ToString(), filename); 		    //修改INI文件中的第1項
                WritePrivateProfileString(strOne, "RatioHeight", numericUpDown7.Value.ToString(), filename); 		    //修改INI文件中的第1項
                
                richTextBox1.Text += "修改成功\n";
            }
            //else
            {
                //MessageBox.Show("对不起，你所要修改的文件不存在，请确认后再进行修改操作！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }



        }

    }
}





