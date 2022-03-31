using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using GAW;

namespace AmazingExamples
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();

			// This line is here because designer keeps removing it.
			// Sigh ... sometimes software can be too smart...
            this.amazingProgressBar4.Style = System.Windows.Forms.ProgressBarStyle.Blocks;

			Set(UpdateMode.Stopped);
        }

		private enum UpdateMode { Minus3, Minus2, Minus1, Stopped, Plus1, Plus2, Plus3 };

		private UpdateMode updateMode = UpdateMode.Stopped;

		private void Set(UpdateMode m)
		{
			updateMode = m;

			minus3RadioButton.Checked  = (updateMode == UpdateMode.Minus3);
			minus2RadioButton.Checked  = (updateMode == UpdateMode.Minus2);
			minus1RadioButton.Checked  = (updateMode == UpdateMode.Minus1);
			stopRadioButton.Checked    = (updateMode == UpdateMode.Stopped);
			plus1RadioButton.Checked   = (updateMode == UpdateMode.Plus1);
			plus2RadioButton.Checked   = (updateMode == UpdateMode.Plus2);
			plus3RadioButton.Checked   = (updateMode == UpdateMode.Plus3);

			if (   updateMode == UpdateMode.Minus3
				|| updateMode == UpdateMode.Plus3)
			{
				updateTimer.Interval = 50;
				updateTimer.Enabled = true;
			}
			else if (   updateMode == UpdateMode.Minus2
					 || updateMode == UpdateMode.Plus2)
			{
				updateTimer.Interval = 100;
				updateTimer.Enabled = true;
			}
			else if (   updateMode == UpdateMode.Minus1
					 || updateMode == UpdateMode.Plus1)
			{
				updateTimer.Interval = 250;
				updateTimer.Enabled = true;
			}
			else
			{
				updateTimer.Enabled = false;
			}
		}

        private void speedChanged(object sender, EventArgs e)
        {
			if      (minus3RadioButton.Checked) Set(UpdateMode.Minus3);
			else if (minus2RadioButton.Checked) Set(UpdateMode.Minus2);
			else if (minus1RadioButton.Checked) Set(UpdateMode.Minus1);
			else if (plus1RadioButton.Checked)  Set(UpdateMode.Plus1);
			else if (plus2RadioButton.Checked)  Set(UpdateMode.Plus2);
			else if (plus3RadioButton.Checked)  Set(UpdateMode.Plus3);
			else                                Set(UpdateMode.Stopped);
        }

        private void updateTimer_Tick(object sender, EventArgs e)
        {
			if (   updateMode == UpdateMode.Minus3
				|| updateMode == UpdateMode.Minus2
				|| updateMode == UpdateMode.Minus1)
			{
				if (amazingProgressBar1.Value > amazingProgressBar1.Minimum)
				{
					SetValue(amazingProgressBar1.Value - 1);
				}
				else
				{
					Set(UpdateMode.Stopped);
				}
			}
			if (   updateMode == UpdateMode.Plus3
				|| updateMode == UpdateMode.Plus2
				|| updateMode == UpdateMode.Plus1)
			{
				if (amazingProgressBar1.Value < amazingProgressBar1.Maximum)
				{
					SetValue(amazingProgressBar1.Value + 1);
				}
				else
				{
					Set(UpdateMode.Stopped);
				}
			}
        }

		private void SetValue(int value)
		{
			SetValue(amazingProgressBar1, value);
			SetValue(amazingProgressBar2, value);
			SetValue(amazingProgressBar3, value);
			SetValue(amazingProgressBar4, value);
			SetValue(amazingProgressBar5, value);
			SetValue(amazingProgressBar6, value);
			SetValue(amazingProgressBar7, value);
		}

		private void SetValue(AmazingProgressBar amazing, int value)
		{
			if (value >= amazing.Minimum && value <= amazing.Maximum)
			{
				amazing.Value = value;
			}
		}
    }
}
