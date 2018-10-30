#!/bin/bash
name=$1
pwd=$2
cd create_table
mysql -u${name} -p${pwd}<<EOF

source /home/n1e/wechat_family/sql/create_table/create_db_user.sql
source /home/n1e/wechat_family/sql/create_table/create_table.sql
EOF
