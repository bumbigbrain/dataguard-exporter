from prometheus_client import start_http_server, Gauge, Counter, Summary, Enum, Histogram, Info
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily
import mysql.connector
import pprint








class Metric():


    def __init__(self, varName, query, type, description, labels, value, function):
        if type.lower() == "gauge":
            self.metric = Gauge(varName, description)
            self.varName = varName
            self.type = type
            self.query = query
            self.description = description
            self.labels = labels
            self.value = value
            self.function = function
        
        
                
            



class DataGuardCollector():
    
    def __init__(self, configMetrics, configDatabase):
       self.metrics = DataGuardCollector.registerMetrics(configMetrics);
       self.conn = DataGuardCollector.registerDatabase(configDatabase)
       self.dbcursor = self.conn.cursor();
       
    def registerMetrics(configMetrics):
        metrics = {}
        for metric, prop in configMetrics["metrics"].items():
            metrics[metric] = (Metric(
                varName = metric,
                type = prop["type"],
                query = prop["query"],
                labels = prop["labels"],
                description = prop["description"],
                value = prop["value"],
                function = prop["function"],
            ))
        
        return metrics    


    def registerDatabase(configDatabase):
        databaseInfo = configDatabase["database"]
        return mysql.connector.connect(
            user = databaseInfo["user"],
            password = databaseInfo["password"],
            host = databaseInfo["host"],
            port = databaseInfo["port"],
            database = databaseInfo["database"]
        )

    
    def showMetrics(self):
        for key, value in self.metrics.items():
            print(key)
            print(value.__dict__)
            
    def testingQuery(self):
        query = "SELECT * FROM V$DATAGUARD_STATS"
        self.dbcursor.execute(query)
        result = self.dbcursor.fetchall()
        print(result)


    def collectMetrics(self):
        for metric, attrs in self.metrics.items():
            print(metric)            
            print(attrs)
             

    
    


        
        
            
            

        
        
        
    
    
        
                
    
                