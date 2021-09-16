using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_1_4_11
{
    public partial class Form1 : Form
    {
        internal System.Windows.Forms.ComboBox comboBox1;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建構comboBox1物件，並設定相關的屬性
            comboBox1 = new ComboBox();
            comboBox1.Location = new System.Drawing.Point(15, 15);
            comboBox1.Name = "ComboBox1";
            comboBox1.Size = new System.Drawing.Size(100, 21);
            comboBox1.TabIndex = 0;
            comboBox1.Text = "網卡";
            string[] installs = new string[] { "滑鼠", "鍵盤", "網卡", "螢幕", "音效卡" };
            comboBox1.Items.AddRange(installs);

            // 將建構後的comboBox1物件加入Form1物件的Controls屬性
            Controls.Add(comboBox1);

            // 設定comboBox1物件的DropDown事件的delegate
            comboBox1.DropDown +=
                new System.EventHandler(comboBox1_DropDown);

            // 設定comboBox1物件的SelectedIndexChanged事件的delegate
            comboBox1.SelectedIndexChanged +=
                new System.EventHandler(comboBox1_SelectedIndexChanged);
        }

        private void comboBox1_DropDown(object sender, System.EventArgs e)
        {
            System.Windows.Forms.ComboBox myCombo = 
                (System.Windows.Forms.ComboBox)sender;
            textBox1.Clear();
            textBox1.AppendText(myCombo.Text);
        }

        private void comboBox1_SelectedIndexChanged(object sender, System.EventArgs e)
        {
            System.Windows.Forms.ComboBox myCombo = 
                (System.Windows.Forms.ComboBox)sender;
            textBox2.Clear();
            textBox2.AppendText(myCombo.Text);
        }
    }
}
