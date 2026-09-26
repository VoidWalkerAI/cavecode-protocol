# CaveCode v1.0 Scaffold

Print an Artifact Map:

```bash
python tools/scaffold/cavecode_new_card.py "My Tool" > MY-TOOL.cavecode.txt
```

Print a Repository Master Project Map:

```bash
python tools/scaffold/cavecode_new_card.py \
  --profile project "My Project" > MY-PROJECT.cavecode.txt
```

The script writes to standard output so mobile, shell, and automation workflows
can choose the destination. It does not silently create directories or files.
