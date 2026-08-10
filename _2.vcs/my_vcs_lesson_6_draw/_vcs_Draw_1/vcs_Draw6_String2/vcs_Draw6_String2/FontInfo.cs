using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace vcs_Draw6_String2
{
    public class FontInfo
    {
        // Heights and positions in pixels.
        public float EmHeightPixels;
        public float AscentPixels;
        public float DescentPixels;
        public float CellHeightPixels;
        public float InternalLeadingPixels;
        public float LineSpacingPixels;
        public float ExternalLeadingPixels;

        // Distances from the top of the cell in pixels.
        public float RelTop;
        public float RelBaseline;
        public float RelBottom;

        // Initialize the properties.
        public FontInfo(Graphics gr, Font f)
        {
            float em_height = f.FontFamily.GetEmHeight(f.Style);
            EmHeightPixels = ConvertUnits(gr, f.Size, f.Unit, GraphicsUnit.Pixel);
            float design_to_pixels = EmHeightPixels / em_height;

            AscentPixels = design_to_pixels * f.FontFamily.GetCellAscent(f.Style);
            DescentPixels = design_to_pixels * f.FontFamily.GetCellDescent(f.Style);
            CellHeightPixels = AscentPixels + DescentPixels;
            InternalLeadingPixels = CellHeightPixels - EmHeightPixels;
            LineSpacingPixels = design_to_pixels * f.FontFamily.GetLineSpacing(f.Style);
            ExternalLeadingPixels = LineSpacingPixels - CellHeightPixels;

            RelTop = InternalLeadingPixels;
            RelBaseline = AscentPixels;
            RelBottom = CellHeightPixels;
        }

        // Convert from one type of unit to another.
        // I don't know how to do Display or World.
        private float ConvertUnits(Graphics gr, float value, GraphicsUnit from_unit, GraphicsUnit to_unit)
        {
            if (from_unit == to_unit) return value;

            // Convert to pixels. 
            switch (from_unit)
            {
                case GraphicsUnit.Document:
                    value *= gr.DpiX / 300;
                    break;
                case GraphicsUnit.Inch:
                    value *= gr.DpiX;
                    break;
                case GraphicsUnit.Millimeter:
                    value *= gr.DpiX / 25.4F;
                    break;
                case GraphicsUnit.Pixel:
                    // Do nothing.
                    break;
                case GraphicsUnit.Point:
                    value *= gr.DpiX / 72;
                    break;
                default:
                    throw new Exception("Unknown input unit " + from_unit.ToString() + " in FontInfo.ConvertUnits");
            }

            // Convert from pixels to the new units. 
            switch (to_unit)
            {
                case GraphicsUnit.Document:
                    value /= gr.DpiX / 300;
                    break;
                case GraphicsUnit.Inch:
                    value /= gr.DpiX;
                    break;
                case GraphicsUnit.Millimeter:
                    value /= gr.DpiX / 25.4F;
                    break;
                case GraphicsUnit.Pixel:
                    // Do nothing.
                    break;
                case GraphicsUnit.Point:
                    value /= gr.DpiX / 72;
                    break;
                default:
                    throw new Exception("Unknown output unit " + to_unit.ToString() + " in FontInfo.ConvertUnits");
            }

            return value;
        }
    }
}
