namespace vcs_Draw3B
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer_random_color = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_spiral = new System.Windows.Forms.PictureBox();
            this.pictureBox_ellipse = new System.Windows.Forms.PictureBox();
            this.timer_draw_ellipse = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_star = new System.Windows.Forms.PictureBox();
            this.timer_draw_star = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_polygon = new System.Windows.Forms.PictureBox();
            this.timer_draw_polygon = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_captcha3 = new System.Windows.Forms.PictureBox();
            this.pictureBox_captcha2 = new System.Windows.Forms.PictureBox();
            this.pictureBox_captcha1 = new System.Windows.Forms.PictureBox();
            this.timer_draw_captcha = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_rectangle = new System.Windows.Forms.PictureBox();
            this.timer_draw_rectangle = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_random_pixel_image = new System.Windows.Forms.PictureBox();
            this.timer_random_pixel_image = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_progressbar = new System.Windows.Forms.PictureBox();
            this.timer_progressbar = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_word = new System.Windows.Forms.PictureBox();
            this.timer_word = new System.Windows.Forms.Timer(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox_compass1 = new System.Windows.Forms.PictureBox();
            this.pictureBox_compass2 = new System.Windows.Forms.PictureBox();
            this.lblDegrees = new System.Windows.Forms.Label();
            this.hbarDegrees = new System.Windows.Forms.HScrollBar();
            this.timer_compass = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_brown = new System.Windows.Forms.PictureBox();
            this.timer_brown = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spiral)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_ellipse)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_star)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_polygon)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_rectangle)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_random_pixel_image)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_progressbar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_word)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_compass1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_compass2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_brown)).BeginInit();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1316, 537);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(70, 30);
            this.bt_clear.TabIndex = 54;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1063, 394);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(323, 211);
            this.richTextBox1.TabIndex = 53;
            this.richTextBox1.Text = "";
            // 
            // timer_random_color
            // 
            this.timer_random_color.Tick += new System.EventHandler(this.timer_random_color_Tick);
            // 
            // pictureBox_spiral
            // 
            this.pictureBox_spiral.BackColor = System.Drawing.Color.Pink;
            this.pictureBox_spiral.Location = new System.Drawing.Point(12, 12);
            this.pictureBox_spiral.Name = "pictureBox_spiral";
            this.pictureBox_spiral.Size = new System.Drawing.Size(250, 250);
            this.pictureBox_spiral.TabIndex = 55;
            this.pictureBox_spiral.TabStop = false;
            // 
            // pictureBox_ellipse
            // 
            this.pictureBox_ellipse.Location = new System.Drawing.Point(287, 12);
            this.pictureBox_ellipse.Name = "pictureBox_ellipse";
            this.pictureBox_ellipse.Size = new System.Drawing.Size(350, 200);
            this.pictureBox_ellipse.TabIndex = 56;
            this.pictureBox_ellipse.TabStop = false;
            // 
            // timer_draw_ellipse
            // 
            this.timer_draw_ellipse.Enabled = true;
            this.timer_draw_ellipse.Interval = 1000;
            this.timer_draw_ellipse.Tick += new System.EventHandler(this.timer_draw_ellipse_Tick);
            // 
            // pictureBox_star
            // 
            this.pictureBox_star.BackColor = System.Drawing.Color.White;
            this.pictureBox_star.Location = new System.Drawing.Point(657, 12);
            this.pictureBox_star.Name = "pictureBox_star";
            this.pictureBox_star.Size = new System.Drawing.Size(121, 118);
            this.pictureBox_star.TabIndex = 57;
            this.pictureBox_star.TabStop = false;
            // 
            // timer_draw_star
            // 
            this.timer_draw_star.Enabled = true;
            this.timer_draw_star.Interval = 1000;
            this.timer_draw_star.Tick += new System.EventHandler(this.timer_draw_star_Tick);
            // 
            // pictureBox_polygon
            // 
            this.pictureBox_polygon.BackColor = System.Drawing.Color.White;
            this.pictureBox_polygon.Location = new System.Drawing.Point(784, 12);
            this.pictureBox_polygon.Name = "pictureBox_polygon";
            this.pictureBox_polygon.Size = new System.Drawing.Size(112, 118);
            this.pictureBox_polygon.TabIndex = 58;
            this.pictureBox_polygon.TabStop = false;
            // 
            // timer_draw_polygon
            // 
            this.timer_draw_polygon.Enabled = true;
            this.timer_draw_polygon.Interval = 1000;
            this.timer_draw_polygon.Tick += new System.EventHandler(this.timer_draw_polygon_Tick);
            // 
            // pictureBox_captcha3
            // 
            this.pictureBox_captcha3.BackColor = System.Drawing.Color.Pink;
            this.pictureBox_captcha3.Location = new System.Drawing.Point(12, 568);
            this.pictureBox_captcha3.Name = "pictureBox_captcha3";
            this.pictureBox_captcha3.Size = new System.Drawing.Size(300, 100);
            this.pictureBox_captcha3.TabIndex = 61;
            this.pictureBox_captcha3.TabStop = false;
            // 
            // pictureBox_captcha2
            // 
            this.pictureBox_captcha2.BackColor = System.Drawing.Color.Pink;
            this.pictureBox_captcha2.Location = new System.Drawing.Point(12, 462);
            this.pictureBox_captcha2.Name = "pictureBox_captcha2";
            this.pictureBox_captcha2.Size = new System.Drawing.Size(300, 100);
            this.pictureBox_captcha2.TabIndex = 60;
            this.pictureBox_captcha2.TabStop = false;
            // 
            // pictureBox_captcha1
            // 
            this.pictureBox_captcha1.BackColor = System.Drawing.Color.Pink;
            this.pictureBox_captcha1.Location = new System.Drawing.Point(12, 356);
            this.pictureBox_captcha1.Name = "pictureBox_captcha1";
            this.pictureBox_captcha1.Size = new System.Drawing.Size(300, 100);
            this.pictureBox_captcha1.TabIndex = 59;
            this.pictureBox_captcha1.TabStop = false;
            // 
            // timer_draw_captcha
            // 
            this.timer_draw_captcha.Enabled = true;
            this.timer_draw_captcha.Interval = 1000;
            this.timer_draw_captcha.Tick += new System.EventHandler(this.timer_draw_captcha_Tick);
            // 
            // pictureBox_rectangle
            // 
            this.pictureBox_rectangle.Location = new System.Drawing.Point(939, 511);
            this.pictureBox_rectangle.Name = "pictureBox_rectangle";
            this.pictureBox_rectangle.Size = new System.Drawing.Size(608, 380);
            this.pictureBox_rectangle.TabIndex = 62;
            this.pictureBox_rectangle.TabStop = false;
            // 
            // timer_draw_rectangle
            // 
            this.timer_draw_rectangle.Enabled = true;
            this.timer_draw_rectangle.Interval = 1000;
            this.timer_draw_rectangle.Tick += new System.EventHandler(this.timer_draw_rectangle_Tick);
            // 
            // pictureBox_random_pixel_image
            // 
            this.pictureBox_random_pixel_image.BackColor = System.Drawing.Color.Pink;
            this.pictureBox_random_pixel_image.Location = new System.Drawing.Point(12, 674);
            this.pictureBox_random_pixel_image.Name = "pictureBox_random_pixel_image";
            this.pictureBox_random_pixel_image.Size = new System.Drawing.Size(300, 100);
            this.pictureBox_random_pixel_image.TabIndex = 63;
            this.pictureBox_random_pixel_image.TabStop = false;
            // 
            // timer_random_pixel_image
            // 
            this.timer_random_pixel_image.Enabled = true;
            this.timer_random_pixel_image.Interval = 1000;
            this.timer_random_pixel_image.Tick += new System.EventHandler(this.timer_random_pixel_image_Tick);
            // 
            // pictureBox_progressbar
            // 
            this.pictureBox_progressbar.Location = new System.Drawing.Point(369, 322);
            this.pictureBox_progressbar.Name = "pictureBox_progressbar";
            this.pictureBox_progressbar.Size = new System.Drawing.Size(543, 86);
            this.pictureBox_progressbar.TabIndex = 64;
            this.pictureBox_progressbar.TabStop = false;
            // 
            // timer_progressbar
            // 
            this.timer_progressbar.Interval = 50;
            this.timer_progressbar.Tick += new System.EventHandler(this.timer_progressbar_Tick);
            // 
            // pictureBox_word
            // 
            this.pictureBox_word.BackColor = System.Drawing.Color.LightGray;
            this.pictureBox_word.Location = new System.Drawing.Point(329, 654);
            this.pictureBox_word.Name = "pictureBox_word";
            this.pictureBox_word.Size = new System.Drawing.Size(120, 120);
            this.pictureBox_word.TabIndex = 65;
            this.pictureBox_word.TabStop = false;
            // 
            // timer_word
            // 
            this.timer_word.Interval = 1000;
            this.timer_word.Tick += new System.EventHandler(this.timer_word_Tick);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.pictureBox_compass1);
            this.groupBox1.Controls.Add(this.pictureBox_compass2);
            this.groupBox1.Controls.Add(this.lblDegrees);
            this.groupBox1.Controls.Add(this.hbarDegrees);
            this.groupBox1.Location = new System.Drawing.Point(939, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(274, 365);
            this.groupBox1.TabIndex = 66;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Compass";
            // 
            // pictureBox_compass1
            // 
            this.pictureBox_compass1.BackColor = System.Drawing.Color.White;
            this.pictureBox_compass1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox_compass1.Location = new System.Drawing.Point(6, 39);
            this.pictureBox_compass1.Name = "pictureBox_compass1";
            this.pictureBox_compass1.Size = new System.Drawing.Size(260, 240);
            this.pictureBox_compass1.TabIndex = 3;
            this.pictureBox_compass1.TabStop = false;
            this.pictureBox_compass1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_compass1_Paint);
            // 
            // pictureBox_compass2
            // 
            this.pictureBox_compass2.BackColor = System.Drawing.Color.White;
            this.pictureBox_compass2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox_compass2.Location = new System.Drawing.Point(6, 284);
            this.pictureBox_compass2.Name = "pictureBox_compass2";
            this.pictureBox_compass2.Size = new System.Drawing.Size(260, 74);
            this.pictureBox_compass2.TabIndex = 0;
            this.pictureBox_compass2.TabStop = false;
            this.pictureBox_compass2.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_compass2_Paint);
            // 
            // lblDegrees
            // 
            this.lblDegrees.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblDegrees.Location = new System.Drawing.Point(223, 20);
            this.lblDegrees.Name = "lblDegrees";
            this.lblDegrees.Size = new System.Drawing.Size(43, 16);
            this.lblDegrees.TabIndex = 2;
            this.lblDegrees.Text = "0";
            this.lblDegrees.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // hbarDegrees
            // 
            this.hbarDegrees.Location = new System.Drawing.Point(6, 20);
            this.hbarDegrees.Maximum = 360;
            this.hbarDegrees.Name = "hbarDegrees";
            this.hbarDegrees.Size = new System.Drawing.Size(214, 17);
            this.hbarDegrees.TabIndex = 1;
            this.hbarDegrees.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hbarDegrees_Scroll);
            // 
            // timer_compass
            // 
            this.timer_compass.Enabled = true;
            this.timer_compass.Interval = 250;
            this.timer_compass.Tick += new System.EventHandler(this.timer_compass_Tick);
            // 
            // pictureBox_brown
            // 
            this.pictureBox_brown.BackColor = System.Drawing.Color.LightGray;
            this.pictureBox_brown.Location = new System.Drawing.Point(479, 654);
            this.pictureBox_brown.Name = "pictureBox_brown";
            this.pictureBox_brown.Size = new System.Drawing.Size(120, 120);
            this.pictureBox_brown.TabIndex = 67;
            this.pictureBox_brown.TabStop = false;
            // 
            // timer_brown
            // 
            this.timer_brown.Enabled = true;
            this.timer_brown.Interval = 1000;
            this.timer_brown.Tick += new System.EventHandler(this.timer_brown_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1398, 786);
            this.Controls.Add(this.pictureBox_brown);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox_word);
            this.Controls.Add(this.pictureBox_progressbar);
            this.Controls.Add(this.pictureBox_random_pixel_image);
            this.Controls.Add(this.pictureBox_rectangle);
            this.Controls.Add(this.pictureBox_captcha3);
            this.Controls.Add(this.pictureBox_captcha2);
            this.Controls.Add(this.pictureBox_captcha1);
            this.Controls.Add(this.pictureBox_polygon);
            this.Controls.Add(this.pictureBox_star);
            this.Controls.Add(this.pictureBox_ellipse);
            this.Controls.Add(this.pictureBox_spiral);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form1_FormClosed);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spiral)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_ellipse)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_star)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_polygon)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_rectangle)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_random_pixel_image)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_progressbar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_word)).EndInit();
            this.groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_compass1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_compass2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_brown)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer_random_color;
        private System.Windows.Forms.PictureBox pictureBox_spiral;
        private System.Windows.Forms.PictureBox pictureBox_ellipse;
        private System.Windows.Forms.Timer timer_draw_ellipse;
        private System.Windows.Forms.PictureBox pictureBox_star;
        private System.Windows.Forms.Timer timer_draw_star;
        private System.Windows.Forms.PictureBox pictureBox_polygon;
        private System.Windows.Forms.Timer timer_draw_polygon;
        private System.Windows.Forms.PictureBox pictureBox_captcha3;
        private System.Windows.Forms.PictureBox pictureBox_captcha2;
        private System.Windows.Forms.PictureBox pictureBox_captcha1;
        private System.Windows.Forms.Timer timer_draw_captcha;
        private System.Windows.Forms.PictureBox pictureBox_rectangle;
        private System.Windows.Forms.Timer timer_draw_rectangle;
        private System.Windows.Forms.PictureBox pictureBox_random_pixel_image;
        private System.Windows.Forms.Timer timer_random_pixel_image;
        private System.Windows.Forms.PictureBox pictureBox_progressbar;
        private System.Windows.Forms.Timer timer_progressbar;
        private System.Windows.Forms.PictureBox pictureBox_word;
        private System.Windows.Forms.Timer timer_word;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.PictureBox pictureBox_compass1;
        private System.Windows.Forms.PictureBox pictureBox_compass2;
        private System.Windows.Forms.Label lblDegrees;
        private System.Windows.Forms.HScrollBar hbarDegrees;
        private System.Windows.Forms.Timer timer_compass;
        private System.Windows.Forms.PictureBox pictureBox_brown;
        private System.Windows.Forms.Timer timer_brown;
    }
}

