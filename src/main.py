import yaml
import argparse
import os
from collector import *


                
    
                 

            


def main():
    
    

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--configmetric",
        type=str,
        dest="config_metric_path",
        default="../config/config01.yml"
        
    )

    args = parser.parse_args()

    config_metric_path = args.config_metric_path

    with open(config_metric_path) as file:
        configFile = yaml.load(file, Loader=yaml.SafeLoader)

    dgExporter = DataGuardExporter(
        configMetrics = configFile
    )

    start_http_server(9100)
    while True:
        pass
    

if __name__ == "__main__":
   main()

