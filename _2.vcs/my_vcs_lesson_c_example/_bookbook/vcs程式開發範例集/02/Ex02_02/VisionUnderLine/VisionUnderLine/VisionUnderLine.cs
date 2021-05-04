using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace VisionUnderLine
{
    public partial class VisionUnderLine : Form
    {
        public VisionUnderLine()
        {
            InitializeComponent();
        }

        private void VisionUnderLine_Load(object sender,EventArgs e)
        {
            System.Windows.Forms.TextBox goal = new CustomTextBoxGroup();//定義一個TextBox對像goal
            goal.Parent = this;//獲取或設置自定義TextBox控件的父容器
            this.Controls.Add(goal);//向窗體中添加自定義TextBox控件goal
        }
    }
}
