
# List directories.
echo '\n\nDirectories:\n\n'
ls -la ../ | python fmt-json.py -h "permissions,count,owner,group,size,day,month,time,name" -P

# List disk mounts.
echo '\n\nDisk Mounts:\n\n'
df -Ph | python fmt-json.py -h "filesystem,blocks,used,available,capacity,mounted_on" -d "\s{2,}" -s 1

# List processes.
echo '\n\nProcesses:\n\n'
ps alx | head -n 10 | python fmt-json.py -h "user,pid,ppid,cpu,pri,ni,vsz,rss,wchan,stat,tt,time,command" -s 1 -P 
