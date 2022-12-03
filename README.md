# python-file-structure-ascii-tree-manager
convert directory tree into ASCII tree string

## Method Overview
`getTree(start_path, sub_file_prefix, sub_dir_indent, start_pos_char)`

## Usage
Code Sample
```python
getTree('my-react-app',  '├─', '─', '│')
```

Print result
```
my-react-app/
│ ├─.gitignore
│ ├─package-lock.json
│ ├─package.json
│ ├─README.md
├─node_modules/
│  ├─.package-lock.json
├──.bin/
│   ├─acorn
│   ├─acorn.cmd
│   ├─acorn.ps1
│   ├─ansi-html
│   ├─ansi-html.cmd
│   ├─ansi-html.ps1
│   ├─autoprefixer
│   ├─autoprefixer.cmd
│   ├─autoprefixer.ps1
│   ├─browserslist
│   ├─browserslist-lint
│   ├─browserslist-lint.cmd
│   ├─browserslist-lint.ps1
│   ├─browserslist.cmd
│   ├─browserslist.ps1
│   ├─css-blank-pseudo
...
```
