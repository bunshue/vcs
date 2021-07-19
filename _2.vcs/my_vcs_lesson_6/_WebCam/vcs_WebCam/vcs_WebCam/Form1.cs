using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebCam
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            Init_WebcamSetup();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 210;
            dy = 42;

            groupBox1.Size = new Size(1000, 250);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(10, 270);

            richTextBox1.Size = new Size(300, 480);
            richTextBox1.Location = new Point(10 + 640 + 10, 270);



            y_st = 20;
            int w = 260;
            int h = 220;
            groupBox2.Size = new Size(w, h);
            groupBox3.Size = new Size(w, h);
            groupBox4.Size = new Size(w, h);

            dx = w + 20;
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            //groupBox2
            x_st = 10;
            y_st = 20;
            dx = 80;
            dy = 30;
            checkBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            checkBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            checkBox3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            radioButton1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            radioButton2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            checkBox1.Enabled = false;
            checkBox2.Enabled = false;
            radioButton1.Enabled = false;
            radioButton2.Enabled = false;

            //groupBox3
            x_st = 10;
            y_st = 20;
            dx = 210;
            dy = 30;
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            comboBox1.Size = new Size(230, 30);
            comboBox2.Size = new Size(230, 30);
            comboBox3.Size = new Size(230, 30);
            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            comboBox2.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            comboBox3.Location = new Point(x_st + dx * 0, y_st + dy * 5);


            //groupBox4
            x_st = 10;
            y_st = 20;
            dx = 80;
            dy = 50;
            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_pause.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_stop.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_refresh.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_snapshot.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_info.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_fullscreen.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            cb_show_time.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            cb_auto_save.Location = new Point(x_st + dx * 1, y_st + dy * 3);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Init_WebcamSetup()
        {

        }


    }
}
