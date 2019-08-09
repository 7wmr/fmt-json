
# Load script content

FMT_JSON=$(cat <<'EOF'
  <add-script-here>
EOF
)

FMT_JSON=$(cat fmt-json.py)



# List directories.
echo '\n\n### Directories:\n\n```json'
ls -la ../ | python -c "$FMT_JSON" -h "permissions,count,owner,group,size,day,month,time_year,name" -P
echo '```'

# List disk mounts.
echo '\n\n### Disk Mounts:\n\n```json'
df -Ph | python -c "$FMT_JSON" -h "filesystem,blocks,used,available,capacity,mounted_on" -d "\s{2,}" -s 1
echo '```'

# List processes.
echo '\n\n### Processes:\n\n```json'
ps alx | head -n 10 | python -c "$FMT_JSON" -h "user,pid,ppid,cpu,pri,ni,vsz,rss,wchan,stat,tt,time,command" -s 1 -P 
echo '```'

# Environment Variables
echo '\n\n### Environment Variables:\n\n```json'
env | head -n 10 | python -c "$FMT_JSON" -h "name,value" -d "=" -P
echo '```'

# Active connections.
echo '\n\n### Connections:\n\n```json'
netstat -a | head -n 10 | python -c "$FMT_JSON" -h "protocol,receive_queue,send_queue,local_address,foreign_address,state" -s 1 -P
echo '```'


