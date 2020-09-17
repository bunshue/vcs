using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseKety_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label2.Text = "";

        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            label2.Text = String.Format("按了 {0} 鍵，鍵碼：{1}", e.KeyCode, e.KeyValue);

            switch (e.KeyCode)
            {
                case Keys.Up:       // 判斷是否按鍵盤上鍵
                    label1.Text = "上";
                    break;
                case Keys.Down:      // 判斷是否按鍵盤下鍵
                    label1.Text = "下";

                    break;
                case Keys.Left:    // 判斷是否按鍵盤左鍵
                    label1.Text = "左";
                    break;
                case Keys.Right:   // 判斷是否按鍵盤右鍵
                    label1.Text = "右";
                    break;
                default:
                    label1.Text = "Form1_KeyDown你按了" + e.KeyCode.ToString() + "";
                    break;
            }

        }
    }
}
