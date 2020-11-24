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

namespace howto_copy_paste_scribble
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
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
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
        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;
            NewPolyline.Points.Add(e.Location);
            picCanvas.Refresh();
        }

        // Stop drawing.
        private void picCanvas_MouseUp(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;

            // See if the new polyline contains more than 1 point.
            if (NewPolyline.Points.Count < 2)
            {
                // Remove it.
                Polylines.RemoveAt(Polylines.Count - 1);
            }

            NewPolyline = null;
            picCanvas.Refresh();
        }

        // Redraw.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(picCanvas.BackColor);

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
            picCanvas.Refresh();
        }

        // Save the drawing.
        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            if (sfdFile.ShowDialog() == DialogResult.OK)
            {
                XmlSerializer xml_serializer = new XmlSerializer(Polylines.GetType());
                using (StreamWriter stream_writer = new StreamWriter(sfdFile.FileName))
                {
                    xml_serializer.Serialize(stream_writer, Polylines);
                    stream_writer.Close();
                }
            }
        }

        // Open a saved drawing.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    XmlSerializer xml_serializer = new XmlSerializer(Polylines.GetType());
                    using (FileStream file_stream = new FileStream(ofdFile.FileName, FileMode.Open))
                    {
                        List<Polyline> new_polylines =
                            (List<Polyline>)xml_serializer.Deserialize(file_stream);
                        Polylines = new_polylines;
                        picCanvas.Refresh();
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        // Copy the scribble to the clipboard.
        private void mnuEditCopy_Click(object sender, EventArgs e)
        {
            Clipboard.SetDataObject(Polylines);
        }

        // Copy the scribble to the clipboard and delete it.
        private void mnuEditCut_Click(object sender, EventArgs e)
        {
            Clipboard.SetDataObject(Polylines);
            Polylines = new List<Polyline>();
            picCanvas.Refresh();
        }

        // Paste a scribble from the clipboard.
        private void mnuEditPaste_Click(object sender, EventArgs e)
        {
            IDataObject data_object = Clipboard.GetDataObject();
            if (data_object.GetDataPresent(Polylines.GetType()))
            {
                Polylines = (List<Polyline>)data_object.GetData(Polylines.GetType());
                if (Polylines == null) Polylines = new List<Polyline>();
                picCanvas.Refresh();
            }
        }
    }
}
