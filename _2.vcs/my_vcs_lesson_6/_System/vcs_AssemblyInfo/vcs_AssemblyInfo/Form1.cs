using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_AssemblyInfo
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
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(750, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title : " + info.Title + "\n";
            richTextBox1.Text += "Description : " + info.Description + "\n";
            richTextBox1.Text += "Company : " + info.Company + "\n";
            richTextBox1.Text += "Product : " + info.Product + "\n";
            richTextBox1.Text += "Copyright : " + info.Copyright + "\n";
            richTextBox1.Text += "Trademark : " + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version : " + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version : " + info.FileVersion + "\n";
            richTextBox1.Text += "GUID : " + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language : " + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible : " + info.IsComVisible.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //組件資訊  Assembly Info

            //方案總管/專案屬性/應用程式/組件資訊 內 修改組件資訊

            //方案總管/加入/現有項目/選取AssemblyInfo.cs, 把 namespace 改成 vcs_System1
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title\t" + info.Title + "\n";
            richTextBox1.Text += "Description\t" + info.Description + "\n";
            richTextBox1.Text += "Company\t" + info.Company + "\n";
            richTextBox1.Text += "Product\t" + info.Product + "\n";
            richTextBox1.Text += "Copyright\t" + info.Copyright + "\n";
            richTextBox1.Text += "Trademark\t" + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version\t" + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version\t" + info.FileVersion + "\n";
            richTextBox1.Text += "GUID\t" + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language\t" + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible\t" + info.IsComVisible.ToString() + "\n";
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/
