def get_file_info(file_path):
    *prev_path, f_full_name = file_path.split('/')
    if len(prev_path) == 0:
        prev_path = ""
    else:
        prev_path = "/".join(prev_path)+"/"
    if '.' in f_full_name:
        *f_name, f_ext = f_full_name.split('.')
        if len(f_name) > 1:
            f_name = '.'.join(f_name)
        else:
            f_name = f_name[0]
    else:
        f_name = ""
        f_ext = f_full_name
    return prev_path, f_name, '.'+f_ext


print(get_file_info('/tmp/MarkdownNavigatorEnhanced-3.0.213.150.zip'))
