using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Text;

namespace vcs_DrawE_FamilyTree
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The root node.
        private TreeNode<PictureNode> root = new TreeNode<PictureNode>(new PictureNode("第零代A0", Properties.Resources.G0));

        // Make a tree.
        private void Form1_Load(object sender, EventArgs e)
        {
            TreeNode<PictureNode> g1a = new TreeNode<PictureNode>(new PictureNode("第一代A", Properties.Resources.G1A));
            TreeNode<PictureNode> g1b = new TreeNode<PictureNode>(new PictureNode("第一代B", Properties.Resources.G1B));
            TreeNode<PictureNode> g1c = new TreeNode<PictureNode>(new PictureNode("第一代C", Properties.Resources.G1C));
            TreeNode<PictureNode> g1d = new TreeNode<PictureNode>(new PictureNode("第一代D", Properties.Resources.G1D));

            TreeNode<PictureNode> g2a1 = new TreeNode<PictureNode>(new PictureNode("第二代A1", Properties.Resources.G2A1));
            TreeNode<PictureNode> g2d1 = new TreeNode<PictureNode>(new PictureNode("第二代D1", Properties.Resources.G2D1));
            TreeNode<PictureNode> g2d2 = new TreeNode<PictureNode>(new PictureNode("第二代D2", Properties.Resources.G2D2));
            TreeNode<PictureNode> g2d3 = new TreeNode<PictureNode>(new PictureNode("第二代D3", Properties.Resources.G2D3));
            TreeNode<PictureNode> g2d4 = new TreeNode<PictureNode>(new PictureNode("第二代D4", Properties.Resources.G2D4));

            TreeNode<PictureNode> g3d2a = new TreeNode<PictureNode>(new PictureNode("第三代D2A", Properties.Resources.G3D2A));
            TreeNode<PictureNode> g3d2b = new TreeNode<PictureNode>(new PictureNode("第三代D2B", Properties.Resources.G3D2B));
            TreeNode<PictureNode> g3d2c = new TreeNode<PictureNode>(new PictureNode("第三代D2C", Properties.Resources.G3D2C));

            root.AddChild(g1a);     //1A add 2A
            g1a.AddChild(g2a1);  //2A add 3A1

            root.AddChild(g1b);        //1A add 2B

            root.AddChild(g1c);      //1A add 2C

            root.AddChild(g1d);      //1A add 2D
            g1d.AddChild(g2d1);    //2D add 3D1
            g1d.AddChild(g2d2);    //2D add 3D2
            g1d.AddChild(g2d3);    //2D add 3D3
            g1d.AddChild(g2d4);    //2D add 3D4

            g2d2.AddChild(g3d2a);    //2D add 3D1
            g2d2.AddChild(g3d2b);    //2D add 3D2
            g2d2.AddChild(g3d2c);    //2D add 3D3

            // Arrange the tree.
            ArrangeTree();
        }

        // Draw the tree.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            e.Graphics.DrawString("清宣宗世系表", new Font("標楷體", 50), new SolidBrush(Color.Green), new PointF(20, 30));
            root.DrawTree(e.Graphics);
        }

        // Center the tree on the form.
        private void pictureBox1_Resize(object sender, EventArgs e)
        {
            ArrangeTree();
        }
        private void ArrangeTree()
        {
            using (Graphics gr = pictureBox1.CreateGraphics())
            {
                // Arrange the tree once to see how big it is.
                float xmin = 0, ymin = 0;
                root.Arrange(gr, ref xmin, ref ymin);

                // Arrange the tree again to center it horizontally.
                xmin = (this.ClientSize.Width - xmin) / 2;
                ymin = 10;
                root.Arrange(gr, ref xmin, ref ymin);
            }

            pictureBox1.Refresh();
        }

        // The currently selected node.
        private TreeNode<PictureNode> SelectedNode;

        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            FindNodeUnderMouse(e.Location);
        }

        // Set SelectedNode to the node under the mouse.
        private void FindNodeUnderMouse(PointF pt)
        {
            // Deselect the previously selected node.
            if (SelectedNode != null)
            {
                SelectedNode.Data.Selected = false;
                lblNodeText.Text = "";
            }

            // Find the node at this position (if any).
            using (Graphics gr = pictureBox1.CreateGraphics())
            {
                SelectedNode = root.NodeAtPoint(gr, pt);
            }

            // Select the node.
            if (SelectedNode != null)
            {
                SelectedNode.Data.Selected = true;
                lblNodeText.Text = SelectedNode.Data.Description;
            }

            // Redraw.
            pictureBox1.Refresh();
        }
    }
}
