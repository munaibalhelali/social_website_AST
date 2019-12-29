import os
import json 
class CounterValues:
    last_counter = {'user':0, 
                    'news_feed':1000000, 
                    'post':1000000000 }

    cwd = os.getcwd()
    cwd = os.path.join(cwd,'..')  if cwd.split('/')[-1] == 'src' else cwd
    
    def get_next(self,type):
        if type in self.last_counter.keys():
            self.last_counter[type] +=1
            self.write_counters_to_file()
            return str(self.last_counter[type])
    def init_counters(self,counters):
        for key in counters.keys():
            self.last_counter[key] = counters[key]
    
    def write_counters_to_file(self):
        """This function is used to write/update counter info in the others folder"""
        with open(os.path.join(self.cwd,'data/others/counters.txt'),'w') as outputfile:
            json.dump(self.last_counter,outputfile)
            
        

