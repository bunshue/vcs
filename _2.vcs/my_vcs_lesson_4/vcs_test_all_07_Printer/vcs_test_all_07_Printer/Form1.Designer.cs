namespace vcs_test_all_07_Printer
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.button0 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.printDocument1 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog1 = new System.Windows.Forms.PrintPreviewDialog();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.printPreviewDialog_image = new System.Windows.Forms.PrintPreviewDialog();
            this.printDocument_image = new System.Drawing.Printing.PrintDocument();
            this.printDocument_draw = new System.Drawing.Printing.PrintDocument();
            this.printDocument_Calendar = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog_Calendar = new System.Windows.Forms.PrintPreviewDialog();
            this.printPreviewDialog_grid = new System.Windows.Forms.PrintPreviewDialog();
            this.printDocument_grid = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog_star = new System.Windows.Forms.PrintPreviewDialog();
            this.printDocument_star = new System.Drawing.Printing.PrintDocument();
            this.txtRadius = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.nudSkip = new System.Windows.Forms.NumericUpDown();
            this.nudPoints = new System.Windows.Forms.NumericUpDown();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox_star = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudSkip)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudPoints)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_star)).BeginInit();
            this.SuspendLayout();
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(16, 15);
            this.button0.Margin = new System.Windows.Forms.Padding(4);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(259, 50);
            this.button0.TabIndex = 45;
            this.button0.Text = "列出目前的印表機";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button9
            // 
            this.button9.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.Location = new System.Drawing.Point(16, 685);
            this.button9.Margin = new System.Windows.Forms.Padding(4);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(259, 50);
            this.button9.TabIndex = 35;
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(16, 295);
            this.button5.Margin = new System.Windows.Forms.Padding(4);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(259, 50);
            this.button5.TabIndex = 33;
            this.button5.Text = "預覽列印 月曆";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(16, 352);
            this.button6.Margin = new System.Windows.Forms.Padding(4);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(259, 50);
            this.button6.TabIndex = 32;
            this.button6.Text = "預覽列印 Grid";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button7.Location = new System.Drawing.Point(54, 119);
            this.button7.Margin = new System.Windows.Forms.Padding(4);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(159, 45);
            this.button7.TabIndex = 31;
            this.button7.Text = "預覽列印 Star";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button8.Location = new System.Drawing.Point(16, 615);
            this.button8.Margin = new System.Windows.Forms.Padding(4);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(259, 50);
            this.button8.TabIndex = 30;
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(16, 238);
            this.button4.Margin = new System.Windows.Forms.Padding(4);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(259, 50);
            this.button4.TabIndex = 29;
            this.button4.Text = "列印畫圖 至 pdf";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(16, 180);
            this.button3.Margin = new System.Windows.Forms.Padding(4);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(259, 50);
            this.button3.TabIndex = 28;
            this.button3.Text = "預覽列印 圖片";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(16, 122);
            this.button2.Margin = new System.Windows.Forms.Padding(4);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(259, 50);
            this.button2.TabIndex = 27;
            this.button2.Text = "列印 至 pdf";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(16, 65);
            this.button1.Margin = new System.Windows.Forms.Padding(4);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(259, 50);
            this.button1.TabIndex = 26;
            this.button1.Text = "預覽列印";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1135, 688);
            this.bt_clear.Margin = new System.Windows.Forms.Padding(4);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 44);
            this.bt_clear.TabIndex = 47;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(727, 15);
            this.richTextBox1.Margin = new System.Windows.Forms.Padding(4);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(640, 759);
            this.richTextBox1.TabIndex = 46;
            this.richTextBox1.Text = "";
            // 
            // printDocument1
            // 
            this.printDocument1.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument1_PrintPage);
            // 
            // printPreviewDialog1
            // 
            this.printPreviewDialog1.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog1.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog1.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog1.Document = this.printDocument1;
            this.printPreviewDialog1.Enabled = true;
            this.printPreviewDialog1.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog1.Icon")));
            this.printPreviewDialog1.Name = "printPreviewDialog1";
            this.printPreviewDialog1.Visible = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(301, 15);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(4);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(376, 481);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 48;
            this.pictureBox1.TabStop = false;
            // 
            // printPreviewDialog_image
            // 
            this.printPreviewDialog_image.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_image.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_image.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_image.Document = this.printDocument_image;
            this.printPreviewDialog_image.Enabled = true;
            this.printPreviewDialog_image.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_image.Icon")));
            this.printPreviewDialog_image.Name = "printPreviewDialog_image";
            this.printPreviewDialog_image.Visible = false;
            // 
            // printDocument_image
            // 
            this.printDocument_image.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_image_PrintPage);
            // 
            // printDocument_draw
            // 
            this.printDocument_draw.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_draw_PrintPage);
            // 
            // printDocument_Calendar
            // 
            this.printDocument_Calendar.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_Calendar_PrintPage);
            this.printDocument_Calendar.QueryPageSettings += new System.Drawing.Printing.QueryPageSettingsEventHandler(this.printDocument_Calendar_QueryPageSettings);
            // 
            // printPreviewDialog_Calendar
            // 
            this.printPreviewDialog_Calendar.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_Calendar.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_Calendar.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_Calendar.Document = this.printDocument_Calendar;
            this.printPreviewDialog_Calendar.Enabled = true;
            this.printPreviewDialog_Calendar.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_Calendar.Icon")));
            this.printPreviewDialog_Calendar.Name = "printPreviewDialog_Calendar";
            this.printPreviewDialog_Calendar.Visible = false;
            // 
            // printPreviewDialog_grid
            // 
            this.printPreviewDialog_grid.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_grid.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_grid.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_grid.Document = this.printDocument_grid;
            this.printPreviewDialog_grid.Enabled = true;
            this.printPreviewDialog_grid.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_grid.Icon")));
            this.printPreviewDialog_grid.Name = "printPreviewDialog_grid";
            this.printPreviewDialog_grid.Visible = false;
            // 
            // printDocument_grid
            // 
            this.printDocument_grid.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_grid_PrintPage);
            // 
            // printPreviewDialog_star
            // 
            this.printPreviewDialog_star.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_star.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_star.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_star.Document = this.printDocument_star;
            this.printPreviewDialog_star.Enabled = true;
            this.printPreviewDialog_star.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_star.Icon")));
            this.printPreviewDialog_star.Name = "printPreviewDialog_star";
            this.printPreviewDialog_star.Visible = false;
            // 
            // printDocument_star
            // 
            this.printDocument_star.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_star_PrintPage);
            // 
            // txtRadius
            // 
            this.txtRadius.Location = new System.Drawing.Point(134, 84);
            this.txtRadius.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtRadius.Name = "txtRadius";
            this.txtRadius.Size = new System.Drawing.Size(79, 25);
            this.txtRadius.TabIndex = 54;
            this.txtRadius.Text = "100";
            this.txtRadius.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(57, 87);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(63, 15);
            this.label3.TabIndex = 53;
            this.label3.Text = "Diameter:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(57, 57);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(37, 15);
            this.label2.TabIndex = 52;
            this.label2.Text = "Skip:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(57, 27);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(57, 15);
            this.label1.TabIndex = 51;
            this.label1.Text = "# Points:";
            // 
            // nudSkip
            // 
            this.nudSkip.Location = new System.Drawing.Point(134, 55);
            this.nudSkip.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.nudSkip.Maximum = new decimal(new int[] {
            3,
            0,
            0,
            0});
            this.nudSkip.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudSkip.Name = "nudSkip";
            this.nudSkip.Size = new System.Drawing.Size(80, 25);
            this.nudSkip.TabIndex = 50;
            this.nudSkip.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.nudSkip.Value = new decimal(new int[] {
            2,
            0,
            0,
            0});
            this.nudSkip.ValueChanged += new System.EventHandler(this.nudSkip_ValueChanged);
            // 
            // nudPoints
            // 
            this.nudPoints.Location = new System.Drawing.Point(134, 25);
            this.nudPoints.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.nudPoints.Minimum = new decimal(new int[] {
            2,
            0,
            0,
            0});
            this.nudPoints.Name = "nudPoints";
            this.nudPoints.Size = new System.Drawing.Size(80, 25);
            this.nudPoints.TabIndex = 49;
            this.nudPoints.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.nudPoints.Value = new decimal(new int[] {
            7,
            0,
            0,
            0});
            this.nudPoints.ValueChanged += new System.EventHandler(this.nudPoints_ValueChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.txtRadius);
            this.groupBox1.Controls.Add(this.nudPoints);
            this.groupBox1.Controls.Add(this.nudSkip);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.button7);
            this.groupBox1.Location = new System.Drawing.Point(16, 409);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(259, 178);
            this.groupBox1.TabIndex = 55;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "預覽列印 Star";
            // 
            // pictureBox_star
            // 
            this.pictureBox_star.Location = new System.Drawing.Point(301, 513);
            this.pictureBox_star.Name = "pictureBox_star";
            this.pictureBox_star.Size = new System.Drawing.Size(299, 265);
            this.pictureBox_star.TabIndex = 56;
            this.pictureBox_star.TabStop = false;
            this.pictureBox_star.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_star_Paint);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1372, 790);
            this.Controls.Add(this.pictureBox_star);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudSkip)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudPoints)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_star)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Drawing.Printing.PrintDocument printDocument1;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_image;
        private System.Drawing.Printing.PrintDocument printDocument_image;
        private System.Drawing.Printing.PrintDocument printDocument_draw;
        private System.Drawing.Printing.PrintDocument printDocument_Calendar;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_Calendar;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_grid;
        private System.Drawing.Printing.PrintDocument printDocument_grid;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_star;
        private System.Drawing.Printing.PrintDocument printDocument_star;
        private System.Windows.Forms.TextBox txtRadius;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown nudSkip;
        private System.Windows.Forms.NumericUpDown nudPoints;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.PictureBox pictureBox_star;
    }
}

