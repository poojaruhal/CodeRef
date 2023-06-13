#!/bin/sh

# pre-training
python src/evaluate.py \
--dataset-root ../dataset \
--dataset-save-dir ../dataset/dataset_saved \
--vocab-save-dir ../dataset/vocab_saved_new \
--project-name test_eval \
--logging-file-path output \
--batch-size 8 \
--eval-batch-size 8 \
--n-epoch 10 \
--n-gpu 1 \
--fp16 \
--model-name pre_train

#--increase-token-embeddings True \
