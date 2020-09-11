using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

//Reference : https://home.gamer.com.tw/creationDetail.php?sn=4281924

namespace vcs_random_color_generator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Label[] lb_color = new Label[101];
        Random r = new Random(Guid.NewGuid().GetHashCode());
        private int _R = 0, _G = 0, _B = 0;
        private int lb_color_x = 0, lb_color_y = 0;
        private Thread _run_rand_color;  

        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 1; i < lb_color.Length; i++)
            {
                lb_color[i] = new Label();
                lb_color[i].Width = 50;
                lb_color[i].Height = 50;
                lb_color[i].Text = " ";
                lb_color[i].Location = new Point(lb_color_x, lb_color_y);
                _R = r.Next(255);
                _G = r.Next(255);
                _B = r.Next(255);
                lb_color[i].BackColor = Color.FromArgb(_R, _G, _B);
                this.Controls.Add(lb_color[i]);
                lb_color_x += 50;

                if (i % 10 == 0)
                {
                    lb_color_x = 0;
                    lb_color_y += 50;
                }
            }

            _run_rand_color = new Thread(run_rand_color);

            if (!_run_rand_color.IsAlive)
            {
                _run_rand_color.Start();
            }  

        }

        private void run_rand_color()
        {
            while (true)
            {
                for (int i = 1; i < lb_color.Length; i++)
                {
                    _R = r.Next(255);
                    _G = r.Next(255);
                    _B = r.Next(255);
                    lb_color[i].BackColor = Color.FromArgb(_R, _G, _B);
                }
                Thread.Sleep(100);
            }
        }  


    }
}
