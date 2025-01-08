%reload_ext tensorboard

%tensorboard --logdir logs --port 6008

!kill -9 $(lsof -t -i:6008)
