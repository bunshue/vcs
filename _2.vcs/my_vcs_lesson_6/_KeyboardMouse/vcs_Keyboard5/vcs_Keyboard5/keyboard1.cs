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

        GroupBox groupBox_keyboard = new GroupBox();

        Label lb_A = new Label();
        Label lb_B = new Label();
        Label lb_C = new Label();
        Label lb_D = new Label();
        Label lb_E = new Label();
        Label lb_F = new Label();
        Label lb_G = new Label();
        Label lb_H = new Label();
        Label lb_I = new Label();
        Label lb_J = new Label();
        Label lb_K = new Label();
        Label lb_L = new Label();
        Label lb_M = new Label();
        Label lb_N = new Label();
        Label lb_O = new Label();
        Label lb_P = new Label();
        Label lb_Q = new Label();
        Label lb_R = new Label();
        Label lb_S = new Label();
        Label lb_T = new Label();
        Label lb_U = new Label();
        Label lb_V = new Label();
        Label lb_W = new Label();
        Label lb_X = new Label();
        Label lb_Y = new Label();
        Label lb_Z = new Label();
        Label lb_1 = new Label();
        Label lb_2 = new Label();
        Label lb_3 = new Label();
        Label lb_4 = new Label();
        Label lb_5 = new Label();
        Label lb_6 = new Label();
        Label lb_7 = new Label();
        Label lb_8 = new Label();
        Label lb_9 = new Label();
        Label lb_0 = new Label();
        Label lb_period = new Label();
        Label lb_backspace = new Label();
        Label lb_esc = new Label();
        Label lb_caps_lock = new Label();
        Label lb_shift = new Label();
        Label lb_space = new Label();
        Label lb_clear = new Label();
        Label lb_OK = new Label();
        TextBox tb_input = new TextBox();
        Label lb_result = new Label();

        bool flag_caps_lock = false;
        bool flag_caps_lock_once = false;

        public keyboard1()
        {
            InitializeComponent();
        }

        private void keyboard1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(660, 230);
            this.BackColor = Color.Pink;
            setup_keyboard();
        }

        void setup_keyboard()
        {
            groupBox_keyboard.Location = new Point(10, 10);
            //groupBox_keyboard.Size = new Size(630, 240);
            groupBox_keyboard.BackColor = groupBox_keyboard_backcolor;
            groupBox_keyboard.Text = "";
            groupBox_keyboard.Dock = DockStyle.Fill;
            this.Controls.Add(groupBox_keyboard);

            lb_A.Name = "lb_A";
            lb_B.Name = "lb_B";
            lb_C.Name = "lb_C";
            lb_D.Name = "lb_D";
            lb_E.Name = "lb_E";
            lb_F.Name = "lb_F";
            lb_G.Name = "lb_G";
            lb_H.Name = "lb_H";
            lb_I.Name = "lb_I";
            lb_J.Name = "lb_J";

            lb_K.Name = "lb_K";
            lb_L.Name = "lb_L";
            lb_M.Name = "lb_M";
            lb_N.Name = "lb_N";
            lb_O.Name = "lb_O";
            lb_P.Name = "lb_P";
            lb_Q.Name = "lb_Q";
            lb_R.Name = "lb_R";
            lb_S.Name = "lb_S";
            lb_T.Name = "lb_T";

            lb_U.Name = "lb_U";
            lb_V.Name = "lb_V";
            lb_W.Name = "lb_W";
            lb_X.Name = "lb_X";
            lb_Y.Name = "lb_Y";
            lb_Z.Name = "lb_Z";

            lb_1.Name = "lb_1";
            lb_2.Name = "lb_2";
            lb_3.Name = "lb_3";
            lb_4.Name = "lb_4";
            lb_5.Name = "lb_5";
            lb_6.Name = "lb_6";
            lb_7.Name = "lb_7";
            lb_8.Name = "lb_8";
            lb_9.Name = "lb_9";
            lb_0.Name = "lb_0";

            lb_period.Name = "lb_period";
            lb_backspace.Name = "lb_backspace";
            lb_esc.Name = "lb_esc";
            lb_caps_lock.Name = "lb_caps_lock";
            lb_shift.Name = "lb_shift";
            lb_space.Name = "lb_space";
            lb_clear.Name = "lb_clear";
            lb_OK.Name = "lb_OK";

            lb_period.MouseDown += new MouseEventHandler(lb_MouseDown);
            lb_period.MouseUp += new MouseEventHandler(lb_MouseUp);

            lb_backspace.MouseDown += new MouseEventHandler(lb_backspace_MouseDown);
            lb_backspace.MouseUp += new MouseEventHandler(lb_backspace_MouseUp);

            lb_esc.MouseDown += new MouseEventHandler(lb_esc_MouseDown);
            lb_esc.MouseUp += new MouseEventHandler(lb_esc_MouseUp);

            lb_caps_lock.MouseDown += new MouseEventHandler(lb_caps_lock_MouseDown);
            lb_caps_lock.MouseUp += new MouseEventHandler(lb_caps_lock_MouseUp);

            lb_shift.MouseDown += new MouseEventHandler(lb_shift_MouseDown);
            lb_shift.MouseUp += new MouseEventHandler(lb_shift_MouseUp);

            lb_space.MouseDown += new MouseEventHandler(lb_MouseDown);
            lb_space.MouseUp += new MouseEventHandler(lb_MouseUp);

            lb_clear.MouseDown += new MouseEventHandler(lb_clear_MouseDown);
            lb_clear.MouseUp += new MouseEventHandler(lb_clear_MouseUp);

            lb_OK.MouseDown += new MouseEventHandler(lb_OK_MouseDown);
            lb_OK.MouseUp += new MouseEventHandler(lb_OK_MouseUp);

            this.groupBox_keyboard.Controls.Add(lb_A);
            this.groupBox_keyboard.Controls.Add(lb_B);
            this.groupBox_keyboard.Controls.Add(lb_C);
            this.groupBox_keyboard.Controls.Add(lb_D);
            this.groupBox_keyboard.Controls.Add(lb_E);
            this.groupBox_keyboard.Controls.Add(lb_F);
            this.groupBox_keyboard.Controls.Add(lb_G);
            this.groupBox_keyboard.Controls.Add(lb_H);
            this.groupBox_keyboard.Controls.Add(lb_I);
            this.groupBox_keyboard.Controls.Add(lb_J);

            this.groupBox_keyboard.Controls.Add(lb_K);
            this.groupBox_keyboard.Controls.Add(lb_L);
            this.groupBox_keyboard.Controls.Add(lb_M);
            this.groupBox_keyboard.Controls.Add(lb_N);
            this.groupBox_keyboard.Controls.Add(lb_O);
            this.groupBox_keyboard.Controls.Add(lb_P);
            this.groupBox_keyboard.Controls.Add(lb_Q);
            this.groupBox_keyboard.Controls.Add(lb_R);
            this.groupBox_keyboard.Controls.Add(lb_S);
            this.groupBox_keyboard.Controls.Add(lb_T);

            this.groupBox_keyboard.Controls.Add(lb_U);
            this.groupBox_keyboard.Controls.Add(lb_V);
            this.groupBox_keyboard.Controls.Add(lb_W);
            this.groupBox_keyboard.Controls.Add(lb_X);
            this.groupBox_keyboard.Controls.Add(lb_Y);
            this.groupBox_keyboard.Controls.Add(lb_Z);

            this.groupBox_keyboard.Controls.Add(lb_1);
            this.groupBox_keyboard.Controls.Add(lb_2);
            this.groupBox_keyboard.Controls.Add(lb_3);
            this.groupBox_keyboard.Controls.Add(lb_4);
            this.groupBox_keyboard.Controls.Add(lb_5);
            this.groupBox_keyboard.Controls.Add(lb_6);
            this.groupBox_keyboard.Controls.Add(lb_7);
            this.groupBox_keyboard.Controls.Add(lb_8);
            this.groupBox_keyboard.Controls.Add(lb_9);
            this.groupBox_keyboard.Controls.Add(lb_0);

            this.groupBox_keyboard.Controls.Add(lb_period);
            this.groupBox_keyboard.Controls.Add(lb_backspace);
            this.groupBox_keyboard.Controls.Add(lb_esc);
            this.groupBox_keyboard.Controls.Add(lb_caps_lock);
            this.groupBox_keyboard.Controls.Add(lb_shift);
            this.groupBox_keyboard.Controls.Add(lb_space);
            this.groupBox_keyboard.Controls.Add(lb_clear);
            this.groupBox_keyboard.Controls.Add(lb_OK);
            this.groupBox_keyboard.Controls.Add(tb_input);

            lb_result.Text = "";
            lb_result.Font = new Font("標楷體", 22);
            lb_result.ForeColor = Color.Black;
            lb_result.AutoSize = true;
            this.groupBox_keyboard.Controls.Add(lb_result);

            setup_keyboard_keys(this.groupBox_keyboard.Controls);
        }

        public void setup_keyboard_keys(Control.ControlCollection cc)
        {
            int x_st = 70;
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
            lb_period.Location = new Point(x_st + dx * 7, y_st + dy * 2);
            lb_backspace.Location = new Point(x_st + dx * 8, y_st + dy * 2);
            lb_esc.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 0);
            lb_caps_lock.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 1);
            lb_shift.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 2);
            lb_space.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            lb_clear.Location = new Point(x_st + dx * 7, y_st + dy * 3);
            tb_input.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 3);
            tb_input.Multiline = true;
            tb_input.Font = new Font("標楷體", 22);
            tb_input.Size = new Size(280, 36);

            x_st = 520;
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
                        setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
                        ((Label)c).MouseDown += new MouseEventHandler(lb_MouseDown);
                        ((Label)c).MouseUp += new MouseEventHandler(lb_MouseUp);
                    }

                    //richTextBox1.Text += ((Label)c).Name + "\t" + ((Label)c).Name.Length.ToString() + "\n";

                    if (((Label)c).Name == "lb_period")
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w, h);  //設定大小
                        ((Label)c).Text = ".";
                    }

                    if (((Label)c).Name == "lb_backspace")
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 - 10, h);  //設定大小
                        ((Label)c).Text = "Back space";
                    }

                    if (((Label)c).Name == "lb_esc")
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w, h);  //設定大小
                        ((Label)c).Text = "Esc";
                    }

                    if (((Label)c).Name == "lb_caps_lock")
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 - 10, h);  //設定大小
                        ((Label)c).Text = "Caps Lock";
                    }

                    if (((Label)c).Name == "lb_shift")
                    {
                        ((Label)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 - 10, h);  //設定大小
                        ((Label)c).Text = "Shift";
                    }

                    //lb_OK
                    if (((Label)c).Name == "lb_OK")
                    {
                        ((Label)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Label)c).Text = "OK";
                    }

                    //lb_space
                    if (((Label)c).Name == "lb_space")
                    {
                        ((Label)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Label)c).Text = "";
                    }

                    //lb_clear
                    if (((Label)c).Name == "lb_clear")
                    {
                        ((Label)c).Font = new Font("標楷體", 14, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Label)c).Text = "Clear";
                    }
                }
                //richTextBox1.Text += "\n";
            }
        }

        void setup_key_text(bool caps_on)
        {
            foreach (Control c in this.groupBox_keyboard.Controls)  //撈出所有控件
            {
                //richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Label")   //判斷是否為 Label 控件
                {
                    if (((Label)c).Name.Length == 4)
                    {
                        //richTextBox1.Text += ((Label)c).Name + "\n";
                        if (caps_on == true)
                        {
                            ((Label)c).Text = ((Label)c).Name[3].ToString();
                        }
                        else
                        {
                            ((Label)c).Text = ((Label)c).Name[3].ToString().ToLower();
                        }
                    }
                }
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

        void lb_esc_MouseDown(object sender, MouseEventArgs e)
        {
            lb_esc.BackColor = key_press_color;

            //TBD
        }

        void lb_esc_MouseUp(object sender, MouseEventArgs e)
        {
            lb_esc.BackColor = key_color;
        }

        void lb_caps_lock_MouseDown(object sender, MouseEventArgs e)
        {
            if (flag_caps_lock == false)
            {
                flag_caps_lock = true;
                lb_caps_lock.BackColor = key_press_color;
            }
            else
            {
                flag_caps_lock = false;
                lb_caps_lock.BackColor = key_color;
            }
            flag_caps_lock_once = false;
            lb_shift.BackColor = key_color;
            setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
        }

        void lb_caps_lock_MouseUp(object sender, MouseEventArgs e)
        {
            //nothing
        }

        void lb_shift_MouseDown(object sender, MouseEventArgs e)
        {
            lb_shift.BackColor = key_press_color;
            flag_caps_lock_once = true;
            setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
        }

        void lb_shift_MouseUp(object sender, MouseEventArgs e)
        {
            //nothing
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
                lb_result.Text = "你輸入了 : " + tb_input.Text.ToString().Replace("_", " ");
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

            if (lb.Name == "lb_period")
            {
                tb_input.Text += ".";
            }
            else if (lb.Name == "lb_space")
            {
                tb_input.Text += "_";
            }
            else
            {
                if (flag_caps_lock ^ flag_caps_lock_once)
                {
                    tb_input.Text += lb.Name.Substring(3, 1);
                }
                else
                {
                    tb_input.Text += lb.Name.Substring(3, 1).ToLower();
                }
            }

            tb_input.SelectionStart = tb_input.Text.Length;

            lb.BackColor = key_press_color;
            if (flag_caps_lock_once == true)
            {
                flag_caps_lock_once = false;
                lb_shift.BackColor = key_color;
                setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
            }
        }

        void lb_MouseUp(object sender, MouseEventArgs e)
        {
            Label lb = (Label)sender;
            lb.BackColor = key_color;
        }
    }
}
