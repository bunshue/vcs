using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyLabelTextBox
{
    public partial class LabelTextBox : UserControl
    {
        public LabelTextBox()
        {
            InitializeComponent();
        }

        [CategoryAttribute("控件")]
        public Label Label
        {
            get
            {
                return label1;
            }
            set
            {
                label1 = value;
            }
        }

        [CategoryAttribute("控件")]
        public TextBox TextBox
        {
            get
            {
                return textBox1;
            }
            set
            {
                textBox1 = value;
            }
        }

        /// <summary>
        /// 調整label與cTextBox的大小
        /// </summary>
        /// <param name="e"></param>
        protected override void OnSizeChanged(EventArgs e)
        {
            int frame = 6;
            this.textBox1.Height = 20;
            //label
            this.label1.Top = this.Height / 2 - this.label1.Height / 2;
            this.label1.Left = frame;

            //TextBox
            if (!this.textBox1.Multiline)
            {
                this.textBox1.Top = this.Height / 2 - this.textBox1.Height / 2;
            }
            else
            {
                this.textBox1.Top = 1;
                this.textBox1.Height = this.Height - 2;
            }
            this.textBox1.Left = label1.Left + label1.Width;
            this.textBox1.Width = this.Width - textBox1.Left - frame - 50;

            base.OnSizeChanged(e);
        }
    }
}

