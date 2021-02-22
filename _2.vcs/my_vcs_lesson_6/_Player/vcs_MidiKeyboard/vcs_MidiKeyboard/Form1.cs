using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using MyFunc;

namespace vcs_MidiKeyboard
{
	public partial class Form1 : Form
	{
		public MidiBoard MB;
		public Form1()
		{
			InitializeComponent();
			MB = new MidiBoard(this, Keyboard1);
			comboBox1.Items.Clear();
			int i = 0;
			foreach (string x in Enum.GetNames(typeof(MidiToneType)))
			{
				comboBox1.Items.Add("(" + i.ToString("000") + ") " + x);
				i++;
			}
			comboBox1.SelectedIndex = 0;
		}

		private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
		{
			MB.Set((MidiToneType)Enum.ToObject(typeof(MidiToneType), comboBox1.SelectedIndex));
            richTextBox1.Text += "你選擇了 : " + comboBox1.Text + "\n";
		}

		private void trackBar1_ValueChanged(object sender, EventArgs e)
		{
			MB.Vol(trackBar1.Value);
		}

		private void button1_Click(object sender, EventArgs e)
		{
            richTextBox1.Text += "使用方法：字母区与数字1-7按键可用，ZAQ1由低到高Do音(C)，支持鼠标与键盘同时操作。上方可选设定音色与音量。\n";


		}

	}
}
