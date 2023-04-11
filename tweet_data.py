import csv

class TweetData:

    def __init__(self):
        self.tweet_count = 0
        self.ids = []
        self.dates = dict()
        self.polarity = dict()
        self.subjectivity = dict()
        self.place = dict()
        self.topic = dict()
        self.place_by_topic = dict()
        self.topic_by_date = dict()
        
        count = 0
        print("Starting Data Read")
        with open('/home/oaster/dissertation_server/assets/training_data.csv', 'r+', encoding="utf8") as file:
                reader = csv.reader((x.replace('\0', '') for x in file), delimiter='␟')
                headers = next(reader)
                for row in reader:
                    count += 1
                    if row[0] in self.ids:
                        continue
                    
                    if len(row) < 11:
                        continue
                    
                    self.tweet_count += 1
                    self.ids.append(row[0])                   
                    
                    self.dates[row[2]] = self.dates.get(row[2], 0) + 1
                    self.polarity[row[2]] = self.polarity.get(row[2], 0) + float(row[8])
                    self.subjectivity[row[2]] = self.subjectivity.get(row[2], 0) + float(row[9])
                    
                    self.place[row[4]] = self.place.get(row[4], 0) + 1
                    
                    self.topic[row[10]] = self.topic.get(row[10], 0) + 1
                    
                    _places = self.place_by_topic.get(row[10], dict())
                    _places[row[4]] = _places.get(row[4], 0) + 1
                    self.place_by_topic[row[10]] = _places
                    
                    _topic_date = self.topic_by_date.get(row[2], dict())
                    _topic_date[row[10]] = _topic_date.get(row[10], 0) + 1
                    self.topic_by_date[row[2]] = _topic_date
                    
        for item in self.polarity:
            self.polarity[item] = self.polarity.get(item) / self.dates.get(item)
            
        for item in self.subjectivity:
            self.subjectivity[item] = self.subjectivity.get(item) / self.dates.get(item)
            
        for item in self.place:
            clean_data = item
            if clean_data == "United States":
                clean_data = "United States of America"
            
            self.place[clean_data] = self.place.get(clean_data, 0) + 1
                
        
        print("Finishing Data Read")
                
        print(str(self.tweet_count) + " tweets avaliable.")