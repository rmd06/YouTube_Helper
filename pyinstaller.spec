import PyInstaller.config
PyInstaller.config.CONF['distpath'] = './'

block_cipher = None

a = Analysis(['main.py'],
             binaries=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
			 datas=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)

a.datas += [
			('assets/Ico.ico', './assets/Ico.ico', 'DATA'),
			('assets/search_icon.png', './assets/search_icon.png', 'DATA'),
			('assets/Documentation.html', './assets/Documentation.html', 'DATA'),
			('Main.ui', './Main.ui', 'DATA'),
			('dialogs/Preferences.ui', './dialogs/Preferences.ui', 'DATA'),
			('dialogs/Documentation.ui', './dialogs/Documentation.ui', 'DATA'),
			('dialogs/About.ui', './dialogs/About.ui', 'DATA'),
			('dialogs/Error.ui', './dialogs/Error.ui', 'DATA'),
			('tabs/search.ui', './tabs/search.ui', 'DATA'),
			('tabs/download.ui', './tabs/download.ui', 'DATA'),
			('tabs/import_histories.ui', './tabs/import_histories.ui', 'DATA'),
			]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          a.binaries,
          name='YouTube Helper',
          debug=False,
          strip=None,
          upx=True,
          console=True,
          icon='assets/Ico.ico')
