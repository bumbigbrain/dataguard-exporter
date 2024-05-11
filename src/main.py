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
        default="../configs-metric/config03.yml"
        
    )

    parser.add_argument(
        "--configdatabase",
        type=str,
        dest="config_database_path",
        default="../configs-database/config01.yml"
        
    )


    args = parser.parse_args()

    config_metric_path = args.config_metric_path
    config_database_path = args.config_database_path

    with open(config_metric_path) as file:
        configMetricsFile = yaml.load(file, Loader=yaml.SafeLoader)

    with open(config_database_path) as file:
        configDatabaseFile = yaml.load(file, Loader=yaml.SafeLoader)

    dgCollector = DataGuardCollector(
        configMetrics = configMetricsFile,
        configDatabase = configDatabaseFile
        
    )

    print("SERVE EXPORTER AT PORT 9110") 
    start_http_server(9110)
    dgCollector.testingQuery()
    # loop fetching and serve 


    

if __name__ == "__main__":
   main()

