using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListBox2
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

            //------------------------------------------------------------  # 60個

            //字串一維陣列
            string[] ZodiacSign = { "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座" };
            listBox_left.Items.AddRange(ZodiacSign);

            SetButtonsEditable();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            int dd = 34;
            int w = 240;
            int h = 310;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 - 60, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            dy = h + 44;
            int ddx = 100;
            listBox0.Size = new Size(w, h);
            listBox1.Size = new Size(w, h);
            label0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 0);
            listBox0.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            listBox1.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 0 + dd);

            listBox_left.Size = new Size(w, h);
            listBox_right.Size = new Size(w, h);
            label_left.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            label_right.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 1);
            listBox_left.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd);
            listBox_right.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 1 + dd);

            ddx = 35;
            int ddy = 50;
            bt_right.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 1 + ddy * 0 + 80);
            bt_right_all.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 1 + ddy * 1 + 80);
            bt_left_all.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 1 + ddy * 2 + 80);
            bt_left.Location = new Point(x_st + dx * 2 + ddx, y_st + dy * 1 + ddy * 3 + 80);

            this.Size = new Size(1120, 750);
            this.Text = "vcs_ListBox2";

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
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        // Enable and disable buttons.
        private void SetButtonsEditable()
        {
            bt_right.Enabled = (listBox_left.SelectedItems.Count > 0);
            bt_right_all.Enabled = (listBox_left.Items.Count > 0);
            bt_left.Enabled = (listBox_right.SelectedItems.Count > 0);
            bt_left_all.Enabled = (listBox_right.Items.Count > 0);
        }

        // Move selected items to listBox_right.
        private void bt_right_Click(object sender, EventArgs e)
        {
            MoveSelectedItems(listBox_left, listBox_right);
        }

        // Move all items to listBox_right.
        private void bt_right_all_Click(object sender, EventArgs e)
        {
            MoveAllItems(listBox_left, listBox_right);
        }

        // Move all items to listBox_left.
        private void bt_left_all_Click(object sender, EventArgs e)
        {
            MoveAllItems(listBox_right, listBox_left);
        }

        // Move selected items to listBox_left.
        private void bt_left_Click(object sender, EventArgs e)
        {
            MoveSelectedItems(listBox_right, listBox_left);
        }

        // Move selected items from one ListBox to another.
        private void MoveSelectedItems(ListBox lstFrom, ListBox lstTo)
        {
            while (lstFrom.SelectedItems.Count > 0)
            {
                string item = (string)lstFrom.SelectedItems[0];
                lstTo.Items.Add(item);
                lstFrom.Items.Remove(item);
            }
            SetButtonsEditable();
        }

        // Move all items from one ListBox to another.
        private void MoveAllItems(ListBox lstFrom, ListBox lstTo)
        {
            lstTo.Items.AddRange(lstFrom.Items);
            lstFrom.Items.Clear();
            SetButtonsEditable();
        }

        // Enable and disable buttons.
        private void listBox_left_right_SelectedIndexChanged(object sender, EventArgs e)
        {
            SetButtonsEditable();
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/

