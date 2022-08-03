#!/usr/bin/env python3

import arrow
import textwrap
from icecream import ic
from pathlib import Path

# verbose icecream
ic.configureOutput(includeContext=True)

# env
home = Path.home()
cwd = Path.cwd()
env = Path('.env')
notes = Path('../notes').mkdir(exist_ok=True)


# TODO: settings.json args; argparse
def gen_notes(start_date):
    """
    Generates 100 markdown files under the notes directory.

    Fills in boilerplate details with the filename, day, date, and example number.
    """
    fn = 'log'
    day = 0

    example = 0
    start = arrow.get(start_date).shift(days=-1)

    for num in range(1, 101):
        day += 1
        date = start.shift(days=day).format('MMMM DD, YYYY')
        example += 1

        # file format
        md_file = Path(f'../notes/{fn}_{num}.md')

        # create file if it doesn't exist
        md_file.touch(mode=0o700, exist_ok=True)

        md_fmt = textwrap.dedent(f"""
        # 100 Days Of Code - Log

        ### Day {day}: {date} (Example {example})
        ##### (delete me or comment me out)

        **Today's Progress**: ...

        **Thoughts:** ...

        **Link to work:** [Calculator App](https://github.com/username/reponame)
        """)

        # write to file
        md_file.write_text(md_fmt, encoding='utf-8', errors=None)
        print(f'{fn}_{num}.md created')


if __name__ == '__main__':
    # ask for date, if left blank, use current date
    try:
        start_date = input('Enter date (YYYY/MM/DD): ')
        if not start_date:
            start_date = arrow.now().format('YYYY/MM/DD')
        gen_notes(start_date.format('YYYY/MM/DD'))
    except KeyboardInterrupt as k:
        print(f"\nError {k}: User canceled. Exiting...")
        exit()
