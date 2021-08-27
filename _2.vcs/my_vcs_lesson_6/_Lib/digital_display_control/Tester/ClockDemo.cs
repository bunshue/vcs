using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace Tester
{
	public partial class ClockDemo : Form
	{
		public ClockDemo()
		{
			InitializeComponent();
		}

		private void ClockDemo_Load(object sender, EventArgs e)
		{

		}

		private void timer1_Tick(object sender, EventArgs e)
		{
			this.digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
		}
	}
}