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
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spiral)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_ellipse)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_star)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_polygon)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_captcha1)).BeginInit();
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
            this.richTextBox1.Location = new System.Drawing.Point(1063, 356);
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
            this.pictureBox_star.Size = new System.Drawing.Size(276, 268);
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
            this.pictureBox_polygon.Location = new System.Drawing.Point(939, 12);
            this.pictureBox_polygon.Name = "pictureBox_polygon";
            this.pictureBox_polygon.Size = new System.Drawing.Size(289, 282);
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
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1398, 680);
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
    }
}

