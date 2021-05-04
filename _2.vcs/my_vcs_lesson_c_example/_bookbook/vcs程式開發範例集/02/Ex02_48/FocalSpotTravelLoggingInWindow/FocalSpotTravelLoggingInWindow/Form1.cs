using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace FocalSpotTravelLoggingInWindow
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 回車切換控件焦點//要想使這個方法起到作用先將窗體的keypreview屬性改為true
        protected override void OnKeyPress(KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)
            {
                this.SelectNextControl(this.ActiveControl, true, true, true, true);

            }
            base.OnKeyPress(e);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }










    }
}
