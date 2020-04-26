#! /usr/bin/env bash

cd ../.. > /dev/null



# build vocabulary
python tools/build_vocab.py \
--count_threshold=0 \
--vocab_path='data/common/vocab.txt' \
--manifest_paths='data/common/manifest.dev-clean'

if [ $? -ne 0 ]; then
    echo "Build vocabulary failed. Terminated."
    exit 1
fi


# compute mean and stddev for normalizer
python tools/compute_mean_std.py \
--manifest_path='data/common/manifest.train' \
--num_samples=2000 \
--specgram_type='linear' \
--output_path='data/common/mean_std.npz'

if [ $? -ne 0 ]; then
    echo "Compute mean and stddev failed. Terminated."
    exit 1
fi


echo "LibriSpeech Data preparation done."
exit 0
