namespace vcs_test_all_05_Print4
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
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.button00 = new System.Windows.Forms.Button();
            this.button03 = new System.Windows.Forms.Button();
            this.button01 = new System.Windows.Forms.Button();
            this.button02 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pageSetupDialog0 = new System.Windows.Forms.PageSetupDialog();
            this.printDialog0 = new System.Windows.Forms.PrintDialog();
            this.printDocument0 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog0 = new System.Windows.Forms.PrintPreviewDialog();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button0 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.printDocument555 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog555 = new System.Windows.Forms.PrintPreviewDialog();
            this.printPreviewDialog_Calendar = new System.Windows.Forms.PrintPreviewDialog();
            this.printDocument_Calendar = new System.Drawing.Printing.PrintDocument();
            this.button3 = new System.Windows.Forms.Button();
            this.printDocument_image = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog_image = new System.Windows.Forms.PrintPreviewDialog();
            this.groupBox0.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.button00);
            this.groupBox0.Controls.Add(this.button03);
            this.groupBox0.Controls.Add(this.button01);
            this.groupBox0.Controls.Add(this.button02);
            this.groupBox0.Location = new System.Drawing.Point(12, 12);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(200, 280);
            this.groupBox0.TabIndex = 151;
            this.groupBox0.TabStop = false;
            // 
            // button00
            // 
            this.button00.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button00.Location = new System.Drawing.Point(10, 20);
            this.button00.Name = "button00";
            this.button00.Size = new System.Drawing.Size(180, 55);
            this.button00.TabIndex = 146;
            this.button00.Text = "版面設定";
            this.button00.UseVisualStyleBackColor = true;
            this.button00.Click += new System.EventHandler(this.button00_Click);
            // 
            // button03
            // 
            this.button03.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button03.Location = new System.Drawing.Point(10, 204);
            this.button03.Name = "button03";
            this.button03.Size = new System.Drawing.Size(180, 55);
            this.button03.TabIndex = 149;
            this.button03.Text = "列印";
            this.button03.UseVisualStyleBackColor = true;
            this.button03.Click += new System.EventHandler(this.button03_Click);
            // 
            // button01
            // 
            this.button01.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button01.Location = new System.Drawing.Point(10, 81);
            this.button01.Name = "button01";
            this.button01.Size = new System.Drawing.Size(180, 55);
            this.button01.TabIndex = 147;
            this.button01.Text = "列印設定";
            this.button01.UseVisualStyleBackColor = true;
            this.button01.Click += new System.EventHandler(this.button01_Click);
            // 
            // button02
            // 
            this.button02.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button02.Location = new System.Drawing.Point(10, 142);
            this.button02.Name = "button02";
            this.button02.Size = new System.Drawing.Size(180, 55);
            this.button02.TabIndex = 148;
            this.button02.Text = "預覽列印";
            this.button02.UseVisualStyleBackColor = true;
            this.button02.Click += new System.EventHandler(this.button02_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(254, 154);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 153;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(237, 117);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 152;
            this.richTextBox1.Text = "";
            // 
            // printDialog0
            // 
            this.printDialog0.UseEXDialog = true;
            // 
            // printDocument0
            // 
            this.printDocument0.DocumentName = "document0";
            this.printDocument0.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument0_PrintPage);
            // 
            // printPreviewDialog0
            // 
            this.printPreviewDialog0.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog0.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog0.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog0.Document = this.printDocument0;
            this.printPreviewDialog0.Enabled = true;
            this.printPreviewDialog0.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog0.Icon")));
            this.printPreviewDialog0.Name = "printPreviewDialog1";
            this.printPreviewDialog0.Visible = false;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(237, 12);
            this.textBox1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 100);
            this.textBox1.TabIndex = 154;
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(22, 320);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(180, 55);
            this.button0.TabIndex = 150;
            this.button0.Text = "版面設定";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(22, 381);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(180, 55);
            this.button1.TabIndex = 155;
            this.button1.Text = "預覽列印555";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(22, 442);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(180, 55);
            this.button2.TabIndex = 156;
            this.button2.Text = "預覽列印 月曆";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // printDocument555
            // 
            this.printDocument555.BeginPrint += new System.Drawing.Printing.PrintEventHandler(this.printDocument555_BeginPrint);
            this.printDocument555.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument555_PrintPage);
            // 
            // printPreviewDialog555
            // 
            this.printPreviewDialog555.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog555.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog555.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog555.Document = this.printDocument555;
            this.printPreviewDialog555.Enabled = true;
            this.printPreviewDialog555.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog555.Icon")));
            this.printPreviewDialog555.Name = "printPreviewDialog555";
            this.printPreviewDialog555.Visible = false;
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
            // printDocument_Calendar
            // 
            this.printDocument_Calendar.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_Calendar_PrintPage);
            this.printDocument_Calendar.QueryPageSettings += new System.Drawing.Printing.QueryPageSettingsEventHandler(this.printDocument_Calendar_QueryPageSettings);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(22, 503);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(180, 55);
            this.button3.TabIndex = 157;
            this.button3.Text = "預覽列印 圖片";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // printDocument_image
            // 
            this.printDocument_image.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_image_PrintPage);
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
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1047, 582);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.Button button00;
        private System.Windows.Forms.Button button03;
        private System.Windows.Forms.Button button01;
        private System.Windows.Forms.Button button02;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PageSetupDialog pageSetupDialog0;
        private System.Windows.Forms.PrintDialog printDialog0;
        private System.Drawing.Printing.PrintDocument printDocument0;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog0;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Drawing.Printing.PrintDocument printDocument555;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog555;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_Calendar;
        private System.Drawing.Printing.PrintDocument printDocument_Calendar;
        private System.Windows.Forms.Button button3;
        private System.Drawing.Printing.PrintDocument printDocument_image;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_image;
    }
}

