using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class7
{
    public partial class Form1 : Form
    {
        ShapeCollection ShapeManager = new ShapeCollection();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showCounter();
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void showCounter()
        {
            lb_count.Text = ShapeManager.getCount().ToString();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增三角形, 建立新表單, 若按OK, 回傳新表單的資料\n";
            TriangleForm tForm = new TriangleForm();

            if (tForm.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增三角形 OK\t加入tForm資料之內部物件\n";
                ShapeManager.add(tForm.tObj);
                richTextBox1.Text += "內容\t" + tForm.tObj.show() + "\n";
                showCounter();
            }
            else
            {
                richTextBox1.Text += "新增三角形 Cancel\n";
            }
            tForm.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增矩形, 建立新表單, 若按OK, 回傳新表單的資料\n";
            RectangleForm rForm = new RectangleForm();

            if (rForm.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增矩形 OK\t加入rForm資料之內部物件\n";
                ShapeManager.add(rForm.rObj);
                richTextBox1.Text += "內容\t" + rForm.rObj.show() + "\n";
                showCounter();
            }
            else
            {
                richTextBox1.Text += "新增矩形 Cancel\n";
            }
            rForm.Dispose();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "目前共有 " + ShapeManager.getCount() + " 個圖形\n";
            richTextBox1.Text += "內容:\n";
            richTextBox1.Text += ShapeManager.listing() + "\n";
            richTextBox1.Text += "圖形次序: " + ShapeManager.rankShape() + "\n";
            richTextBox1.Text += "最大圖形: " + ShapeManager.maxShape() + "\n";
        }
    }
}
