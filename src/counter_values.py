class CounterValues:
    last_counter = {'user':0, 
                    'news_feed':1000000, 
                    'post':1000000000 }


    def get_next(self,type):
        if type in self.last_counter.keys():
            self.last_counter[type] +=1
            return self.last_counter[type]
    def init_counters(self,counters):
        for key in counters.keys():
            self.last_counter[key] = counters[key]
        

