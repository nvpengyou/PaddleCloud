# -*- coding: utf-8 -*-
import argparse
import paddle
from plsc import Entry
import zip_reader as reader

parser = argparse.ArgumentParser()
parser.add_argument("--data_dir",
                    type=str,
                    default="./train_data",
                    help="Directory for datasets.")
parser.add_argument("--model_dir",
                    type=str,
                    default="./saved_model",
                    help="Directory for datasets.")
args = parser.parse_args()


def main():
    global args
    ins = Entry()
    ins.set_dataset_dir(args.data_dir)
    train_reader = reader.arc_train(args.data_dir)
    # Batch the above samples;
    batched_train_reader = paddle.batch(train_reader,
                                        ins.train_batch_size)
    # Set the reader to use during training to the above batch reader.
    ins.train_reader = batched_train_reader

    ins.set_train_epochs(1)
    print("model_dir is {0}".format(args.model_dir))
    ins.set_model_save_dir(args.model_dir)
    ins.set_with_test(False)
    ins.set_loss_type('arcface')
    ins.train()


if __name__ == "__main__":
    main()
