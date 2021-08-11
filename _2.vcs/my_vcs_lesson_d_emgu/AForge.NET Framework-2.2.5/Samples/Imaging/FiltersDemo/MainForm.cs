// Image Processing filters demo
// AForge.NET framework
// http://www.aforgenet.com/framework/
//
// Copyright ?AForge.NET, 2006-2011
// contacts@aforgenet.com
//

using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

using AForge;
using AForge.Imaging;
using AForge.Imaging.Filters;
using AForge.Imaging.Textures;

namespace FiltersDemo
{
    /// <summary>
    /// Summary description for MainForm.
    /// </summary>
    public class MainForm : System.Windows.Forms.Form
    {
        private System.Windows.Forms.MenuItem fileItem;
        private System.Windows.Forms.MenuItem openFileItem;
        private System.Windows.Forms.MenuItem menuItem3;
        private System.Windows.Forms.MenuItem exitFilrItem;
        private System.Windows.Forms.OpenFileDialog openFileDialog;
        private System.Windows.Forms.PictureBox pictureBox;
        private System.Windows.Forms.MainMenu mainMenu;
        private System.Windows.Forms.MenuItem sizeItem;
        private System.Windows.Forms.MenuItem normalSizeItem;
        private System.Windows.Forms.MenuItem stretchedSizeItem;
        private System.Windows.Forms.MenuItem centeredSizeItem;
        private System.Windows.Forms.MenuItem filtersItem;
        private System.Windows.Forms.MenuItem noneFiltersItem;
        private System.Windows.Forms.MenuItem menuItem1;
        private System.Windows.Forms.MenuItem sepiaFiltersItem;
        private System.Windows.Forms.MenuItem invertFiltersItem;
        private System.Windows.Forms.MenuItem rotateChannelFiltersItem;
        private System.Windows.Forms.MenuItem grayscaleFiltersItem;
        private System.Windows.Forms.MenuItem colorFiltersItem;
        private System.Windows.Forms.MenuItem menuItem2;
        private System.Windows.Forms.MenuItem hueModifierFiltersItem;
        private System.Windows.Forms.MenuItem saturationAdjustingFiltersItem;
        private System.Windows.Forms.MenuItem brightnessAdjustingFiltersItem;
        private System.Windows.Forms.MenuItem contrastAdjustingFiltersItem;
        private System.Windows.Forms.MenuItem hslFiltersItem;
        private System.Windows.Forms.MenuItem menuItem4;
        private System.Windows.Forms.MenuItem yCbCrLinearFiltersItem;
        private System.Windows.Forms.MenuItem yCbCrFiltersItem;
        private System.Windows.Forms.MenuItem menuItem5;
        private System.Windows.Forms.MenuItem thresholdFiltersItem;
        private System.Windows.Forms.MenuItem floydFiltersItem;
        private System.Windows.Forms.MenuItem orderedDitheringFiltersItem;
        private System.Windows.Forms.MenuItem menuItem6;
        private System.Windows.Forms.MenuItem convolutionFiltersItem;
        private System.Windows.Forms.MenuItem sharpenFiltersItem;
        private System.Windows.Forms.MenuItem menuItem7;
        private System.Windows.Forms.MenuItem differenceEdgesFiltersItem;
        private System.Windows.Forms.MenuItem homogenityEdgesFiltersItem;
        private System.Windows.Forms.MenuItem sobelEdgesFiltersItem;
        private System.Windows.Forms.MenuItem rgbLinearFiltersItem;
        private System.Windows.Forms.MenuItem menuItem8;
        private System.Windows.Forms.MenuItem jitterFiltersItem;
        private System.Windows.Forms.MenuItem oilFiltersItem;
        private MenuItem gaussianFiltersItem;
        private MenuItem textureFiltersItem;
        private IContainer components;

        private System.Drawing.Bitmap sourceImage;
        private RichTextBox richTextBox1;
        private Button button1;
        private Button button2;
        private Button button3;
        private Button button4;
        private Button button5;
        private Button button6;
        private Button button7;
        private Button button8;
        private Button button9;
        private Button button10;
        private Button button11;
        private Button button12;
        private Button button13;
        private Button button14;
        private Button button15;
        private Button button16;
        private Button button17;
        private Button button18;
        private Button button19;
        private Button button20;
        private Button button21;
        private Button button22;
        private Button button23;
        private Button button24;
        private Button button25;
        private Button button0;
        private System.Drawing.Bitmap filteredImage;

        // Constructor
        public MainForm()
        {
            //
            // Required for Windows Form Designer support
            //
            InitializeComponent();

            // set default size mode of picture box
            pictureBox.SizeMode = PictureBoxSizeMode.StretchImage;
        }

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.mainMenu = new System.Windows.Forms.MainMenu(this.components);
            this.fileItem = new System.Windows.Forms.MenuItem();
            this.openFileItem = new System.Windows.Forms.MenuItem();
            this.menuItem3 = new System.Windows.Forms.MenuItem();
            this.exitFilrItem = new System.Windows.Forms.MenuItem();
            this.filtersItem = new System.Windows.Forms.MenuItem();
            this.noneFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem1 = new System.Windows.Forms.MenuItem();
            this.grayscaleFiltersItem = new System.Windows.Forms.MenuItem();
            this.sepiaFiltersItem = new System.Windows.Forms.MenuItem();
            this.invertFiltersItem = new System.Windows.Forms.MenuItem();
            this.rotateChannelFiltersItem = new System.Windows.Forms.MenuItem();
            this.colorFiltersItem = new System.Windows.Forms.MenuItem();
            this.rgbLinearFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem2 = new System.Windows.Forms.MenuItem();
            this.hueModifierFiltersItem = new System.Windows.Forms.MenuItem();
            this.saturationAdjustingFiltersItem = new System.Windows.Forms.MenuItem();
            this.brightnessAdjustingFiltersItem = new System.Windows.Forms.MenuItem();
            this.contrastAdjustingFiltersItem = new System.Windows.Forms.MenuItem();
            this.hslFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem4 = new System.Windows.Forms.MenuItem();
            this.yCbCrLinearFiltersItem = new System.Windows.Forms.MenuItem();
            this.yCbCrFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem5 = new System.Windows.Forms.MenuItem();
            this.thresholdFiltersItem = new System.Windows.Forms.MenuItem();
            this.floydFiltersItem = new System.Windows.Forms.MenuItem();
            this.orderedDitheringFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem6 = new System.Windows.Forms.MenuItem();
            this.convolutionFiltersItem = new System.Windows.Forms.MenuItem();
            this.sharpenFiltersItem = new System.Windows.Forms.MenuItem();
            this.gaussianFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem7 = new System.Windows.Forms.MenuItem();
            this.differenceEdgesFiltersItem = new System.Windows.Forms.MenuItem();
            this.homogenityEdgesFiltersItem = new System.Windows.Forms.MenuItem();
            this.sobelEdgesFiltersItem = new System.Windows.Forms.MenuItem();
            this.menuItem8 = new System.Windows.Forms.MenuItem();
            this.jitterFiltersItem = new System.Windows.Forms.MenuItem();
            this.oilFiltersItem = new System.Windows.Forms.MenuItem();
            this.textureFiltersItem = new System.Windows.Forms.MenuItem();
            this.sizeItem = new System.Windows.Forms.MenuItem();
            this.normalSizeItem = new System.Windows.Forms.MenuItem();
            this.stretchedSizeItem = new System.Windows.Forms.MenuItem();
            this.centeredSizeItem = new System.Windows.Forms.MenuItem();
            this.openFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.pictureBox = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button16 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.button19 = new System.Windows.Forms.Button();
            this.button20 = new System.Windows.Forms.Button();
            this.button21 = new System.Windows.Forms.Button();
            this.button22 = new System.Windows.Forms.Button();
            this.button23 = new System.Windows.Forms.Button();
            this.button24 = new System.Windows.Forms.Button();
            this.button25 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // mainMenu
            // 
            this.mainMenu.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.fileItem,
            this.filtersItem,
            this.sizeItem});
            // 
            // fileItem
            // 
            this.fileItem.Index = 0;
            this.fileItem.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.openFileItem,
            this.menuItem3,
            this.exitFilrItem});
            this.fileItem.Text = "&File";
            // 
            // openFileItem
            // 
            this.openFileItem.Index = 0;
            this.openFileItem.Shortcut = System.Windows.Forms.Shortcut.CtrlO;
            this.openFileItem.Text = "&Open";
            this.openFileItem.Click += new System.EventHandler(this.openFileItem_Click);
            // 
            // menuItem3
            // 
            this.menuItem3.Index = 1;
            this.menuItem3.Text = "-";
            // 
            // exitFilrItem
            // 
            this.exitFilrItem.Index = 2;
            this.exitFilrItem.Text = "E&xit";
            this.exitFilrItem.Click += new System.EventHandler(this.exitFilrItem_Click);
            // 
            // filtersItem
            // 
            this.filtersItem.Enabled = false;
            this.filtersItem.Index = 1;
            this.filtersItem.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.noneFiltersItem,
            this.menuItem1,
            this.grayscaleFiltersItem,
            this.sepiaFiltersItem,
            this.invertFiltersItem,
            this.rotateChannelFiltersItem,
            this.colorFiltersItem,
            this.rgbLinearFiltersItem,
            this.menuItem2,
            this.hueModifierFiltersItem,
            this.saturationAdjustingFiltersItem,
            this.brightnessAdjustingFiltersItem,
            this.contrastAdjustingFiltersItem,
            this.hslFiltersItem,
            this.menuItem4,
            this.yCbCrLinearFiltersItem,
            this.yCbCrFiltersItem,
            this.menuItem5,
            this.thresholdFiltersItem,
            this.floydFiltersItem,
            this.orderedDitheringFiltersItem,
            this.menuItem6,
            this.convolutionFiltersItem,
            this.sharpenFiltersItem,
            this.gaussianFiltersItem,
            this.menuItem7,
            this.differenceEdgesFiltersItem,
            this.homogenityEdgesFiltersItem,
            this.sobelEdgesFiltersItem,
            this.menuItem8,
            this.jitterFiltersItem,
            this.oilFiltersItem,
            this.textureFiltersItem});
            this.filtersItem.Text = "Fi&lters";
            // 
            // noneFiltersItem
            // 
            this.noneFiltersItem.Index = 0;
            this.noneFiltersItem.Text = "&None";
            this.noneFiltersItem.Click += new System.EventHandler(this.noneFiltersItem_Click);
            // 
            // menuItem1
            // 
            this.menuItem1.Index = 1;
            this.menuItem1.Text = "-";
            // 
            // grayscaleFiltersItem
            // 
            this.grayscaleFiltersItem.Index = 2;
            this.grayscaleFiltersItem.Text = "&Grayscale";
            this.grayscaleFiltersItem.Click += new System.EventHandler(this.grayscaleFiltersItem_Click);
            // 
            // sepiaFiltersItem
            // 
            this.sepiaFiltersItem.Index = 3;
            this.sepiaFiltersItem.Text = "&Sepia";
            this.sepiaFiltersItem.Click += new System.EventHandler(this.sepiaFiltersItem_Click);
            // 
            // invertFiltersItem
            // 
            this.invertFiltersItem.Index = 4;
            this.invertFiltersItem.Text = "&Invert";
            this.invertFiltersItem.Click += new System.EventHandler(this.invertFiltersItem_Click);
            // 
            // rotateChannelFiltersItem
            // 
            this.rotateChannelFiltersItem.Index = 5;
            this.rotateChannelFiltersItem.Text = "&Rotate channel";
            this.rotateChannelFiltersItem.Click += new System.EventHandler(this.rotateChannelFiltersItem_Click);
            // 
            // colorFiltersItem
            // 
            this.colorFiltersItem.Index = 6;
            this.colorFiltersItem.Text = "Color filtering";
            this.colorFiltersItem.Click += new System.EventHandler(this.colorFiltersItem_Click);
            // 
            // rgbLinearFiltersItem
            // 
            this.rgbLinearFiltersItem.Index = 7;
            this.rgbLinearFiltersItem.Text = "Levels linear correction";
            this.rgbLinearFiltersItem.Click += new System.EventHandler(this.rgbLinearFiltersItem_Click);
            // 
            // menuItem2
            // 
            this.menuItem2.Index = 8;
            this.menuItem2.Text = "-";
            // 
            // hueModifierFiltersItem
            // 
            this.hueModifierFiltersItem.Index = 9;
            this.hueModifierFiltersItem.Text = "Hue modifier";
            this.hueModifierFiltersItem.Click += new System.EventHandler(this.hueModifierFiltersItem_Click);
            // 
            // saturationAdjustingFiltersItem
            // 
            this.saturationAdjustingFiltersItem.Index = 10;
            this.saturationAdjustingFiltersItem.Text = "Saturation adjusting";
            this.saturationAdjustingFiltersItem.Click += new System.EventHandler(this.saturationAdjustingFiltersItem_Click);
            // 
            // brightnessAdjustingFiltersItem
            // 
            this.brightnessAdjustingFiltersItem.Index = 11;
            this.brightnessAdjustingFiltersItem.Text = "Brightness adjusting";
            this.brightnessAdjustingFiltersItem.Click += new System.EventHandler(this.brightnessAdjustingFiltersItem_Click);
            // 
            // contrastAdjustingFiltersItem
            // 
            this.contrastAdjustingFiltersItem.Index = 12;
            this.contrastAdjustingFiltersItem.Text = "Contrast adjusting";
            this.contrastAdjustingFiltersItem.Click += new System.EventHandler(this.contrastAdjustingFiltersItem_Click);
            // 
            // hslFiltersItem
            // 
            this.hslFiltersItem.Index = 13;
            this.hslFiltersItem.Text = "HSL filtering";
            this.hslFiltersItem.Click += new System.EventHandler(this.hslFiltersItem_Click);
            // 
            // menuItem4
            // 
            this.menuItem4.Index = 14;
            this.menuItem4.Text = "-";
            // 
            // yCbCrLinearFiltersItem
            // 
            this.yCbCrLinearFiltersItem.Index = 15;
            this.yCbCrLinearFiltersItem.Text = "YCbCr linear correction";
            this.yCbCrLinearFiltersItem.Click += new System.EventHandler(this.yCbCrLinearFiltersItem_Click);
            // 
            // yCbCrFiltersItem
            // 
            this.yCbCrFiltersItem.Index = 16;
            this.yCbCrFiltersItem.Text = "YCbCr filtering";
            this.yCbCrFiltersItem.Click += new System.EventHandler(this.yCbCrFiltersItem_Click);
            // 
            // menuItem5
            // 
            this.menuItem5.Index = 17;
            this.menuItem5.Text = "-";
            // 
            // thresholdFiltersItem
            // 
            this.thresholdFiltersItem.Index = 18;
            this.thresholdFiltersItem.Text = "Threshold &binarization";
            this.thresholdFiltersItem.Click += new System.EventHandler(this.thresholdFiltersItem_Click);
            // 
            // floydFiltersItem
            // 
            this.floydFiltersItem.Index = 19;
            this.floydFiltersItem.Text = "Floyd-Steinberg dithering";
            this.floydFiltersItem.Click += new System.EventHandler(this.floydFiltersItem_Click);
            // 
            // orderedDitheringFiltersItem
            // 
            this.orderedDitheringFiltersItem.Index = 20;
            this.orderedDitheringFiltersItem.Text = "Ordered dithering";
            this.orderedDitheringFiltersItem.Click += new System.EventHandler(this.orderedDitheringFiltersItem_Click);
            // 
            // menuItem6
            // 
            this.menuItem6.Index = 21;
            this.menuItem6.Text = "-";
            // 
            // convolutionFiltersItem
            // 
            this.convolutionFiltersItem.Index = 22;
            this.convolutionFiltersItem.Text = "Convolution";
            this.convolutionFiltersItem.Click += new System.EventHandler(this.convolutionFiltersItem_Click);
            // 
            // sharpenFiltersItem
            // 
            this.sharpenFiltersItem.Index = 23;
            this.sharpenFiltersItem.Text = "Sharpen";
            this.sharpenFiltersItem.Click += new System.EventHandler(this.sharpenFiltersItem_Click);
            // 
            // gaussianFiltersItem
            // 
            this.gaussianFiltersItem.Index = 24;
            this.gaussianFiltersItem.Text = "Gaussian blur";
            this.gaussianFiltersItem.Click += new System.EventHandler(this.gaussianFiltersItem_Click);
            // 
            // menuItem7
            // 
            this.menuItem7.Index = 25;
            this.menuItem7.Text = "-";
            // 
            // differenceEdgesFiltersItem
            // 
            this.differenceEdgesFiltersItem.Index = 26;
            this.differenceEdgesFiltersItem.Text = "Difference edge detector";
            this.differenceEdgesFiltersItem.Click += new System.EventHandler(this.differenceEdgesFiltersItem_Click);
            // 
            // homogenityEdgesFiltersItem
            // 
            this.homogenityEdgesFiltersItem.Index = 27;
            this.homogenityEdgesFiltersItem.Text = "Homogenity edge detector";
            this.homogenityEdgesFiltersItem.Click += new System.EventHandler(this.homogenityEdgesFiltersItem_Click);
            // 
            // sobelEdgesFiltersItem
            // 
            this.sobelEdgesFiltersItem.Index = 28;
            this.sobelEdgesFiltersItem.Text = "Sobel edge detector";
            this.sobelEdgesFiltersItem.Click += new System.EventHandler(this.sobelEdgesFiltersItem_Click);
            // 
            // menuItem8
            // 
            this.menuItem8.Index = 29;
            this.menuItem8.Text = "-";
            // 
            // jitterFiltersItem
            // 
            this.jitterFiltersItem.Index = 30;
            this.jitterFiltersItem.Text = "Jitter";
            this.jitterFiltersItem.Click += new System.EventHandler(this.jitterFiltersItem_Click);
            // 
            // oilFiltersItem
            // 
            this.oilFiltersItem.Index = 31;
            this.oilFiltersItem.Text = "Oil Painting";
            this.oilFiltersItem.Click += new System.EventHandler(this.oilFiltersItem_Click);
            // 
            // textureFiltersItem
            // 
            this.textureFiltersItem.Index = 32;
            this.textureFiltersItem.Text = "Texture";
            this.textureFiltersItem.Click += new System.EventHandler(this.textureFiltersItem_Click);
            // 
            // sizeItem
            // 
            this.sizeItem.Index = 2;
            this.sizeItem.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.normalSizeItem,
            this.stretchedSizeItem,
            this.centeredSizeItem});
            this.sizeItem.Text = "&Size mode";
            this.sizeItem.Popup += new System.EventHandler(this.sizeItem_Popup);
            // 
            // normalSizeItem
            // 
            this.normalSizeItem.Index = 0;
            this.normalSizeItem.Text = "&Normal";
            this.normalSizeItem.Click += new System.EventHandler(this.normalSizeItem_Click);
            // 
            // stretchedSizeItem
            // 
            this.stretchedSizeItem.Index = 1;
            this.stretchedSizeItem.Text = "&Stretched";
            this.stretchedSizeItem.Click += new System.EventHandler(this.stretchedSizeItem_Click);
            // 
            // centeredSizeItem
            // 
            this.centeredSizeItem.Index = 2;
            this.centeredSizeItem.Text = "&Centered";
            this.centeredSizeItem.Click += new System.EventHandler(this.centeredSizeItem_Click);
            // 
            // openFileDialog
            // 
            this.openFileDialog.Filter = "Image files (*.jpg,*.png,*.tif,*.bmp,*.gif)|*.jpg;*.png;*.tif;*.bmp;*.gif|JPG fil" +
                "es (*.jpg)|*.jpg|PNG files (*.png)|*.png|TIF files (*.tif)|*.tif|BMP files (*.bm" +
                "p)|*.bmp|GIF files (*.gif)|*.gif";
            this.openFileDialog.Title = "Open image";
            // 
            // pictureBox
            // 
            this.pictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox.Location = new System.Drawing.Point(6, 6);
            this.pictureBox.Name = "pictureBox";
            this.pictureBox.Size = new System.Drawing.Size(730, 641);
            this.pictureBox.TabIndex = 0;
            this.pictureBox.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1008, 6);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(165, 550);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(755, 33);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(110, 40);
            this.button1.TabIndex = 2;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(755, 62);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(110, 40);
            this.button2.TabIndex = 3;
            this.button2.Text = "button2";
            this.button2.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(755, 91);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(110, 40);
            this.button3.TabIndex = 4;
            this.button3.Text = "button3";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(755, 120);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(110, 40);
            this.button4.TabIndex = 5;
            this.button4.Text = "button4";
            this.button4.UseVisualStyleBackColor = true;
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(755, 149);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(110, 40);
            this.button5.TabIndex = 6;
            this.button5.Text = "button5";
            this.button5.UseVisualStyleBackColor = true;
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(755, 178);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(110, 40);
            this.button6.TabIndex = 7;
            this.button6.Text = "button6";
            this.button6.UseVisualStyleBackColor = true;
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(755, 207);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(110, 40);
            this.button7.TabIndex = 8;
            this.button7.Text = "button7";
            this.button7.UseVisualStyleBackColor = true;
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(755, 236);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(110, 40);
            this.button8.TabIndex = 9;
            this.button8.Text = "button8";
            this.button8.UseVisualStyleBackColor = true;
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(755, 265);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(110, 40);
            this.button9.TabIndex = 10;
            this.button9.Text = "button9";
            this.button9.UseVisualStyleBackColor = true;
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(755, 294);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(110, 40);
            this.button10.TabIndex = 11;
            this.button10.Text = "button10";
            this.button10.UseVisualStyleBackColor = true;
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(755, 323);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(110, 40);
            this.button11.TabIndex = 12;
            this.button11.Text = "button11";
            this.button11.UseVisualStyleBackColor = true;
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(755, 352);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(110, 40);
            this.button12.TabIndex = 13;
            this.button12.Text = "button12";
            this.button12.UseVisualStyleBackColor = true;
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(892, 2);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(110, 40);
            this.button13.TabIndex = 14;
            this.button13.Text = "button13";
            this.button13.UseVisualStyleBackColor = true;
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(892, 31);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(110, 40);
            this.button14.TabIndex = 15;
            this.button14.Text = "button14";
            this.button14.UseVisualStyleBackColor = true;
            // 
            // button15
            // 
            this.button15.Location = new System.Drawing.Point(892, 62);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(110, 40);
            this.button15.TabIndex = 16;
            this.button15.Text = "button15";
            this.button15.UseVisualStyleBackColor = true;
            // 
            // button16
            // 
            this.button16.Location = new System.Drawing.Point(892, 91);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(110, 40);
            this.button16.TabIndex = 17;
            this.button16.Text = "button16";
            this.button16.UseVisualStyleBackColor = true;
            // 
            // button17
            // 
            this.button17.Location = new System.Drawing.Point(892, 120);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(110, 40);
            this.button17.TabIndex = 18;
            this.button17.Text = "button17";
            this.button17.UseVisualStyleBackColor = true;
            // 
            // button18
            // 
            this.button18.Location = new System.Drawing.Point(892, 149);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(110, 40);
            this.button18.TabIndex = 19;
            this.button18.Text = "button18";
            this.button18.UseVisualStyleBackColor = true;
            // 
            // button19
            // 
            this.button19.Location = new System.Drawing.Point(892, 178);
            this.button19.Name = "button19";
            this.button19.Size = new System.Drawing.Size(110, 40);
            this.button19.TabIndex = 20;
            this.button19.Text = "button19";
            this.button19.UseVisualStyleBackColor = true;
            // 
            // button20
            // 
            this.button20.Location = new System.Drawing.Point(892, 207);
            this.button20.Name = "button20";
            this.button20.Size = new System.Drawing.Size(110, 40);
            this.button20.TabIndex = 21;
            this.button20.Text = "button20";
            this.button20.UseVisualStyleBackColor = true;
            // 
            // button21
            // 
            this.button21.Location = new System.Drawing.Point(892, 236);
            this.button21.Name = "button21";
            this.button21.Size = new System.Drawing.Size(110, 40);
            this.button21.TabIndex = 22;
            this.button21.Text = "button21";
            this.button21.UseVisualStyleBackColor = true;
            // 
            // button22
            // 
            this.button22.Location = new System.Drawing.Point(892, 265);
            this.button22.Name = "button22";
            this.button22.Size = new System.Drawing.Size(110, 40);
            this.button22.TabIndex = 23;
            this.button22.Text = "button22";
            this.button22.UseVisualStyleBackColor = true;
            // 
            // button23
            // 
            this.button23.Location = new System.Drawing.Point(892, 294);
            this.button23.Name = "button23";
            this.button23.Size = new System.Drawing.Size(110, 40);
            this.button23.TabIndex = 24;
            this.button23.Text = "button23";
            this.button23.UseVisualStyleBackColor = true;
            // 
            // button24
            // 
            this.button24.Location = new System.Drawing.Point(892, 323);
            this.button24.Name = "button24";
            this.button24.Size = new System.Drawing.Size(110, 40);
            this.button24.TabIndex = 25;
            this.button24.Text = "button24";
            this.button24.UseVisualStyleBackColor = true;
            // 
            // button25
            // 
            this.button25.Location = new System.Drawing.Point(892, 352);
            this.button25.Name = "button25";
            this.button25.Size = new System.Drawing.Size(110, 40);
            this.button25.TabIndex = 26;
            this.button25.Text = "button25";
            this.button25.UseVisualStyleBackColor = true;
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(755, 4);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(110, 40);
            this.button0.TabIndex = 27;
            this.button0.Text = "button26";
            this.button0.UseVisualStyleBackColor = true;
            // 
            // MainForm
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(1185, 653);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button25);
            this.Controls.Add(this.button24);
            this.Controls.Add(this.button23);
            this.Controls.Add(this.button22);
            this.Controls.Add(this.button21);
            this.Controls.Add(this.button20);
            this.Controls.Add(this.button19);
            this.Controls.Add(this.button18);
            this.Controls.Add(this.button17);
            this.Controls.Add(this.button16);
            this.Controls.Add(this.button15);
            this.Controls.Add(this.button14);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox);
            this.Menu = this.mainMenu;
            this.MinimumSize = new System.Drawing.Size(320, 277);
            this.Name = "MainForm";
            this.Text = "Image Processing filters demo";
            this.Load += new System.EventHandler(this.MainForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).EndInit();
            this.ResumeLayout(false);

        }
        #endregion

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.Run(new MainForm());
        }

        // On File->Exit menu item
        private void exitFilrItem_Click(object sender, System.EventArgs e)
        {
            Application.Exit();
        }

        // On File->Open menu item
        private void openFileItem_Click(object sender, System.EventArgs e)
        {
            try
            {
                // show file open dialog
                openFileDialog.InitialDirectory = @"C:\______test_files\";
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
                    pictureBox.Image = sourceImage;
                    noneFiltersItem.Checked = true;

                    // enable filters menu
                    filtersItem.Enabled = (sourceImage != null);
                }
            }
            catch
            {
                MessageBox.Show("Failed loading the image", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        // On Size mode->Normal menu item
        private void normalSizeItem_Click(object sender, System.EventArgs e)
        {
            pictureBox.SizeMode = PictureBoxSizeMode.Normal;
        }

        // On Size mode->Stretched menu item
        private void stretchedSizeItem_Click(object sender, System.EventArgs e)
        {
            pictureBox.SizeMode = PictureBoxSizeMode.StretchImage;
        }

        // On Size mode->Centered size menu item
        private void centeredSizeItem_Click(object sender, System.EventArgs e)
        {
            pictureBox.SizeMode = PictureBoxSizeMode.CenterImage;
        }

        // On Size menu item popup
        private void sizeItem_Popup(object sender, System.EventArgs e)
        {
            normalSizeItem.Checked = (pictureBox.SizeMode == PictureBoxSizeMode.Normal);
            stretchedSizeItem.Checked = (pictureBox.SizeMode == PictureBoxSizeMode.StretchImage);
            centeredSizeItem.Checked = (pictureBox.SizeMode == PictureBoxSizeMode.CenterImage);
        }

        // Clear current image in picture box
        private void ClearCurrentImage()
        {
            // clear current image from picture box
            pictureBox.Image = null;
            // free current image
            if ((noneFiltersItem.Checked == false) && (filteredImage != null))
            {
                filteredImage.Dispose();
                filteredImage = null;
            }
            // uncheck all menu items
            foreach (MenuItem item in filtersItem.MenuItems)
                item.Checked = false;
        }

        // Apply filter to the source image and show the filtered image
        private void ApplyFilter(IFilter filter)
        {
            ClearCurrentImage();
            // apply filter
            filteredImage = filter.Apply(sourceImage);
            // display filtered image
            pictureBox.Image = filteredImage;
        }

        // On Filters->None item
        private void noneFiltersItem_Click(object sender, System.EventArgs e)
        {
            ClearCurrentImage();
            // display source image
            pictureBox.Image = sourceImage;
            noneFiltersItem.Checked = true;
        }

        // On Filters->Grayscale item
        private void grayscaleFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(Grayscale.CommonAlgorithms.BT709);
            grayscaleFiltersItem.Checked = true;
        }

        // On Filters->Sepia item
        private void sepiaFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new Sepia());
            sepiaFiltersItem.Checked = true;
        }

        // On Filters->Invert item
        private void invertFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new Invert());
            invertFiltersItem.Checked = true;
        }

        // On Filters->Rotate Channels item
        private void rotateChannelFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new RotateChannels());
            rotateChannelFiltersItem.Checked = true;
        }

        // On Filters->Color filtering
        private void colorFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new ColorFiltering(new IntRange(25, 230), new IntRange(25, 230), new IntRange(25, 230)));
            colorFiltersItem.Checked = true;
        }

        // On Filters->Hue modifier
        private void hueModifierFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new HueModifier(50));
            hueModifierFiltersItem.Checked = true;
        }

        // On Filters->Saturation adjusting
        private void saturationAdjustingFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new SaturationCorrection(0.15f));
            saturationAdjustingFiltersItem.Checked = true;
        }

        // On Filters->Brightness adjusting
        private void brightnessAdjustingFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new BrightnessCorrection());
            brightnessAdjustingFiltersItem.Checked = true;
        }

        // On Filters->Contrast adjusting
        private void contrastAdjustingFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new ContrastCorrection());
            contrastAdjustingFiltersItem.Checked = true;
        }

        // On Filters->HSL filtering
        private void hslFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new HSLFiltering(new IntRange(330, 30), new Range(0, 1), new Range(0, 1)));
            hslFiltersItem.Checked = true;
        }

        // On Filters->YCbCr filtering
        private void yCbCrLinearFiltersItem_Click(object sender, System.EventArgs e)
        {
            YCbCrLinear filter = new YCbCrLinear();

            filter.InCb = new Range(-0.3f, 0.3f);

            ApplyFilter(filter);
            yCbCrLinearFiltersItem.Checked = true;
        }

        // On Filters->YCbCr filtering
        private void yCbCrFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new YCbCrFiltering(new Range(0.2f, 0.9f), new Range(-0.3f, 0.3f), new Range(-0.3f, 0.3f)));
            yCbCrFiltersItem.Checked = true;
        }

        // On Filters->Threshold binarization
        private void thresholdFiltersItem_Click(object sender, System.EventArgs e)
        {
            // save original image
            Bitmap originalImage = sourceImage;
            // get grayscale image
            sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
            // apply threshold filter
            ApplyFilter(new Threshold());
            // delete grayscale image and restore original
            sourceImage.Dispose();
            sourceImage = originalImage;

            thresholdFiltersItem.Checked = true;
        }

        // On Filters->Floyd-Steinberg dithering
        private void floydFiltersItem_Click(object sender, System.EventArgs e)
        {
            // save original image
            Bitmap originalImage = sourceImage;
            // get grayscale image
            sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
            // apply threshold filter
            ApplyFilter(new FloydSteinbergDithering());
            // delete grayscale image and restore original
            sourceImage.Dispose();
            sourceImage = originalImage;

            floydFiltersItem.Checked = true;
        }

        // On Filters->Ordered dithering
        private void orderedDitheringFiltersItem_Click(object sender, System.EventArgs e)
        {
            // save original image
            Bitmap originalImage = sourceImage;
            // get grayscale image
            sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
            // apply threshold filter
            ApplyFilter(new OrderedDithering());
            // delete grayscale image and restore original
            sourceImage.Dispose();
            sourceImage = originalImage;

            orderedDitheringFiltersItem.Checked = true;
        }

        // On Filters->Correlation
        private void convolutionFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new Convolution(new int[,] {
								{ 1, 2, 3, 2, 1 },
								{ 2, 4, 5, 4, 2 },
								{ 3, 5, 6, 5, 3 },
								{ 2, 4, 5, 4, 2 },
								{ 1, 2, 3, 2, 1 } }));
            convolutionFiltersItem.Checked = true;
        }

        // On Filters->Sharpen
        private void sharpenFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new Sharpen());
            sharpenFiltersItem.Checked = true;
        }

        // On Filters->Difference edge detector
        private void differenceEdgesFiltersItem_Click(object sender, System.EventArgs e)
        {
            // save original image
            Bitmap originalImage = sourceImage;
            // get grayscale image
            sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
            // apply edge filter
            ApplyFilter(new DifferenceEdgeDetector());
            // delete grayscale image and restore original
            sourceImage.Dispose();
            sourceImage = originalImage;

            differenceEdgesFiltersItem.Checked = true;
        }

        // On Filters->Homogenity edge detector
        private void homogenityEdgesFiltersItem_Click(object sender, System.EventArgs e)
        {
            // save original image
            Bitmap originalImage = sourceImage;
            // get grayscale image
            sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
            // apply edge filter
            ApplyFilter(new HomogenityEdgeDetector());
            // delete grayscale image and restore original
            sourceImage.Dispose();
            sourceImage = originalImage;

            homogenityEdgesFiltersItem.Checked = true;
        }

        // On Filters->Sobel edge detector
        private void sobelEdgesFiltersItem_Click(object sender, System.EventArgs e)
        {
            // save original image
            Bitmap originalImage = sourceImage;
            // get grayscale image
            sourceImage = Grayscale.CommonAlgorithms.RMY.Apply(sourceImage);
            // apply edge filter
            ApplyFilter(new SobelEdgeDetector());
            // delete grayscale image and restore original
            sourceImage.Dispose();
            sourceImage = originalImage;

            sobelEdgesFiltersItem.Checked = true;
        }

        // On Filters->Levels Linear Correction
        private void rgbLinearFiltersItem_Click(object sender, System.EventArgs e)
        {
            LevelsLinear filter = new LevelsLinear();

            filter.InRed = new IntRange(30, 230);
            filter.InGreen = new IntRange(50, 240);
            filter.InBlue = new IntRange(10, 210);

            ApplyFilter(filter);
            rgbLinearFiltersItem.Checked = true;
        }

        // On Filters->Jitter
        private void jitterFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new Jitter());
            jitterFiltersItem.Checked = true;
        }

        // On Filters->Oil Painting
        private void oilFiltersItem_Click(object sender, System.EventArgs e)
        {
            ApplyFilter(new OilPainting());
            oilFiltersItem.Checked = true;
        }

        // On Filters->Gaussin blur
        private void gaussianFiltersItem_Click(object sender, EventArgs e)
        {
            ApplyFilter(new GaussianBlur(2.0, 7));
            gaussianFiltersItem.Checked = true;
        }

        // On Filters->Texture
        private void textureFiltersItem_Click(object sender, EventArgs e)
        {
            ApplyFilter(new Texturer(new TextileTexture(), 1.0, 0.8));
            textureFiltersItem.Checked = true;
        }

        private void MainForm_Load(object sender, EventArgs e)
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
            string name = ((Button)sender).Name;
            string text = ((Button)sender).Text;
            richTextBox1.Text += name + "\t" + text + "\n";

            switch (name)
            {
                case "button0":
                    richTextBox1.Text += "On Filters->None item\n";
                    ClearCurrentImage();
                    pictureBox.Image = sourceImage;
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
                    /*
                    richTextBox1.Text += "On Filters->YCbCr filtering\n";
                    YCbCrLinear filter = new YCbCrLinear();
                    filter.InCb = new Range(-0.3f, 0.3f);
                    ApplyFilter(filter);
                    */
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
                    pictureBox.Image = sourceImage;
                    break;
            }
        }
    }
}
