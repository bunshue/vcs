using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory
using System.Collections;   //for ArrayList

namespace vcs_DynamicAddRemoveControls6_ShowPicture
{
    public partial class Form1 : Form
    {
        private const int COLUMNS = 3;
        private const int ROWS = 2;
        private const int PICTURE_WIDTH = 1920 / COLUMNS * 9 / 10;
        private const int PICTURE_HEIGHT = 1080 / ROWS * 9 / 10;

        string path = @"C:\______test_files\__pic\_MU";

        ArrayList picture_files = new ArrayList();

        int total_picture_count = 0;
        int current_picture_count = 0;

        public Form1()
        {
            InitializeComponent();
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showPictures();
        }

        void showPictures()
        {
            picture_files = GetFiles(path);

            total_picture_count = picture_files.Count;

            if (total_picture_count == 0)
            {
                MessageBox.Show("無圖可秀");
                Application.Exit();
            }

            this.Text = total_picture_count.ToString();

            /*
            richTextBox1.Text += "總共" + total_picture_count.ToString() + "個檔案\n";
            richTextBox1.Text += "分別是:\n";
            int i;
            for (i = 0; i < total_picture_count; i++)
            {
                richTextBox1.Text += picture_files[i].ToString() + "\n";
            }
            */

            //動態產生pictureBox
            DynamicGeneratePictureBox(picture_files);

            richTextBox1.Visible = false;
        }

        //讀取資料夾下所有檔案, 只看一層
        private ArrayList GetFiles(string path)
        {
            ArrayList files = new ArrayList();

            if (Directory.Exists(path))     //確認資料夾是否存在
            {
                //files.AddRange(Directory.GetFiles(path)); 加入所有檔案, 但無法區分是否為圖片檔, 捨棄

                string[] f = System.IO.Directory.GetFiles(path, "*.*", System.IO.SearchOption.AllDirectories);
                foreach (string filename in f)
                {
                    richTextBox1.Text += filename + "\n";

                    FileInfo fi = new FileInfo(filename);

                    if (fi.Exists == true)      //確認檔案是否存在
                    {
                        /*
                        richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                        richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                        richTextBox1.Text += "副檔名：" + fi.Extension + Environment.NewLine;
                        richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                        richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                        richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                        richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;
                        */
                        if ((fi.Extension == ".bmp") || (fi.Extension == ".jpg") || (fi.Extension == ".png"))
                        {
                            files.Add(fi.Directory + "//" + fi.Name);
                        }
                    }
                    else
                        richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                }
            }
            return files;
        }

        private void DynamicGeneratePictureBox(ArrayList files)
        {
            // 設定位置及圖片方塊寬高值
            int LEFT_ANCHOR = 0;
            int TOP_ANCHOR = 0;

            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            richTextBox1.Text += "總共" + files.Count.ToString() + "個檔案\n";

            int i;
            int j;
            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    // 實例化圖片方塊
                    PictureBox pbx = new PictureBox();

                    //pbx.Size = new Size(PICTURE_WIDTH, PICTURE_HEIGHT);

                    // 設定圖片方塊參數
                    pbx.Left = LEFT_ANCHOR + PICTURE_WIDTH * i;
                    pbx.Top = TOP_ANCHOR + PICTURE_HEIGHT * j;
                    pbx.Width = PICTURE_WIDTH;
                    pbx.Height = PICTURE_HEIGHT;
                    //pbx.BackColor = Color.Pink;
                    //pbx.Text = i.ToString() + ", " + j.ToString();
                    pbx.Tag = "dynamic" + (COLUMNS * j + i).ToString("D2");
                    pbx.Name = "pbx" + (COLUMNS * j + i).ToString("D2");
                    pbx.SizeMode = PictureBoxSizeMode.Zoom;
                    if (current_picture_count < files.Count)
                    {
                        pbx.Image = Image.FromFile(files[current_picture_count].ToString());
                        current_picture_count++;
                        this.Text = current_picture_count.ToString() + " / " + total_picture_count.ToString();
                    }
                    // 將圖片方塊加入表單
                    this.Controls.Add(pbx);
                }
            }
            this.ClientSize = new Size(PICTURE_WIDTH * COLUMNS + LEFT_ANCHOR * 2, PICTURE_HEIGHT * ROWS + TOP_ANCHOR * 2);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)
            {
                if (current_picture_count >= total_picture_count)
                {
                    current_picture_count = 0;
                }

                removeAllPictureBox();
                //動態產生pictureBox
                DynamicGeneratePictureBox(picture_files);
            }
            else if (e.KeyCode == Keys.PageDown)
            {
                if (current_picture_count < total_picture_count)
                {
                    removeAllPictureBox();
                    //動態產生pictureBox
                    DynamicGeneratePictureBox(picture_files);
                }
                else
                {
                    //this.Text = "XXX";
                }
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                if (current_picture_count >= COLUMNS * ROWS * 2)
                {
                    if ((current_picture_count % (COLUMNS * ROWS)) > 0)
                    {
                        current_picture_count -= COLUMNS * ROWS;
                        current_picture_count -= current_picture_count % (COLUMNS * ROWS);
                    }
                    else
                        current_picture_count -= COLUMNS * ROWS * 2;

                    removeAllPictureBox();
                    //動態產生pictureBox
                    DynamicGeneratePictureBox(picture_files);
                }
                else
                {
                    //this.Text = "xxx";
                }
            }
            else if (e.KeyCode == Keys.Home)
            {
                if (current_picture_count > 0)
                {
                    current_picture_count = 0;

                    removeAllPictureBox();
                    //動態產生pictureBox
                    DynamicGeneratePictureBox(picture_files);
                }
                else
                {
                    //this.Text = "NNNN";
                }

            }
            else if (e.KeyCode == Keys.End)
            {
                int last_picture_count = total_picture_count / (COLUMNS * ROWS) * (COLUMNS * ROWS);

                if (current_picture_count != last_picture_count)
                {
                    current_picture_count = last_picture_count;

                    removeAllPictureBox();
                    //動態產生pictureBox
                    DynamicGeneratePictureBox(picture_files);
                }
            }
            else if ((e.KeyCode == Keys.X) || (e.KeyCode == Keys.Escape))
            {
                Application.Exit();
            }
        }

        //移除圖片方塊部分,  一趟並不會將所有表單上的圖片方塊回傳, 所以多做幾趟
        void removeAllPictureBox()
        {
            bool remove_item = false;
            int i;
            for (i = 0; i < 10; i++)
            {
                remove_item = false;
                foreach (Control item in this.Controls.OfType<PictureBox>())
                {
                    PictureBox pbx = (PictureBox)item;
                    this.Controls.Remove(item);
                    remove_item = true;
                }
                //richTextBox1.Text += "i = " + i.ToString() + "\tremove = " + remove_item.ToString() + "\n";
                if (remove_item == false)
                    break;
            }
        }
    }
}
