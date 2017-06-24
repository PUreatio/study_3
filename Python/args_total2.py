# -*- coding: utf-8 -*-
import sys

print "process start"

try:
	# 起動引数を取得する。
	args = sys.argv
	print args

	# 先頭はファイル名のため、2番目以降の引数を取得する。
	start_args = map(lambda x: int(x), args[1:])
	print start_args

	# 奇数番目の引数のみ対象として取得する。
	odd_args = [x for x in start_args if x % 2 == 1]
	print odd_args

	# 引数を全て加算する。
	total = reduce((lambda x, y: x + y), odd_args)

	# 結果を出力する。
	print "total : %d" % (total)
except Exception, e:
	print e
else:
	print "process end!"