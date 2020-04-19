#! /usr/bin/env bash

cd ../.. > /dev/null

# download language model
cd models/lm > /dev/null
bash download_lm_en.sh
if [ $? -ne 0 ]; then
    exit 1
fi
cd - > /dev/null


# infer
CUDA_VISIBLE_DEVICES=0 \
python -u infer.py \
--num_samples=64 \
--beam_size=500 \
--num_proc_bsearch=8 \
--num_conv_layers=2 \
--num_rnn_layers=3 \
--rnn_layer_size=2048 \
--alpha=2.5 \
--beta=0.3 \
--cutoff_prob=1.0 \
--cutoff_top_n=40 \
--use_gru=False \
--use_gpu=False \
--share_rnn_weights=True \
--infer_manifest='data/tiny/manifest.test-clean' \
--mean_std_path='data/tiny/mean_std.npz' \
--vocab_path='data/tiny/vocab.txt' \
--model_path='./checkpoints/tiny/step_final' \
--lang_model_path='models/lm/common_crawl_00.prune01111.trie.klm' \
--decoding_method='ctc_beam_search' \
--error_rate_type='wer' \
--specgram_type='linear'

if [ $? -ne 0 ]; then
    echo "Failed in inference!"
    exit 1
fi


exit 0
