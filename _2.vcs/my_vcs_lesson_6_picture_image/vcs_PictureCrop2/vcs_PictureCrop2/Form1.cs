using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace vcs_PictureCrop2
{
    public partial class Form1 : Form
    {
        private RectangleF SelectionRectangle;

        private bool Dragging = false;
        private HitTypes CurrentHitType = HitTypes.None;
        private Point LastPoint;
        private PointF OppositeCorner;

        private Bitmap bitmap1 = null;
        private Bitmap bitmap2 = null;

        private float ImageScale = 1f;
        private float AspectWidth = 1f;
        private float AspectHeight = 1f;
        private float AspectRatio = 1f;
        private float RectWidth = 1f;
        private float RectHeight = 1f;

        string filename = @"C:\______test_files\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private enum HitTypes
        {
            None,
            Body,
            LeftEdge,
            RightEdge,
            TopEdge,
            BottomEdge,
            ULCorner,
            URCorner,
            LLCorner,
            LRCorner,
        };

        private void Form1_Load(object sender, EventArgs e)
        {
            float.TryParse(txtWidth.Text, out RectWidth);
            float.TryParse(txtHeight.Text, out RectHeight);
            ReadAspectRatio();
            SelectionRectangle.X = 10;
            SelectionRectangle.Y = 10;

            // Prepare to use the mouse wheel.
            this.MouseWheel += Form_MouseWheel;

            // Load the image.
            bitmap1 = LoadBitmapUnlocked(filename);
            ShowScaledImage();
        }

        // Display the scaled image.
        private void ShowScaledImage()
        {
            if (bitmap1 == null)
            {
                return;
            }
            int scaled_width = (int)(bitmap1.Width * ImageScale);
            int scaled_height = (int)(bitmap1.Height * ImageScale);
            bitmap2 = new Bitmap(scaled_width, scaled_height);
            using (Graphics g = Graphics.FromImage(bitmap2))
            {
                Point[] dest_points =
                {
                    new Point(0, 0),
                    new Point(scaled_width - 1, 0),
                    new Point(0, scaled_height - 1),
                };
                Rectangle src_rect = new Rectangle(
                    0, 0,
                    bitmap1.Width - 1,
                    bitmap1.Height - 1);
                g.DrawImage(bitmap1, dest_points, src_rect, GraphicsUnit.Pixel);
            }
            picImage.Image = bitmap2;
            picImage.Visible = true;
            picImage.Refresh();
        }

        // Draw the selection rectangle.
        private const int HandleRadius = 4;
        private void picImage_Paint(object sender, PaintEventArgs e)
        {
            try
            {
                // Draw the selection rectangle.
                RectangleF scaled_rect = ScaledSelectionRectangle();
                using (Pen pen = new Pen(Color.Red, 2))
                {
                    e.Graphics.DrawRectangle(pen, scaled_rect);

                    pen.Color = Color.Yellow;
                    pen.DashPattern = new float[] { 5, 5 };
                    e.Graphics.DrawRectangle(pen, scaled_rect);
                }

                PointF[] corners =
                {
                    new PointF(scaled_rect.Left, scaled_rect.Top),
                    new PointF(scaled_rect.Right, scaled_rect.Top),
                    new PointF(scaled_rect.Left, scaled_rect.Bottom),
                    new PointF(scaled_rect.Right, scaled_rect.Bottom),
                };
                foreach (PointF point in corners)
                {
                    e.Graphics.DrawBox(Brushes.White, Pens.Black, point, HandleRadius);
                }
            }
            catch
            {
            }
        }

        // Scale the selection rectangle.
        private RectangleF ScaledSelectionRectangle()
        {
            float x = ImageScale * SelectionRectangle.X;
            float y = ImageScale * SelectionRectangle.Y;
            float wid = ImageScale * SelectionRectangle.Width;
            float hgt = ImageScale * SelectionRectangle.Height;
            {
                return new RectangleF(x, y, wid, hgt);
            }
        }

        // Start dragging.
        private void picImage_MouseDown(object sender, MouseEventArgs e)
        {
            // If the mouse is not over the
            // selection rectangle, do nothing.
            CurrentHitType = FindHitType(e.Location);
            if (CurrentHitType == HitTypes.None)
            {
                return;
            }

            // Start the drag.
            LastPoint = e.Location;
            switch (CurrentHitType)
            {
                case HitTypes.None:
                    break;
                case HitTypes.ULCorner:
                case HitTypes.TopEdge:
                case HitTypes.LeftEdge:
                    OppositeCorner = new PointF(SelectionRectangle.Right, SelectionRectangle.Bottom);
                    break;
                case HitTypes.URCorner:
                    OppositeCorner = new PointF(SelectionRectangle.Left, SelectionRectangle.Bottom);
                    break;
                case HitTypes.LRCorner:
                case HitTypes.BottomEdge:
                case HitTypes.RightEdge:
                    OppositeCorner = new PointF(SelectionRectangle.Left, SelectionRectangle.Top);
                    break;
                case HitTypes.LLCorner:
                    OppositeCorner = new PointF(SelectionRectangle.Right, SelectionRectangle.Top);
                    break;
            }

            Dragging = true;
        }

        // Continue dragging.
        private void picImage_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Dragging)
            {
                MouseMoveNotDragging(e.Location);
            }
            else
            {
                MouseMoveDragging(e.Location);
            }
        }

        private void MouseMoveNotDragging(Point point)
        {
            Cursor new_cursor = Cursors.Default;
            CurrentHitType = FindHitType(point);
            switch (CurrentHitType)
            {
                case HitTypes.ULCorner:
                case HitTypes.LRCorner:
                    new_cursor = Cursors.SizeNWSE;
                    break;
                case HitTypes.URCorner:
                case HitTypes.LLCorner:
                    new_cursor = Cursors.SizeNESW;
                    break;
                case HitTypes.LeftEdge:
                case HitTypes.RightEdge:
                    new_cursor = Cursors.SizeWE;
                    break;
                case HitTypes.TopEdge:
                case HitTypes.BottomEdge:
                    new_cursor = Cursors.SizeNS;
                    break;
                case HitTypes.Body:
                    new_cursor = Cursors.SizeAll;
                    break;
            }

            if (picImage.Cursor != new_cursor)
            {
                picImage.Cursor = new_cursor;
            }
        }

        private void MouseMoveDragging(Point point)
        {
            // Find the new size for corner drags.
            float corner_wid = Math.Abs(OppositeCorner.X - point.X / ImageScale);
            float corner_hgt = Math.Abs(OppositeCorner.Y - point.Y / ImageScale);
            SizeF corner_size = GetReducedSize(corner_wid, corner_hgt);

            // Find the new size for edge drags.
            SizeF edge_size = new SizeF();
            if ((CurrentHitType == HitTypes.TopEdge) || (CurrentHitType == HitTypes.BottomEdge))
            {
                edge_size = GetEnlargedSize(0, corner_hgt);
            }
            else if ((CurrentHitType == HitTypes.LeftEdge) || (CurrentHitType == HitTypes.RightEdge))
            {
                edge_size = GetEnlargedSize(corner_wid, 0);
            }

            // Find the center of the selection rectangle for edge drags.
            float cx = SelectionRectangle.X + SelectionRectangle.Width / 2f;
            float cy = SelectionRectangle.Y + SelectionRectangle.Height / 2f;

            switch (CurrentHitType)
            {
                // Corners.
                case HitTypes.ULCorner:
                    SelectionRectangle = new RectangleF(SelectionRectangle.Right - corner_size.Width, SelectionRectangle.Bottom - corner_size.Height, corner_size.Width, corner_size.Height);
                    break;
                case HitTypes.URCorner:
                    SelectionRectangle = new RectangleF(SelectionRectangle.Left, SelectionRectangle.Bottom - corner_size.Height, corner_size.Width, corner_size.Height);
                    break;
                case HitTypes.LRCorner:
                    SelectionRectangle = new RectangleF(SelectionRectangle.X, SelectionRectangle.Y, corner_size.Width, corner_size.Height);
                    break;
                case HitTypes.LLCorner:
                    SelectionRectangle = new RectangleF(SelectionRectangle.Right - corner_size.Width, SelectionRectangle.Top, corner_size.Width, corner_size.Height);
                    break;

                // Edges.
                case HitTypes.TopEdge:
                    SelectionRectangle = new RectangleF(cx - edge_size.Width / 2f, SelectionRectangle.Bottom - edge_size.Height, edge_size.Width, edge_size.Height);
                    break;
                case HitTypes.RightEdge:
                    SelectionRectangle = new RectangleF(SelectionRectangle.Left, cy - edge_size.Height / 2f, edge_size.Width, edge_size.Height);
                    break;
                case HitTypes.BottomEdge:
                    SelectionRectangle = new RectangleF(cx - edge_size.Width / 2f, SelectionRectangle.Top, edge_size.Width, edge_size.Height);
                    break;
                case HitTypes.LeftEdge:
                    SelectionRectangle = new RectangleF(SelectionRectangle.Right - edge_size.Width, cy - edge_size.Height / 2f, edge_size.Width, edge_size.Height);
                    break;

                // Body.
                case HitTypes.Body:
                    int dx = (int)((point.X - LastPoint.X) / ImageScale);
                    int dy = (int)((point.Y - LastPoint.Y) / ImageScale);
                    SelectionRectangle.X += dx;
                    SelectionRectangle.Y += dy;
                    break;
            }
            LastPoint = point;
            picImage.Refresh();
            ShowWidthAndHeight();
        }

        private void ShowWidthAndHeight()
        {
            IgnoreTextChanged = true;
            txtWidth.Text = SelectionRectangle.Width.ToString();
            txtHeight.Text = SelectionRectangle.Height.ToString();
            IgnoreTextChanged = false;

            nud_x_st.Value = (decimal)SelectionRectangle.X;
            nud_y_st.Value = (decimal)SelectionRectangle.Y;
            nud_w.Value = (decimal)SelectionRectangle.Width;
            nud_h.Value = (decimal)SelectionRectangle.Height;
        }

        private SizeF GetEnlargedSize(float new_width, float new_height)
        {
            if (new_width < 10)
            {
                new_width = 10;
            }
            if (new_height < 10)
            {
                new_height = 10;
            }

            if (new_width / new_height > AspectRatio)
            {
                // Too short and wide. Increase the height.
                new_height = new_width / AspectRatio;
            }
            else
            {
                // Too tall and thin. Increase the width.
                new_width = new_height * AspectRatio;
            }
            return new SizeF(new_width, new_height);
        }

        private SizeF GetReducedSize(float new_width, float new_height)
        {
            if (new_width < 10)
            {
                new_width = 10;
            }
            if (new_height < 10)
            {
                new_height = 10;
            }

            if (new_width / new_height > AspectRatio)
            {
                // Too short and wide. Decrease the width.
                new_width = new_height * AspectRatio;
            }
            else
            {
                // Too tall and thin. Decrease the height.
                new_height = new_width / AspectRatio;
            }
            return new SizeF(new_width, new_height);
        }

        private HitTypes FindHitType(Point point)
        {
            RectangleF scaled_rect = ScaledSelectionRectangle();
            bool hit_left, hit_right, hit_top, hit_bottom;
            hit_left = ((point.X >= scaled_rect.Left - HandleRadius) && (point.X <= scaled_rect.Left + HandleRadius));
            hit_right = ((point.X >= scaled_rect.Right - HandleRadius) && (point.X <= scaled_rect.Right + HandleRadius));
            hit_top = ((point.Y >= scaled_rect.Top - HandleRadius) && (point.Y <= scaled_rect.Top + HandleRadius));
            hit_bottom = ((point.Y >= scaled_rect.Bottom - HandleRadius) && (point.Y <= scaled_rect.Bottom + HandleRadius));

            if (hit_left && hit_top)
            {
                return HitTypes.ULCorner;
            }
            if (hit_right && hit_top)
            {
                return HitTypes.URCorner;
            }
            if (hit_left && hit_bottom)
            {
                return HitTypes.LLCorner;
            }
            if (hit_right && hit_bottom)
            {
                return HitTypes.LRCorner;
            }
            if (hit_left)
            {
                return HitTypes.LeftEdge;
            }
            if (hit_right)
            {
                return HitTypes.RightEdge;
            }
            if (hit_top)
            {
                return HitTypes.TopEdge;
            }
            if (hit_bottom)
            {
                return HitTypes.BottomEdge;
            }
            if ((point.X >= scaled_rect.Left) && (point.X <= scaled_rect.Right) && (point.Y >= scaled_rect.Top) && (point.Y <= scaled_rect.Bottom))
            {
                return HitTypes.Body;
            }
            return HitTypes.None;
        }

        // Stop dragging.
        private void picImage_MouseUp(object sender, MouseEventArgs e)
        {
            Dragging = false;
        }

        private void mnuScale_Click(object sender, EventArgs e)
        {
            // Get the scale factor.
            SetScale(sender as ToolStripMenuItem);
        }

        // Set the appropriate scale for this menu item.
        private void SetScale(ToolStripMenuItem menu_item)
        {
            // Get the scale factor.
            string scale_text = menu_item.Text.Replace("&", "").Replace("%", "");

            richTextBox1.Text += scale_text + "\t";

            ImageScale = float.Parse(scale_text) / 100f;

            richTextBox1.Text += ImageScale + "\n";

            ShowScaledImage();
        }

        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                return new Bitmap(bm);
            }
        }

        private void txtAspectRatio_TextChanged(object sender, EventArgs e)
        {
            ReadAspectRatio();
        }

        private void ReadAspectRatio()
        {
            // Get the new aspect ratio.
            string[] fields = txtAspectRatio.Text.Split(':');
            if (fields.Length < 2)
            {
                return;
            }

            if (!float.TryParse(fields[0], out AspectWidth))
            {
                return;
            }
            if (!float.TryParse(fields[1], out AspectHeight))
            {
                return;
            }
            AspectRatio = (float)AspectWidth / (float)AspectHeight;

            // Update the entered height.
            SetWidth(RectWidth);
        }

        private bool IgnoreTextChanged = false;
        private void SetWidth(float width)
        {
            RectHeight = (float)(width / AspectRatio);
            IgnoreTextChanged = true;
            txtHeight.Text = RectHeight.ToString();
            IgnoreTextChanged = false;
            SetSelectionRectangle();
        }
        private void SetHeight(float height)
        {
            RectWidth = (float)(height * AspectRatio);
            IgnoreTextChanged = true;
            txtWidth.Text = RectWidth.ToString();
            IgnoreTextChanged = false;
            SetSelectionRectangle();
        }

        private void txtWidth_TextChanged(object sender, EventArgs e)
        {
            if (IgnoreTextChanged)
            {
                return;
            }
            if (!float.TryParse(txtWidth.Text, out RectWidth))
            {
                return;
            }
            SetWidth(RectWidth);
        }

        private void txtHeight_TextChanged(object sender, EventArgs e)
        {
            if (IgnoreTextChanged)
            {
                return;
            }
            if (!float.TryParse(txtHeight.Text, out RectHeight))
            {
                return;
            }
            SetHeight(RectHeight);
        }

        private void SetSelectionRectangle()
        {
            float cx = SelectionRectangle.X + SelectionRectangle.Width / 2f;
            float cy = SelectionRectangle.Y + SelectionRectangle.Height / 2f;
            SelectionRectangle = new Rectangle((int)(cx - RectWidth / 2f), (int)(cy - RectHeight / 2f), (int)RectWidth, (int)RectHeight);
            picImage.Refresh();
        }

        // Respond to the mouse wheel.
        private void Form_MouseWheel(object sender, MouseEventArgs e)
        {
            if (bitmap1 == null)
            {
                return;
            }

            // Find the current scale.
            int int_scale = (int)(ImageScale * 100);

            // Find the index of the corresponding menu item.
            ToolStripMenuItem[] menu_items =
            {
                mnuScale100,
                mnuScale75,
                mnuScale66,
                mnuScale50,
                mnuScale25,
                mnuScale15,
            };
            List<int> scales = new List<int>() { 100, 75, 66, 50, 25, 15 };
            int index = scales.IndexOf(int_scale);

            // If we're zooming out, move to a smaller scale.
            // Else move to a larger scale.
            if (e.Delta < 0)
            {
                index++;
            }
            else
            {
                index--;
            }

            // Select the new scale menu item.
            if ((index >= 0) && (index < menu_items.Length))
            {
                SetScale(menu_items[index]);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟檔案
            // Load the image.
            bitmap1 = LoadBitmapUnlocked(filename);
            ShowScaledImage();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //選取部分存檔

            try
            {
                // Copy the selected area into a new Bitmap.
                Bitmap bitmap1 = new Bitmap((int)SelectionRectangle.Width, (int)SelectionRectangle.Height);
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    g.DrawImage(bitmap1, 0, 0, SelectionRectangle, GraphicsUnit.Pixel);
                }

                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //100

            ImageScale = 100 / 100f;
            richTextBox1.Text += ImageScale + "\n";
            ShowScaledImage();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //75
            ImageScale = 75 / 100f;
            richTextBox1.Text += ImageScale + "\n";
            ShowScaledImage();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //66
            ImageScale = 66 / 100f;
            richTextBox1.Text += ImageScale + "\n";
            ShowScaledImage();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //50
            ImageScale = 50 / 100f;
            richTextBox1.Text += ImageScale + "\n";
            ShowScaledImage();


        }

        private void button7_Click(object sender, EventArgs e)
        {
            //25
            ImageScale = 25 / 100f;
            richTextBox1.Text += ImageScale + "\n";
            ShowScaledImage();


        }

        private void button8_Click(object sender, EventArgs e)
        {
            //15
            ImageScale = 15 / 100f;
            richTextBox1.Text += ImageScale + "\n";
            ShowScaledImage();
        }
    }
}
