# tensorboard
%reload_ext tensorboard

%tensorboard --logdir logs --port 6008

!kill -9 $(lsof -t -i:6008)


###################################################### code correction
from tensorboard.plugins import projector

projector_config = projector.ProjectorConfig()
# projector_config = tf.compat.v1.summary.ProjectorConfig()
embedding_config = projector_config.embeddings.add()
embedding_config.tensor_name = "embedding/.ATTRIBUTES/VARIABLE_VALUE"
embedding_config.metadata_path = metadata_file
tf.compat.v1.disable_eager_execution()  # to use old summary writer
summary_writer = tf.compat.v1.summary.FileWriter(embedding_log_dir)
projector.visualize_embeddings(summary_writer, projector_config)
print("Run `tensorboard --logdir=./logs` to visualize the embedding in TensorBoard projector.")
summary_writer.close()
###################################################### 

###################################################### not working TF==2.11
# tf.keras.utils.Progbar
# # Set up config for the projector
# config = tf.compat.v1.keras.utils.progbar_utils.ProgbarConfig(
#     embeddings=[
#         tf.compat.v1.keras.utils.ProgbarConfig.Embedding(
#             tensor_name='embedding/.ATTRIBUTES/VARIABLE_VALUE',
#             metadata_path='metadata.tsv',
#         )
#     ]
# )

# with open(os.path.join(logdir, 'projector_config.pbtxt'), 'w') as f:
#     f.write(str(config))
######################################################




###################################################### ###################################################### ###################################################### ------------------



# downgrade python version on colab
!sudo apt-get install python3.7

!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1

!sudo update-alternatives --config python3

!sudo apt install python3-pip

!sudo apt-get install python3.7-distutils

!pip install tensorflow==1.15
