using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_PictureCloseup2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int ScaleFactor = 2;
        private const int SmallRadius = 25;
        private const int BigRadius = SmallRadius * ScaleFactor;
        private const int BigDiameter = 2 * BigRadius;

        private int OriginalWid, OriginalHgt;
        private Bitmap BigMap, OriginalMap, ModifiedMap, MapPatch;
        private Rectangle PatchRect = new Rectangle(0, 0, BigDiameter, BigDiameter);

        private Rectangle SrcRect = new Rectangle(0, 0, BigDiameter, BigDiameter);
        private Rectangle DestRect = new Rectangle(0, 0, BigDiameter, BigDiameter);

        // Save the original small map image.
        private void Form1_Load(object sender, EventArgs e)
        {
            OriginalWid = picMap.Image.Width;
            OriginalHgt = picMap.Image.Height;

            // Save the big map.
            BigMap = (Bitmap)picHidden.Image;

            // Save the original map.
            OriginalMap = (Bitmap)picMap.Image;

            // Make a copy to display.
            ModifiedMap = (Bitmap)(OriginalMap.Clone());

            // Make a patch area.
            MapPatch = new Bitmap(BigDiameter, BigDiameter);
        }

            // Prepare the new map image.
            private void picMap_MouseMove(object sender, MouseEventArgs e)
            {
                // Adjust where the source and destination bitmaps are.
                SrcRect.X = e.X * ScaleFactor - BigRadius;
                SrcRect.Y = e.Y * ScaleFactor - BigRadius;
                DestRect.X = e.X - BigRadius;
                DestRect.Y = e.Y - BigRadius;

                // Make a piece of the small map with a transparent hole in it.
                using (Graphics gr = Graphics.FromImage(MapPatch))
                {
                    // Draw the small map image into the patch.
                    gr.DrawImage(OriginalMap, PatchRect, DestRect, GraphicsUnit.Pixel);

                    // Make a transparent hole in the patch.
                    using (SolidBrush br = new SolidBrush(Color.FromArgb(255, 1, 2, 3)))
                    {
                        gr.FillEllipse(br, PatchRect);
                        MapPatch.MakeTransparent(br.Color);
                    }
                }

                using (Graphics gr = Graphics.FromImage(ModifiedMap))
                {
                    gr.SmoothingMode = SmoothingMode.AntiAlias;

                    // Restore the original map.
                    gr.DrawImage(OriginalMap, 0, 0, OriginalWid, OriginalHgt);

                    // Copy a chunk of the big image into it.
                    gr.DrawImage(BigMap, DestRect, SrcRect, GraphicsUnit.Pixel);

                    // Draw the patch to make the closeup round.
                    gr.DrawImage(MapPatch, DestRect, PatchRect, GraphicsUnit.Pixel);

                    // Outline the area.
                    gr.DrawEllipse(Pens.Blue, DestRect);

                    // Display the result.
                    picMap.Image = ModifiedMap;
                }
            }
    }
}
