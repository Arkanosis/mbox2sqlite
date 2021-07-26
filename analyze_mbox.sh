#! /bin/sh

"$(dirname "$0")/mbox2csv.py" > "/tmp/mbox-stats.csv"

sqlite3 <<EOF
.mode csv
.separator \t
.import /tmp/mbox-stats.csv stats
select sum(size)/1000000 as total, behalf from stats group by behalf order by total desc;
EOF
