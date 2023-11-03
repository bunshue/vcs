using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1202
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int k = 0;
        Color[] tint = new Color[5];

        private void Form1_Load(object sender, EventArgs e)
        {
            lblMsg.Text = "在標籤上按一下滑鼠鍵會出現數字\n" +
               "，雙擊滑鼠左鍵改變背顏色";
            tint[0] = Color.Brown;
            tint[1] = Color.Azure;
            tint[2] = Color.Chartreuse;
            tint[3] = Color.Cyan;
            tint[4] = Color.Gainsboro;
            //將兩個標籤的文字對齊以垂直置中，水平置中
            lblMouse.TextAlign = ContentAlignment.MiddleCenter;
            lblMsg.TextAlign = ContentAlignment.MiddleCenter;
        }

        //滑鼠單擊事件
        private void lblMouse_Click(object sender,
              EventArgs e)
        {
            lblMouse.Text = k.ToString();
            k += 1;
            if (k > 4)
                k = 0;
        }

        //滑鼠雙擊事件
        private void lblMouse_DoubleClick(object sender,
              EventArgs e)
        {
            lblMouse.Text = string.Empty;
            lblMouse.BackColor = tint[k];
        }
    }
}
