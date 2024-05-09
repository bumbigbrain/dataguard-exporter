from prometheus_client import start_http_server, Gauge, Counter, Summary, Enum, Histogram, Info
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily
import yaml
import argparse
import os




class DataGuardExporter():
    
    def __init__(self, configMetrics):
        self.configMetrics = configMetrics
        
                
    def iterConfigMetrics(self):
        for collector in self.configMetrics.values(): 
            query = collector["query"]
            print(query)
            for metric in collector["metrics"].values():
                v = metric
                des = metric["description"]
                type = metric["type"]
                labels = metric["labels"]
                print(v, des, type, labels)                

                
                
            

            


def main():
    
    

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--configfile",
        type=str,
        dest="configFilePath",
        default="../config/config01.yml"
        
    )

    args = parser.parse_args()

    configPath = args.configFilePath

    with open(configPath) as file:
        configFile = yaml.load(file, Loader=yaml.SafeLoader)

    dgExporter = DataGuardExporter(
        configMetrics = configFile
    )

    dgExporter.iterConfigMetrics()
    start_http_server(9100)
    while True:
        pass
    

if __name__ == "__main__":
   main()

