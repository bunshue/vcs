# -*- coding:utf-8 -*-
# file: pyDirectSound.py
#
import pywintypes									# 匯入模組
import struct
from win32com.directsound import directsound
import tkinter
import tkinter.filedialog
WAV_HEADER_SIZE = struct.calcsize('<4sl4s4slhhllhh4sl')					# 設定WAV頭
class Window:
	def __init__(self):
		self.root = root = tkinter.Tk()						# 建立元件
		buttonAdd = tkinter.Button(root, text = 'Add',
				command = self.add)
		buttonAdd.pack(side = 'left')
		buttonPlay = tkinter.Button(root, text = 'Play',
				command = self.play)
		buttonPlay.pack(side = 'left')
		buttonStop = tkinter.Button(root, text = 'Stop',
				command = self.stop)
		buttonStop.pack(side = 'left')
	def MainLoop(self):								# 進入訊息循環
		self.root.mainloop()
	def add(self):									# 加入播放檔案
		self.file = tkinter.filedialog.askopenfilename(
				title = 'Python DirectSound',
				filetypes=[('WAV', '*.wav')])
	def play(self):									# 播放檔案
		print(self.file)
		f = open(self.file, 'rb')						# 開啟檔案
		header = f.read(WAV_HEADER_SIZE)					# 讀取WAV檔案頭
		(riff, riffsize, wave, fmt, fmtsize, 
			format, nchannels, samplespersecond,
			datarate, blockalign, bitspersample, 
			data, size) =\
		struct.unpack('<4sl4s4slhhllhh4sl', header)				# 取得參數值
		print(riff, riffsize, wave, fmt, fmtsize, 
			format, nchannels, samplespersecond,
			datarate, blockalign, bitspersample, 
			data, size)
		if riff != 'RIFF' or fmtsize != 16 or fmt != 'fmt ' or data != 'data':	# 判斷檔案格式
			raise  Exception('Data Error')
		wfx = pywintypes.WAVEFORMATEX()						# 建立WAVEFORMATEX結構
		wfx.wFormatTag = format
		wfx.nChannels = nchannels
		wfx.nSamplesPerSec = samplespersecond
		wfx.nAvgBytesPerSec = datarate
		wfx.nBlockAlign = blockalign
		wfx.wBitsPerSample = bitspersample
		d = directsound.DirectSoundCreate(None, None)				# 使用DirectSound播放音效
		d.SetCooperativeLevel(None, directsound.DSSCL_PRIORITY)
		sdesc = directsound.DSBUFFERDESC()
		sdesc.dwFlags = (
				directsound.DSBCAPS_STICKYFOCUS | 
				directsound.DSBCAPS_CTRLPOSITIONNOTIFY
				)
		sdesc.dwBufferBytes = size
		sdesc.lpwfxFormat = wfx
		self.buffer = buffer = d.CreateSoundBuffer(sdesc, None)
		buffer.Update(0, f.read(size))
		buffer.Play(0)
	def stop(self):
		self.buffer.Stop()							# 停止
window = Window()
window.MainLoop()
