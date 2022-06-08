using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
    表單Form1的屬性/ 

    BackColor 改 White
    FormBorderStyle 改 None
    TransparencyKey = 改 White
    
    選一張圖，白色部分就會變成透明
    BackgroundImage
    BackgroundImageLayout 改 Center

    // Set the form's TransparencyKey and BackColor
    // to the image's transparent color.
*/


//隱藏到系統
//出現一下子 就消失
//看看會不會影響其他最上層顯示


namespace vcs_Ladybug2
{
    public partial class Form1 : Form
    {
        Bitmap ladybug;
        int W = 0;
        int H = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackColor = Color.White;
            this.FormBorderStyle = FormBorderStyle.None;
            this.TransparencyKey = Color.Black;
            this.BackgroundImageLayout = ImageLayout.None;

            ladybug = vcs_Ladybug2.Properties.Resources.ladybug;
            this.BackgroundImage = ladybug;
            W = ladybug.Width;
            H = ladybug.Height;
            this.ClientSize = new Size(W, H);



        }

        bool flag_show_on = true;
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_show_on == true)
            {
                flag_show_on = false;
                //最小最小化
                this.WindowState = FormWindowState.Minimized;
                this.ShowInTaskbar = false;
            }
            else
            {
                flag_show_on = true;
                //恢復顯示
                this.WindowState = FormWindowState.Normal;
                this.ShowInTaskbar = false;
            }

        }
    }
}

