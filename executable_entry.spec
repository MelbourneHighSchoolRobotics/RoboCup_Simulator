# -*- mode: python ; coding: utf-8 -*-
import os, pymunk
pymunk_dir = os.path.dirname(pymunk.__file__)
# For linux and osx support, the .dylib and .so files for chipmunk need to be copied as well.
chipmunk_libs = [
    ('chipmunk.dll', os.path.join(pymunk_dir, 'chipmunk.dll'), 'DATA'),
]

block_cipher = None


a = Analysis(['executable_entry.py'],
             pathex=['C:\\Users\\jgoer\\Documents\\GitHub\\RoboCup_Simulator'],
             binaries=[],
             datas=[
                 ('ev3sim', 'ev3sim'),
                 ('venv/Lib/site-packages/pygame_gui/data', 'pygame_gui/data'),
             ],
             hiddenimports=[
                 'opensimplex',
                 'pyperclip',
                 # Not sure why these are needed specifically. Might think that pyinstaller isn't windows and so doesn't include the packages.
                 'ev3dev2.button',
                 'ev3dev2.motor',
                 'ev3dev2.sensor.lego',
             ],
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
          [],
          exclude_binaries=True,
          name='ev3sim',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries + chipmunk_libs,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ev3sim')
