using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
方案 右鍵
加入/使用者控制項(U)/輸入控件名 WordArt
編輯WordArt.cs
編譯後 工具箱出現 WordArt 控件可供使用
*/

namespace vcs_WordArt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "方案 右鍵\n加入/使用者控制項(U)/輸入控件名 WordArt\n編輯WordArt.cs\n編譯後 工具箱出現 WordArt 控件可供使用";


        }
    }
}
