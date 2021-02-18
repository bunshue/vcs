using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Drag_Picture_To_PictureBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            foreach (Control items in Controls)
            {
                if (items.GetType().Name == "PictureBox")
                {
                    items.AllowDrop = true;//允許拖曳
                    items.DragDrop += Items_DragDrop;
                    items.DragEnter += Items_DragEnter;
                }
            }
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;//PictureBox 顯示模式
        }

        private void Items_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.All;//拖曳效果
        }

        private void Items_DragDrop(object sender, DragEventArgs e)
        {
            string filename = (e.Data.GetData((DataFormats.FileDrop)) as string[])[0];//取得檔案位置
            if (pictureBox1.Image != null)//判斷PictureBox是否有圖片
            {
                pictureBox1.Image = null;//清除PictureBox裡的圖片
                GC.Collect();//GC收集
            }
            pictureBox1.Image = Image.FromFile(filename);//顯示
        }

    }
}
