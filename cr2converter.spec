# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cr2converter.py'],
    pathex=[],
    binaries=[],
    datas=[('cr2icon_256x256x32.png', '.'), ('CR2toX', '.')],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='cr2converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='cr2icon.icns',
)
app = BUNDLE(
    exe,
    name='cr2converter.app',
    icon='cr2icon.icns',
    bundle_identifier=None,
)
