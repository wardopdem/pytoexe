import sys, io, zipfile

def make_exe(src, out_file, exe_mod, python_path=None):
    bs = io.BytesIO()
    with zipfile.ZipFile(bs, 'w') as z:
        if isinstance(src, str):
            z.write(src, '__main__.py')
        else:
            z.writestr('__main__.py', src)
    with open(out_file, 'wb') as f:
        f.write(open(exe_mod, 'rb').read())
        if python_path is None:
            python_path = 'python.exe'
        elif python_path is True:      
            python_path = sys.executable
        f.write('#!{}\n'.format(python_path).encode())
        f.write(bs.getvalue())    
