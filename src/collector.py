from prometheus_client import start_http_server, Gauge, Counter, Summary, Enum, Histogram, Info
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily





class Metric():


    def __init__(self, varName, query, type, description, labels):
        self.varName = varName
        self.type = type
        self.labels = labels
        self.query = query
        self.description = description 
        
                
            



class DataGuardCollector():
    
    def __init__(self, configMetrics):
       self.metrics = DataGuardCollector.initMetrics(configMetrics);
       self.showMetrics()
       
    def initMetrics(configMetrics):
        metrics = []
        for metric, prop in configMetrics["metrics"].items():
            metrics.append(Metric(
                varName = metric,
                type = prop["type"],
                query = prop["query"],
                labels = prop["labels"],
                description = prop["description"]
            ))
        
        return metrics    

    
    def showMetrics(self):
        for metric in self.metrics:
            print(metric.varName)
            print("    ", metric.type)
            print("    ", metric.description)
            print("    ", metric.labels)
            print("    ", metric.query)


    
    


        
        
            
            

        
        
        
    
    
        
                
    
                