#!/usr/bin/env python3

import arrow
# import git
# import numpy as np
# import os
# import markdown
import pandas as pd
# import re
import textwrap
# from icecream import ic
from pathlib import Path

## verbose icecream
# ic.configureOutput(includeContext=True)

# env
home = Path.home()
cwd = Path.cwd()
now = arrow.now().format('YYYYMMDD_HHmm')
env = Path('.env')

day = 0
date = arrow.now().format('MMMM DD, YYYY')
example = 0

# ONE FILE
# # file format
# md_file = Path(f'../jrnl/log_{day}.md')

# # create file if it doesn't exist
# md_file.touch(mode=0o700, exist_ok=False)

# # write to file
# md_file.write_text(md_fmt, encoding='utf-8', errors=None)

# 100 FILES
for num in range(1, 101):
    day += 1
    date = arrow.now().shift(days=day).format('MMMM DD, YYYY')
    example += 1

    # file format
    md_file = Path(f'../notes/log_{num}.md')

    # create file if it doesn't exist
    md_file.touch(mode=0o700, exist_ok=True)

    md_fmt = textwrap.dedent(f"""\
    # 100 Days Of Code - Log

    ### Day {day}: {date} (Example {example})
    ##### (delete me or comment me out)

    **Today's Progress**: ...

    **Thoughts:** ...

    **Link to work:** [Calculator App](https://github.com/username/reponame)
    """)

    # write to file
    md_file.write_text(md_fmt, encoding='utf-8', errors=None)
    print(f'log_{num}.md created')
