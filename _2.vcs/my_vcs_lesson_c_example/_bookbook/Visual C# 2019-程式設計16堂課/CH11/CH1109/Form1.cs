using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1109
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] choice = {
            "國文", "英文", "數學", "理化", "地理",
            "歷史", "自然科學", "生物" };
            clstCourse.Items.AddRange(choice);
            //單擊滑鼠左鍵就能選取控制項
            clstCourse.CheckOnClick = true;
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            clstCourse.Items.Add(txtItem.Text);//新增項目
        }

        private void btnRemove_Click(object sender, EventArgs e)
        {
            clstCourse.Items.Remove(txtItem.Text);//移除項目
        }

        private void clstCourse_ItemCheck(object sender,
              ItemCheckEventArgs e)
        {
            //將勾選的項目以文字方塊顯示
            txtItem.Text = clstCourse.SelectedItem.ToString();
        }
    }
}
