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


        private void addButton_Click(object sender, EventArgs e)
        {
            if (fileDialog.ShowDialog() == DialogResult.OK)
                pictureList.Items.Add(fileDialog.FileName);
        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            if (pictureList.SelectedIndex != -1)
                pictureList.Items.RemoveAt(pictureList.SelectedIndex);
        }

        private void setButton_Click(object sender, EventArgs e)
        {
            timer1.Interval = int.Parse(intervalText.Text);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (pictureList.Items.Count != 0) {
                pictureList.SelectedIndex = (pictureList.SelectedIndex + 1) % pictureList.Items.Count;
                pictureBox.ImageLocation = pictureList.SelectedItem.ToString();
            }
        }

        private void pictureBox_Click(object sender, EventArgs e)
        {
            if (pictureList.Visible) {
                pictureList.Visible = false;
                addButton.Visible = false;
                removeButton.Visible = false;
                setButton.Visible = false;
                intervalText.Visible = false;
            }
            else {
                pictureList.Visible = true;
                addButton.Visible = true;
                removeButton.Visible = true;
                setButton.Visible = true;
                intervalText.Visible = true;
            }
        }

    }
}
