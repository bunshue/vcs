using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class ShapeManagerForm : Form
    {
        public ShapeManagerForm()
        {
            InitializeComponent();
        }

        ShapeCollection ShapeManager = new ShapeCollection();
       
        private void ShapeManagerForm_Load(object sender, EventArgs e)
        {
           lblCounter.Text = "目前共有" + ShapeManager.getCount() + "個圖形";
           richTextBox1.Text += "目前共有" + ShapeManager.getCount() + "個圖形\n";
        }

        private void btnTriangle_Click(object sender, EventArgs e)
        {
            TriangleForm tForm = new TriangleForm();

            if (tForm.ShowDialog() == DialogResult.OK)
            {
                ShapeManager.add(tForm.tObj);
                txtOutput.Text = "新增三角形\r\n" + tForm.tObj.show() + "\r\n";
                lblCounter.Text = "目前共有" + ShapeManager.getCount() + "個圖形";

                richTextBox1.Text += "新增三角形\r\n" + tForm.tObj.show() + "\n";
                richTextBox1.Text += "目前共有" + ShapeManager.getCount() + "個圖形\n";
            }

            tForm.Dispose();
        }

        private void btnRectangle_Click(object sender, EventArgs e)
        {
            RectangleForm rForm = new RectangleForm();

            if (rForm.ShowDialog() == DialogResult.OK)
            {
                ShapeManager.add(rForm.rObj);
                txtOutput.Text = "新增矩形\r\n" + rForm.rObj.show() + "\r\n";
                lblCounter.Text = "目前共有" + ShapeManager.getCount() + "個圖形";

                richTextBox1.Text += "新增矩形\r\n" + rForm.rObj.show() + "\n";
                richTextBox1.Text += "目前共有" + ShapeManager.getCount() + "個圖形\n";
            }

            rForm.Dispose();
        }

        private void btnListing_Click(object sender, EventArgs e)
        {
            string str = "<<< 列出所有圖形 >>>\r\n";
            str += ShapeManager.listing();
            txtOutput.Text = str;
            richTextBox1.Text += str;
        }

        private void btnCompare_Click(object sender, EventArgs e)
        {
            string str = "<<< 圖形比較 >>>\r\n";
            str += ShapeManager.listing();
            str += "圖形次序: " + ShapeManager.rankShape();
            str += "\r\n最大圖形: " + ShapeManager.maxShape(); 
            txtOutput.Text = str;
            richTextBox1.Text += str;
        }
                
    }
}
