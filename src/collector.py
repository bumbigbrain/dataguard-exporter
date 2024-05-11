from prometheus_client import start_http_server, Gauge, Counter, Summary, Enum, Histogram, Info
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily
import mysql.connector
import pprint
import time







class Metric():


    def __init__(self, varName, query, type, description, labels, value, function):
        if type.lower() == "gauge":
            self.metric = Gauge(varName, description, labelnames=labels)
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


    def turnResultToDict(self, result):
        column_name = [desc[0] for desc in self.dbcursor.description] 
        data_dict = dict(zip(column_name, result[0]))
        return data_dict

            
    def toMillisec(self, value): 
        #+00 00:00:00
        mill_hour = int(value[4:6]) * 3600000
        mill_min = int(value[7:9]) * 60000
        mill_sec = int(value[10:12]) * 1000

        return mill_hour + mill_min + mill_sec
        
    
        
        
        


    def collectMetrics(self):
        while True:
            for metric, attrs in self.metrics.items():
                # now  support only gauge
                # print(metric)            
                # print(attrs.metric)
                # print(attrs.type)
                # print(attrs.description)
                
                self.dbcursor.execute(attrs.query) 
                result = self.turnResultToDict(self.dbcursor.fetchall()) 
                print(result)
                value = result[attrs.value.upper()]  
                func = attrs.function
                match func:
                    case "to_millisec":
                        value = self.toMillisec(value)
                    
                
                label = result[attrs.labels[0].upper()] 
                attrs.metric.labels(label).set(value)
                self.conn.commit()
            print("==================================")
            time.sleep(1)  

            
            
        
            
            
            
            
             

    
    


        
        
            
            

        
        
        
    
    
        
                
    
                