namespace vcs_ImageProcessing4
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
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
            this.btnEmboss1 = new System.Windows.Forms.Button();
            this.btnBlur1 = new System.Windows.Forms.Button();
            this.btnBlur2 = new System.Windows.Forms.Button();
            this.btnHighPass1 = new System.Windows.Forms.Button();
            this.btnHighPass2 = new System.Windows.Forms.Button();
            this.btnEdge1 = new System.Windows.Forms.Button();
            this.btnEdge2 = new System.Windows.Forms.Button();
            this.btnEmboss2 = new System.Windows.Forms.Button();
            this.btnEdge3 = new System.Windows.Forms.Button();
            this.btnAverage = new System.Windows.Forms.Button();
            this.btnGrayscale = new System.Windows.Forms.Button();
            this.btnGreen = new System.Windows.Forms.Button();
            this.btnRed = new System.Windows.Forms.Button();
            this.btnBlue = new System.Windows.Forms.Button();
            this.btnInvert = new System.Windows.Forms.Button();
            this.btnMaximum = new System.Windows.Forms.Button();
            this.btnMinimum = new System.Windows.Forms.Button();
            this.btnPixellate = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txtRank = new System.Windows.Forms.TextBox();
            this.btnPointellate = new System.Windows.Forms.Button();
            this.btnEmboss3 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_image_process_b0 = new System.Windows.Forms.Button();
            this.bt_image_process_b1 = new System.Windows.Forms.Button();
            this.bt_image_process_b2 = new System.Windows.Forms.Button();
            this.bt_image_process_b3 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.bt_image_process_a7 = new System.Windows.Forms.Button();
            this.bt_image_process_a0 = new System.Windows.Forms.Button();
            this.bt_image_process_a6 = new System.Windows.Forms.Button();
            this.bt_image_process_a1 = new System.Windows.Forms.Button();
            this.bt_image_process_a5 = new System.Windows.Forms.Button();
            this.bt_image_process_a2 = new System.Windows.Forms.Button();
            this.bt_image_process_a4 = new System.Windows.Forms.Button();
            this.bt_image_process_a3 = new System.Windows.Forms.Button();
            this.btnGrayscale2 = new System.Windows.Forms.Button();
            this.bt_reset = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox2.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnEmboss1
            // 
            this.btnEmboss1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEmboss1.Location = new System.Drawing.Point(12, 7);
            this.btnEmboss1.Name = "btnEmboss1";
            this.btnEmboss1.Size = new System.Drawing.Size(200, 60);
            this.btnEmboss1.TabIndex = 1;
            this.btnEmboss1.Text = "浮雕 1";
            this.btnEmboss1.Click += new System.EventHandler(this.btnEmboss1_Click);
            // 
            // btnBlur1
            // 
            this.btnBlur1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnBlur1.Location = new System.Drawing.Point(12, 188);
            this.btnBlur1.Name = "btnBlur1";
            this.btnBlur1.Size = new System.Drawing.Size(200, 60);
            this.btnBlur1.TabIndex = 4;
            this.btnBlur1.Text = "高斯模糊";
            this.btnBlur1.Click += new System.EventHandler(this.btnBlur1_Click);
            // 
            // btnBlur2
            // 
            this.btnBlur2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnBlur2.Location = new System.Drawing.Point(12, 248);
            this.btnBlur2.Name = "btnBlur2";
            this.btnBlur2.Size = new System.Drawing.Size(200, 60);
            this.btnBlur2.TabIndex = 5;
            this.btnBlur2.Text = "平均模糊";
            this.btnBlur2.Click += new System.EventHandler(this.btnBlur2_Click);
            // 
            // btnHighPass1
            // 
            this.btnHighPass1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnHighPass1.Location = new System.Drawing.Point(12, 307);
            this.btnHighPass1.Name = "btnHighPass1";
            this.btnHighPass1.Size = new System.Drawing.Size(200, 60);
            this.btnHighPass1.TabIndex = 6;
            this.btnHighPass1.Text = "高通 1";
            this.btnHighPass1.Click += new System.EventHandler(this.btnHighPass1_Click);
            // 
            // btnHighPass2
            // 
            this.btnHighPass2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnHighPass2.Location = new System.Drawing.Point(12, 366);
            this.btnHighPass2.Name = "btnHighPass2";
            this.btnHighPass2.Size = new System.Drawing.Size(200, 60);
            this.btnHighPass2.TabIndex = 7;
            this.btnHighPass2.Text = "高通 2";
            this.btnHighPass2.Click += new System.EventHandler(this.btnHighPass2_Click);
            // 
            // btnEdge1
            // 
            this.btnEdge1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEdge1.Location = new System.Drawing.Point(12, 426);
            this.btnEdge1.Name = "btnEdge1";
            this.btnEdge1.Size = new System.Drawing.Size(200, 60);
            this.btnEdge1.TabIndex = 8;
            this.btnEdge1.Text = "邊緣檢測 1";
            this.btnEdge1.Click += new System.EventHandler(this.btnEdge1_Click);
            // 
            // btnEdge2
            // 
            this.btnEdge2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEdge2.Location = new System.Drawing.Point(12, 484);
            this.btnEdge2.Name = "btnEdge2";
            this.btnEdge2.Size = new System.Drawing.Size(200, 60);
            this.btnEdge2.TabIndex = 9;
            this.btnEdge2.Text = "邊緣檢測 2";
            this.btnEdge2.Click += new System.EventHandler(this.btnEdge2_Click);
            // 
            // btnEmboss2
            // 
            this.btnEmboss2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEmboss2.Location = new System.Drawing.Point(12, 66);
            this.btnEmboss2.Name = "btnEmboss2";
            this.btnEmboss2.Size = new System.Drawing.Size(200, 60);
            this.btnEmboss2.TabIndex = 2;
            this.btnEmboss2.Text = "浮雕 2";
            this.btnEmboss2.Click += new System.EventHandler(this.btnEmboss2_Click);
            // 
            // btnEdge3
            // 
            this.btnEdge3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEdge3.Location = new System.Drawing.Point(12, 544);
            this.btnEdge3.Name = "btnEdge3";
            this.btnEdge3.Size = new System.Drawing.Size(200, 60);
            this.btnEdge3.TabIndex = 10;
            this.btnEdge3.Text = "邊緣檢測 3";
            this.btnEdge3.Click += new System.EventHandler(this.btnEdge3_Click);
            // 
            // btnAverage
            // 
            this.btnAverage.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnAverage.Location = new System.Drawing.Point(231, 7);
            this.btnAverage.Name = "btnAverage";
            this.btnAverage.Size = new System.Drawing.Size(200, 60);
            this.btnAverage.TabIndex = 16;
            this.btnAverage.Text = "平均";
            this.btnAverage.Click += new System.EventHandler(this.btnAverage_Click);
            // 
            // btnGrayscale
            // 
            this.btnGrayscale.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnGrayscale.Location = new System.Drawing.Point(231, 66);
            this.btnGrayscale.Name = "btnGrayscale";
            this.btnGrayscale.Size = new System.Drawing.Size(200, 60);
            this.btnGrayscale.TabIndex = 17;
            this.btnGrayscale.Text = "灰階";
            this.btnGrayscale.Click += new System.EventHandler(this.btnGrayscale_Click);
            // 
            // btnGreen
            // 
            this.btnGreen.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnGreen.Location = new System.Drawing.Point(231, 178);
            this.btnGreen.Name = "btnGreen";
            this.btnGreen.Size = new System.Drawing.Size(200, 60);
            this.btnGreen.TabIndex = 19;
            this.btnGreen.Text = "G";
            this.btnGreen.Click += new System.EventHandler(this.btnGreen_Click);
            // 
            // btnRed
            // 
            this.btnRed.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnRed.Location = new System.Drawing.Point(231, 125);
            this.btnRed.Name = "btnRed";
            this.btnRed.Size = new System.Drawing.Size(200, 60);
            this.btnRed.TabIndex = 18;
            this.btnRed.Text = "R";
            this.btnRed.Click += new System.EventHandler(this.btnRed_Click);
            // 
            // btnBlue
            // 
            this.btnBlue.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnBlue.Location = new System.Drawing.Point(231, 238);
            this.btnBlue.Name = "btnBlue";
            this.btnBlue.Size = new System.Drawing.Size(200, 60);
            this.btnBlue.TabIndex = 20;
            this.btnBlue.Text = "B";
            this.btnBlue.Click += new System.EventHandler(this.btnBlue_Click);
            // 
            // btnInvert
            // 
            this.btnInvert.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnInvert.Location = new System.Drawing.Point(231, 297);
            this.btnInvert.Name = "btnInvert";
            this.btnInvert.Size = new System.Drawing.Size(200, 60);
            this.btnInvert.TabIndex = 21;
            this.btnInvert.Text = "反相(負片)";
            this.btnInvert.Click += new System.EventHandler(this.btnInvert_Click);
            // 
            // btnMaximum
            // 
            this.btnMaximum.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnMaximum.Location = new System.Drawing.Point(231, 389);
            this.btnMaximum.Name = "btnMaximum";
            this.btnMaximum.Size = new System.Drawing.Size(200, 60);
            this.btnMaximum.TabIndex = 12;
            this.btnMaximum.Text = "Maximum";
            this.btnMaximum.Click += new System.EventHandler(this.btnMaximum_Click);
            // 
            // btnMinimum
            // 
            this.btnMinimum.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnMinimum.Location = new System.Drawing.Point(231, 447);
            this.btnMinimum.Name = "btnMinimum";
            this.btnMinimum.Size = new System.Drawing.Size(200, 60);
            this.btnMinimum.TabIndex = 13;
            this.btnMinimum.Text = "Minimum";
            this.btnMinimum.Click += new System.EventHandler(this.btnMinimum_Click);
            // 
            // btnPixellate
            // 
            this.btnPixellate.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnPixellate.Location = new System.Drawing.Point(231, 507);
            this.btnPixellate.Name = "btnPixellate";
            this.btnPixellate.Size = new System.Drawing.Size(200, 60);
            this.btnPixellate.TabIndex = 14;
            this.btnPixellate.Text = "Pixellate";
            this.btnPixellate.Click += new System.EventHandler(this.btnPixellate_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(260, 359);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 19);
            this.label1.TabIndex = 19;
            this.label1.Text = "Rank:";
            // 
            // txtRank
            // 
            this.txtRank.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.txtRank.Location = new System.Drawing.Point(302, 359);
            this.txtRank.Name = "txtRank";
            this.txtRank.Size = new System.Drawing.Size(38, 30);
            this.txtRank.TabIndex = 11;
            this.txtRank.Text = "9";
            this.txtRank.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnPointellate
            // 
            this.btnPointellate.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnPointellate.Location = new System.Drawing.Point(231, 567);
            this.btnPointellate.Name = "btnPointellate";
            this.btnPointellate.Size = new System.Drawing.Size(200, 60);
            this.btnPointellate.TabIndex = 15;
            this.btnPointellate.Text = "Pointellate";
            this.btnPointellate.Click += new System.EventHandler(this.btnPointellate_Click);
            // 
            // btnEmboss3
            // 
            this.btnEmboss3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEmboss3.Location = new System.Drawing.Point(12, 127);
            this.btnEmboss3.Name = "btnEmboss3";
            this.btnEmboss3.Size = new System.Drawing.Size(200, 60);
            this.btnEmboss3.TabIndex = 3;
            this.btnEmboss3.Text = "浮雕 3";
            this.btnEmboss3.Click += new System.EventHandler(this.btnEmboss3_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(565, 587);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 22;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(586, 640);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 23;
            this.bt_clear.Text = "Clear";
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(441, 587);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 24;
            this.pictureBox1.TabStop = false;
            // 
            // bt_image_process_b0
            // 
            this.bt_image_process_b0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_b0.Location = new System.Drawing.Point(19, 21);
            this.bt_image_process_b0.Name = "bt_image_process_b0";
            this.bt_image_process_b0.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_b0.TabIndex = 36;
            this.bt_image_process_b0.Text = "No Lock Bits";
            this.bt_image_process_b0.UseVisualStyleBackColor = true;
            this.bt_image_process_b0.Click += new System.EventHandler(this.bt_image_process_b0_Click);
            // 
            // bt_image_process_b1
            // 
            this.bt_image_process_b1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_b1.Location = new System.Drawing.Point(19, 87);
            this.bt_image_process_b1.Name = "bt_image_process_b1";
            this.bt_image_process_b1.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_b1.TabIndex = 37;
            this.bt_image_process_b1.Text = "Lock Bits";
            this.bt_image_process_b1.UseVisualStyleBackColor = true;
            this.bt_image_process_b1.Click += new System.EventHandler(this.bt_image_process_b1_Click);
            // 
            // bt_image_process_b2
            // 
            this.bt_image_process_b2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_b2.Location = new System.Drawing.Point(19, 153);
            this.bt_image_process_b2.Name = "bt_image_process_b2";
            this.bt_image_process_b2.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_b2.TabIndex = 38;
            this.bt_image_process_b2.Text = "Quarter";
            this.bt_image_process_b2.UseVisualStyleBackColor = true;
            this.bt_image_process_b2.Click += new System.EventHandler(this.bt_image_process_b2_Click);
            // 
            // bt_image_process_b3
            // 
            this.bt_image_process_b3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_b3.Location = new System.Drawing.Point(19, 219);
            this.bt_image_process_b3.Name = "bt_image_process_b3";
            this.bt_image_process_b3.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_b3.TabIndex = 39;
            this.bt_image_process_b3.UseVisualStyleBackColor = true;
            this.bt_image_process_b3.Click += new System.EventHandler(this.bt_image_process_b3_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.bt_image_process_a7);
            this.groupBox2.Controls.Add(this.bt_image_process_a0);
            this.groupBox2.Controls.Add(this.bt_image_process_a6);
            this.groupBox2.Controls.Add(this.bt_image_process_a1);
            this.groupBox2.Controls.Add(this.bt_image_process_a5);
            this.groupBox2.Controls.Add(this.bt_image_process_a2);
            this.groupBox2.Controls.Add(this.bt_image_process_a4);
            this.groupBox2.Controls.Add(this.bt_image_process_a3);
            this.groupBox2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox2.Location = new System.Drawing.Point(440, 10);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(225, 534);
            this.groupBox2.TabIndex = 50;
            this.groupBox2.TabStop = false;
            // 
            // bt_image_process_a7
            // 
            this.bt_image_process_a7.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a7.Location = new System.Drawing.Point(22, 443);
            this.bt_image_process_a7.Name = "bt_image_process_a7";
            this.bt_image_process_a7.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a7.TabIndex = 43;
            this.bt_image_process_a7.UseVisualStyleBackColor = true;
            this.bt_image_process_a7.Click += new System.EventHandler(this.bt_image_process_a7_Click);
            // 
            // bt_image_process_a0
            // 
            this.bt_image_process_a0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a0.Location = new System.Drawing.Point(22, 25);
            this.bt_image_process_a0.Name = "bt_image_process_a0";
            this.bt_image_process_a0.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a0.TabIndex = 36;
            this.bt_image_process_a0.Text = "Fish Eye";
            this.bt_image_process_a0.UseVisualStyleBackColor = true;
            this.bt_image_process_a0.Click += new System.EventHandler(this.bt_image_process_a0_Click);
            // 
            // bt_image_process_a6
            // 
            this.bt_image_process_a6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a6.Location = new System.Drawing.Point(22, 381);
            this.bt_image_process_a6.Name = "bt_image_process_a6";
            this.bt_image_process_a6.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a6.TabIndex = 42;
            this.bt_image_process_a6.UseVisualStyleBackColor = true;
            this.bt_image_process_a6.Click += new System.EventHandler(this.bt_image_process_a6_Click);
            // 
            // bt_image_process_a1
            // 
            this.bt_image_process_a1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a1.Location = new System.Drawing.Point(22, 85);
            this.bt_image_process_a1.Name = "bt_image_process_a1";
            this.bt_image_process_a1.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a1.TabIndex = 37;
            this.bt_image_process_a1.Text = "Twist";
            this.bt_image_process_a1.UseVisualStyleBackColor = true;
            this.bt_image_process_a1.Click += new System.EventHandler(this.bt_image_process_a1_Click);
            // 
            // bt_image_process_a5
            // 
            this.bt_image_process_a5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a5.Location = new System.Drawing.Point(22, 321);
            this.bt_image_process_a5.Name = "bt_image_process_a5";
            this.bt_image_process_a5.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a5.TabIndex = 41;
            this.bt_image_process_a5.Text = "Double Wave";
            this.bt_image_process_a5.UseVisualStyleBackColor = true;
            this.bt_image_process_a5.Click += new System.EventHandler(this.bt_image_process_a5_Click);
            // 
            // bt_image_process_a2
            // 
            this.bt_image_process_a2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a2.Location = new System.Drawing.Point(22, 144);
            this.bt_image_process_a2.Name = "bt_image_process_a2";
            this.bt_image_process_a2.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a2.TabIndex = 38;
            this.bt_image_process_a2.Text = "Wave";
            this.bt_image_process_a2.UseVisualStyleBackColor = true;
            this.bt_image_process_a2.Click += new System.EventHandler(this.bt_image_process_a2_Click);
            // 
            // bt_image_process_a4
            // 
            this.bt_image_process_a4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a4.Location = new System.Drawing.Point(22, 262);
            this.bt_image_process_a4.Name = "bt_image_process_a4";
            this.bt_image_process_a4.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a4.TabIndex = 40;
            this.bt_image_process_a4.Text = "Wiggles";
            this.bt_image_process_a4.UseVisualStyleBackColor = true;
            this.bt_image_process_a4.Click += new System.EventHandler(this.bt_image_process_a4_Click);
            // 
            // bt_image_process_a3
            // 
            this.bt_image_process_a3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_image_process_a3.Location = new System.Drawing.Point(22, 203);
            this.bt_image_process_a3.Name = "bt_image_process_a3";
            this.bt_image_process_a3.Size = new System.Drawing.Size(180, 60);
            this.bt_image_process_a3.TabIndex = 39;
            this.bt_image_process_a3.Text = "Small Top";
            this.bt_image_process_a3.UseVisualStyleBackColor = true;
            this.bt_image_process_a3.Click += new System.EventHandler(this.bt_image_process_a3_Click);
            // 
            // btnGrayscale2
            // 
            this.btnGrayscale2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnGrayscale2.Location = new System.Drawing.Point(231, 627);
            this.btnGrayscale2.Name = "btnGrayscale2";
            this.btnGrayscale2.Size = new System.Drawing.Size(200, 60);
            this.btnGrayscale2.TabIndex = 51;
            this.btnGrayscale2.Text = "灰階";
            this.btnGrayscale2.Click += new System.EventHandler(this.btnGrayscale2_Click);
            // 
            // bt_reset
            // 
            this.bt_reset.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_reset.Location = new System.Drawing.Point(462, 627);
            this.bt_reset.Name = "bt_reset";
            this.bt_reset.Size = new System.Drawing.Size(72, 36);
            this.bt_reset.TabIndex = 229;
            this.bt_reset.Text = "Reset";
            this.bt_reset.UseVisualStyleBackColor = true;
            this.bt_reset.Click += new System.EventHandler(this.bt_reset_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_image_process_b0);
            this.groupBox1.Controls.Add(this.bt_image_process_b3);
            this.groupBox1.Controls.Add(this.bt_image_process_b1);
            this.groupBox1.Controls.Add(this.bt_image_process_b2);
            this.groupBox1.Location = new System.Drawing.Point(670, 10);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(215, 297);
            this.groupBox1.TabIndex = 230;
            this.groupBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(951, 744);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_reset);
            this.Controls.Add(this.btnGrayscale2);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnEmboss3);
            this.Controls.Add(this.btnPointellate);
            this.Controls.Add(this.txtRank);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnPixellate);
            this.Controls.Add(this.btnMinimum);
            this.Controls.Add(this.btnMaximum);
            this.Controls.Add(this.btnInvert);
            this.Controls.Add(this.btnBlue);
            this.Controls.Add(this.btnGreen);
            this.Controls.Add(this.btnRed);
            this.Controls.Add(this.btnGrayscale);
            this.Controls.Add(this.btnAverage);
            this.Controls.Add(this.btnEdge3);
            this.Controls.Add(this.btnEmboss2);
            this.Controls.Add(this.btnEdge2);
            this.Controls.Add(this.btnEdge1);
            this.Controls.Add(this.btnHighPass2);
            this.Controls.Add(this.btnHighPass1);
            this.Controls.Add(this.btnBlur2);
            this.Controls.Add(this.btnBlur1);
            this.Controls.Add(this.btnEmboss1);
            this.Name = "Form1";
            this.Text = "vcs_ImageProcessing4";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Button btnEmboss1;
        internal System.Windows.Forms.Button btnBlur1;
        internal System.Windows.Forms.Button btnBlur2;
        internal System.Windows.Forms.Button btnHighPass1;
        internal System.Windows.Forms.Button btnHighPass2;
        internal System.Windows.Forms.Button btnEdge1;
        internal System.Windows.Forms.Button btnEdge2;
        internal System.Windows.Forms.Button btnEmboss2;
        internal System.Windows.Forms.Button btnEdge3;
        internal System.Windows.Forms.Button btnAverage;
        internal System.Windows.Forms.Button btnGrayscale;
        internal System.Windows.Forms.Button btnGreen;
        internal System.Windows.Forms.Button btnRed;
        internal System.Windows.Forms.Button btnBlue;
        internal System.Windows.Forms.Button btnInvert;
        internal System.Windows.Forms.Button btnMaximum;
        internal System.Windows.Forms.Button btnMinimum;
        internal System.Windows.Forms.Button btnPixellate;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtRank;
        internal System.Windows.Forms.Button btnPointellate;
        internal System.Windows.Forms.Button btnEmboss3;
        private System.Windows.Forms.RichTextBox richTextBox1;
        internal System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_image_process_b0;
        private System.Windows.Forms.Button bt_image_process_b1;
        private System.Windows.Forms.Button bt_image_process_b2;
        private System.Windows.Forms.Button bt_image_process_b3;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button bt_image_process_a7;
        private System.Windows.Forms.Button bt_image_process_a0;
        private System.Windows.Forms.Button bt_image_process_a6;
        private System.Windows.Forms.Button bt_image_process_a1;
        private System.Windows.Forms.Button bt_image_process_a5;
        private System.Windows.Forms.Button bt_image_process_a2;
        private System.Windows.Forms.Button bt_image_process_a4;
        private System.Windows.Forms.Button bt_image_process_a3;
        internal System.Windows.Forms.Button btnGrayscale2;
        private System.Windows.Forms.Button bt_reset;
        private System.Windows.Forms.GroupBox groupBox1;
    }
}

