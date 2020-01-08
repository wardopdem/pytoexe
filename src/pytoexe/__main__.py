import sys, os, argparse, pkg_resources 
from . import make_exe

def main(argv=None):
    parser = argparse.ArgumentParser(description='Создание exe-файла из скрипта на Python (посто запуск python.exe)', formatter_class=argparse.RawTextHelpFormatter)
    src_group = parser.add_mutually_exclusive_group(required=True)
    src_group.add_argument('src', nargs='?', help='исходный файл со скриптом на языке Python')
    src_group.add_argument('-c', '--command', help='явно заданный текст программы')
    parser.add_argument('-p', '--platform', default='t32',  help='целевая платформа и тип приложения (t-консоль, w-оконное)', choices=['t32', 't64', 'w32', 'w64'])
    parser.add_argument('-o', '--out-file', help='выходной файл')
    parser.add_argument('-i', '--imbedded', action='store_true', default=False, help='использовать встроенные файлы загрузчика (иначе из пакета PIP)')
    args = parser.parse_args(argv)
    try:
        exe_mod = args.platform+'.exe'
        if args.imbedded:
           mod, res = 'pytoexe', os.path.join('exe_mods', exe_mod)             
        else:
            mod, res = 'pip', os.path.join(r'_vendor\distlib', exe_mod)
        exe_path = pkg_resources.resource_filename(mod, res)
    except:
        err = 'Ошибка: не удаётся найти файл {}'.format(exe_mod)
        if not args.imbedded:
            err += ', попробуйте использовать ключ -i/--imbedded'
        print(err)
        exit(1)
    if args.out_file:
        out_file = os.path.splitext(args.out_file)[0] + '.exe'
    elif args.src:
        out_file = os.path.splitext(args.src)[0] + '.exe'
    else:
        print('Ошибка: при заданом параметре --command обязательно задание параметра --out-file')
        exit(2)
    make_exe(args.src or args.command.encode(), out_file, exe_path)

if __name__=='__main__':
    main()