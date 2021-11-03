using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FlowLayoutPanel
{
    public partial class Form1 : Form
    {
        FlowLayoutPanel newPanel = new FlowLayoutPanel();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            newPanel.AutoScroll = true;
            //newPanel.FlowDirection = FlowDirection.BottomUp;
            //newPanel.WrapContents = false;
            newPanel.Dock = DockStyle.Fill;
            newPanel.BackColor = Color.White;
            button1.Anchor = (AnchorStyles.Bottom | AnchorStyles.Right);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            newPanel.Controls.Clear();
            int i = 1;

            foreach (var item in typeof(Color).GetMembers())
            {
                if (item.MemberType == System.Reflection.MemberTypes.Property && System.Drawing.Color.FromName(item.Name).IsKnownColor == true)//只取屬性且為屬性中的已知Color，剔除byte屬性以及一些布爾屬性等（A B G R IsKnownColor Name等）
                {
                    Label myLable = new Label();
                    myLable.AutoSize = true;

                    myLable.BackColor = System.Drawing.Color.FromName(item.Name);
                    myLable.Text = System.Drawing.Color.FromName(item.Name).Name;
                    newPanel.Controls.Add(myLable);
                    //newPanel.GetFlowBreak(myLable);

                    i++;
                }
            }

            this.Controls.Add(newPanel);
            this.Text = "共有 " + i.ToString() + " 個顏色";
        }
    }
}

