import os
from get_data import read_params, get_data
import argparse

def load_update_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    # df = df.drop(axis=1,columns=['Rotational speed [rpm]','Machine failure','RNF',
    #                                       'UDI','Product ID','Type','PWF','Torque [Nm]','Tool wear [min]','TWF','HDF','OSF'])
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=",",index=False)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    data = load_update_save(config_path=parsed_args.config)
