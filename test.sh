
# List directories.
ls -la / | python fmt-json.py -h "permissions,count,owner,group,size,day,month,time,name" -p true

# List disk mounts.
df -Ph | python fmt-json.py -h "filesystem,blocks,used,available,capacity,mounted_on" -p true -d "\s{2,}" -s 1

# List processes.
ps alx | head -n 10 | python fmt-json.py -h "user,pid,ppid,cpu,pri,ni,vsz,rss,wchan,stat,tt,time,command" -s 1 -p true
