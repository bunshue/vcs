using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.InteropServices;

namespace MyFunc
{
	/// <summary>
	/// 乐器音色代码列表
	/// </summary>
	public enum MidiToneType
	{
		大钢琴 = 0,
		亮音大钢琴 = 1,
		电钢琴 = 2,
		酒吧钢琴 = 3,
		练习音钢琴 = 4,
		合唱加钢琴 = 5,
		拨弦古钢琴 = 6,
		击弦古钢琴 = 7,
		钢片琴 = 8,
		钟琴 = 9,
		八音盒 = 10,
		电颤琴 = 11,
		马林巴 = 12,
		木琴 = 13,
		管钟 = 14,
		扬琴 = 15,
		击杆风琴 = 16,
		打击型风琴 = 17,
		摇滚风琴 = 18,
		管风琴 = 19,
		簧风琴 = 20,
		手风琴 = 21,
		口琴 = 22,
		探戈手风琴 = 23,
		尼龙弦吉他 = 24,
		钢弦吉他 = 25,
		爵士乐电吉他 = 26,
		清音电吉他 = 27,
		弱音电吉他 = 28,
		驱动音效吉他 = 29,
		失真音效吉他 = 30,
		吉他泛音 = 31,
		原声贝司 = 32,
		指拨电贝司 = 33,
		拨片拨电贝司 = 34,
		无品贝司 = 35,
		击弦贝司1 = 36,
		击弦贝司2 = 37,
		合成贝司1 = 38,
		合成贝司2 = 39,
		小提琴 = 40,
		中提琴 = 41,
		大提琴 = 42,
		低音提琴 = 43,
		弦乐震音 = 44,
		弦乐拨奏 = 45,
		竖琴 = 46,
		定音鼓 = 47,
		弦乐合奏1 = 48,
		弦乐合奏2 = 49,
		合成弦乐1 = 50,
		合成弦乐2 = 51,
		合唱啊音 = 52,
		人声嘟音 = 53,
		合成人声 = 54,
		乐队打击乐 = 55,
		小号 = 56,
		长号 = 57,
		大号 = 58,
		弱音小号 = 59,
		圆号 = 60,
		铜管组 = 61,
		合成铜管1 = 62,
		合成铜管2 = 63,
		高音萨克斯 = 64,
		中音萨克斯 = 65,
		次中音萨克斯 = 66,
		上低音萨克斯 = 67,
		双簧管 = 68,
		英国管 = 69,
		大管 = 70,
		单簧管 = 71,
		短笛 = 72,
		长笛 = 73,
		竖笛 = 74,
		排笛 = 75,
		吹瓶口 = 76,
		尺八 = 77,
		哨 = 78,
		洋埙 = 79,
		合成主音1方波 = 80,
		合成主音2锯齿波 = 81,
		合成主音3汽笛风琴 = 82,
		合成主音4吹管 = 83,
		合成主音5吉他 = 84,
		合成主音6人声 = 85,
		合成主音7五度 = 86,
		合成主音8低音加主音 = 87,
		合成柔音1新时代 = 88,
		合成柔音暖音 = 89,
		合成柔音3复合成 = 90,
		合成柔音4合唱 = 91,
		合成柔音5弓弦 = 92,
		合成柔音6金属 = 93,
		合成柔音7光环 = 94,
		合成柔音8扫弦 = 95,
		合成特效1雨 = 96,
		合成特效2音轨 = 97,
		合成特效3水晶 = 98,
		合成特效4大气 = 99,
		合成特效5亮音 = 100,
		合成特效6小妖 = 101,
		合成特效7回声 = 102,
		合成特效8科幻 = 103,
		锡塔尔 = 104,
		班卓 = 105,
		三味线 = 106,
		筝 = 107,
		卡林巴 = 108,
		风笛 = 109,
		古提琴 = 110,
		唢呐 = 111,
		铃铛 = 112,
		拉丁打铃 = 113,
		钢鼓 = 114,
		木块 = 115,
		太鼓 = 116,
		嗵鼓 = 117,
		合成鼓 = 118,
		镲波形反转 = 119,
		磨弦声 = 120,
		呼吸声 = 121,
		海浪声 = 122,
		鸟鸣声 = 123,
		电话铃声 = 124,
		直升机声 = 125,
		鼓掌声 = 126,
		枪声 = 127
	}

	/// <summary>
	/// 连接Winmm.dll库
	/// </summary>
	public class MidiBase
	{

		[DllImport("winmm.dll")]
		private static extern UInt32 midiOutShortMsg(UInt32 hMidiOut, UInt32 dwMsg);

		[DllImport("winmm.dll")]
		private static extern UInt32 midiOutOpen(out UInt32 lphMidiOut, uint uDeviceID, UInt32 dwCallback, UInt32 dwInstance, UInt32 dwFlags);

		[DllImport("winmm.dll")]
		private static extern UInt32 midiOutReset(UInt32 hMidiOut);

		[DllImport("winmm.dll")]
		private static extern UInt32 midiOutClose(UInt32 hMidiOut);

		private UInt32 lphMidiOut;

		private byte volume;
		private bool isopen;

		/// <summary>
		/// 音量信息（0-127）
		/// </summary>
		public byte Volume
		{
			get { return volume; }
			set { if (value >= 0 && value <= 127) volume = value; }
		}

		/// <summary>
		/// 是否已成功打开通道
		/// </summary>
		public bool isOpen
		{
			get { return isopen; }
		}

		/// <summary>
		/// 始始化
		/// </summary>
		public MidiBase()
		{
			UInt32 r = midiOutOpen(out lphMidiOut, 0, 0, 0, 0);
			isopen = (r == 0);
			volume = 96;
		}

		/// <summary>
		/// 构析时关闭winmm调用
		/// </summary>
		~MidiBase()
		{
			if (isOpen) midiOutClose(lphMidiOut);
		}

		/// <summary>
		/// 直接发送消息
		/// </summary>
		/// <param name="dwMsg">消息内容</param>
		public void PostMessage(UInt32 dwMsg)
		{
			if (isOpen) midiOutShortMsg(lphMidiOut, dwMsg);
		}

		/// <summary>
		/// 按键按下
		/// </summary>
		/// <param name="chn">频道</param>
		/// <param name="vol">音量</param>
		/// <param name="scl">音阶</param>
		public void Down(byte chn, byte vol, byte scl)
		{
			var x = volume * 65536 + scl * 256 + 144 + chn;
			if (isopen) PostMessage((UInt32)x);
		}

		/// <summary>
		/// 接键按下
		/// </summary>
		/// <param name="scl">音阶</param>
		public void Down(byte scl)
		{
			this.Down(0, this.volume, scl);
		}

		/// <summary>
		/// 按键按下
		/// </summary>
		/// <param name="chn">频道</param>
		/// <param name="scl">音阶</param>
		public void Down(byte chn, byte scl)
		{
			this.Down(chn, this.volume, scl);
		}

		/// <summary>
		/// 取消发音
		/// </summary>
		/// <param name="chn">频道</param>
		/// <param name="scl">音阶</param>
		public void Up(byte chn, byte scl)
		{
			var x = scl * 256 + 128 + chn;
			if (isopen) PostMessage((UInt32)x);
		}

		/// <summary>
		/// 取消发音
		/// </summary>
		/// <param name="scl">音阶</param>
		public void Up(byte scl)
		{
			this.Up(0, scl);
		}

		/// <summary>
		/// 设定乐器音色
		/// </summary>
		/// <param name="timbre">音色</param>
		/// <param name="chn">频道</param>
		public void SetTimbre(byte timbre, byte chn)
		{
			var x = timbre * 256 + 192 + chn;
			if (isopen) PostMessage((UInt32)x);
		}

		/// <summary>
		/// 设定乐器音色
		/// </summary>
		/// <param name="timbre">音乐</param>
		public void SetTimbre(byte timbre)
		{
			this.SetTimbre(timbre, 0);
		}
	}
}
