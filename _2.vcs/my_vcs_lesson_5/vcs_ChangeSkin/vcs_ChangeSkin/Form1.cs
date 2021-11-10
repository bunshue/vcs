using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//工具箱 加入 IrisSkin4.dll 新增 skinEngine

namespace vcs_ChangeSkin
{
    public partial class Form1 : Form
    {
        int total_skins = 0;
        int current_skin = 0;
        List<string> Skins = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Skins = Directory.GetFiles("..\\..\\IrisSkin4.dll\\Skins\\", "*.ssk").ToList();

            total_skins = Skins.Count;
            richTextBox1.Text += "total_skins = " + total_skins.ToString() + "\n";

            Random r = new Random();
            current_skin = r.Next(total_skins);
            richTextBox1.Text += "Select " + current_skin.ToString() + "\tname : " + Skins[current_skin] + "\n";

            skinEngine1.SkinFile = Skins[current_skin];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            current_skin++;
            current_skin %= total_skins;
            richTextBox1.Text += "Select " + current_skin.ToString() + "\tname : " + Skins[current_skin] + "\n";

            skinEngine1.SkinFile = Skins[current_skin];
        }
    }
}

