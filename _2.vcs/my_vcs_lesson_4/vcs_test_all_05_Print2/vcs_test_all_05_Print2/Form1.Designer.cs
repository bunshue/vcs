namespace vcs_test_all_05_Print2
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
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pageSetupDialog0 = new System.Windows.Forms.PageSetupDialog();
            this.printDialog0 = new System.Windows.Forms.PrintDialog();
            this.printDocument0 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog0 = new System.Windows.Forms.PrintPreviewDialog();
            this.button00 = new System.Windows.Forms.Button();
            this.button01 = new System.Windows.Forms.Button();
            this.button02 = new System.Windows.Forms.Button();
            this.button03 = new System.Windows.Forms.Button();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button10 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.pageSetupDialog1 = new System.Windows.Forms.PageSetupDialog();
            this.printDialog1 = new System.Windows.Forms.PrintDialog();
            this.printDocument1 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog1 = new System.Windows.Forms.PrintPreviewDialog();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.button30 = new System.Windows.Forms.Button();
            this.button33 = new System.Windows.Forms.Button();
            this.button31 = new System.Windows.Forms.Button();
            this.button32 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.printDialog2 = new System.Windows.Forms.PrintDialog();
            this.printDialog3 = new System.Windows.Forms.PrintDialog();
            this.printDocument3 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog3 = new System.Windows.Forms.PrintPreviewDialog();
            this.printPreviewControl1 = new System.Windows.Forms.PrintPreviewControl();
            this.printDocumentA = new System.Drawing.Printing.PrintDocument();
            this.printDialogB = new System.Windows.Forms.PrintDialog();
            this.printPreviewDialog2 = new System.Windows.Forms.PrintPreviewDialog();
            this.groupBox0.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(229, 337);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 131;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(209, 303);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 122;
            this.richTextBox1.Text = "";
            // 
            // printDialog0
            // 
            this.printDialog0.UseEXDialog = true;
            // 
            // printDocument0
            // 
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
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.button00);
            this.groupBox0.Controls.Add(this.button03);
            this.groupBox0.Controls.Add(this.button01);
            this.groupBox0.Controls.Add(this.button02);
            this.groupBox0.Location = new System.Drawing.Point(3, 0);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(200, 280);
            this.groupBox0.TabIndex = 150;
            this.groupBox0.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button10);
            this.groupBox1.Controls.Add(this.button13);
            this.groupBox1.Controls.Add(this.button11);
            this.groupBox1.Controls.Add(this.button12);
            this.groupBox1.Location = new System.Drawing.Point(209, 0);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(200, 280);
            this.groupBox1.TabIndex = 151;
            this.groupBox1.TabStop = false;
            // 
            // button10
            // 
            this.button10.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button10.Location = new System.Drawing.Point(10, 20);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(180, 55);
            this.button10.TabIndex = 146;
            this.button10.Text = "版面設定";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // button13
            // 
            this.button13.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button13.Location = new System.Drawing.Point(10, 204);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(180, 55);
            this.button13.TabIndex = 149;
            this.button13.Text = "列印";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // button11
            // 
            this.button11.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button11.Location = new System.Drawing.Point(10, 82);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(180, 55);
            this.button11.TabIndex = 147;
            this.button11.Text = "列印設定";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // button12
            // 
            this.button12.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button12.Location = new System.Drawing.Point(10, 143);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(180, 55);
            this.button12.TabIndex = 148;
            this.button12.Text = "預覽列印";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // printDialog1
            // 
            this.printDialog1.UseEXDialog = true;
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
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.button30);
            this.groupBox3.Controls.Add(this.button33);
            this.groupBox3.Controls.Add(this.button31);
            this.groupBox3.Controls.Add(this.button32);
            this.groupBox3.Location = new System.Drawing.Point(415, 0);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(200, 280);
            this.groupBox3.TabIndex = 152;
            this.groupBox3.TabStop = false;
            // 
            // button30
            // 
            this.button30.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button30.Location = new System.Drawing.Point(10, 20);
            this.button30.Name = "button30";
            this.button30.Size = new System.Drawing.Size(180, 55);
            this.button30.TabIndex = 146;
            this.button30.Text = "版面設定";
            this.button30.UseVisualStyleBackColor = true;
            this.button30.Click += new System.EventHandler(this.button30_Click);
            // 
            // button33
            // 
            this.button33.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button33.Location = new System.Drawing.Point(10, 204);
            this.button33.Name = "button33";
            this.button33.Size = new System.Drawing.Size(180, 55);
            this.button33.TabIndex = 149;
            this.button33.Text = "列印";
            this.button33.UseVisualStyleBackColor = true;
            this.button33.Click += new System.EventHandler(this.button33_Click);
            // 
            // button31
            // 
            this.button31.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button31.Location = new System.Drawing.Point(10, 81);
            this.button31.Name = "button31";
            this.button31.Size = new System.Drawing.Size(180, 55);
            this.button31.TabIndex = 147;
            this.button31.Text = "列印設定";
            this.button31.UseVisualStyleBackColor = true;
            this.button31.Click += new System.EventHandler(this.button31_Click);
            // 
            // button32
            // 
            this.button32.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button32.Location = new System.Drawing.Point(10, 142);
            this.button32.Name = "button32";
            this.button32.Size = new System.Drawing.Size(180, 55);
            this.button32.TabIndex = 148;
            this.button32.Text = "預覽列印";
            this.button32.UseVisualStyleBackColor = true;
            this.button32.Click += new System.EventHandler(this.button32_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(23, 348);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(160, 55);
            this.button1.TabIndex = 153;
            this.button1.Text = "設定印表機";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(23, 470);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(160, 55);
            this.button3.TabIndex = 154;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(23, 531);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(160, 55);
            this.button4.TabIndex = 155;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(23, 409);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(160, 55);
            this.button2.TabIndex = 156;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(23, 286);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(160, 55);
            this.button0.TabIndex = 162;
            this.button0.Text = "printDocumentA";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // printDialog2
            // 
            this.printDialog2.UseEXDialog = true;
            // 
            // printDialog3
            // 
            this.printDialog3.Document = this.printDocument3;
            this.printDialog3.UseEXDialog = true;
            // 
            // printDocument3
            // 
            this.printDocument3.DocumentName = "document3";
            this.printDocument3.EndPrint += new System.Drawing.Printing.PrintEventHandler(this.printDocument3_EndPrint);
            this.printDocument3.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument3_PrintPage);
            // 
            // printPreviewDialog3
            // 
            this.printPreviewDialog3.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog3.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog3.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog3.Document = this.printDocument3;
            this.printPreviewDialog3.Enabled = true;
            this.printPreviewDialog3.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog3.Icon")));
            this.printPreviewDialog3.Name = "printPreviewDialog1";
            this.printPreviewDialog3.Visible = false;
            // 
            // printPreviewControl1
            // 
            this.printPreviewControl1.Location = new System.Drawing.Point(336, 304);
            this.printPreviewControl1.Name = "printPreviewControl1";
            this.printPreviewControl1.Size = new System.Drawing.Size(100, 100);
            this.printPreviewControl1.TabIndex = 163;
            // 
            // printDocumentA
            // 
            this.printDocumentA.DocumentName = "documentA";
            this.printDocumentA.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocumentA_PrintPage);
            // 
            // printDialogB
            // 
            this.printDialogB.UseEXDialog = true;
            // 
            // printPreviewDialog2
            // 
            this.printPreviewDialog2.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog2.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog2.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog2.Enabled = true;
            this.printPreviewDialog2.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog2.Icon")));
            this.printPreviewDialog2.Name = "printPreviewDialog2";
            this.printPreviewDialog2.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1127, 598);
            this.Controls.Add(this.printPreviewControl1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PageSetupDialog pageSetupDialog0;
        private System.Windows.Forms.PrintDialog printDialog0;
        private System.Drawing.Printing.PrintDocument printDocument0;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog0;
        private System.Windows.Forms.Button button00;
        private System.Windows.Forms.Button button01;
        private System.Windows.Forms.Button button02;
        private System.Windows.Forms.Button button03;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.PageSetupDialog pageSetupDialog1;
        private System.Windows.Forms.PrintDialog printDialog1;
        private System.Drawing.Printing.PrintDocument printDocument1;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Button button30;
        private System.Windows.Forms.Button button33;
        private System.Windows.Forms.Button button31;
        private System.Windows.Forms.Button button32;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.PrintDialog printDialog2;
        private System.Windows.Forms.PrintDialog printDialog3;
        private System.Drawing.Printing.PrintDocument printDocument3;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog3;
        private System.Windows.Forms.PrintPreviewControl printPreviewControl1;
        private System.Drawing.Printing.PrintDocument printDocumentA;
        private System.Windows.Forms.PrintDialog printDialogB;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog2;
    }
}

