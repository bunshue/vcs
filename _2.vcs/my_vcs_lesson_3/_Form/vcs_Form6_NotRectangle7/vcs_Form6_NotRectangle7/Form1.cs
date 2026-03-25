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

namespace vcs_Form6_NotRectangle7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }
    }
}
