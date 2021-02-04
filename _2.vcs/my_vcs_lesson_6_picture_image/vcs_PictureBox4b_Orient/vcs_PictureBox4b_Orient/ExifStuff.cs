using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Drawing.Text;

namespace vcs_PictureBox4b_Orient
{
    public static class ExifStuff
    {
        // Orientations.
        private const int OrientationId = 0x0112;
        public enum ExifOrientations : byte
        {
            Unknown = 0,
            TopLeft = 1,
            TopRight = 2,
            BottomRight = 3,
            BottomLeft = 4,
            LeftTop = 5,
            RightTop = 6,
            RightBottom = 7,
            LeftBottom = 8,
        }

        // Return the image's orientation.
        public static ExifOrientations ImageOrientation(Image img)
        {
            // Get the index of the orientation property.
            int orientation_index = Array.IndexOf(img.PropertyIdList, OrientationId);

            // If there is no such property, return Unknown.
            if (orientation_index < 0) return ExifOrientations.Unknown;

            // Return the orientation value.
            return (ExifOrientations)img.GetPropertyItem(OrientationId).Value[0];
        }

        // Orient the image properly.
        public static void OrientImage(Image img)
        {
            // Get the image's orientation.
            ExifOrientations orientation = ImageOrientation(img);

            // Orient the image.
            switch (orientation)
            {
                case ExifOrientations.Unknown:
                case ExifOrientations.TopLeft:
                    break;
                case ExifOrientations.TopRight:
                    img.RotateFlip(RotateFlipType.RotateNoneFlipX);
                    break;
                case ExifOrientations.BottomRight:
                    img.RotateFlip(RotateFlipType.Rotate180FlipNone);
                    break;
                case ExifOrientations.BottomLeft:
                    img.RotateFlip(RotateFlipType.RotateNoneFlipY);
                    break;
                case ExifOrientations.LeftTop:
                    img.RotateFlip(RotateFlipType.Rotate90FlipX);
                    break;
                case ExifOrientations.RightTop:
                    img.RotateFlip(RotateFlipType.Rotate90FlipNone);
                    break;
                case ExifOrientations.RightBottom:
                    img.RotateFlip(RotateFlipType.Rotate90FlipY);
                    break;
                case ExifOrientations.LeftBottom:
                    img.RotateFlip(RotateFlipType.Rotate270FlipNone);
                    break;
            }

            // Set the image's orientation to TopLeft.
            SetImageOrientation(img, ExifOrientations.TopLeft);
        }

        // Set the image's orientation.
        public static void SetImageOrientation(Image img, ExifOrientations orientation)
        {
            // Get the index of the orientation property.
            int orientation_index = Array.IndexOf(img.PropertyIdList, OrientationId);

            // If there is no such property, do nothing.
            if (orientation_index < 0) return;

            // Set the orientation value.
            PropertyItem item = img.GetPropertyItem(OrientationId);
            item.Value[0] = (byte)orientation;
            img.SetPropertyItem(item);
        }

        // Make an image to demonstrate orientations.
        public static Image OrientationImage(ExifOrientations orientation)
        {
            const int size = 64;
            Bitmap bm = new Bitmap(size, size);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                // Orient the result.
                switch (orientation)
                {
                    case ExifOrientations.TopLeft:
                        break;
                    case ExifOrientations.TopRight:
                        gr.ScaleTransform(-1, 1);
                        break;
                    case ExifOrientations.BottomRight:
                        gr.RotateTransform(180);
                        break;
                    case ExifOrientations.BottomLeft:
                        gr.ScaleTransform(1, -1);
                        break;
                    case ExifOrientations.LeftTop:
                        gr.RotateTransform(90);
                        gr.ScaleTransform(-1, 1, MatrixOrder.Append);
                        break;
                    case ExifOrientations.RightTop:
                        gr.RotateTransform(-90);
                        break;
                    case ExifOrientations.RightBottom:
                        gr.RotateTransform(90);
                        gr.ScaleTransform(1, -1, MatrixOrder.Append);
                        break;
                    case ExifOrientations.LeftBottom:
                        gr.RotateTransform(90);
                        break;
                }

                // Translate the result to the center of the bitmap.
                gr.TranslateTransform(
                    size / 2, size / 2, MatrixOrder.Append);

                using (StringFormat string_format = new StringFormat())
                {
                    string_format.LineAlignment = StringAlignment.Center;
                    string_format.Alignment = StringAlignment.Center;
                    using (Font font = new Font("Times New Roman", 40,
                        GraphicsUnit.Point))
                    {
                        if (orientation == ExifOrientations.Unknown)
                        {
                            gr.DrawString("?", font, Brushes.Black,
                                0, 0, string_format);
                        }
                        else
                        {
                            gr.DrawString("F", font, Brushes.Black,
                                0, 0, string_format);
                        }
                    }
                }
            }

            return bm;
        }
    }
}
