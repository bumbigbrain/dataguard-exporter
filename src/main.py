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

    dgExporter = DataGuardCollector(
        configMetrics = configFile
    )

    print("SERVE EXPORTER AT PORT 9110") 
    start_http_server(9110)
    # loop fetching and serve 


    

if __name__ == "__main__":
   main()

