using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            removeButton.Enabled = false;
            clearButton.Enabled = false;
            resultButton.Enabled = false;
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            orderList.Items.Add(menuCombo.Text);
            //若「移除」、「清空訂單」和「開始統計」有任一個Enabled為false則全改設為true
            if (!removeButton.Enabled || !clearButton.Enabled || !resultButton.Enabled) {
                removeButton.Enabled = true;
                clearButton.Enabled = true;
                resultButton.Enabled = true;
            }
        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            if (orderList.SelectedIndex != -1)
                orderList.Items.RemoveAt(orderList.SelectedIndex);
            
            //若選項清單為空的則「移除」、「清空訂單」和「開始統計」全改設為false
            if (orderList.Items.Count == 0)
            {
                removeButton.Enabled = false;
                clearButton.Enabled = false;
                resultButton.Enabled = false;
            }
        }

        private void clearButton_Click(object sender, EventArgs e)
        {
            orderList.Items.Clear();
            removeButton.Enabled = false;
            clearButton.Enabled = false;
            resultButton.Enabled = false;
        }

        private void resultButton_Click(object sender, EventArgs e)
        {
            int food1 = 0, food2 = 0, food3 = 0, food4 = 0, food5 = 0;

            for(int i=0; i < orderList.Items.Count; ++i){
                if (orderList.Items[i].ToString() == "排骨飯")
                    ++food1;
                else if (orderList.Items[i].ToString() == "雞腿飯")
                    ++food2;
                else if (orderList.Items[i].ToString() == "焢肉飯")
                    ++food3;
                else if (orderList.Items[i].ToString() == "鱈魚飯")
                    ++food4;
                else if (orderList.Items[i].ToString() == "豬腳飯")
                    ++food5;
            }

            resultLabel.Text = "排骨飯共 " + food1 + " 個" + Environment.NewLine;
            resultLabel.Text += "雞腿飯共 " + food2 + " 個" + Environment.NewLine;
            resultLabel.Text += "焢肉飯共 " + food3 + " 個" + Environment.NewLine;
            resultLabel.Text += "鱈魚飯共 " + food4 + " 個" + Environment.NewLine;
            resultLabel.Text += "豬腳飯共 " + food5 + " 個";
        }


    }
}
