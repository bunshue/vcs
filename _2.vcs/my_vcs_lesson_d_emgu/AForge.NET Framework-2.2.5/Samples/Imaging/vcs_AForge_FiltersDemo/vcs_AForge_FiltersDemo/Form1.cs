using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

using AForge;
using AForge.Imaging;
using AForge.Imaging.Filters;
using AForge.Imaging.Textures;

namespace vcs_AForge_FiltersDemo
{
    public partial class Form1 : Form
    {
        private System.Drawing.Bitmap filteredImage = null;
        private System.Drawing.Bitmap sourceImage = null;

        // Clear current image in picture box
        private void ClearCurrentImage()
        {
            // clear current image from picture box
            pictureBox1.Image = null;

            // free current image
            if (filteredImage != null)
            {
                filteredImage.Dispose();
                filteredImage = null;
            }
        }

        // Apply filter to the source image and show the filtered image
        private void ApplyFilter(IFilter filter)
        {
            ClearCurrentImage();
            // apply filter
            filteredImage = filter.Apply(sourceImage);
            // display filtered image
            pictureBox1.Image = filteredImage;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 740;
            y_st = 10;
            dx = 120;
            dy = 45;

            bt_open.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 0);

            y_st += 70;
            button0.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 0);
            button14.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 1);
            button15.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 2);
            button16.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 3);
            button17.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 4);
            button18.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 5);
            button19.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 7);
            button21.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 8);
            button22.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 9);
            button23.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 10);
            button24.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 11);
            button25.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 12);

            button0.Text = "No Filter";
            button1.Text = "Grayscale";
            button2.Text = "Sepia";
            button3.Text = "Invert";
            button4.Text = "Rotate channel";
            button5.Text = "Color filtering";
            button6.Text = "Levels linear correction";
            button7.Text = "Hue modifier";
            button8.Text = "Saturation adjusting";
            button9.Text = "Brightness adjusting";
            button10.Text = "Contrast adjusting";
            button11.Text = "HSL filtering";
            button12.Text = "YCbCr linear correction";
            button13.Text = "YCbCr filtering";
            button14.Text = "Threshold binarization";
            button15.Text = "Floyd-Steinberg dithering";
            button16.Text = "Ordered dithering";
            button17.Text = "Convolution";
            button18.Text = "Sharpen";
            button19.Text = "Gaussian blur";
            button20.Text = "Difference edge detector";
            button21.Text = "Homogenity edge detector";
            button22.Text = "Sobel edge detector";
            button23.Text = "Jitter";
            button24.Text = "Oil Painting";
            button25.Text = "Texture";

            this.button0.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button1.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button2.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button3.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button4.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button5.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button6.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button7.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button8.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button9.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button10.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button11.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button12.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button13.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button14.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button15.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button16.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button17.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button18.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button19.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button20.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button21.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button22.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button23.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button24.Click += new System.EventHandler(this.bt_filter_select_Click);
            this.button25.Click += new System.EventHandler(this.bt_filter_select_Click);
        }

        private void bt_filter_select_Click(object sender, EventArgs e)
        {
            if (sourceImage == null)
            {
                richTextBox1.Text += "尚未開啟圖片\n";
                return;
            }

            string name = ((Button)sender).Name;
            string text = ((Button)sender).Text;
            richTextBox1.Text += name + "\t" + text + "\n";

            switch (name)
            {
                case "button0":
                    richTextBox1.Text += "On Filters->None item\n";
                    ClearCurrentImage();
                    pictureBox1.Image = sourceImage;
                    break;
                case "button1":
                    richTextBox1.Text += "On Filters->Grayscale item\n";
                    ApplyFilter(Grayscale.CommonAlgorithms.BT709);
                    break;
                case "button2":
                    richTextBox1.Text += "On Filters->Sepia item\n";
                    ApplyFilter(new Sepia());
                    break;
                case "button3":
                    richTextBox1.Text += "On Filters->Invert item\n";
                    ApplyFilter(new Invert());
                    break;
                case "button4":
                    richTextBox1.Text += "On Filters->Rotate Channels item\n";
                    ApplyFilter(new RotateChannels());
                    break;
                case "button5":
                    richTextBox1.Text += "On Filters->Color filtering\n";
                    ApplyFilter(new ColorFiltering(new IntRange(25, 230), new IntRange(25, 230), new IntRange(25, 230)));
                    break;
                case "button6":
                    richTextBox1.Text += "On Filters->Levels Linear Correction\n";
                    LevelsLinear filter = new LevelsLinear();

                    filter.InRed = new IntRange(30, 230);
                    filter.InGreen = new IntRange(50, 240);
                    filter.InBlue = new IntRange(10, 210);

                    ApplyFilter(filter);
                    break;
                case "button7":
                    richTextBox1.Text += "On Filters->Hue modifier\n";
                    ApplyFilter(new HueModifier(50));
                    break;
                case "button8":
                    richTextBox1.Text += "On Filters->Saturation adjusting\n";
                    ApplyFilter(new SaturationCorrection(0.15f));
                    break;
                case "button9":
                    richTextBox1.Text += "On Filters->Brightness adjusting\n";
                    ApplyFilter(new BrightnessCorrection());
                    break;
                case "button10":
                    richTextBox1.Text += "On Filters->Contrast adjusting\n";
                    ApplyFilter(new ContrastCorrection());
                    break;
                case "button11":
                    richTextBox1.Text += "On Filters->HSL filtering\n";
                    ApplyFilter(new HSLFiltering(new IntRange(330, 30), new Range(0, 1), new Range(0, 1)));
                    break;
                case "button12":
                    richTextBox1.Text += "On Filters->YCbCr filtering\n";
                    YCbCrLinear filter2 = new YCbCrLinear();
                    filter2.InCb = new Range(-0.3f, 0.3f);
                    ApplyFilter(filter2);
                    break;
                case "button13":
                    richTextBox1.Text += "On Filters->YCbCr filtering\n";
                    ApplyFilter(new YCbCrFiltering(new Range(0.2f, 0.9f), new Range(-0.3f, 0.3f), new Range(-0.3f, 0.3f)));
                    break;
                case "button14":
                    richTextBox1.Text += "On Filters->Threshold binarization\n";
                    // save original image
                    Bitmap originalImage5 = sourceImage;
                    // get grayscale image
                    sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
                    // apply threshold filter
                    ApplyFilter(new Threshold());
                    // delete grayscale image and restore original
                    sourceImage.Dispose();
                    sourceImage = originalImage5;
                    break;
                case "button15":
                    richTextBox1.Text += "On Filters->Floyd-Steinberg dithering\n";
                    // save original image
                    Bitmap originalImage6 = sourceImage;
                    // get grayscale image
                    sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
                    // apply threshold filter
                    ApplyFilter(new FloydSteinbergDithering());
                    // delete grayscale image and restore original
                    sourceImage.Dispose();
                    sourceImage = originalImage6;
                    break;
                case "button16":
                    richTextBox1.Text += "On Filters->Ordered dithering\n";
                    // save original image
                    Bitmap originalImage7 = sourceImage;
                    // get grayscale image
                    sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
                    // apply threshold filter
                    ApplyFilter(new OrderedDithering());
                    // delete grayscale image and restore original
                    sourceImage.Dispose();
                    sourceImage = originalImage7;
                    break;
                case "button17":
                    richTextBox1.Text += "On Filters->Correlation\n";
                    ApplyFilter(new Convolution(new int[,] {
								{ 1, 2, 3, 2, 1 },
								{ 2, 4, 5, 4, 2 },
								{ 3, 5, 6, 5, 3 },
								{ 2, 4, 5, 4, 2 },
								{ 1, 2, 3, 2, 1 } }));
                    break;
                case "button18":
                    richTextBox1.Text += "On Filters->Sharpen\n";
                    ApplyFilter(new Sharpen());
                    break;
                case "button19":
                    richTextBox1.Text += "On Filters->Gaussin blur\n";
                    ApplyFilter(new GaussianBlur(2.0, 7));
                    break;
                case "button20":
                    richTextBox1.Text += "On Filters->Difference edge detector\n";
                    // save original image
                    Bitmap originalImage9 = sourceImage;
                    // get grayscale image
                    sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
                    // apply edge filter
                    ApplyFilter(new DifferenceEdgeDetector());
                    // delete grayscale image and restore original
                    sourceImage.Dispose();
                    sourceImage = originalImage9;
                    break;
                case "button21":
                    richTextBox1.Text += "On Filters->Homogenity edge detector\n";
                    // save original image
                    Bitmap originalImage10 = sourceImage;
                    // get grayscale image
                    sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
                    // apply edge filter
                    ApplyFilter(new HomogenityEdgeDetector());
                    // delete grayscale image and restore original
                    sourceImage.Dispose();
                    sourceImage = originalImage10;
                    break;
                case "button22":
                    richTextBox1.Text += "On Filters->Sobel edge detector\n";
                    // save original image
                    Bitmap originalImage11 = sourceImage;
                    // get grayscale image
                    sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
                    // apply edge filter
                    ApplyFilter(new SobelEdgeDetector());
                    // delete grayscale image and restore original
                    sourceImage.Dispose();
                    sourceImage = originalImage11;
                    break;
                case "button23":
                    richTextBox1.Text += "On Filters->Jitter\n";
                    ApplyFilter(new Jitter());
                    break;
                case "button24":
                    richTextBox1.Text += "On Filters->Oil Painting\n";
                    ApplyFilter(new OilPainting());
                    break;
                case "button25":
                    richTextBox1.Text += "On Filters->Texture\n";
                    ApplyFilter(new Texturer(new TextileTexture(), 1.0, 0.8));
                    break;
                default:
                    ClearCurrentImage();
                    pictureBox1.Image = sourceImage;
                    break;
            }
        }

        private void bt_open_Click(object sender, EventArgs e)
        {
            try
            {
                // show file open dialog
                openFileDialog.InitialDirectory = @"C:\______test_files1\";
                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    // load image
                    sourceImage = (Bitmap)Bitmap.FromFile(openFileDialog.FileName);

                    // check pixel format
                    if ((sourceImage.PixelFormat == PixelFormat.Format16bppGrayScale) ||
                         (Bitmap.GetPixelFormatSize(sourceImage.PixelFormat) > 32))
                    {
                        MessageBox.Show("The demo application supports only color images.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        // free image
                        sourceImage.Dispose();
                        sourceImage = null;
                    }
                    else
                    {
                        // make sure the image has 24 bpp format
                        if (sourceImage.PixelFormat != PixelFormat.Format24bppRgb)
                        {
                            Bitmap temp = AForge.Imaging.Image.Clone(sourceImage, PixelFormat.Format24bppRgb);
                            sourceImage.Dispose();
                            sourceImage = temp;
                        }
                    }

                    ClearCurrentImage();

                    // display image
                    pictureBox1.Image = sourceImage;
                    //noneFiltersItem.Checked = true;

                    // enable filters menu
                    //filtersItem.Enabled = (sourceImage != null);
                }
            }
            catch
            {
                MessageBox.Show("Failed loading the image", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
