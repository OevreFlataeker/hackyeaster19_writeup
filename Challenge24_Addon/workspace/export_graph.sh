#!/bin/bash
python models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path pre-trained-model/pipeline.config --trained_checkpoint_prefix training/model.ckpt-23542 --output_directory inference_graph
