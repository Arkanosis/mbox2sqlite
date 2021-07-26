# mbox2sqlite [![License](https://img.shields.io/badge/license-ISC-blue.svg)](/LICENSE)

**mbox2sqlite** is a quick-and-dirty set of tools to perform SQL analysis on a mailbox (eg. Gmail mbox takeout).

There is very little engineering in there, but is works suprisingly well and while feeding the database is just fast enough (a few minutes for ~15 GiB worth of email), analyzing it with SQL is instant thanks to sqlite.

## Usage

```bash
./analyze_mbox.sh
```

## License

mbox2sqlite is copyright (C) 2021 Jérémie Roquet <jroquet@arkanosis.net> and
licensed under the ISC license.
