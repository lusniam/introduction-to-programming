# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
('idle1''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\idle1.png'),
('idle2''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\idle1.png'),
('idle3''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\idle2.png'),
('idle4''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\idle3.png'),
('atak1''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\idle4.png'),
('atak2''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak1.png'),
('atak3''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak2.png'),
('atak4''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak3.png'),
('atak5''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak4.png'),
('atak6''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak5.png'),
('atak7''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak6.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\gracz\\atak7.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak1.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak2.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak3.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak4.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak5.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak6.png'),
('''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\atak\\atak7.png'),
arena=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\arena.png')
atak=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\atak.png')
boss=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\boss.png')
miecz=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\miecz.png')
mikstura=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\mikstura.png')
mocny=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\mocny.png')
normalny=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\normalny.png')
powrot=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\powrot.png')
reset=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\reset.png')
sklep=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\sklep.png')
start=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\start.png')
staty=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\stats.png')
szybki=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\szybki.png')
tak=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\tak.png')
tawerna=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\tawerna.png')
trudny=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\trudny.png')
walka=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\walka.png')
wyjdz=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\wyjdz.png')
zbroja=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\przyciski\\zbroja.png')
arena=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\tla\\arena.png')
menu=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\tla\\menu.png')
miasto=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\tla\\miasto.png')
sklep=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\tla\\sklep.png')
tawerna=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\tla\\tawerna.png')
tlo=Tlo()
moneta=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\moneta.png')
potka=(''C:\\Users\\Windows X\\Desktop\\Zaliczenie\\potka.png')
('atak1','C:\\Users\\Windows X\\Desktop\\Zaliczenie\\mp3\\atak1.wav')
atak2('C:\\Users\\Windows X\\Desktop\\Zaliczenie\\mp3\\atak2.wav')
mikstura('C:\\Users\\Windows X\\Desktop\\Zaliczenie\\mp3\\mikstura.wav')
przycisk('C:\\Users\\Windows X\\Desktop\\Zaliczenie\\mp3\\przycisk.wav') 

a = Analysis(
    ['game.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='game',
)
