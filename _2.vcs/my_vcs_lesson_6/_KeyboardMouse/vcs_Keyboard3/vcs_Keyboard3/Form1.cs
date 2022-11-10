using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Keyboard3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setup_keyboard();
        }

        void setup_keyboard()
        {
            int x_st = 20;
            int y_st = 30;
            int w = 35;
            int h = 35;
            int dx = w + 5;
            int dy = h + 5;
            lb_Q.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_W.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_E.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            lb_R.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            lb_T.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            lb_Y.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            lb_U.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            lb_I.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            lb_O.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            lb_P.Location = new Point(x_st + dx * 9, y_st + dy * 0);
            tb_input.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            x_st += 20;
            lb_A.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_S.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_D.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            lb_F.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            lb_G.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            lb_H.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            lb_J.Location = new Point(x_st + dx * 6, y_st + dy * 1);
            lb_K.Location = new Point(x_st + dx * 7, y_st + dy * 1);
            lb_L.Location = new Point(x_st + dx * 8, y_st + dy * 1);

            x_st += 20;
            lb_Z.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_X.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_C.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            lb_V.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            lb_B.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            lb_N.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            lb_M.Location = new Point(x_st + dx * 6, y_st + dy * 2);
            lb_backspace.Location = new Point(x_st + dx * 7, y_st + dy * 2);
            lb_clear.Location = new Point(x_st + dx * 7, y_st + dy * 3);

            x_st = 450;
            y_st = 30;
            lb_1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            lb_4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            lb_7.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_8.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_9.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            lb_0.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_OK.Location = new Point(x_st + dx * 1, y_st + dy * 3);

            groupBox_keyboard.Size = new Size(600, 220);

            lb_backspace.Click += new EventHandler(lb_backspace_Click);
            lb_clear.Click += new EventHandler(lb_clear_Click);
            lb_OK.Click += new EventHandler(lb_OK_Click);

            setup_keyboard_keys(this.groupBox_keyboard.Controls);
        }

        void lb_Click(object sender, EventArgs e)
        {
            Label l = (Label)sender;
            tb_input.Text += l.Name.Substring(3, 1);
            tb_input.SelectionStart = tb_input.Text.Length;
        }

        void lb_backspace_Click(object sender, EventArgs e)
        {
            if (tb_input.Text.Length <= 0)
                return;
            Label l = (Label)sender;
            tb_input.Text = tb_input.Text.Substring(0, tb_input.Text.Length - 1);
            tb_input.SelectionStart = tb_input.Text.Length;
        }

        void lb_clear_Click(object sender, EventArgs e)
        {
            tb_input.Clear();
        }

        void lb_OK_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你輸入了 : " + tb_input.Text.ToString() + "\n";
            tb_input.Text = "";
        }

        public void setup_keyboard_keys(Control.ControlCollection cc)
        {
            foreach (Control c in cc)  //撈出所有控件
            {
                //richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Label")   //判斷是否為 Button 控件
                {
                    //richTextBox1.Text += "\t" + ((Label)c).Name + "\t" + ((Label)c).Text + "\t" + ((Label)c).Size.Width.ToString() + " X " + ((Label)c).Size.Height.ToString();

                    //改 backcolor.size.text font alignment...
                    //((Label)c).Size = new Size(((Label)c).Size.Width / 2, ((Label)c).Size.Height / 2);    //設定大小
                    ((Label)c).BackColor = Color.Lime;
                    ((Label)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                    ((Label)c).TextAlign = ContentAlignment.MiddleCenter;

                    if (((Label)c).Name.Length == 4)
                    {
                        //richTextBox1.Text += ((Label)c).Name + "\n";
                        ((Label)c).Click += new EventHandler(lb_Click);
                    }

                    //richTextBox1.Text += ((Label)c).Name + "\t" + ((Label)c).Name.Length.ToString() + "\n";

                    //lb_backspace	12
                    if (((Label)c).Name.Length == 12)
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                    }

                    //lb_OK	5
                    if (((Label)c).Name.Length == 5)
                    {
                        ((Label)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                    }

                    //lb_clear	8
                    if (((Label)c).Name.Length == 8)
                    {
                        ((Label)c).Font = new Font("標楷體", 14, FontStyle.Bold);  //建立字體對象
                    }


                }
                //richTextBox1.Text += "\n";
            }
        }
    }
}
