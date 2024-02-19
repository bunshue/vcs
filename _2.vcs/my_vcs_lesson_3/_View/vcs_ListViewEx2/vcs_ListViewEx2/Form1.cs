using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

namespace vcs_ListViewEx2
{
	/// <summary>
	/// Zusammenfassung für Form1.
	/// </summary>
	public class Form1 : System.Windows.Forms.Form
	{
		private ListViewEx listView1;
		private System.Windows.Forms.ColumnHeader columnHeader1;
		private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private RichTextBox richTextBox1;
		private System.ComponentModel.IContainer components;

		public Form1()
		{
			//
			// Erforderlich für die Windows Form-Designerunterstützung
			//
			InitializeComponent();
		}

		/// <summary>
		/// Die verwendeten Ressourcen bereinigen.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Vom Windows Form-Designer generierter Code
		/// <summary>
		/// Erforderliche Methode für die Designerunterstützung. 
		/// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.
		/// </summary>
		private void InitializeComponent()
		{
            System.Windows.Forms.ListViewItem listViewItem1 = new System.Windows.Forms.ListViewItem("Item1");
            System.Windows.Forms.ListViewItem listViewItem2 = new System.Windows.Forms.ListViewItem("Item2");
            System.Windows.Forms.ListViewItem listViewItem3 = new System.Windows.Forms.ListViewItem("Item3");
            System.Windows.Forms.ListViewItem listViewItem4 = new System.Windows.Forms.ListViewItem("Item4");
            System.Windows.Forms.ListViewItem listViewItem5 = new System.Windows.Forms.ListViewItem("Item5");
            System.Windows.Forms.ListViewItem listViewItem6 = new System.Windows.Forms.ListViewItem("Item6");
            System.Windows.Forms.ListViewItem listViewItem7 = new System.Windows.Forms.ListViewItem("Item7");
            System.Windows.Forms.ListViewItem listViewItem8 = new System.Windows.Forms.ListViewItem("Item8");
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.listView1 = new vcs_ListViewEx2.ListViewEx();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(553, 28);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(304, 414);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // listView1
            // 
            this.listView1.AllowColumnReorder = true;
            this.listView1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.listView1.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2,
            this.columnHeader3});
            this.listView1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.listView1.FullRowSelect = true;
            this.listView1.HideSelection = false;
            this.listView1.Items.AddRange(new System.Windows.Forms.ListViewItem[] {
            listViewItem1,
            listViewItem2,
            listViewItem3,
            listViewItem4,
            listViewItem5,
            listViewItem6,
            listViewItem7,
            listViewItem8});
            this.listView1.Location = new System.Drawing.Point(16, 28);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(518, 414);
            this.listView1.TabIndex = 0;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "ColumnHeader1";
            this.columnHeader1.Width = 119;
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "ColumnHeader2";
            this.columnHeader2.Width = 124;
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "ColumnHeader3";
            this.columnHeader3.Width = 121;
            // 
            // Form1
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(869, 471);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.listView1);
            this.Name = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

		}
		#endregion

		/// <summary>
		/// Der Haupteinstiegspunkt für die Anwendung.
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.EnableVisualStyles();
			Application.Run(new Form1());
		}

        private void Form1_Load(object sender, System.EventArgs e)
        {
            // Create some controls and embed them in our ListView

            /*
            // Second, a RichTextBox (slightly modified to make it non-selectable)
            ReadOnlyRichTextBox rtb = new ReadOnlyRichTextBox();
            rtb.ScrollBars = RichTextBoxScrollBars.None;
            rtb.BorderStyle = BorderStyle.None;
            rtb.WordWrap = false;
            rtb.BackColor = Color.White;
            rtb.Cursor = Cursors.Default;
            rtb.Rtf = @"{\rtf1\ansi\ansicpg1252\deff0\deflang1031{\fonttbl{\f0\fnil\fcharset0 Arial;}}{\colortbl ;\red255\green0\blue0;}\viewkind4\uc1\pard\fs14 Sample\cf1\b\fs20 Entry\cf0\par}";
            // Embed it
            listView1.AddEmbeddedControl(rtb, 2, 5);
            */

            foreach (ListViewItem i in listView1.Items)
            {
                int cnt = 123;
                i.SubItems.Add(cnt.ToString());
                //cnt = 234;
                //i.SubItems.Add(cnt.ToString());
            }

            Button btn0 = new Button();
            btn0.Text = "ClickMe0";
            btn0.BackColor = SystemColors.Control;
            btn0.Font = this.Font;
            btn0.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn0, 2, 0);

            Button btn1 = new Button();
            btn1.Text = "ClickMe1";
            btn1.BackColor = SystemColors.Control;
            btn1.Font = this.Font;
            btn1.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn1, 2, 1);


            Button btn2 = new Button();
            btn2.Text = "ClickMe2";
            btn2.BackColor = SystemColors.Control;
            btn2.Font = this.Font;
            btn2.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn2, 2, 2);


            Button btn3 = new Button();
            btn3.Text = "ClickMe3";
            btn3.BackColor = SystemColors.Control;
            btn3.Font = this.Font;
            btn3.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn3, 2, 3);


            Button btn4 = new Button();
            btn4.Text = "ClickMe4";
            btn4.BackColor = SystemColors.Control;
            btn4.Font = this.Font;
            btn4.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn4, 2, 4);


            Button btn5 = new Button();
            btn5.Text = "ClickMe5";
            btn5.BackColor = SystemColors.Control;
            btn5.Font = this.Font;
            btn5.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn5, 2, 5);





        }

		private void btn_Click(object sender, EventArgs e)
		{
            richTextBox1.Text += "ccccccc\n";
		}

		// Switch ListView View
		private void comboBox1_SelectedIndexChanged(object sender, System.EventArgs e)
		{
            listView1.View = View.Details;
		}

	}
}
