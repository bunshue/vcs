using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ShieldPasteFunction
{
    public partial class ShieldPasteFunction : Form
    {
        public ShieldPasteFunction()
        {
            InitializeComponent();
        }
        TextBox NoStiky = new CustomTextBoxGroup();//聲明一個自定義類CustomTextBoxGroup的對象
        private void ShieldPasteFunction_Load(object sender, EventArgs e)
        {
            this.NoStiky.Parent = this;//設定自定義控件的父容器為當前窗口
            this.Controls.Add(this.NoStiky);//在當前窗體中添加自定義控件
        }
    }
}
