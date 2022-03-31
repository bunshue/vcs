using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using GAW;

namespace AmazingExplorer
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();

			switch (amazing.Style)
			{
				case ProgressBarStyle.Blocks     : styleComboBox.SelectedIndex = 0; break;
				case ProgressBarStyle.Continuous : styleComboBox.SelectedIndex = 1; break;
				case ProgressBarStyle.Marquee    : styleComboBox.SelectedIndex = 2; break;
			}
			marqueeSpeedTextBox.Text = amazing.MarqueeAnimationSpeed.ToString();
			widthTextBox.Text = amazing.Size.Width.ToString();
			heightTextBox.Text = amazing.Size.Height.ToString();
			foreColorLabel.BackColor = amazing.ForeColor;
			backColorLabel.BackColor = amazing.BackColor;

			UpdateRange();

			switch (amazing.MazeStyle)
			{
				case AmazingProgressBar.MazeStyleType.SingleRight             : mazeStyleComboBox.SelectedIndex = 0; break;
				case AmazingProgressBar.MazeStyleType.SingleLeft              : mazeStyleComboBox.SelectedIndex = 1; break;
				case AmazingProgressBar.MazeStyleType.SingleUp                : mazeStyleComboBox.SelectedIndex = 2; break;
				case AmazingProgressBar.MazeStyleType.SingleDown              : mazeStyleComboBox.SelectedIndex = 3; break;
				case AmazingProgressBar.MazeStyleType.SplitConvergeHorizontal : mazeStyleComboBox.SelectedIndex = 4; break;
				case AmazingProgressBar.MazeStyleType.SplitConvergeVertical   : mazeStyleComboBox.SelectedIndex = 5; break;
				case AmazingProgressBar.MazeStyleType.SplitDivergeHorizontal  : mazeStyleComboBox.SelectedIndex = 6; break;
				case AmazingProgressBar.MazeStyleType.SplitDivergeVertical    : mazeStyleComboBox.SelectedIndex = 7; break;
			}

			switch (amazing.Gradient)
			{
				case AmazingProgressBar.GradientType.None    : gradientComboBox.SelectedIndex = 0; break;
                case AmazingProgressBar.GradientType.Rows    : gradientComboBox.SelectedIndex = 1; break;
                case AmazingProgressBar.GradientType.Columns : gradientComboBox.SelectedIndex = 2; break;
                case AmazingProgressBar.GradientType.Flow    : gradientComboBox.SelectedIndex = 3; break;
			}

			startColorLabel.BackColor = amazing.GradientStartColor;
			endColorLabel.BackColor = amazing.GradientEndColor;

			wallColorLabel.BackColor = amazing.WallColor;
			wallSizeTextBox.Text = amazing.WallSize.ToString();
			borderColorLabel.BackColor = amazing.BorderColor;
			borderSizeTextBox.Text = amazing.BorderSize.ToString();
			rowCountTextBox.Text = amazing.RowCount.ToString();

            borderGradientCheckBox.Checked = amazing.BorderGradient;
			borderRoundCheckBox.Checked = amazing.BorderRoundCorners;

			ytop = amazing.Top;

			UpdateControls();
        }

		private int ytop = -1;

        private void MainForm_SizeChanged(object sender, EventArgs e)
        {
			if (ytop >= 0)
			{
				amazing.Location = new Point((ClientSize.Width - amazing.Width) / 2, ytop);
			}
        }

        private void amazing_MazeChanged(object sender, EventArgs e)
        {
			infoLabel.Text = string.Format("Columns: {0}; PathLen: {1}", amazing.ColCount, amazing.PathLength);
        }

		private void UpdateSize()
		{
			amazing.Location = new Point((this.Size.Width - amazing.Size.Width) / 2, amazing.Location.Y);
		}

		private enum AutoMode { Minus3, Minus2, Minus1, Stopped, Plus1, Plus2, Plus3 };

		private AutoMode autoMode = AutoMode.Stopped;

		private void UpdateControls()
		{
			marqueeSpeedButton.Enabled = (marqueeSpeedTextBox.Text.Length > 0);
			widthButton.Enabled = (widthTextBox.Text.Length > 0);
			heightButton.Enabled = (heightTextBox.Text.Length > 0);
			startColorButton.Enabled = (minTextBox.Text.Length > 0);
			endColorButton.Enabled = (maxTextBox.Text.Length > 0);
			valueButton.Enabled = (valueTextBox.Text.Length > 0);

			wallSizeButton.Enabled = (wallSizeTextBox.Text.Length > 0);
			borderSizeButton.Enabled = (borderSizeTextBox.Text.Length > 0);
			rowCountButton.Enabled = (rowCountTextBox.Text.Length > 0);

			minus3RadioButton.Enabled = (amazing.Style != ProgressBarStyle.Marquee);
			minus2RadioButton.Enabled = (amazing.Style != ProgressBarStyle.Marquee);
			minus1RadioButton.Enabled = (amazing.Style != ProgressBarStyle.Marquee);
			stopRadioButton.Enabled   = (amazing.Style != ProgressBarStyle.Marquee);
			plus1RadioButton.Enabled  = (amazing.Style != ProgressBarStyle.Marquee);
			plus2RadioButton.Enabled  = (amazing.Style != ProgressBarStyle.Marquee);
			plus3RadioButton.Enabled  = (amazing.Style != ProgressBarStyle.Marquee);
		}

		private void UpdateRange()
		{
			minTextBox.Text = amazing.Minimum.ToString();
			maxTextBox.Text = amazing.Maximum.ToString();
			valueTextBox.Text = amazing.Value.ToString();
		}

		private bool GetIntValue(string name, string text, out int val)
		{
			val = 0;
			try
			{
				val = Convert.ToInt32(text);
			}
			catch
			{
				MessageBox.Show("Invalid " + name + " value", "ERROR");
				return false;
			}
			return true;
		}

		private bool SetColor(Label label)
		{
			ColorDialog d = new ColorDialog();
			d.Color = label.BackColor;
			if (d.ShowDialog() == DialogResult.OK)
			{
				label.BackColor = d.Color;
				return true;
			}
			return false;
		}

        private void styleComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
			switch (styleComboBox.SelectedIndex)
			{
				case 0 : amazing.Style = ProgressBarStyle.Blocks;     break;
				case 1 : amazing.Style = ProgressBarStyle.Continuous; break;
				case 2 : amazing.Style = ProgressBarStyle.Marquee;    break;
			}
			UpdateControls();
        }

        private void TextBox_TextChanged(object sender, EventArgs e)
        {
			UpdateControls();
        }

        private void marqueeSpeedButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Marquee time", marqueeSpeedTextBox.Text, out val))
			{
				try
				{
					amazing.MarqueeAnimationSpeed = val;
				}
				catch (Exception ex)
				{
					MessageBox.Show(ex.Message, "Exception");
				}
			}
			UpdateControls();
        }

        private void widthButton_Click(object sender, EventArgs e)
        {
            int val;
			if (GetIntValue("Width", widthTextBox.Text, out val))
			{
				try
				{
					amazing.Size = new Size(val, amazing.Size.Height);
				}
				catch (Exception ex)
				{
					MessageBox.Show(ex.Message, "Exception");
				}
				UpdateSize();
			}
			UpdateControls();
        }

        private void heightButton_Click(object sender, EventArgs e)
        {
            int val;
			if (GetIntValue("Height", heightTextBox.Text, out val))
			{
				try
				{
					amazing.Size = new Size(amazing.Size.Width, val);
				}
				catch (Exception ex)
				{
					MessageBox.Show(ex.Message, "Exception");
				}
				UpdateSize();
			}
			UpdateControls();
        }

        private void rotateButton_Click(object sender, EventArgs e)
        {
			int width = amazing.Height;
			int height = amazing.Width;
			int x = (ClientSize.Width - width) / 2;

			amazing.Size = new Size(width, height);
			amazing.Location = new Point(x, ytop);

			widthTextBox.Text = amazing.Size.Width.ToString();
			heightTextBox.Text = amazing.Size.Height.ToString();
        }

        private void foreColorButton_Click(object sender, EventArgs e)
        {
			if (SetColor(foreColorLabel))
			{
				amazing.ForeColor = foreColorLabel.BackColor;
			}
        }

        private void backColorButton_Click(object sender, EventArgs e)
        {
			if (SetColor(backColorLabel))
			{
				amazing.BackColor = backColorLabel.BackColor;
			}
        }

        private void minButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Minimum", minTextBox.Text, out val))
			{
				try
				{
					amazing.Minimum = val;
				}
				catch (Exception ex)
				{
					MessageBox.Show(ex.Message, "Exception");
				}
				UpdateRange();
			}
        }

        private void maxButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Maximum", maxTextBox.Text, out val))
			{
				try
				{
					amazing.Maximum = val;
				}
				catch (Exception ex)
				{
					MessageBox.Show(ex.Message, "Exception");
				}
				UpdateRange();
			}
        }

        private void valueButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Value", valueTextBox.Text, out val))
			{
				try
				{
					amazing.Value = val;
				}
				catch (Exception ex)
				{
					MessageBox.Show(ex.Message, "Exception");
				}
				UpdateRange();
			}
        }

        private void mazeStyleComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
			switch (mazeStyleComboBox.SelectedIndex)
			{
				case 0 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SingleRight;             break;
				case 1 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SingleLeft;              break;
				case 2 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SingleUp;                break;
				case 3 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SingleDown;              break;
				case 4 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SplitConvergeHorizontal; break;
				case 5 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SplitConvergeVertical;   break;
				case 6 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SplitDivergeHorizontal;  break;
				case 7 : amazing.MazeStyle = AmazingProgressBar.MazeStyleType.SplitDivergeVertical;    break;
			}
        }

        private void gradientComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
			switch (gradientComboBox.SelectedIndex)
			{
				case 0 : amazing.Gradient = AmazingProgressBar.GradientType.None;    break;
				case 1 : amazing.Gradient = AmazingProgressBar.GradientType.Rows;    break;
				case 2 : amazing.Gradient = AmazingProgressBar.GradientType.Columns; break;
				case 3 : amazing.Gradient = AmazingProgressBar.GradientType.Flow;    break;
			}
        }

        private void startColorButton_Click(object sender, EventArgs e)
        {
			if (SetColor(startColorLabel))
			{
				amazing.GradientStartColor = startColorLabel.BackColor;
			}
        }

        private void endColorButton_Click(object sender, EventArgs e)
        {
			if (SetColor(endColorLabel))
			{
				amazing.GradientEndColor = endColorLabel.BackColor;
			}
        }

        private void rowCountButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Row count", rowCountTextBox.Text, out val))
			{
				amazing.RowCount = val;
				rowCountTextBox.Text = amazing.RowCount.ToString();
			}
        }

        private void wallColorButton_Click(object sender, EventArgs e)
        {
			if (SetColor(wallColorLabel))
			{
				amazing.WallColor = wallColorLabel.BackColor;
			}
        }

        private void wallSizeButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Wall size", wallSizeTextBox.Text, out val))
			{
				amazing.WallSize = val;
				wallSizeTextBox.Text = amazing.WallSize.ToString();
			}
        }

        private void borderSizeButton_Click(object sender, EventArgs e)
        {
			int val;
			if (GetIntValue("Border size", borderSizeTextBox.Text, out val))
			{
				amazing.BorderSize = val;
				borderSizeTextBox.Text = amazing.BorderSize.ToString();
			}
        }

        private void borderColorButton_Click(object sender, EventArgs e)
        {
			if (SetColor(borderColorLabel))
			{
				amazing.BorderColor = borderColorLabel.BackColor;
			}
        }

        private void borderGradientCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            amazing.BorderGradient = borderGradientCheckBox.Checked;
        }

        private void borderRoundCheckBox_CheckedChanged(object sender, EventArgs e)
        {
			amazing.BorderRoundCorners = borderRoundCheckBox.Checked;
        }

        private void regenButton_Click(object sender, EventArgs e)
        {
			amazing.Regenerate();
        }

		private void Set(AutoMode m)
		{
			autoMode = m;

			minus3RadioButton.Checked  = (autoMode == AutoMode.Minus3);
			minus2RadioButton.Checked  = (autoMode == AutoMode.Minus2);
			minus1RadioButton.Checked  = (autoMode == AutoMode.Minus1);
			stopRadioButton.Checked    = (autoMode == AutoMode.Stopped);
			plus1RadioButton.Checked   = (autoMode == AutoMode.Plus1);
			plus2RadioButton.Checked   = (autoMode == AutoMode.Plus2);
			plus3RadioButton.Checked   = (autoMode == AutoMode.Plus3);

			if (   autoMode == AutoMode.Minus3
				|| autoMode == AutoMode.Plus3)
			{
				autoModeTimer.Interval = 50;
				autoModeTimer.Enabled = true;
			}
			else if (   autoMode == AutoMode.Minus2
					 || autoMode == AutoMode.Plus2)
			{
				autoModeTimer.Interval = 150;
				autoModeTimer.Enabled = true;
			}
			else if (   autoMode == AutoMode.Minus1
					 || autoMode == AutoMode.Plus1)
			{
				autoModeTimer.Interval = 500;
				autoModeTimer.Enabled = true;
			}
			else
			{
				autoModeTimer.Enabled = false;
			}

			UpdateControls();
		}

        private void speedChange(object sender, EventArgs e)
        {
			if      (minus3RadioButton.Checked) Set(AutoMode.Minus3);
			else if (minus2RadioButton.Checked) Set(AutoMode.Minus2);
			else if (minus1RadioButton.Checked) Set(AutoMode.Minus1);
			else if (plus1RadioButton.Checked)  Set(AutoMode.Plus1);
			else if (plus2RadioButton.Checked)  Set(AutoMode.Plus2);
			else if (plus3RadioButton.Checked)  Set(AutoMode.Plus3);
			else                                Set(AutoMode.Stopped);
        }

        private void autoModeTimer_Tick(object sender, EventArgs e)
        {
			if (   autoMode == AutoMode.Minus3
				|| autoMode == AutoMode.Minus2
				|| autoMode == AutoMode.Minus1)
			{
				if (amazing.Value > amazing.Minimum)
				{
					amazing.Value--;
				}
				else
				{
					Set(AutoMode.Stopped);
				}
			}
			if (   autoMode == AutoMode.Plus3
				|| autoMode == AutoMode.Plus2
				|| autoMode == AutoMode.Plus1)
			{
                if (amazing.Value < amazing.Maximum)
				{
                    amazing.Value++;
				}
				else
				{
					Set(AutoMode.Stopped);
				}
			}
			UpdateRange();
        }
    }
}
