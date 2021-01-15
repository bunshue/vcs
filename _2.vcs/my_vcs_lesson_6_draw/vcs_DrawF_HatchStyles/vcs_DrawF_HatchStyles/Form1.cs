using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;
using System.Drawing.Drawing2D;

namespace vcs_DrawF_HatchStyles
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the names and samples of the HatchStyle values.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Get a list of the HatchStyles.
            foreach (HatchStyle hatch_style in Enum.GetValues(typeof(HatchStyle)))
            {
                DisplayHatchStyle(hatch_style);
            }
        }

        // Return a list of an enumerated type's values.
        private List<T> GetEnumValues<T>()
        {
            // Get the type's Type information.
            Type t_type = typeof(T);

            // Enumerate the Enum's fields.
            FieldInfo[] field_infos = t_type.GetFields();

            // Loop over the fields.
            List<T> results = new List<T>();
            foreach (FieldInfo field_info in field_infos)
            {
                // See if this is a literal value (set at compile time).
                if (field_info.IsLiteral)
                {
                    // Add it.
                    T value = (T)field_info.GetValue(null);
                    results.Add(value);
                }
            }
            return results;
        }

        // Display a sample of the HatchStyle.
        private void DisplayHatchStyle(HatchStyle hatch_style)
        {
            const int WID = 150;
            const int HGT = 50;
            const int BM_WID = WID;
            const int BM_HGT = 32;

            // Make a Panel to hold the sample and its label.
            Panel pan = new Panel();
            pan.Size = new Size(WID, HGT);
            flowLayoutPanel1.Controls.Add(pan);

            // Display the cursor's name in a Label.
            Label lbl = new Label();
            lbl.AutoSize = false;
            lbl.Text = hatch_style.ToString();
            lbl.Size = new Size(WID, 13);
            lbl.TextAlign = ContentAlignment.MiddleCenter;
            lbl.Location = new Point(0, 0);
            pan.Controls.Add(lbl);

            // Draw the cursor onto a Bitmap.
            Bitmap bm = new Bitmap(BM_WID, BM_HGT);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                using (HatchBrush br = new HatchBrush(hatch_style,Color.Black,Color.White))
                {
                    gr.FillRectangle(br, 0, 0, BM_WID, BM_HGT);
                }
            }

            // Display the Bitmap in a PictureBox.
            PictureBox pic = new PictureBox();
            pic.Location = new Point((WID - BM_WID) / 2, 15);
            pic.BorderStyle = BorderStyle.Fixed3D;
            pic.ClientSize = new Size(BM_WID, BM_HGT);
            pic.Image = bm;
            pan.Controls.Add(pic);
        }
    }
}
