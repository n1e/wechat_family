#!/bin/sh
name="hello,shell"
echo "hehe"
echo $name
echo ${name}isxx
for file in $(ls /);do
	echo '$file''\n'"$file"
done
string="hello,world"
echo `expr index "$string" ,`

echo ${#string}
arr[0]='test'
arr[c]='hello'
arr[xx]='world'
arr[1]='tenp'
echo ${#arr[*]}
echo ${#arr[@]}
echo ${arr[xx]}
:<<EOF
测试...
多行
EOF
