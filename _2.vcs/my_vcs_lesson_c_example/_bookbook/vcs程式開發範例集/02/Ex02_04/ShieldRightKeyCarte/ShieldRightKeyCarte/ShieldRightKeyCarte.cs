using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ShieldRightKeyCarte
{
    public partial class ShieldRightKeyCarte : Form
    {
        public ShieldRightKeyCarte()
        {
            InitializeComponent();
        }

        System.Windows.Forms.TextBox RightKeyCarte;//聲明一個自定義類CustomTextBoxGroup的對象
        private void ShieldRightKeyCarte_Load(object sender, EventArgs e)
        {
            this.RightKeyCarte = new CustomTextBoxGroup();//實例化該類的對象
            this.RightKeyCarte.Parent = this; //設定自定義控件的父容器為當前窗口
            this.Controls.Add(this.RightKeyCarte);//在當前窗體中添加自定義控件
        }
    }
}
