using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Keyboard5
{
    public partial class keyboard1 : UserControl
    {
        Color groupBox_keyboard_backcolor = Color.LightSalmon;
        Color key_color = Color.Lime;
        Color key_press_color = Color.Green;

        Label lb_result = new Label();

        public keyboard1()
        {
            InitializeComponent();
        }

        private void keyboard1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(600, 260);
            setup_keyboard();
        }

        void setup_keyboard()
        {
            groupBox_keyboard.Location = new Point(10, 10);
            groupBox_keyboard.Size = new Size(600, 240);
            groupBox_keyboard.BackColor = groupBox_keyboard_backcolor;
            groupBox_keyboard.Text = "";

            lb_backspace.MouseDown += new MouseEventHandler(lb_backspace_MouseDown);
            lb_backspace.MouseUp += new MouseEventHandler(lb_backspace_MouseUp);

            lb_clear.MouseDown += new MouseEventHandler(lb_clear_MouseDown);
            lb_clear.MouseUp += new MouseEventHandler(lb_clear_MouseUp);

            lb_OK.MouseDown += new MouseEventHandler(lb_OK_MouseDown);
            lb_OK.MouseUp += new MouseEventHandler(lb_OK_MouseUp);

            lb_result.Text = "";
            lb_result.Font = new Font("標楷體", 22);
            lb_result.ForeColor = Color.Black;
            lb_result.BackColor = Color.Pink;
            lb_result.AutoSize = true;
            this.groupBox_keyboard.Controls.Add(lb_result);

            setup_keyboard_keys(this.groupBox_keyboard.Controls);
        }

        public void setup_keyboard_keys(Control.ControlCollection cc)
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
            tb_input.Size = new Size(300, 36);

            lb_result.Location = new Point(x_st + dx * 0, y_st + dy * 4);

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

            foreach (Control c in cc)  //撈出所有控件
            {
                //richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Label")   //判斷是否為 Label 控件
                {
                    //richTextBox1.Text += "\t" + ((Label)c).Name + "\t" + ((Label)c).Text + "\t" + ((Label)c).Size.Width.ToString() + " X " + ((Label)c).Size.Height.ToString();

                    //改 backcolor.size.text font alignment...
                    ((Label)c).Size = new Size(w, h);  //設定大小
                    ((Label)c).BackColor = key_color;
                    ((Label)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                    ((Label)c).TextAlign = ContentAlignment.MiddleCenter;

                    if (((Label)c).Name.Length == 4)
                    {
                        //richTextBox1.Text += ((Label)c).Name + "\n";
                        ((Label)c).MouseDown += new MouseEventHandler(lb_MouseDown);
                        ((Label)c).MouseUp += new MouseEventHandler(lb_MouseUp);
                    }

                    //richTextBox1.Text += ((Label)c).Name + "\t" + ((Label)c).Name.Length.ToString() + "\n";

                    //lb_backspace	12
                    if (((Label)c).Name.Length == 12)
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Label)c).Text = "Backspace";
                    }

                    //lb_OK	5
                    if (((Label)c).Name.Length == 5)
                    {
                        ((Label)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Label)c).Text = "OK";
                    }

                    //lb_clear	8
                    if (((Label)c).Name.Length == 8)
                    {
                        ((Label)c).Font = new Font("標楷體", 14, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Label)c).Text = "Clear";
                    }
                }
                //richTextBox1.Text += "\n";
            }
        }

        void lb_backspace_MouseDown(object sender, MouseEventArgs e)
        {
            lb_backspace.BackColor = key_press_color;

            if (tb_input.Text.Length <= 0)
                return;
            tb_input.Text = tb_input.Text.Substring(0, tb_input.Text.Length - 1);
            tb_input.SelectionStart = tb_input.Text.Length;
        }

        void lb_backspace_MouseUp(object sender, MouseEventArgs e)
        {
            lb_backspace.BackColor = key_color;
        }

        void lb_clear_MouseDown(object sender, MouseEventArgs e)
        {
            lb_clear.BackColor = key_press_color;
            tb_input.Clear();
        }

        void lb_clear_MouseUp(object sender, MouseEventArgs e)
        {
            lb_clear.BackColor = key_color;
        }

        void lb_OK_MouseDown(object sender, MouseEventArgs e)
        {
            lb_OK.BackColor = key_press_color;

            if (tb_input.Text.Length <= 0)
            {
                lb_result.Text = "未輸入資料";
            }
            else
            {
                lb_result.Text = "你輸入了 : " + tb_input.Text.ToString();
            }
            tb_input.Text = "";
        }

        void lb_OK_MouseUp(object sender, MouseEventArgs e)
        {
            lb_OK.BackColor = key_color;
        }

        void lb_MouseDown(object sender, MouseEventArgs e)
        {
            Label lb = (Label)sender;
            tb_input.Text += lb.Name.Substring(3, 1);
            tb_input.SelectionStart = tb_input.Text.Length;

            lb.BackColor = key_press_color;
        }

        void lb_MouseUp(object sender, MouseEventArgs e)
        {
            Label lb = (Label)sender;
            lb.BackColor = key_color;
        }
    }
}
