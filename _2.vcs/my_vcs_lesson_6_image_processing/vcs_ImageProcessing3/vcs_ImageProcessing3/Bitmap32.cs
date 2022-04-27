using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

namespace vcs_ImageProcessing3
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
                    byte red   = (byte)(255 - GetRed(x, y));
                    byte green = (byte)(255 - GetGreen(x, y));
                    byte blue  = (byte)(255 - GetBlue(x, y));
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
            public float Weight, Offset;

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
                    Offset = 127,
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
                    Offset = 127,
                    Kernel = new float[,]
                    {
                        {2,  0,  0},
                        {0, -1,  0},
                        {0,  0, -1},
                    }
                };
            }
        }

        // A less standard embossing filter.
        public static Filter EmbossingFilter3
        {
            get
            {
                return new Filter()
                {
                    Weight = 1,
                    Offset = 0,
                    Kernel = new float[,]
                    {
                        {1,  1, -1},
                        {1,  1, -1},
                        {1, -1, -1},
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
                    Offset = 0,
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
                    Offset = 0,
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
                    Offset = 0,
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
                    Offset = 0,
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
                    Offset = 0,
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
                    Offset = 127,
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
            get{
                Filter result = new Filter()
                {
                    Offset = 127,
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

                            red   += new_red   * filter.Kernel[row, col];
                            green += new_green * filter.Kernel[row, col];
                            blue  += new_blue  * filter.Kernel[row, col];
                        }
                        if (skip_pixel) break;
                    }

                    if (!skip_pixel)
                    {
                        // Divide by the weight, add the offset, and
                        // make sure the result is between 0 and 255.
                        red = filter.Offset + red / filter.Weight;
                        if (red < 0) red = 0;
                        if (red > 255) red = 255;

                        green = filter.Offset + green / filter.Weight;
                        if (green < 0) green = 0;
                        if (green > 255) green = 255;

                        blue = filter.Offset + blue / filter.Weight;
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

        #region "Rank Filters"

        // Use the maximum brightness value in a region.
        public Bitmap32 RankMaximum(int rank, bool lock_result)
        {
            // Make a copy of this Bitmap32.
            Bitmap32 result = this.Clone();

            // Lock both bitmaps.
            bool was_locked = this.IsLocked;
            this.LockBitmap();
            result.LockBitmap();

            // Calculate bounds to iterate over.
            int start_i = -rank / 2;
            int stop_i = rank + start_i;

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    // Find the brightest pixel around this one.
                    int best_brightness = GetRed(x, y) + GetGreen(x, y) + GetBlue(x, y);
                    int best_row = y;
                    int best_col = x;
                    for (int dy = start_i; dy < stop_i; dy++)
                    {
                        int row = y + dy;
                        if ((row >= 0) && (row < Height))
                        {
                            for (int dx = start_i; dx < stop_i; dx++)
                            {
                                int col = x + dx;
                                if ((col >= 0) && (col < Width))
                                {
                                    int test_brightness =
                                        GetRed(col, row) +
                                        GetGreen(col, row) +
                                        GetBlue(col, row);
                                    if (test_brightness > best_brightness)
                                    {
                                        best_brightness = test_brightness;
                                        best_row = row;
                                        best_col = col;
                                    }
                                }
                            }
                        }
                    }

                    // Set this pixel to the brighest value we found.
                    result.SetPixel(x, y,
                        GetRed(best_col, best_row),
                        GetGreen(best_col, best_row),
                        GetBlue(best_col, best_row),
                        255);
                }
            }

            // Unlock the bitmaps.
            if (!lock_result) result.UnlockBitmap();
            if (!was_locked) this.UnlockBitmap();

            // Return the result.
            return result;
        }

        // Use the minimum brightness value in a region.
        public Bitmap32 RankMinimum(int rank, bool lock_result)
        {
            // Make a copy of this Bitmap32.
            Bitmap32 result = this.Clone();

            // Lock both bitmaps.
            bool was_locked = this.IsLocked;
            this.LockBitmap();
            result.LockBitmap();

            // Calculate bounds to iterate over.
            int start_i = -rank / 2;
            int stop_i = rank + start_i;

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    // Find the brightest pixel around this one.
                    int best_brightness = GetRed(x, y) + GetGreen(x, y) + GetBlue(x, y);
                    int best_row = y;
                    int best_col = x;
                    for (int dy = start_i; dy < stop_i; dy++)
                    {
                        int row = y + dy;
                        if ((row >= 0) && (row < Height))
                        {
                            for (int dx = start_i; dx < stop_i; dx++)
                            {
                                int col = x + dx;
                                if ((col >= 0) && (col < Width))
                                {
                                    int test_brightness =
                                        GetRed(col, row) +
                                        GetGreen(col, row) +
                                        GetBlue(col, row);
                                    if (test_brightness < best_brightness)
                                    {
                                        best_brightness = test_brightness;
                                        best_row = row;
                                        best_col = col;
                                    }
                                }
                            }
                        }
                    }

                    // Set this pixel to the brighest value we found.
                    result.SetPixel(x, y,
                        GetRed(best_col, best_row),
                        GetGreen(best_col, best_row),
                        GetBlue(best_col, best_row),
                        255);
                }
            }

            // Unlock the bitmaps.
            if (!lock_result) result.UnlockBitmap();
            if (!was_locked) this.UnlockBitmap();

            // Return the result.
            return result;
        }

        // Pixellate the image.
        public void Pixellate(int rank, bool lock_result)
        {
            // Lock the bitmap.
            bool was_locked = this.IsLocked;
            this.LockBitmap();

            for (int y = 0; y < Height; y += rank)
            {
                for (int x = 0; x < Width; x += rank)
                {
                    // Add up the pixel values in this area.
                    int total_r = 0;
                    int total_g = 0;
                    int total_b = 0;
                    int num_pixels = 0;
                    for (int row = y; row < y + rank; row++)
                    {
                        if (row < Height)
                        {
                            for (int col = x; col < x + rank; col++)
                            {
                                if (col < Width)
                                {
                                    total_r += GetRed(col, row);
                                    total_g += GetGreen(col, row);
                                    total_b += GetBlue(col, row);
                                    num_pixels++;
                                }
                            }
                        }
                    }

                    // Calculate the averages.
                    byte byte_r = (byte)(total_r / num_pixels);
                    byte byte_g = (byte)(total_g / num_pixels);
                    byte byte_b = (byte)(total_b / num_pixels);

                    // Set the color for this area.
                    for (int row = y; row < y + rank; row++)
                    {
                        if (row < Height)
                        {
                            for (int col = x; col < x + rank; col++)
                            {
                                if (col < Width)
                                {
                                    SetPixel(col, row,
                                        byte_r, byte_g, byte_b, 255);
                                }
                            }
                        }
                    }
                }
            }

            // Unlock the bitmaps.
            if (!was_locked) this.UnlockBitmap();
        }

        // Pointellate the image.
        public Bitmap Pointellate(int rank, int point_diameter, bool lock_result)
        {
            // Lock the bitmap.
            bool was_locked = this.IsLocked;
            this.LockBitmap();

            // Create the result Bitmap.
            Bitmap bm = new Bitmap(Width, Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

                for (int y = 0; y < Height; y += rank)
                {
                    for (int x = 0; x < Width; x += rank)
                    {
                        // Add up the pixel values in this area.
                        int total_r = 0;
                        int total_g = 0;
                        int total_b = 0;
                        int num_pixels = 0;
                        for (int row = y; row < y + rank; row++)
                        {
                            if (row < Height)
                            {
                                for (int col = x; col < x + rank; col++)
                                {
                                    if (col < Width)
                                    {
                                        total_r += GetRed(col, row);
                                        total_g += GetGreen(col, row);
                                        total_b += GetBlue(col, row);
                                        num_pixels++;
                                    }
                                }
                            }
                        }

                        // Calculate the averages.
                        byte byte_r = (byte)(total_r / num_pixels);
                        byte byte_g = (byte)(total_g / num_pixels);
                        byte byte_b = (byte)(total_b / num_pixels);

                        // Set the color for this area.
                        int offset = (rank - point_diameter) / 2;
                        using (Brush br = new
                            SolidBrush(Color.FromArgb(255, byte_r, byte_g, byte_b)))
                        {
                            gr.FillEllipse(br,
                                x + offset, y + offset,
                                point_diameter, point_diameter);
                        }
                    }
                }
            }

            // Unlock the bitmaps.
            if (!was_locked) this.UnlockBitmap();

            // Return the new bitmap.
            return bm;
        }

        #endregion // Rank Filters

    }
}
