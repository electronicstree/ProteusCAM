# camera_overlay_gui.spec

block_cipher = None

a = Analysis(
    ['camera_overlay_gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Proteuscam.ico', '.'),  # Title bar icon
        ('camera.ico', '.'),      # App icon
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ProteusCAM',  # Name of the output EXE
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    icon='camera.ico',  # App icon
    version='file_version_info.txt'  # Version info file
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='ProteusCAM'
)
