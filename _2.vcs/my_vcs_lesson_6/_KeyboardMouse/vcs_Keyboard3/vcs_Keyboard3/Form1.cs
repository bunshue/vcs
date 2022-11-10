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

            lb_0.Click += new EventHandler(lb_Click);
            lb_1.Click += new EventHandler(lb_Click);
            lb_2.Click += new EventHandler(lb_Click);
            lb_3.Click += new EventHandler(lb_Click);
            lb_4.Click += new EventHandler(lb_Click);
            lb_5.Click += new EventHandler(lb_Click);
            lb_6.Click += new EventHandler(lb_Click);
            lb_7.Click += new EventHandler(lb_Click);
            lb_8.Click += new EventHandler(lb_Click);
            lb_9.Click += new EventHandler(lb_Click);
            lb_Q.Click += new EventHandler(lb_Click);
            lb_W.Click += new EventHandler(lb_Click);
            lb_R.Click += new EventHandler(lb_Click);
            lb_E.Click += new EventHandler(lb_Click);
            lb_T.Click += new EventHandler(lb_Click);
            lb_Y.Click += new EventHandler(lb_Click);
            lb_U.Click += new EventHandler(lb_Click);
            lb_I.Click += new EventHandler(lb_Click);
            lb_O.Click += new EventHandler(lb_Click);
            lb_P.Click += new EventHandler(lb_Click);
            lb_A.Click += new EventHandler(lb_Click);
            lb_S.Click += new EventHandler(lb_Click);
            lb_D.Click += new EventHandler(lb_Click);
            lb_F.Click += new EventHandler(lb_Click);
            lb_G.Click += new EventHandler(lb_Click);
            lb_H.Click += new EventHandler(lb_Click);
            lb_J.Click += new EventHandler(lb_Click);
            lb_K.Click += new EventHandler(lb_Click);
            lb_L.Click += new EventHandler(lb_Click);
            lb_Z.Click += new EventHandler(lb_Click);
            lb_X.Click += new EventHandler(lb_Click);
            lb_C.Click += new EventHandler(lb_Click);
            lb_V.Click += new EventHandler(lb_Click);
            lb_B.Click += new EventHandler(lb_Click);
            lb_N.Click += new EventHandler(lb_Click);
            lb_M.Click += new EventHandler(lb_Click);
            lb_backspace.Click += new EventHandler(lb_backspace_Click);
            lb_OK.Click += new EventHandler(lb_OK_Click);
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

        void lb_OK_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你輸入了 : " + tb_input.Text.ToString() + "\n";
            tb_input.Text = "";
        }



    }
}
