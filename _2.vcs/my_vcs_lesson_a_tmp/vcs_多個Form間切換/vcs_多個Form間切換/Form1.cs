using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_多個Form間切換
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            Form2 f = new Form2();//產生Form2的物件，才可以使用它所提供的Method

            this.Visible = false;//將Form1隱藏。由於在Form1的程式碼內使用this，所以this為Form1的物件本身
            f.Visible = true;//顯示第二個視窗
            */



            /*
            Form2 f = new Form2();//產生Form2的物件，才可以使用它所提供的Method
            f.Show(this);//設定Form2為Form1的上層，並開啟Form2視窗。由於在Form1的程式碼內使用this，所以this為Form1的物件本身

            f.TopMost = true;
            */
            /* 下面這段程式碼的用處在於是否要將Form2始終顯示在Form1上面。
             * f.TopMost
               其為布林值，true代表要始終顯示在上面；false代表Form1可以在Form2上面，預設為true。*/

            textBox1.Text = "";//先清空textbox1的文字

            Form2 f = new Form2();//產生Form2的物件，才可以使用它所提供的Method
            f.ShowDialog(this);//設定Form2為Form1的上層，並開啟Form2視窗。由於在Form1的程式碼內使用this，所以this為Form1的物件本身

            if (f.DialogResult == System.Windows.Forms.DialogResult.OK)
            {
                //若使用者在Form2按下了OK，則進入這個判斷式
                textBox1.Text = "按下了" + f.DialogResult.ToString();
            }
            else if (f.DialogResult == System.Windows.Forms.DialogResult.Cancel)
            {
                //若使用者在Form2按下了Cancel或者直接點選X關閉視窗，都會進入這個判斷式
                textBox1.Text = "按下了" + f.DialogResult.ToString();
            }
            else
            {
                textBox1.Text = "按下了" + f.DialogResult.ToString();
            }
        }
    }
}
