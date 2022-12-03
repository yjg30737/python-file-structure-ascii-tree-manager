import os


def getTree(start_path, sub_file_prefix, sub_dir_indent, start_pos_char):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ''
        if level > 0:
            indent += sub_file_prefix
        indent += (level-1) * sub_dir_indent
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * (level + 1)
        for f in files:
            print('{}{}{}{}'.format(start_pos_char, sub_indent, sub_file_prefix, f))