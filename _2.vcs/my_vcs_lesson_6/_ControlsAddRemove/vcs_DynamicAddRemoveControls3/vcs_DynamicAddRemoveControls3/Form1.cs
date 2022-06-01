using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

//所有的PNG檔要選屬性/複製到輸出目錄/選 有更新時才複製

namespace vcs_DynamicAddRemoveControls3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        // Display all of the images in the Buttons folder.
        private void button1_Click(object sender, EventArgs e)
        {
            const int wid = 40;
            const int hgt = 40;
            const int margin = 3;
            int x = margin;
            int y = margin;
            const int num_columns = 10;
            const int xmax = num_columns * (wid + margin);

            // Find the images.
            foreach (string filename in Directory.GetFiles("Buttons", "*.png"))
            {
                // Make a new Button.
                Button btn = new Button();
                btn.Parent = this;
                btn.Image = new Bitmap(filename);
                btn.Size = new Size(32, 32);
                btn.Location = new Point(x, y);
                x += wid + margin;
                if (x > xmax)
                {
                    x = margin;
                    y += hgt + margin;
                }

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }

            // Size the form to fit.
            //this.ClientSize = new Size(xmax + margin, y + hgt + margin);


        }

        private void button2_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\______test_files\__pic\_臨江仙";
            const int wid = 64 + 8;
            const int hgt = 64 + 8;
            const int margin = 3;
            int x = margin;
            int y = margin;
            const int num_columns = 6;
            const int xmax = num_columns * (wid + margin);

            int x_offset = 450;

            // Find the images.
            foreach (string filename in Directory.GetFiles(foldername, "*.jpeg"))
            {
                // Make a new Button.
                Button btn = new Button();
                btn.Parent = this;
                btn.BackgroundImage = new Bitmap(filename);
                btn.BackgroundImageLayout = ImageLayout.Zoom;
                btn.Size = new Size(64, 64);
                btn.Location = new Point(x + x_offset, y);
                x += wid + margin;
                if (x > xmax)
                {
                    x = margin;
                    y += hgt + margin;
                }

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }

            // Size the form to fit.
            //this.ClientSize = new Size(xmax + margin, y + hgt + margin);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Button[] btn = new Button[10];//Button 陣列

            richTextBox1.Text += "在 表單/panel/pictureBox/richtextBox 上動態建立10個按鈕控件\n";

            for (int i = 0; i < 10; i++)
            {
                btn[i] = new Button();//實體化Button

                btn[i].Size = new Size(60, 40);

                btn[i].Location = new Point(70 * (i % 5) + 20, 450 + 100 * (i / 5));

                btn[i].Text = i.ToString();

                btn[i].Click += new EventHandler(this.btnXO_Click);//事件

                this.Controls.Add(btn[i]); //add 到 this 容器
                //panel1.Controls.Add(btn[i]); //add 到 panel1 容器
                //pictureBox1.Controls.Add(btn[i]); //add 到 pictureBox1 容器
                //richTextBox1.Controls.Add(btn[i]); //add 到 richTextBox1 容器
            }
        }

        private void btnXO_Click(object sender, EventArgs e)//動態Button 的事件
        {
            richTextBox1.Text += "你按下: " + ((Button)(sender)).Text + "\t" +
            "索引值: " + ((Button)(sender)).TabIndex.ToString() + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            for (int j = 0; j < 10; j++)
            {
                for (int i = 0; i < this.Controls.Count; i++)
                {
                    if ((this.Controls[i].Name == "button1") || (this.Controls[i].Name == "button2") || (this.Controls[i].Name == "button3") || (this.Controls[i].Name == "button4"))
                    {
                        //richTextBox1.Text += "跳過 : " + this.Controls[i].Name + "\n";
                        continue;
                    }
                    else if (this.Controls[i].Name == "toolTip1")
                    {
                        //richTextBox1.Text += "跳過 : " + this.Controls[i].Name + "\n";
                        continue;
                    }
                    else if (this.Controls[i].Name == "richTextBox1")
                    {
                        //richTextBox1.Text += "跳過 : " + this.Controls[i].Name + "\n";
                        continue;
                    }

                    //richTextBox1.Text += "XXXXXXXX : " + this.Controls[i].Name + "\n";
                    //richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                    //richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                    //richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";

                    this.Controls.Remove(this.Controls[i]);
                }
            }
        }
    }
}

