using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

namespace howto_outline_graphics
{
    public class Bitmap32
    {
        // Provide public access to the picture's byte data.
        public byte[] ImageBytes;
        public int RowSizeBytes;
        public const int PixelDataSize = 32;

        // A reference to the Bitmap.
        public Bitmap Bitmap;

        // True when locked.
        private bool m_IsLocked = false;
        public bool IsLocked
        {
            get
            {
                return m_IsLocked;
            }
        }

        // Save a reference to the bitmap.
        public Bitmap32(Bitmap bm)
        {
            Bitmap = bm;
        }

        // Bitmap data.
        private BitmapData m_BitmapData;

        // Return the image's dimensions.
        public int Width
        {
            get
            {
                return Bitmap.Width;
            }
        }
        public int Height
        {
            get
            {
                return Bitmap.Height;
            }
        }

        // Provide easy access to the color values.
        public void GetPixel(int x, int y, out byte red, out byte green, out byte blue, out byte alpha)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            blue = ImageBytes[i++];
            green = ImageBytes[i++];
            red = ImageBytes[i++];
            alpha = ImageBytes[i];
        }
        public void SetPixel(int x, int y, byte red, byte green, byte blue, byte alpha)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            ImageBytes[i++] = blue;
            ImageBytes[i++] = green;
            ImageBytes[i++] = red;
            ImageBytes[i] = alpha;
        }
        public byte GetBlue(int x, int y)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            return ImageBytes[i];
        }
        public void SetBlue(int x, int y, byte blue)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            ImageBytes[i] = blue;
        }
        public byte GetGreen(int x, int y)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            return ImageBytes[i + 1];
        }
        public void SetGreen(int x, int y, byte green)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            ImageBytes[i + 1] = green;
        }
        public byte GetRed(int x, int y)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            return ImageBytes[i + 2];
        }
        public void SetRed(int x, int y, byte red)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            ImageBytes[i + 2] = red;
        }
        public byte GetAlpha(int x, int y)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            return ImageBytes[i + 3];
        }
        public void SetAlpha(int x, int y, byte alpha)
        {
            int i = y * m_BitmapData.Stride + x * 4;
            ImageBytes[i + 3] = alpha;
        }

        // Lock the bitmap's data.
        public void LockBitmap()
        {
            // If it's already locked, do nothing.
            if (IsLocked) return;

            // Lock the bitmap data.
            Rectangle bounds = new Rectangle(
                0, 0, Bitmap.Width, Bitmap.Height);
            m_BitmapData = Bitmap.LockBits(bounds,
                ImageLockMode.ReadWrite,
                PixelFormat.Format32bppArgb);
            RowSizeBytes = m_BitmapData.Stride;

            // Allocate room for the data.
            int total_size = m_BitmapData.Stride * m_BitmapData.Height;
            ImageBytes = new byte[total_size];

            // Copy the data into the ImageBytes array.
            Marshal.Copy(m_BitmapData.Scan0, ImageBytes, 0, total_size);

            // It is now locked.
            m_IsLocked = true;
        }

        // Copy the data back into the Bitmap
        // and release resources.
        public void UnlockBitmap()
        {
            // If it's already unlocked, do nothing.
            if (!IsLocked) return;

            // Copy the data back into the bitmap.
            int total_size = m_BitmapData.Stride * m_BitmapData.Height;
            Marshal.Copy(ImageBytes, 0, m_BitmapData.Scan0, total_size);

            // Unlock the bitmap.
            Bitmap.UnlockBits(m_BitmapData);

            // Release resources.
            ImageBytes = null;
            m_BitmapData = null;

            // It is now unlocked.
            m_IsLocked = false;
        }

        // Convert to grayscale by averaging each pixel's
        // red, green, and blue components.
        public void Average()
        {
            // Remember if we are locked and lock the bitmap.
            bool was_locked = IsLocked;
            LockBitmap();

            // Convert to grayscale.
            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    byte red, green, blue, alpha;
                    GetPixel(x, y, out red, out green, out blue, out alpha);
                    byte gray = (byte)((red + green + blue) / 3);
                    SetPixel(x, y, gray, gray, gray, alpha);
                }
            }

            // Unlock if appropriate.
            if (!was_locked) UnlockBitmap();
        }

        // Convert to grayscale.
        public void Grayscale()
        {
            // Remember if we are locked and lock the bitmap.
            bool was_locked = IsLocked;
            LockBitmap();

            // Convert to grayscale.
            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    byte red, green, blue, alpha;
                    GetPixel(x, y, out red, out green, out blue, out alpha);
                    byte gray = (byte)(0.3 * red + 0.5 * green + 0.2 * blue);
                    SetPixel(x, y, gray, gray, gray, alpha);
                }
            }

            // Unlock if appropriate.
            if (!was_locked) UnlockBitmap();
        }

        // Clear the red color components.
        public void ClearRed()
        {
            // Remember if we are locked and lock the bitmap.
            bool was_locked = IsLocked;
            LockBitmap();

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    SetRed(x, y, 0);
                }
            }

            // Unlock if appropriate.
            if (!was_locked) UnlockBitmap();
        }

        // Clear the green color components.
        public void ClearGreen()
        {
            // Remember if we are locked and lock the bitmap.
            bool was_locked = IsLocked;
            LockBitmap();

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    SetGreen(x, y, 0);
                }
            }

            // Unlock if appropriate.
            if (!was_locked) UnlockBitmap();
        }

        // Clear the blue color components.
        public void ClearBlue()
        {
            // Remember if we are locked and lock the bitmap.
            bool was_locked = IsLocked;
            LockBitmap();

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    SetBlue(x, y, 0);
                }
            }

            // Unlock if appropriate.
            if (!was_locked) UnlockBitmap();
        }

        // Invert the pixel values.
        public void Invert()
        {
            // Remember if we are locked and lock the bitmap.
            bool was_locked = IsLocked;
            LockBitmap();

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    byte red = (byte)(255 - GetRed(x, y));
                    byte green = (byte)(255 - GetGreen(x, y));
                    byte blue = (byte)(255 - GetBlue(x, y));
                    byte alpha = GetAlpha(x, y);
                    SetPixel(x, y, red, green, blue, alpha);
                }
            }

            // Unlock if appropriate.
            if (!was_locked) UnlockBitmap();
        }

        #region "FilterStuff"

        // A public class to represent filters.
        public class Filter
        {
            public float[,] Kernel;
            public float Weight, offset;

            // Set the filter's weight equal to the sum
            // of the kernel's values.
            public void Normalize()
            {
                Weight = 0;
                for (int row = 0; row <= Kernel.GetUpperBound(0); row++)
                {
                    for (int col = 0; col <= Kernel.GetUpperBound(1); col++)
                    {
                        Weight += Kernel[row, col];
                    }
                }
            }

            // Set the valeu of the center kernel coefficient
            // so the kernel has a zero total.
            public void ZeroKernel()
            {
                float total = 0;
                for (int row = 0; row <= Kernel.GetUpperBound(0); row++)
                {
                    for (int col = 0; col <= Kernel.GetUpperBound(1); col++)
                    {
                        total += Kernel[row, col];
                    }
                }

                int row_mid = (int)(Kernel.GetUpperBound(0) / 2);
                int col_mid = (int)(Kernel.GetUpperBound(1) / 2);
                total -= Kernel[row_mid, col_mid];
                Kernel[row_mid, col_mid] = -total;
            }
        }

        // Make a deep copy of this object.
        public Bitmap32 Clone()
        {
            // See if we are locked.
            bool was_locked = this.IsLocked;

            // Lock this bitmap.
            this.LockBitmap();

            // Perform a shallow copy.
            Bitmap32 result = (Bitmap32)this.MemberwiseClone();

            // Copy the Bitmap.
            result.Bitmap = new Bitmap(this.Bitmap.Width, this.Bitmap.Height);
            result.m_IsLocked = false;

            // Unlock if appropriate.
            if (!was_locked) this.UnlockBitmap();

            // Return the result.
            return result;
        }

        // A standard embossing filter.
        public static Filter EmbossingFilter
        {
            get
            {
                return new Filter()
                {
                    Weight = 1,
                    offset = 127,
                    Kernel = new float[,]
                    {
                        {-1, 0, 0},
                        {0, 0, 0},
                        {0, 0, 1},
                    }
                };
            }
        }

        // A standard embossing filter.
        public static Filter EmbossingFilter2
        {
            get
            {
                return new Filter()
                {
                    Weight = 1,
                    offset = 127,
                    Kernel = new float[,]
                    {
                        {2,  0,  0},
                        {0, -1,  0},
                        {0,  0, -1},
                    }
                };
            }
        }

        // A standard blurring filter.
        public static Filter BlurFilter5x5Gaussian
        {
            get
            {
                Filter result = new Filter()
                {
                    offset = 0,
                    Kernel = new float[,]
                    {
                        {1,  4,  7,  4, 1},
                        {4, 16, 26, 16, 4},
                        {7, 26, 41, 26, 7},
                        {4, 16, 26, 16, 4},
                        {1,  4,  7,  4, 1},
                    }
                };
                result.Normalize();
                return result;
            }
        }

        // A mean blurring filter.
        public static Filter BlurFilter5x5Mean
        {
            get
            {
                Filter result = new Filter()
                {
                    offset = 0,
                    Kernel = new float[,]
                    {
                        {1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1},
                    }
                };
                result.Normalize();
                return result;
            }
        }

        // An edge detecting filter.
        public static Filter EdgeDetectionFilterULtoLR
        {
            get
            {
                return new Filter()
                {
                    Weight = 1,
                    offset = 0,
                    Kernel = new float[,]
                    {
                        {-5, 0, 0},
                        { 0, 0, 0},
                        { 0, 0, 5},
                    }
                };
            }
        }

        // An edge detecting filter.
        public static Filter EdgeDetectionFilterTopToBottom
        {
            get
            {
                return new Filter()
                {
                    Weight = 1,
                    offset = 0,
                    Kernel = new float[,]
                    {
                        {-1, -1, -1},
                        { 0,  0,  0},
                        { 1,  1,  1},
                    }
                };
            }
        }

        // An edge detecting filter.
        public static Filter EdgeDetectionFilterLeftToRight
        {
            get
            {
                return new Filter()
                {
                    Weight = 1,
                    offset = 0,
                    Kernel = new float[,]
                    {
                        {-1, 0, 1},
                        {-1, 0, 1},
                        {-1, 0, 1},
                    }
                };
            }
        }

        // A high-pass filter.
        public static Filter HighPassFilter3x3
        {
            get
            {
                return new Filter()
                {
                    Weight = 16,
                    offset = 127,
                    Kernel = new float[,]
                    {
                        {-1, -2, -1},
                        {-2, 12, -2},
                        {-1, -2, -1},
                    }
                };
            }
        }

        // A high-pass filter.
        public static Filter HighPassFilter5x5
        {
            get
            {
                Filter result = new Filter()
                {
                    offset = 127,
                    Kernel = new float[,]
                    {
                        {-1,  -4,  -7,  -4, -1},
                        {-4, -16, -26, -16, -4},
                        {-7, -26, -41, -26, -7},
                        {-4, -16, -26, -16, -4},
                        {-1,  -4,  -7,  -4, -1},
                    }
                };
                // Set the weight.
                result.Normalize();
                result.Weight = -result.Weight;

                // Set the kernel's center value.
                result.ZeroKernel();
                return result;
            }
        }

        // Apply a filter to the image.
        public Bitmap32 ApplyFilter(Filter filter, bool lock_result)
        {
            // Make a copy of this Bitmap32.
            Bitmap32 result = this.Clone();

            // Lock both bitmaps.
            bool was_locked = this.IsLocked;
            this.LockBitmap();
            result.LockBitmap();

            // Apply the filter.
            int xoffset = -(int)(filter.Kernel.GetUpperBound(1) / 2);
            int yoffset = -(int)(filter.Kernel.GetUpperBound(0) / 2);
            int xmin = -xoffset;
            int xmax = Bitmap.Width - filter.Kernel.GetUpperBound(1);
            int ymin = -yoffset;
            int ymax = Bitmap.Height - filter.Kernel.GetUpperBound(0);
            int row_max = filter.Kernel.GetUpperBound(0);
            int col_max = filter.Kernel.GetUpperBound(1);

            for (int x = xmin; x <= xmax; x++)
            {
                for (int y = ymin; y <= ymax; y++)
                {
                    // Skip the pixel if any under the kernel
                    // is completely transparent.
                    bool skip_pixel = false;

                    // Apply the filter to pixel (x, y).
                    float red = 0, green = 0, blue = 0;
                    for (int row = 0; row <= row_max; row++)
                    {
                        for (int col = 0; col <= col_max; col++)
                        {
                            int ix = x + col + xoffset;
                            int iy = y + row + yoffset;
                            byte new_red, new_green, new_blue, new_alpha;
                            this.GetPixel(ix, iy, out new_red, out new_green, out new_blue, out new_alpha);

                            // See if we should skip this pixel.
                            if (new_alpha == 0)
                            {
                                skip_pixel = true;
                                break;
                            }

                            red += new_red * filter.Kernel[row, col];
                            green += new_green * filter.Kernel[row, col];
                            blue += new_blue * filter.Kernel[row, col];
                        }
                        if (skip_pixel) break;
                    }

                    if (!skip_pixel)
                    {
                        // Divide by the weight, add the offset, and
                        // make sure the result is between 0 and 255.
                        red = filter.offset + red / filter.Weight;
                        if (red < 0) red = 0;
                        if (red > 255) red = 255;

                        green = filter.offset + green / filter.Weight;
                        if (green < 0) green = 0;
                        if (green > 255) green = 255;

                        blue = filter.offset + blue / filter.Weight;
                        if (blue < 0) blue = 0;
                        if (blue > 255) blue = 255;

                        // Set the new pixel's value.
                        result.SetPixel(x, y, (byte)red, (byte)green, (byte)blue,
                            this.GetAlpha(x, y));
                    }
                }
            }

            // Unlock the bitmaps.
            if (!lock_result) result.UnlockBitmap();
            if (!was_locked) this.UnlockBitmap();

            // Return the result.
            return result;
        }

        #endregion // FilterStuff

        #region Warping Methods

        // Warping types.
        public enum WarpOperations
        {
            Identity,
            FishEye,
            Twist,
            Wave,
            SmallTop,
            Wiggles,
            DoubleWave,
        }

        // Warp an image and return a new Bitmap32 holding the result.
        public Bitmap32 Warp(WarpOperations warp_op, bool lock_result)
        {
            // Make a copy of this Bitmap32.
            Bitmap32 result = this.Clone();

            // Lock both bitmaps.
            bool was_locked = this.IsLocked;
            this.LockBitmap();
            result.LockBitmap();

            // Warp the image.
            WarpImage(this, result, warp_op);

            // Unlock the bitmaps.
            if (!lock_result) result.UnlockBitmap();
            if (!was_locked) this.UnlockBitmap();

            // Return the result.
            return result;
        }

        // Transform the image.
        private static void WarpImage(Bitmap32 bm_src, Bitmap32 bm_dest, WarpOperations warp_op)
        {
            // Calculate some image information.
            double xmid = bm_dest.Width / 2.0;
            double ymid = bm_dest.Height / 2.0;
            double rmax = bm_dest.Width * 0.75;

            int ix_max = bm_src.Width - 2;
            int iy_max = bm_src.Height - 2;

            // Generate a result for each output pixel.
            double x0, y0;
            for (int y1 = 0; y1 < bm_dest.Height; y1++)
            {
                for (int x1 = 0; x1 < bm_dest.Width; x1++)
                {
                    // Map back to the source image.
                    MapPixel(warp_op, xmid, ymid, rmax, x1, y1, out x0, out y0);

                    // Interpolate to get the result pixel's value.
                    // Find the next smaller integral position.
                    int ix0 = (int)x0;
                    int iy0 = (int)y0;

                    // See if this is out of bounds.
                    if ((ix0 < 0) || (ix0 > ix_max) ||
                        (iy0 < 0) || (iy0 > iy_max))
                    {
                        // The point is outside the image. Use white.
                        bm_dest.SetPixel(x1, y1, 255, 255, 255, 255);
                    }
                    else
                    {
                        // The point lies within the image.
                        // Calculate its value.
                        double dx0 = x0 - ix0;
                        double dy0 = y0 - iy0;
                        double dx1 = 1 - dx0;
                        double dy1 = 1 - dy0;

                        // Get the colors of the surrounding pixels.
                        byte r00, g00, b00, a00, r01, g01, b01, a01,
                             r10, g10, b10, a10, r11, g11, b11, a11;
                        bm_src.GetPixel(ix0, iy0, out r00, out g00, out b00, out a00);
                        bm_src.GetPixel(ix0, iy0 + 1, out r01, out g01, out b01, out a01);
                        bm_src.GetPixel(ix0 + 1, iy0, out r10, out g10, out b10, out a10);
                        bm_src.GetPixel(ix0 + 1, iy0 + 1, out r11, out g11, out b11, out a11);

                        // Compute the weighted average.
                        int r = (int)(
                            r00 * dx1 * dy1 + r01 * dx1 * dy0 +
                            r10 * dx0 * dy1 + r11 * dx0 * dy0);
                        int g = (int)(
                            g00 * dx1 * dy1 + g01 * dx1 * dy0 +
                            g10 * dx0 * dy1 + g11 * dx0 * dy0);
                        int b = (int)(
                            b00 * dx1 * dy1 + b01 * dx1 * dy0 +
                            b10 * dx0 * dy1 + b11 * dx0 * dy0);
                        int a = (int)(
                            a00 * dx1 * dy1 + a01 * dx1 * dy0 +
                            a10 * dx0 * dy1 + a11 * dx0 * dy0);
                        bm_dest.SetPixel(x1, y1, (byte)r, (byte)g, (byte)b, (byte)a);
                    }
                }
            }
        }

        // Map the output pixel (x1, y1) back to the input pixel (x0, y0).
        private static void MapPixel(WarpOperations warp_op, double xmid, double ymid, double rmax, int x1, int y1, out double x0, out double y0)
        {
            const double pi_over_2 = Math.PI / 2.0;
            const double K = 100.0;
            const double offset = -pi_over_2;
            double dx, dy, r1, r2;

            switch (warp_op)
            {
                case WarpOperations.Identity:
                    x0 = x1;
                    y0 = y1;
                    break;
                case WarpOperations.FishEye:
                    dx = x1 - xmid;
                    dy = y1 - ymid;
                    r1 = Math.Sqrt(dx * dx + dy * dy);
                    if (r1 == 0)
                    {
                        x0 = xmid;
                        y0 = ymid;
                    }
                    else
                    {
                        r2 = rmax / 2 * (1 / (1 - r1 / rmax) - 1);
                        x0 = dx * r2 / r1 + xmid;
                        y0 = dy * r2 / r1 + ymid;
                    }
                    break;
                case WarpOperations.Twist:
                    dx = x1 - xmid;
                    dy = y1 - ymid;
                    r1 = Math.Sqrt(dx * dx + dy * dy);
                    if (r1 == 0)
                    {
                        x0 = 0;
                        y0 = 0;
                    }
                    else
                    {
                        double theta = Math.Atan2(dx, dy) - r1 / K - offset;
                        x0 = r1 * Math.Cos(theta);
                        y0 = r1 * Math.Sin(theta);
                    }
                    x0 = x0 + xmid;
                    y0 = y0 + ymid;
                    break;
                case WarpOperations.Wave:
                    x0 = x1;
                    y0 = y1 - 10 * (Math.Sin(x1 / 50.0 * Math.PI) + 1) + 5;
                    break;
                case WarpOperations.SmallTop:
                    dx = xmid - x1;
                    dx = dx * ymid * 2 / (y1 + 1);
                    x0 = xmid - dx;
                    y0 = y1;
                    break;
                case WarpOperations.Wiggles:
                    dx = xmid - x1;
                    dx = dx * (Math.Sin(y1 / 50.0 * Math.PI) / 2 + 1.5);
                    x0 = xmid - dx;
                    y0 = y1;
                    break;
                case WarpOperations.DoubleWave:
                    x0 = x1 - 10 * (Math.Sin(y1 / 50.0 * Math.PI) + 1) + 5;
                    y0 = y1 - 10 * (Math.Sin(x1 / 50.0 * Math.PI) + 1) + 5;
                    break;
                default:    // Flip vertically and horizontally.
                    x0 = 2 * xmid - x1;
                    y0 = 2 * ymid - y1;
                    break;
            }
        }

        #endregion Warping Methods

    }
}
