# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['eword_tkinter3.py'],
             pathex=['C:\\Python自學聖經_第二版\\本書範例\\ch36\\eword_tkinter3'],
             binaries=[],
             datas=[('eword.txt','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='eword_tkinter3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
