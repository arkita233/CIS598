#! /usr/bin/env bash

cd ../.. > /dev/null

# train model
# if you wish to resume from an exists model, uncomment --init_from_pretrained_model
export FLAGS_sync_nccl_allreduce=0

CUDA_VISIBLE_DEVICES=0 \
python -u train.py \
--batch_size=7 \
--num_epoch=20 \
--num_conv_layers=2 \
--num_rnn_layers=3 \
--rnn_layer_size=2048 \
--num_iter_print=100 \
--save_epoch=1 \
--num_samples=20000 \
--learning_rate=5e-4 \
--max_duration=27.0 \
--min_duration=0.0 \
--test_off=False \
--use_sortagrad=True \
--use_gru=False \
--use_gpu=True \
--is_local=True \
--share_rnn_weights=True \
--train_manifest='data/common/manifest.train' \
--dev_manifest='data/common/manifest.dev-clean' \
--mean_std_path='data/common/mean_std.npz' \
--vocab_path='data/common/vocab.txt' \
--output_model_dir='./checkpoints/comm' \
--augment_conf_path='conf/augmentation.config' \
--specgram_type='linear' \
--shuffle_method='batch_shuffle_clipped' \

if [ $? -ne 0 ]; then
    echo "Failed in training!"
    exit 1
fi


exit 0
