# popup-learning

My crontab entry looks like this:
```bash
DISPLAY=:0
45 9-17 * * * /usr/bin/python3 /home/myusername/personal_projects/popup-learning/main.py
```

I'm on WSL ubuntu, so to get it working I also had to run:
```bash
service cron status
sudo service cron start
```
