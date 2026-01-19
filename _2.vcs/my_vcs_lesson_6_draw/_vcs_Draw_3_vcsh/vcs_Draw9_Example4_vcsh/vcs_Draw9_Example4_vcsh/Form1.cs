using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

using System.Drawing.Imaging;   //for ImageFormat

using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw9_Example4_vcsh
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        // hit curve
        // The points that define the curve.
        private Point[] Points =
        {
            new Point(213, 204),
            new Point(63, 143),
            new Point(227, 60),
            new Point(123, 222),
            new Point(72, 64),
        };

        // A GraphicsPath to represent the curve.
        GraphicsPath Path = new GraphicsPath();

        // Hits and misses.
        private List<Point> Hits = new List<Point>();
        private List<Point> Misses = new List<Point>();

        //for unique progressbar ST
        // Groups of controls to use as progress bars.
        private Control[] Labels;
        private Control[] ColoredLabels;
        private Control[] SmallLabels;

        // The bitmap displayed for the colors PictureBox.
        private Bitmap ColorsBm;

        // The bitmap displayed for the picture.
        private Bitmap PictureBm;
        //for unique progressbar SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.Red);             //useless??
            pictureBox1.BackColor = Color.Pink;
            show_item_location();

            // Make a GraphicsPath for the curve.
            Path = new GraphicsPath();
            Path.AddCurve(Points);

            //for unique progressbar ST

            // Initialize the control arrays.
            Labels = new Control[] { label1, label2, label3, label4, label5, label6, label7, label8, label9, label10 };
            ColoredLabels = new Control[] { label11, label12, label13, label14, label15, label16, label17, label18, label19, label20 };
            SmallLabels = new Control[] { label21, label22, label23, label24, label25, label26, label27, label28, label29, label30, label31, label32, label33, label34, label35, label36, label37, label38, label39, label40 };

            // Set ColoredLabels colors.
            for (int i = 0; i < ColoredLabels.Length; i++)
            {
                int x = (int)(255f * i / (ColoredLabels.Length - 1f));
                ColoredLabels[i].BackColor = Color.FromArgb(255, 255, x, 0);
            }

            // Hide the control arrays.
            HideControls(Labels);
            HideControls(ColoredLabels);
            HideControls(SmallLabels);

            // Make the color bitmap.
            ColorsBm = new Bitmap(picColors.ClientSize.Width, picColors.ClientSize.Height);
            picColors.Image = ColorsBm;
            picColors.Visible = false;

            // Make the picture bitmap.
            PictureBm = new Bitmap(picHidden.Image.Width, picHidden.Image.Height);
            picVisible.Image = PictureBm;
            //for unique progressbar SP
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 850;
            y_st = 10;
            dx = 110;
            dy = 45;

            bt_save.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            bt_exit.Location = new Point(x_st + dx * 4, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }




        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void pictureBox_hit_curve_MouseClick(object sender, MouseEventArgs e)
        {
            if (PointIsOverCurve(e.Location))
                Hits.Add(e.Location);
            else
                Misses.Add(e.Location);
            Refresh();

        }

        // See if the mouse is over the curve's GraphicsPath.
        private void pictureBox_hit_curve_MouseMove(object sender, MouseEventArgs e)
        {
            if (PointIsOverCurve(e.Location))
                Cursor = Cursors.Cross;
            else
                Cursor = Cursors.Default;

        }

        // Draw the curve.
        private void pictureBox_hit_curve_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawString("點擊曲線", new Font("標楷體", 25), new SolidBrush(Color.Blue), new PointF(30, 10));
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the curve.
            e.Graphics.DrawCurve(Pens.Blue, Points);

            // Draw the hits and misses.
            foreach (Point point in Misses)
                DrawPoint(e.Graphics, Brushes.Pink, Pens.Red, point);
            foreach (Point point in Hits)
                DrawPoint(e.Graphics, Brushes.Lime, Pens.Green, point);
        }

        // Return true if the point is over the curve.
        private bool PointIsOverCurve(Point point)
        {
            // Use a three pixel wide pen.
            using (Pen thick_pen = new Pen(Color.Black, 3))
            {
                return Path.IsOutlineVisible(point, thick_pen);
            }
        }

        // Draw a point.
        private void DrawPoint(Graphics gr, Brush brush, Pen pen, Point point)
        {
            const int radius = 3;
            const int diameter = 2 * radius;
            Rectangle rect = new Rectangle(
                point.X - radius, point.Y - radius,
                diameter, diameter);
            gr.FillEllipse(brush, rect);
            gr.DrawEllipse(pen, rect);
        }

        //for unique progressbar ST

        // Start or stop the timer.
        private void btnGo_Click(object sender, EventArgs e)
        {
            if (btnGo.Text == "Go")
            {
                btnGo.Text = "Reset";

                // Disable the button and enable the timers.
                tmrLabels.Enabled = true;
                tmrColoredLabels.Enabled = true;
                tmrSmallLabels.Enabled = true;
                tmrColorBar.Enabled = true;
                tmrPicture.Enabled = true;

                // Clear the colorbar.
                using (Graphics gr = Graphics.FromImage(ColorsBm))
                {
                    gr.Clear(picColors.BackColor);
                }
                picColors.Visible = true;

                // Display a pale picture.
                using (Graphics gr = Graphics.FromImage(PictureBm))
                {
                    Rectangle rect = new Rectangle(0, 0, PictureBm.Width, PictureBm.Height);
                    using (TextureBrush br = new TextureBrush(picHidden.Image))
                    {
                        gr.FillRectangle(br, rect);
                    }
                    using (SolidBrush br = new SolidBrush(Color.FromArgb(128, 255, 255, 255)))
                    {
                        gr.FillRectangle(br, rect);
                    }
                }
                picVisible.Visible = true;

                this.Cursor = Cursors.WaitCursor;
            }
            else
            {
                btnGo.Text = "Go";
                HideControls(Labels);
                HideControls(ColoredLabels);
                HideControls(SmallLabels);
                picColors.Visible = false;
                picVisible.Visible = false;

                this.Cursor = Cursors.Default;
            }

        }

        // Show progress by displaying some hidden controls.
        private void ShowProgressWithVisible(float value, float max_value, Control[] controls)
        {
            // Calculate the index of the last visible control.
            int last_visible = (int)(controls.Length * value / max_value);

            // Make sure all controls up to this one are visible.
            for (int i = 0; i <= last_visible; i++)
            {
                if (!controls[i].Visible) controls[i].Visible = true;
            }
        }

        // Hide the progress controls.
        private void HideControls(Control[] controls)
        {
            foreach (Control ctl in controls) ctl.Visible = false;
        }

        // Display progress using labels.
        private int ProgressLabels = -1;
        private void tmrLabels_Tick(object sender, EventArgs e)
        {
            // Increment progress and see if we're done.
            if (++ProgressLabels >= Labels.Length)
            {
                // We're done. Stop the timer.
                ProgressLabels = -1;
                tmrLabels.Enabled = false;
                return;
            }

            // Display the progress.
            ShowProgressWithVisible(ProgressLabels, Labels.Length, Labels);
        }

        // Display progress using colored labels.
        private int ProgressColored = -1;
        private void tmrColoredLabels_Tick(object sender, EventArgs e)
        {
            // Increment progress and see if we're done.
            if (++ProgressColored >= ColoredLabels.Length)
            {
                // We're done. Stop the timer.
                ProgressColored = -1;
                tmrColoredLabels.Enabled = false;
                return;
            }

            // Display the progress.
            ShowProgressWithVisible(ProgressColored, ColoredLabels.Length, ColoredLabels);
        }

        // Display the next small label progress indicator.
        private int ProgressSmall = -1;
        private void tmrSmallLabels_Tick(object sender, EventArgs e)
        {
            // Increment progress and see if we're done.
            if (++ProgressSmall >= SmallLabels.Length)
            {
                // We're done. Stop the timer.
                ProgressSmall = -1;
                tmrSmallLabels.Enabled = false;
                this.Cursor = Cursors.Default;
                return;
            }

            // Display the next progress control.
            SmallLabels[ProgressSmall].Visible = true;
        }

        // Display progress with a colored bar.
        private int ProgressColorBar = -1;
        private void tmrColorBar_Tick(object sender, EventArgs e)
        {
            const int max_progress = 20;

            // Increment progress and see if we're done.
            if (++ProgressColorBar >= max_progress)
            {
                // We're done. Stop the timer.
                ProgressColorBar = -1;
                tmrColorBar.Enabled = false;
                return;
            }

            // Display the next chunk of colors.
            using (LinearGradientBrush br = new LinearGradientBrush(
                new Point(0, 0), new Point(ColorsBm.Width, 0), Color.Red, Color.Yellow))
            {
                using (Graphics gr = Graphics.FromImage(ColorsBm))
                {
                    float wid = ColorsBm.Width * ProgressColorBar / (max_progress - 1);
                    float hgt = ColorsBm.Height;
                    RectangleF rect = new RectangleF(0, 0, wid, hgt);
                    gr.FillRectangle(br, rect);
                }
            }
            picColors.Refresh();
        }

        // Display progress with a picture.
        private int ProgressPicture = -1;
        private void tmrPicture_Tick(object sender, EventArgs e)
        {
            const int max_progress = 20;

            // Increment progress and see if we're done.
            if (++ProgressPicture >= max_progress)
            {
                // We're done. Stop the timer.
                ProgressPicture = -1;
                tmrPicture.Enabled = false;
                return;
            }

            // Display the next chunk of picture.
            using (TextureBrush br = new TextureBrush(picHidden.Image))
            {
                using (Graphics gr = Graphics.FromImage(PictureBm))
                {
                    float wid = PictureBm.Width * ProgressPicture / (max_progress - 1);
                    float hgt = PictureBm.Height;
                    RectangleF rect = new RectangleF(0, 0, wid, hgt);
                    gr.FillRectangle(br, rect);
                }
            }
            picVisible.Refresh();
        }




        //for unique progressbar SP




    }
}
