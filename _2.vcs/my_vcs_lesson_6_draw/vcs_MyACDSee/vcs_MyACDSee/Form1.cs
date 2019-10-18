using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections;   //for ArrayList

namespace vcs_MyACDSee
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            pictureBox1.BackColor = Color.Black;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //MessageBox.Show("do FormClosing......");
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            //MessageBox.Show("Form Closed............");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //全螢幕
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            string src = @"C:\______test_files\bear.jpg";
            pictureBox1.Dock = DockStyle.Fill; 
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            Image loadedImage = Image.FromFile(src);
            pictureBox1.Image = loadedImage;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        ArrayList picFileName = new ArrayList();
        int picFileCount = 0;
        int currentPicFileCount = 0;

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            int i;
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Up:
                    MessageBox.Show("上");
                    //richTextBox1.Text += "上";
                    break;
                case Keys.Down:
                    //richTextBox1.Text += "下";
                    MessageBox.Show("下");
                    break;
                case Keys.Left:
                    //richTextBox1.Text += "左";
                    MessageBox.Show("左");
                    break;
                case Keys.Right:
                    //richTextBox1.Text += "右";
                    MessageBox.Show("右");
                    break;
                case Keys.PageUp:
                    //richTextBox1.Text += "PageUp";
                    //MessageBox.Show("PageUp");
                    //MessageBox.Show("PageUp, current = " + currentPicFileCount.ToString() + ", all = " + picFileCount.ToString());
                    if (currentPicFileCount > 0)
                    {
                        currentPicFileCount--;
                        Image loadedImage = Image.FromFile((string)picFileName[currentPicFileCount]);
                        pictureBox1.Image = loadedImage;
                    }
                    break;
                case Keys.PageDown:
                    //richTextBox1.Text += "PageDown";
                    //MessageBox.Show("PageDown, current = " + currentPicFileCount.ToString() + ", all = " + picFileCount.ToString());
                    if (currentPicFileCount < (picFileCount - 1))
                    {
                        currentPicFileCount++;
                        Image loadedImage = Image.FromFile((string)picFileName[currentPicFileCount]);
                        pictureBox1.Image = loadedImage;
                    }
                    break;
                case Keys.Home:
                    //richTextBox1.Text += "PageDown";
                    //MessageBox.Show("PageDown, current = " + currentPicFileCount.ToString() + ", all = " + picFileCount.ToString());
                    if (currentPicFileCount <= (picFileCount - 1))
                    {
                        currentPicFileCount = 0;
                        Image loadedImage = Image.FromFile((string)picFileName[currentPicFileCount]);
                        pictureBox1.Image = loadedImage;
                    }
                    break;
                case Keys.End:
                    //richTextBox1.Text += "PageDown";
                    //MessageBox.Show("PageDown, current = " + currentPicFileCount.ToString() + ", all = " + picFileCount.ToString());
                    if (currentPicFileCount < (picFileCount - 1))
                    {
                        currentPicFileCount = picFileCount - 1;
                        Image loadedImage = Image.FromFile((string)picFileName[currentPicFileCount]);
                        pictureBox1.Image = loadedImage;
                    }
                    break;
                case Keys.Space:
                    if (currentPicFileCount < (picFileCount - 1))
                    {
                        currentPicFileCount++;
                        Image loadedImage = Image.FromFile((string)picFileName[currentPicFileCount]);
                        pictureBox1.Image = loadedImage;
                    }
                    else
                    {
                        currentPicFileCount = 0;
                        Image loadedImage = Image.FromFile((string)picFileName[currentPicFileCount]);
                        pictureBox1.Image = loadedImage;
                    }
                    break;
                case Keys.O:
                    // Set the file dialog to filter for graphics files.
                    openFileDialog1.Filter = "Images (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" + "All files (*.*)|*.*";

                    // Allow the user to select multiple images.
                    openFileDialog1.Multiselect = true;
                    openFileDialog1.Title = "My Image Browser";

                    if (openFileDialog1.ShowDialog() == DialogResult.OK)
                    {
                        i = 0;
                        //richTextBox1.Text += "取得 " + openFileDialog1.FileNames.Length.ToString() + " 個檔案\n";
                        //richTextBox1.Text += "檔案：\n";
                        foreach (string filename in openFileDialog1.FileNames)
                        {
                            i++;
                            picFileName.Add(filename);
                            //richTextBox1.Text += "檔案: " + filename + "\n";
                            //listBox1.Items.Add(filename);

                        }
                        picFileCount = picFileName.Count;
                        currentPicFileCount = 0;
                        //richTextBox1.Text += "\n";
                        Image loadedImage = Image.FromFile(openFileDialog1.FileName);
                        pictureBox1.Image = loadedImage;
                    }
                    break;
                case Keys.Escape:
                    Application.Exit();
                    break;
                case Keys.Enter:
                    if (this.FormBorderStyle == FormBorderStyle.FixedSingle)
                        this.FormBorderStyle = FormBorderStyle.None;
                    else
                        this.FormBorderStyle = FormBorderStyle.FixedSingle;
                    //this.FormBorderStyle = FormBorderStyle.None;
                    //this.WindowState = FormWindowState.Maximized;
                    //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
                    break;
                default:
                    MessageBox.Show("x");
                    //richTextBox1.Text += "KeyCode: " + e.KeyCode.ToString() + "\n";
                    break;
            }

        }

        private void button1_Click_1(object sender, EventArgs e)
        {

        }
    }
}
