# tensorboard
%reload_ext tensorboard

%tensorboard --logdir logs --port 6008

!kill -9 $(lsof -t -i:6008)



# downgrade python version on colab
!sudo apt-get install python3.7

!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1

!sudo update-alternatives --config python3

!sudo apt install python3-pip

!sudo apt-get install python3.7-distutils

!pip install tensorflow==1.15
