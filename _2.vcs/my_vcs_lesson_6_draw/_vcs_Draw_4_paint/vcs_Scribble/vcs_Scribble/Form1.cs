using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Xml.Serialization;
using System.IO;

namespace vcs_Scribble
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The polylines we draw.
        private List<Polyline> Polylines = new List<Polyline>();

        // The new polyline we are drawing.
        private Polyline NewPolyline = null;

        // The currently selected drawing parameters.
        private Color DrawingColor = Color.Black;
        private int DrawingThickness = 1;
        private DashStyle DrawingDashStyle = DashStyle.Solid;

        // The auto-save file name.
        //string filename = Application.StartupPath + "\\xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";
        private string AutoSaveFile = Application.StartupPath + "\\scribble.tmp";

        // The dimensions of the drawing area in world coordinates.
        private const int WorldWidth = 200 * 3;
        private const int WorldHeight = 200 * 3;

        // The current scale.
        private float PictureScale = 1.0f;

        // Initially select full scale.
        // Look for an auto-save file.
        // Load some test data.
        private void Form1_Load(object sender, EventArgs e)
        {
            cboScale.SelectedIndex = 2;

            // See if the file exists.
            if (File.Exists(AutoSaveFile))
            {
                /*
                // Ask the user if we should load this file.
                if (MessageBox.Show("An auto-save file exists. Do you want to load it?",
                    "Restore?", MessageBoxButtons.YesNo, MessageBoxIcon.Question)
                    == DialogResult.Yes)
                {
                    // Load the file.
                    LoadFromFile(AutoSaveFile);
                }
                */
                Form_Load fl = new Form_Load();
                DialogResult result = fl.ShowDialog();
                if (result == DialogResult.Yes)
                {
                    richTextBox1.Text += "你按了 Yes\n";
                    // Load the file.
                    LoadFromFile(AutoSaveFile);
                }
                else if (result == DialogResult.No)
                {
                    richTextBox1.Text += "你按了 No\n";
                    File.Delete(AutoSaveFile);
                }
                else
                {
                    richTextBox1.Text += "你按了 XXXXX\n";
                }
            }

            MakeTestData();
            pictureBox1.Refresh();
        }

        // Make some test data.
        private void MakeTestData()
        {
            Color[] colors = 
            {
                Color.Black, Color.Red, Color.Green, Color.Blue,
                Color.Lime, Color.Cyan, Color.Orange, Color.Yellow,
            };
            DashStyle[] styles =
            {
                DashStyle.Solid, DashStyle.Solid, DashStyle.Solid, 
                DashStyle.Dash, DashStyle.DashDot,
            };
            Random rand = new Random();
            for (int i = 0; i < 10; i++)
            {
                int cx = rand.Next(30, WorldWidth - 30);
                int cy = rand.Next(30, WorldHeight - 30);
                int radius = rand.Next(10, 100);
                Polyline polyline = DrawCircle(cx, cy, radius, 100);
                polyline.Color = colors[rand.Next(0, colors.Length)];
                polyline.DashStyle = styles[rand.Next(0, styles.Length)];
                polyline.Thickness = rand.Next(1, 6);
                Polylines.Add(polyline);
            }
        }

        // Draw a circle.
        private Polyline DrawCircle(int cx, int cy, int radius, int num_lines)
        {
            Polyline polyline = new Polyline();

            float theta = 0;
            float dtheta = (float)(2 * Math.PI / num_lines);
            for (int i = 0; i <= num_lines; i++)
            {
                int x = (int)(cx + radius * Math.Cos(theta));
                int y = (int)(cy + radius * Math.Sin(theta));
                theta += dtheta;
                polyline.Points.Add(new Point(x, y));
            }
            return polyline;
        }

        // Remove the auto-save file.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Form_Close fc = new Form_Close();
            DialogResult result = fc.ShowDialog();
            if (result == DialogResult.Yes)
            {
                richTextBox1.Text += "你按了 Yes, 存檔\n";

                string filename = Application.StartupPath + "\\xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";
                SaveIntoFile(filename);

                File.Delete(AutoSaveFile);  //連同刪除暫存檔
            }
            else if (result == DialogResult.No)
            {
                richTextBox1.Text += "你按了 No\n";

                File.Delete(AutoSaveFile);  //連同刪除暫存檔
            }
            else if (result == DialogResult.Abort)
            {
                richTextBox1.Text += "你按了 Abort 暫存\n";
                AutoSave();
            }
            else if (result == DialogResult.Cancel)
            {
                richTextBox1.Text += "你按了 Cancel\n";
                e.Cancel = true;
            }
            else
            {
                richTextBox1.Text += "你按了 XXXXX\n";
            }
        }

        // Auto-save.
        private void AutoSave()
        {
            SaveIntoFile(AutoSaveFile);
        }

        // Select the appropriate color.
        private void ColorTool_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem tool = sender as ToolStripMenuItem;
            toolColor.Image = tool.Image;
            DrawingColor = tool.ForeColor;
        }

        // Select the line thickness.
        private void ThicknessTool_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem tool = sender as ToolStripMenuItem;
            toolThick.Image = tool.Image;
            DrawingThickness = int.Parse(tool.Text);
        }

        // Select the dash style.
        private void StyleTool_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem tool = sender as ToolStripMenuItem;
            toolStyle.Image = tool.Image;
            switch (tool.Text)
            {
                case "Solid":
                    DrawingDashStyle = DashStyle.Solid;
                    break;
                case "Dash":
                    DrawingDashStyle = DashStyle.Dash;
                    break;
                case "Dot":
                    DrawingDashStyle = DashStyle.Dot;
                    break;
                case "Custom":
                    DrawingDashStyle = DashStyle.Custom;
                    break;
            }
        }

        // Start drawing.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Create the new polyline.
            NewPolyline = new Polyline();
            Polylines.Add(NewPolyline);

            // Initialize it and add the first point.
            NewPolyline.Color = DrawingColor;
            NewPolyline.Thickness = DrawingThickness;
            NewPolyline.DashStyle = DrawingDashStyle;
            NewPolyline.Points.Add(e.Location);
        }

        // Continue drawing.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;
            NewPolyline.Points.Add(e.Location);
            pictureBox1.Refresh();
        }

        // Stop drawing.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;

            // See if the new polyline contains more than 1 point.
            if (NewPolyline.Points.Count < 2)
            {
                // Remove it.
                Polylines.RemoveAt(Polylines.Count - 1);
            }

            // Redraw.
            NewPolyline = null;
            pictureBox1.Refresh();

            // Save a new snapshot in the undo list.
            SaveSnapshot(true);
        }

        // Draw the picture.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            // Ready.
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(pictureBox1.BackColor);

            // Scale.
            e.Graphics.ScaleTransform(PictureScale, PictureScale);

            // Draw the polylines.
            foreach (Polyline polyline in Polylines)
            {
                polyline.Draw(e.Graphics);
            }
        }

        // Exit.
        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Start a new drawing.
        private void mnuFileNew_Click(object sender, EventArgs e)
        {
            Polylines = new List<Polyline>();
            pictureBox1.Refresh();

            // Save a new snapshot in the undo list.
            UndoList = new Stack<string>();
            RedoList = new Stack<string>();
            //SaveSnapshot(true); ????
        }

        // Save the drawing.
        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";
            SaveIntoFile(filename);
        }

        // Save the current picture into a file.
        private void SaveIntoFile(string filename)
        {
            XmlSerializer xml_serializer = new XmlSerializer(Polylines.GetType());
            using (StreamWriter stream_writer = new StreamWriter(filename))
            {
                xml_serializer.Serialize(stream_writer, Polylines);
                stream_writer.Close();
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
        }

        // Open a saved drawing.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = Application.StartupPath;
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                LoadFromFile(openFileDialog1.FileName);
            }
        }

        // Load a saved picture from a file.
        private void LoadFromFile(string filename)
        {
            try
            {
                XmlSerializer xml_serializer = new XmlSerializer(Polylines.GetType());
                using (FileStream file_stream = new FileStream(filename, FileMode.Open))
                {
                    List<Polyline> new_polylines =
                        (List<Polyline>)xml_serializer.Deserialize(file_stream);
                    Polylines = new_polylines;
                    pictureBox1.Refresh();

                    // Save a new snapshot in the undo list.
                    UndoList = new Stack<string>();
                    RedoList = new Stack<string>();
                    SaveSnapshot(false);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // The undo and redo history lists.
        private Stack<string> UndoList = new Stack<string>();
        private Stack<string> RedoList = new Stack<string>();

        // Save a snapshot in the undo list.
        private void SaveSnapshot(bool auto_save)
        {
            // Save the snapshot.
            UndoList.Push(GetSnapshot());

            // Empty the redo list.
            if (RedoList.Count > 0) RedoList = new Stack<string>();

            // Enable or disable the Undo and Redo menu items.
            EnableUndo();

            // Auto-save.
            if (auto_save)
            {
                AutoSave();
            }
        }

        // Enable or disable the Undo and Redo menu items.
        private void EnableUndo()
        {
            mnuEditUndo.Enabled = (UndoList.Count > 0);
            mnuEditRedo.Enabled = (RedoList.Count > 0);
        }

        // Return an XML serialization of the current drawing.
        private string GetSnapshot()
        {
            XmlSerializer xml_serializer = new XmlSerializer(Polylines.GetType());
            using (StringWriter string_writer = new StringWriter())
            {
                xml_serializer.Serialize(string_writer, Polylines);
                return string_writer.ToString();
            }
        }

        // Use an XML serialization to load a drawing.
        private void RestoreTopUndoItem()
        {
            if (UndoList.Count == 0)
            {
                // The undo list is empty. Display a blank drawing.
                Polylines = new List<Polyline>();
            }
            else
            {
                // Restore the first serialization from the undo list.
                XmlSerializer xml_serializer = new XmlSerializer(Polylines.GetType());
                using (StringReader string_reader = new StringReader(UndoList.Peek()))
                {
                    List<Polyline> new_polylines =
                        (List<Polyline>)xml_serializer.Deserialize(string_reader);
                    Polylines = new_polylines;
                }
            }
            pictureBox1.Refresh();

            // Auto-save.
            AutoSave();
        }

        // Undo.
        private void mnuEditUndo_Click(object sender, EventArgs e)
        {
            // Move the most recent change to the redo list.
            RedoList.Push(UndoList.Pop());

            // Restore the top item in the Undo list.
            RestoreTopUndoItem();

            // Enable or disable the Undo and Redo menu items.
            EnableUndo();
        }

        // Redo.
        private void mnuEditRedo_Click(object sender, EventArgs e)
        {
            // Move the most recently undone item back to the undo list.
            UndoList.Push(RedoList.Pop());

            // Restore the top item in the Undo list.
            RestoreTopUndoItem();

            // Enable or disable the Undo and Redo menu items.
            EnableUndo();
        }

        // Select the new scale.
        private void cboScale_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (cboScale.Text)
            {
                case "x 1/4":
                    SetScale(0.25f);
                    break;
                case "x 1/2":
                    SetScale(0.5f);
                    break;
                case "x 1":
                    SetScale(1.0f);
                    break;
                case "x 2":
                    SetScale(2.0f);
                    break;
                case "x 4":
                    SetScale(4.0f);
                    break;
                case "x 8":
                    SetScale(8.0f);
                    break;
            }
        }

        // Set the scale and redraw.
        private void SetScale(float picture_scale)
        {
            // Set the scale.
            PictureScale = picture_scale;

            // Resize the PictureBox.
            pictureBox1.ClientSize = new Size(
                (int)(WorldWidth * PictureScale),
                (int)(WorldHeight * PictureScale));

            // Redraw.
            pictureBox1.Refresh();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "tmp = " + Polylines.GetType().ToString() + "\n";
            int len = Polylines.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 段資料\n";

            if (len == 0)
                return;

            int i;
            int j;

            int len2;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 段資料\n";
                richTextBox1.Text += "Color:\t" + Polylines[i].Color.ToString() + "\n";
                richTextBox1.Text += "Thickness:\t" + Polylines[i].Thickness.ToString() + "\n";
                richTextBox1.Text += "DashStyle:\t" + Polylines[i].DashStyle.ToString() + "\n";

                len2 = Polylines[i].Points.Count;
                if (len2 > 10)
                    len2 = 10;
                for (j = 0; j < len2; j++)
                {
                    richTextBox1.Text += Polylines[i].Points[j].ToString() + "\n";
                }
            }
        }
    }
}
