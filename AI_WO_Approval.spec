# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\ccerq\\Envs\\pythonProject1\\ML_CostAnalysis\\Lib\\site-packages\\embedchain-0.1.110.dist-info', 'embedchain-0.1.110.dist-info'), ('C:\\Users\\ccerq\\OneDrive\\Documentos\\Python Scripts\\ML_CostAnalysis\\crewai\\translations\\en.json', 'crewai/translations'), ('C:\\Users\\ccerq\\OneDrive\\Documentos\\Python Scripts\\ML_CostAnalysis\\best_random_forest_model.joblib', '.')],
    hiddenimports=['embedchain', 'importlib_metadata', 'sklearn.ensemble._forest'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AI_WO_Approval',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)