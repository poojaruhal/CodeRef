#!/bin/sh

python src/prepare_dataset.py \
--dataset-root ../dataset \
--dataset-save-dir ../dataset/dataset_saved \
--logging-file-path output
