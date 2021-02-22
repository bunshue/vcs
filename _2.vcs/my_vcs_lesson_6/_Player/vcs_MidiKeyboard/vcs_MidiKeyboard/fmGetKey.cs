using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_MidiKeyboard
{
	public partial class fmGetKey : Form
	{
		public fmGetKey()
		{
			InitializeComponent();
			KeyValue = 0;
			Key = Keys.None;
		}

		public int KeyValue;
		public Keys Key;


		private void fmGetKey_KeyDown(object sender, KeyEventArgs e)
		{
			KeyValue = e.KeyValue;
			Key = e.KeyCode;
			this.Close();
		}
	}
}
