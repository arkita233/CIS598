#! /usr/bin/env bash

cd ../.. > /dev/null

# train model
# if you wish to resume from an exists model, uncomment --init_from_pretrained_model
export FLAGS_sync_nccl_allreduce=0

CUDA_VISIBLE_DEVICES=0 \
python -u train.py \
--batch_size=5 \
--num_epoch=10 \
--num_conv_layers=2 \
--num_rnn_layers=3 \
--rnn_layer_size=2048 \
--num_iter_print=100 \
--save_epoch=1 \
--num_samples=50000 \
--learning_rate=3e-4 \
--max_duration=27.0 \
--min_duration=0.0 \
--test_off=False \
--use_sortagrad=True \
--use_gru=False \
--use_gpu=True \
--is_local=True \
--share_rnn_weights=True \
--init_from_pretrained_model='./checkpoints/libri/460/epoch_5' \
--train_manifest='data/librispeech/manifest.train' \
--dev_manifest='data/librispeech/manifest.dev-clean' \
--mean_std_path='data/librispeech/mean_std.npz' \
--vocab_path='data/librispeech/vocab.txt' \
--output_model_dir='./checkpoints/libri/460_3rate' \
--augment_conf_path='conf/augmentation.config' \
--specgram_type='linear' \
--shuffle_method='batch_shuffle_clipped' \

if [ $? -ne 0 ]; then
    echo "Failed in training!"
    exit 1
fi


exit 0
