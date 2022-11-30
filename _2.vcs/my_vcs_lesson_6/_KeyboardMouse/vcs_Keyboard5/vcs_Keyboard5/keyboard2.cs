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
    public partial class keyboard2 : UserControl
    {
        Color groupBox_keyboard_backcolor = Color.LightSalmon;
        Color key_color = Color.Lime;
        Color key_press_color = Color.Green;

        GroupBox groupBox_keyboard = new GroupBox();

        Button bt_A = new Button();
        Button bt_B = new Button();
        Button bt_C = new Button();
        Button bt_D = new Button();
        Button bt_E = new Button();
        Button bt_F = new Button();
        Button bt_G = new Button();
        Button bt_H = new Button();
        Button bt_I = new Button();
        Button bt_J = new Button();
        Button bt_K = new Button();
        Button bt_L = new Button();
        Button bt_M = new Button();
        Button bt_N = new Button();
        Button bt_O = new Button();
        Button bt_P = new Button();
        Button bt_Q = new Button();
        Button bt_R = new Button();
        Button bt_S = new Button();
        Button bt_T = new Button();
        Button bt_U = new Button();
        Button bt_V = new Button();
        Button bt_W = new Button();
        Button bt_X = new Button();
        Button bt_Y = new Button();
        Button bt_Z = new Button();
        Button bt_1 = new Button();
        Button bt_2 = new Button();
        Button bt_3 = new Button();
        Button bt_4 = new Button();
        Button bt_5 = new Button();
        Button bt_6 = new Button();
        Button bt_7 = new Button();
        Button bt_8 = new Button();
        Button bt_9 = new Button();
        Button bt_0 = new Button();
        Button bt_period = new Button();
        Button bt_backspace = new Button();
        Button bt_esc = new Button();
        Button bt_caps_lock = new Button();
        Button bt_shift = new Button();
        Button bt_space = new Button();
        Button bt_clear = new Button();
        Button bt_OK = new Button();
        TextBox tb_input = new TextBox();
        Label lb_result = new Label();

        bool flag_caps_lock = false;
        bool flag_caps_lock_once = false;

        public keyboard2()
        {
            InitializeComponent();
        }

        private void keyboard2_Load(object sender, EventArgs e)
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

            bt_A.Name = "bt_A";
            bt_B.Name = "bt_B";
            bt_C.Name = "bt_C";
            bt_D.Name = "bt_D";
            bt_E.Name = "bt_E";
            bt_F.Name = "bt_F";
            bt_G.Name = "bt_G";
            bt_H.Name = "bt_H";
            bt_I.Name = "bt_I";
            bt_J.Name = "bt_J";

            bt_K.Name = "bt_K";
            bt_L.Name = "bt_L";
            bt_M.Name = "bt_M";
            bt_N.Name = "bt_N";
            bt_O.Name = "bt_O";
            bt_P.Name = "bt_P";
            bt_Q.Name = "bt_Q";
            bt_R.Name = "bt_R";
            bt_S.Name = "bt_S";
            bt_T.Name = "bt_T";

            bt_U.Name = "bt_U";
            bt_V.Name = "bt_V";
            bt_W.Name = "bt_W";
            bt_X.Name = "bt_X";
            bt_Y.Name = "bt_Y";
            bt_Z.Name = "bt_Z";

            bt_1.Name = "bt_1";
            bt_2.Name = "bt_2";
            bt_3.Name = "bt_3";
            bt_4.Name = "bt_4";
            bt_5.Name = "bt_5";
            bt_6.Name = "bt_6";
            bt_7.Name = "bt_7";
            bt_8.Name = "bt_8";
            bt_9.Name = "bt_9";
            bt_0.Name = "bt_0";

            bt_period.Name = "bt_period";
            bt_backspace.Name = "bt_backspace";
            bt_esc.Name = "bt_esc";
            bt_caps_lock.Name = "bt_caps_lock";
            bt_shift.Name = "bt_shift";
            bt_space.Name = "bt_space";
            bt_clear.Name = "bt_clear";
            bt_OK.Name = "bt_OK";

            bt_period.MouseDown += new MouseEventHandler(bt_MouseDown);
            bt_period.MouseUp += new MouseEventHandler(bt_MouseUp);

            bt_backspace.MouseDown += new MouseEventHandler(bt_backspace_MouseDown);
            bt_backspace.MouseUp += new MouseEventHandler(bt_backspace_MouseUp);

            bt_esc.MouseDown += new MouseEventHandler(bt_esc_MouseDown);
            bt_esc.MouseUp += new MouseEventHandler(bt_esc_MouseUp);

            bt_caps_lock.MouseDown += new MouseEventHandler(bt_caps_lock_MouseDown);
            bt_caps_lock.MouseUp += new MouseEventHandler(bt_caps_lock_MouseUp);

            bt_shift.MouseDown += new MouseEventHandler(bt_shift_MouseDown);
            bt_shift.MouseUp += new MouseEventHandler(bt_shift_MouseUp);

            bt_space.MouseDown += new MouseEventHandler(bt_MouseDown);
            bt_space.MouseUp += new MouseEventHandler(bt_MouseUp);

            bt_clear.MouseDown += new MouseEventHandler(bt_clear_MouseDown);
            bt_clear.MouseUp += new MouseEventHandler(bt_clear_MouseUp);

            bt_OK.MouseDown += new MouseEventHandler(bt_OK_MouseDown);
            bt_OK.MouseUp += new MouseEventHandler(bt_OK_MouseUp);

            this.groupBox_keyboard.Controls.Add(bt_A);
            this.groupBox_keyboard.Controls.Add(bt_B);
            this.groupBox_keyboard.Controls.Add(bt_C);
            this.groupBox_keyboard.Controls.Add(bt_D);
            this.groupBox_keyboard.Controls.Add(bt_E);
            this.groupBox_keyboard.Controls.Add(bt_F);
            this.groupBox_keyboard.Controls.Add(bt_G);
            this.groupBox_keyboard.Controls.Add(bt_H);
            this.groupBox_keyboard.Controls.Add(bt_I);
            this.groupBox_keyboard.Controls.Add(bt_J);

            this.groupBox_keyboard.Controls.Add(bt_K);
            this.groupBox_keyboard.Controls.Add(bt_L);
            this.groupBox_keyboard.Controls.Add(bt_M);
            this.groupBox_keyboard.Controls.Add(bt_N);
            this.groupBox_keyboard.Controls.Add(bt_O);
            this.groupBox_keyboard.Controls.Add(bt_P);
            this.groupBox_keyboard.Controls.Add(bt_Q);
            this.groupBox_keyboard.Controls.Add(bt_R);
            this.groupBox_keyboard.Controls.Add(bt_S);
            this.groupBox_keyboard.Controls.Add(bt_T);

            this.groupBox_keyboard.Controls.Add(bt_U);
            this.groupBox_keyboard.Controls.Add(bt_V);
            this.groupBox_keyboard.Controls.Add(bt_W);
            this.groupBox_keyboard.Controls.Add(bt_X);
            this.groupBox_keyboard.Controls.Add(bt_Y);
            this.groupBox_keyboard.Controls.Add(bt_Z);

            this.groupBox_keyboard.Controls.Add(bt_1);
            this.groupBox_keyboard.Controls.Add(bt_2);
            this.groupBox_keyboard.Controls.Add(bt_3);
            this.groupBox_keyboard.Controls.Add(bt_4);
            this.groupBox_keyboard.Controls.Add(bt_5);
            this.groupBox_keyboard.Controls.Add(bt_6);
            this.groupBox_keyboard.Controls.Add(bt_7);
            this.groupBox_keyboard.Controls.Add(bt_8);
            this.groupBox_keyboard.Controls.Add(bt_9);
            this.groupBox_keyboard.Controls.Add(bt_0);

            this.groupBox_keyboard.Controls.Add(bt_period);
            this.groupBox_keyboard.Controls.Add(bt_backspace);
            this.groupBox_keyboard.Controls.Add(bt_esc);
            this.groupBox_keyboard.Controls.Add(bt_caps_lock);
            this.groupBox_keyboard.Controls.Add(bt_shift);
            this.groupBox_keyboard.Controls.Add(bt_space);
            this.groupBox_keyboard.Controls.Add(bt_clear);
            this.groupBox_keyboard.Controls.Add(bt_OK);
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
            int w = 40;
            int h = 40;
            int dx = w + 2;
            int dy = h + 2;
            bt_Q.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_W.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_E.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_R.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_T.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_Y.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_U.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_I.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_O.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            bt_P.Location = new Point(x_st + dx * 9, y_st + dy * 0);

            lb_result.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            x_st += 20;
            bt_A.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_S.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_D.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_F.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_G.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            bt_H.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            bt_J.Location = new Point(x_st + dx * 6, y_st + dy * 1);
            bt_K.Location = new Point(x_st + dx * 7, y_st + dy * 1);
            bt_L.Location = new Point(x_st + dx * 8, y_st + dy * 1);

            x_st += 20;
            bt_Z.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_X.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_C.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_V.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            bt_B.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            bt_N.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            bt_M.Location = new Point(x_st + dx * 6, y_st + dy * 2);
            bt_period.Location = new Point(x_st + dx * 7, y_st + dy * 2);
            bt_backspace.Location = new Point(x_st + dx * 8, y_st + dy * 2);
            bt_esc.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 0);
            bt_caps_lock.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 1);
            bt_shift.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 2);
            bt_space.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            bt_clear.Location = new Point(x_st + dx * 7, y_st + dy * 3);
            tb_input.Location = new Point(x_st + dx * 0 - 95, y_st + dy * 3);
            tb_input.Multiline = true;
            tb_input.Font = new Font("標楷體", 22);
            tb_input.Size = new Size(280, 36);

            x_st = 520;
            y_st = 30;
            bt_1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_7.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_8.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_9.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_0.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_OK.Location = new Point(x_st + dx * 1, y_st + dy * 3);

            foreach (Control c in cc)  //撈出所有控件
            {
                //richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    //richTextBox1.Text += "\t" + ((Button)c).Name + "\t" + ((Button)c).Text + "\t" + ((Button)c).Size.Width.ToString() + " X " + ((Button)c).Size.Height.ToString();

                    //改 backcolor.size.text font alignment...
                    ((Button)c).Size = new Size(w, h);  //設定大小
                    ((Button)c).BackColor = key_color;
                    ((Button)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                    ((Button)c).TextAlign = ContentAlignment.MiddleCenter;

                    if (((Button)c).Name.Length == 4)
                    {
                        //richTextBox1.Text += ((Button)c).Name + "\n";
                        setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
                        ((Button)c).MouseDown += new MouseEventHandler(bt_MouseDown);
                        ((Button)c).MouseUp += new MouseEventHandler(bt_MouseUp);
                    }

                    //richTextBox1.Text += ((Button)c).Name + "\t" + ((Button)c).Name.Length.ToString() + "\n";

                    if (((Button)c).Name == "bt_period")
                    {
                        ((Button)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w, h);  //設定大小
                        ((Button)c).Text = ".";
                    }

                    if (((Button)c).Name == "bt_backspace")
                    {
                        ((Button)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w * 2 - 10, h);  //設定大小
                        ((Button)c).Text = "Back space";
                    }

                    if (((Button)c).Name == "bt_esc")
                    {
                        ((Button)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w, h);  //設定大小
                        ((Button)c).Text = "Esc";
                    }

                    if (((Button)c).Name == "bt_caps_lock")
                    {
                        ((Button)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w * 2 - 10, h);  //設定大小
                        ((Button)c).Text = "Caps Lock";
                    }

                    if (((Button)c).Name == "bt_shift")
                    {
                        ((Button)c).Font = new Font("標楷體", 8, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w * 2 - 10, h);  //設定大小
                        ((Button)c).Text = "Shift";
                    }

                    //bt_OK
                    if (((Button)c).Name == "bt_OK")
                    {
                        ((Button)c).Font = new Font("標楷體", 18, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Button)c).Text = "OK";
                    }

                    //bt_space
                    if (((Button)c).Name == "bt_space")
                    {
                        ((Button)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Button)c).Text = "";
                    }

                    //bt_clear
                    if (((Button)c).Name == "bt_clear")
                    {
                        ((Button)c).Font = new Font("標楷體", 14, FontStyle.Bold);  //建立字體對象
                        ((Button)c).Size = new Size(w * 2 + 5, h);  //設定大小
                        ((Button)c).Text = "Clear";
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

                if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    if (((Button)c).Name.Length == 4)
                    {
                        //richTextBox1.Text += ((Button)c).Name + "\n";
                        if (caps_on == true)
                        {
                            ((Button)c).Text = ((Button)c).Name[3].ToString();
                        }
                        else
                        {
                            ((Button)c).Text = ((Button)c).Name[3].ToString().ToLower();
                        }
                    }
                }
            }
        }

        void bt_backspace_MouseDown(object sender, MouseEventArgs e)
        {
            bt_backspace.BackColor = key_press_color;

            if (tb_input.Text.Length <= 0)
                return;
            tb_input.Text = tb_input.Text.Substring(0, tb_input.Text.Length - 1);
            tb_input.SelectionStart = tb_input.Text.Length;
        }

        void bt_backspace_MouseUp(object sender, MouseEventArgs e)
        {
            bt_backspace.BackColor = key_color;
        }

        void bt_esc_MouseDown(object sender, MouseEventArgs e)
        {
            bt_esc.BackColor = key_press_color;

            //TBD
        }

        void bt_esc_MouseUp(object sender, MouseEventArgs e)
        {
            bt_esc.BackColor = key_color;
        }

        void bt_caps_lock_MouseDown(object sender, MouseEventArgs e)
        {
            if (flag_caps_lock == false)
            {
                flag_caps_lock = true;
                bt_caps_lock.BackColor = key_press_color;
            }
            else
            {
                flag_caps_lock = false;
                bt_caps_lock.BackColor = key_color;
            }
            flag_caps_lock_once = false;
            bt_shift.BackColor = key_color;
            setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
        }

        void bt_caps_lock_MouseUp(object sender, MouseEventArgs e)
        {
            //nothing
        }

        void bt_shift_MouseDown(object sender, MouseEventArgs e)
        {
            bt_shift.BackColor = key_press_color;
            flag_caps_lock_once = true;
            setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
        }

        void bt_shift_MouseUp(object sender, MouseEventArgs e)
        {
            //nothing
        }

        void bt_clear_MouseDown(object sender, MouseEventArgs e)
        {
            bt_clear.BackColor = key_press_color;
            tb_input.Clear();
        }

        void bt_clear_MouseUp(object sender, MouseEventArgs e)
        {
            bt_clear.BackColor = key_color;
        }

        void bt_OK_MouseDown(object sender, MouseEventArgs e)
        {
            bt_OK.BackColor = key_press_color;

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

        void bt_OK_MouseUp(object sender, MouseEventArgs e)
        {
            bt_OK.BackColor = key_color;
        }

        void bt_MouseDown(object sender, MouseEventArgs e)
        {
            Button bt = (Button)sender;

            if (bt.Name == "bt_period")
            {
                tb_input.Text += ".";
            }
            else if (bt.Name == "bt_space")
            {
                tb_input.Text += "_";
            }
            else
            {
                if (flag_caps_lock ^ flag_caps_lock_once)
                {
                    tb_input.Text += bt.Name.Substring(3, 1);
                }
                else
                {
                    tb_input.Text += bt.Name.Substring(3, 1).ToLower();
                }
            }

            tb_input.SelectionStart = tb_input.Text.Length;

            bt.BackColor = key_press_color;
            if (flag_caps_lock_once == true)
            {
                flag_caps_lock_once = false;
                bt_shift.BackColor = key_color;
                setup_key_text(flag_caps_lock ^ flag_caps_lock_once);
            }
        }

        void bt_MouseUp(object sender, MouseEventArgs e)
        {
            Button bt = (Button)sender;
            bt.BackColor = key_color;
        }
    }
}
