import platform

# -*- mode: python -*-

block_cipher = None

if platform.system() == 'Windows':
    a = Analysis(['app/__main__.py'],
                pathex=['app'],
                binaries=[('app/external/exiftool.exe','external'),('app/external/dji_thermal_sdk_v1.5_20240507','external/dji_thermal_sdk_v1.5_20240507'), ('app/external/autel', 'external/autel')],
                datas=[('resources/icons/ADIAT.ico','.'),('app/algorithms.conf','.')],
                hiddenimports=[],
                hookspath=None,
                runtime_hooks=None,
                excludes=None,
                cipher=block_cipher)
elif platform.system() == 'Darwin':
    a = Analysis(['app/__main__.py'],
                    pathex=['app'],
                    datas=[('resources/icons/ADIAT.ico','.'),('app/algorithms.conf','.')],
                    hiddenimports=[],
                    hookspath=None,
                    runtime_hooks=None,
                    excludes=None,
                    cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ADIAT',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='resources/icons/ADIAT.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ADIAT')

app = BUNDLE(coll,
             name='ADIAT.app',
             icon='resources/icons/ADIAT.ico',
             bundle_identifier=None)