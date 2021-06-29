using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_Draw_Path
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Dictionary<int, PathSNode> Nodes = null;
        private Dictionary<string, PathSLink> Links = null;
        private PathSNode Root = null;
        private bool GotPathTree = false;
        private PathSNode Destination = null;

        private const float RADIUS = 10;
        private const float RADIUS_SQUARED = RADIUS * RADIUS;

        // Exit.
        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Load a network file.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (dlgNet.ShowDialog() == DialogResult.OK)
            {
                LoadNetwork(dlgNet.FileName);

                // Display the network.
                this.Refresh();
            }
        }

        // Load the network data from a file with format:
        //   # Nodes, # Links
        //   For each node: Id, X, Y
        //   For each link: Node1, Node2, Cost
        private void LoadNetwork(string fname)
        {
            // Open the file.
            this.Text = "PathS[]";
            try
            {
                float xmax = 0, ymax = 0;

                // Open the file.
                using (TextReader reader = new StreamReader(fname))
                {
                    // Read the number of nodes and links.
                    int num_nodes = int.Parse(reader.ReadLine());
                    int num_links = int.Parse(reader.ReadLine());

                    // Read the node identifiers and coordinates.
                    Nodes = new Dictionary<int, PathSNode>();
                    for (int i = 0; i < num_nodes; i++)
                    {
                        PathSNode new_node = new PathSNode();
                        new_node.Id = int.Parse(reader.ReadLine());
                        new_node.Location.X = int.Parse(reader.ReadLine());
                        new_node.Location.Y = int.Parse(reader.ReadLine());

                        if (xmax < new_node.Location.X) xmax = new_node.Location.X;
                        if (ymax < new_node.Location.Y) ymax = new_node.Location.Y;
                        Nodes.Add(new_node.Id, new_node);
                    }

                    // Read the links.
                    Links = new Dictionary<string,PathSLink>();
                    for (int i = 0; i < num_links; i++)
                    {
                        PathSLink new_link = new PathSLink();

                        // Get the node IDs.
                        int node1_num = int.Parse(reader.ReadLine());
                        int node2_num = int.Parse(reader.ReadLine());

                        // Find the nodes.
                        new_link.Node1 = Nodes[node1_num];
                        new_link.Node2 = Nodes[node2_num];

                        Links.Add(node1_num.ToString() + "-" + node2_num.ToString(), new_link);

                        // Get the cost.
                        new_link.Cost = int.Parse(reader.ReadLine());

                        // Add the link to the nodes' Links collections.
                        new_link.Node1.Links.Add(node2_num, new_link);
                        new_link.Node2.Links.Add(node1_num, new_link);
                    }
                }

                // Size the form to fit.
                Rectangle new_rect = Rectangle.Union(
                    this.ClientRectangle,
                    new Rectangle(0, 0, 
                        (int)(xmax + RADIUS + 10), (int)(ymax + RADIUS + 10)));
                this.ClientSize = new Size(new_rect.Width, new_rect.Height);

                // Display the file's name.
                FileInfo file_info = new FileInfo(fname);
                this.Text = "PathS[" + file_info.Name + "]";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error reading network file.\n" + ex.Message,
                    "File Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation);
            }
        }

        // Draw the current network.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            DrawNetwork(e.Graphics);
        }

        // Display the network.
        private void DrawNetwork(Graphics gr)
        {
            gr.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            gr.Clear(this.BackColor);
            if (Nodes == null) return;

            // Draw the links.
            using (Pen tree_pen = new Pen(Color.Blue, 3),
                path_pen = new Pen(Color.Red, 3))
            {
                Pen link_pen;
                using (Brush bg_brush = new SolidBrush(this.BackColor))
                {
                    foreach (PathSLink link in Links.Values)
                    {
                        // Pick the link's color based on its current use.
                        if (link.LinkUsage == PathSLink.LinkUseageType.InTree)
                        {
                            link_pen = tree_pen;
                        }
                        else if (link.LinkUsage == PathSLink.LinkUseageType.InPath)
                        {
                            link_pen = path_pen;
                        }
                        else
                        {
                            link_pen = Pens.Black;
                        }

                        float x1 = link.Node1.Location.X;
                        float y1 = link.Node1.Location.Y;
                        float x2 = link.Node2.Location.X;
                        float y2 = link.Node2.Location.Y;
                        float dx = x2 - x1;
                        float dy = y2 - y1;
                        float dist = (float)(Math.Sqrt(dx * dx + dy * dy));
                        if (dist > 0)
                        {
                            dx = dx * RADIUS / dist;
                            dy = dy * RADIUS / dist;

                            // Draw the link.
                            x1 = x1 + dx;
                            y1 = y1 + dy;
                            x2 = x2 - dx;
                            y2 = y2 - dy;
                            gr.DrawLine(link_pen, x1, y1, x2, y2);

                            // Draw the link cost.
                            x1 = (x1 + x2) / 2;
                            y1 = (y1 + y2) / 2;
                            gr.FillEllipse(bg_brush,
                                x1 - RADIUS, y1 - RADIUS,
                                2 * RADIUS, 2 * RADIUS);
                            string txt = link.Cost.ToString();
                            SizeF txt_size = gr.MeasureString(txt, this.Font);
                            gr.DrawString(txt, this.Font, Brushes.Black,
                                x1 - txt_size.Width / 2,
                                y1 - txt_size.Height / 2);
                        }
                    } // foreach (PathSLink link in m_Links)
                } // using bg_brush
            } // using tree_pen, path_pen

            // Draw the nodes.
            Brush text_brush, node_brush;
            Pen node_pen;
            foreach (PathSNode node in Nodes.Values)
            {
                // Draw the node and its links.
                if ((node == Root) || (node == Destination))
                {
                    // Highlight the node.
                    text_brush = Brushes.White;
                    node_brush = Brushes.Black;
                    node_pen = Pens.White;
                }
                else
                {
                    // Do not highlight the node.
                    text_brush = Brushes.Black;
                    node_brush = Brushes.White;
                    node_pen = Pens.Black;
                }

                // Draw the node.
                gr.FillEllipse(node_brush,
                    node.Location.X - RADIUS, node.Location.Y - RADIUS,
                    2 * RADIUS, 2 * RADIUS);
                gr.DrawEllipse(node_pen,
                    node.Location.X - RADIUS, node.Location.Y - RADIUS,
                    2 * RADIUS, 2 * RADIUS);
                string txt = node.Id.ToString();
                SizeF txt_size = gr.MeasureString(txt, this.Font);
                gr.DrawString(txt, this.Font, text_brush,
                    node.Location.X - txt_size.Width / 2,
                    node.Location.Y - txt_size.Height / 2);
            }
        }

        // Find the shortest path tree rooted at the clicked node.
        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            if (Nodes == null) return;

            // Find the node at this point.
            PathSNode node_at = NodeAt(e.X, e.Y);
            if (node_at == null) return;

            if (e.Button == MouseButtons.Left)
            {
                // Find the shortest path tree rooted at this node.
                FindPathTree(node_at);
            }
            else
            {
                // Set this node as the destination.
                Destination = node_at;
                FindShortestPath();
            }
        }

        // Find the node at this point.
        private PathSNode NodeAt(int X, int Y)
        {
            foreach (PathSNode node in Nodes.Values)
            {
                float dx = node.Location.X - X;
                float dy = node.Location.Y - Y;
                if (dx * dx + dy * dy <= RADIUS_SQUARED) return node;
            }

            return null;
        }

        // Find a shortest path tree rooted at this node
        // using a label setting algorithm.
        private void FindPathTree(PathSNode root)
        {
            if (root == null) return;
            Root = root;

            List<PathSNode> candidates = new List<PathSNode>();

            // Reset all nodes' Marked and NodeStatus values,
            // and all links' Used and LinkUsage flags.
            ResetPathTree();

            // Start with the root in the shortest path tree.
            root.Dist = 0;
            root.InLink = null;
            root.NodeStatus = PathSNode.NodeStatusType.NowInList;
            candidates.Add(root);

            // Process the candidates.
            while (candidates.Count > 0)
            {
                // Find the candidate closest to the root.
                int best_dist = int.MaxValue;
                int best_i = -1;
                for (int i = 0; i < candidates.Count; i++)
                {
                    PathSNode candidate_node = candidates[i];
                    int new_dist = candidate_node.Dist;
                    if (new_dist < best_dist)
                    {
                        best_i = i;
                        best_dist = new_dist;
                    }
                }

                // Add this node to the shortest path tree.
                PathSNode node = candidates[best_i];
                candidates.RemoveAt(best_i);
                node.NodeStatus = PathSNode.NodeStatusType.WasInList;

                // Examine the node's neighbors.
                foreach (PathSLink link in node.Links.Values)
                {
                    PathSNode to_node;
                    if (node == link.Node1)
                    {
                        to_node = link.Node2;
                    }
                    else
                    {
                        to_node = link.Node1;
                    }
                    if (to_node.NodeStatus == PathSNode.NodeStatusType.NotInList)
                    {
                        // The node has not been in the candidate list. Add it.
                        candidates.Add(to_node);
                        to_node.NodeStatus = PathSNode.NodeStatusType.NowInList;
                        to_node.Dist = best_dist + link.Cost;
                        to_node.InLink = link;
                    }
                    else if (to_node.NodeStatus == PathSNode.NodeStatusType.NowInList)
                    {
                        // The node is in the candidate list.
                        // Update its Dist and inlink values if necessary.
                        int new_dist = best_dist + link.Cost;
                        if (new_dist < to_node.Dist)
                        {
                            to_node.Dist = new_dist;
                            to_node.InLink = link;
                        }
                    }
                } // foreach (PathSLink link in node.Links)
            } // while (candidates.Count > 0)

            GotPathTree = true;

            // Mark the inlinks so they are easy to draw.
            foreach (PathSNode node in Nodes.Values)
            {
                if (node.InLink != null) 
                {
                    node.InLink.LinkUsage = PathSLink.LinkUseageType.InTree;
                }
            }

            // Start with no destination.
            Destination = null;

            // Redraw the network.
            this.Refresh();
        }

        // Remove all links from the shortest path tree.
        private void ResetPathTree()
        {
            // Don't bother if there's no shortest path tree.
            if (!GotPathTree) return;

            foreach (PathSNode node in Nodes.Values)
            {
                node.NodeStatus = PathSNode.NodeStatusType.NotInList;
            }

            foreach (PathSLink link in Links.Values)
            {
                link.LinkUsage = PathSLink.LinkUseageType.Unused;
            }

            GotPathTree = false;
        }

        // Find the shortest path from the destination to the root.
        private void FindShortestPath()
        {
            // Reset any links that were in the previous shortest path.
            foreach (PathSLink link in Links.Values)
            {
                if (link.LinkUsage == PathSLink.LinkUseageType.InPath)
                {
                    link.LinkUsage = PathSLink.LinkUseageType.InTree;
                }
            }

            // Trace the path from the destination to the root.
            PathSNode node = Destination;
            while (node != Root)
            {
                node.InLink.LinkUsage = PathSLink.LinkUseageType.InPath;
                if (node.InLink.Node1 == node)
                {
                    node = node.InLink.Node2;
                }
                else
                {
                    node = node.InLink.Node1;
                }
            }

            // Redraw the network.
            this.Refresh();
        }
    }
}
