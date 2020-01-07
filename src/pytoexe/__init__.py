from zipfile import ZipFile
import io

def make_exe(src, out_file, exe_mod):
    bs = io.BytesIO()
    with ZipFile(bs, 'w') as z: 
        if isinstance(src, str):
            z.write(src, '__main__.py')
        else:
            z.writestr('__main__.py', src)
    with open(out_file, 'wb') as f:
        f.write(open(exe_mod, 'rb').read())
        f.write('#!python.exe\n'.encode())
        f.write(bs.getvalue())    
