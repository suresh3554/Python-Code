#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This session file is used to List files in the directory whose name satisfies given regular rexpressions
# Usage: python ListFilesInDirectory.py D:\ *.jpg *.py *.mp4
# Author 	: Suresh Ganiger - (ssg)
# Created On: 16-June-2015

import os
import sys
import fnmatch

def ListDirectorycontents(dir_name, dir_path, filters):
	filecount = 0;
	dirlist = [];
	filelist = [];
	if dir_name != "" :
		dir_name = dir_name + "/";
	for item in os.listdir(dir_path):
		new_path = os.path.join(dir_path,item);
		if os.path.isdir(new_path):
			dirlist.append(new_path);
		else:
			for filter in filters:
				if fnmatch.fnmatch(item,filter):
					filelist.append(dir_name + item);
					filecount = filecount + 1;

	for dir_item in dirlist:
		new_name = dir_name + os.path.basename(dir_item);
		count,list = ListDirectorycontents(new_name,dir_item,filters);
		filecount = filecount + count;
		filelist = filelist + list;

	return filecount,filelist

if __name__ == "__main__":
	arg_len = len(sys.argv);
	err = 0;
	if arg_len > 1:
		path = sys.argv[1];
		exp = [];
		if(arg_len == 2):
			exp.append("*");
		else:
			i = 2;
			while(i < arg_len):
				exp.append(sys.argv[i]);
				i = i + 1;

		if os.path.isdir(path) == True:
			print ("\nListing files  !!!\n");
			file_count, file_list = ListDirectorycontents("", path, exp);
			for item in file_list:
				print (item);
			print ("\nNumber of files found : " + str(file_count)) ;
			print ("")
		else:
			err = 1;
	else:
		err = 1;
	if(err == 1):
		print ("Usage : " + sys.argv[0] + " directory_path reg_Exp1 reg_Exp2 ...");