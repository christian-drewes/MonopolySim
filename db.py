from tinydb import TinyDB, Query
import os
import json
from graphs.graphs import Graph

class Database:
    def __init__(self):
        if os.path.exists('db.json'):
            print('DB exists')
            self.db = TinyDB('db.json')
        else:
            with open('propertiesData.json') as jd:
                data = json.load(jd)
            self.db = TinyDB('db.json')
            for item in data:
                self.db.insert(item)

    def incrementLanded(self, landed):
        Space = Query()
        prop = self.db.search(Space.Name == landed)
        for doc in prop:
            doc['Landed'] += 1
        self.db.write_back(prop)

    def purgeDocuments(self):
        self.db.purge()
        os.remove('db.json')

    def createGraph(self):
        name = []
        timesLanded = []
        costs = []
        rents = []
        self.removeDataPoints() # Removes All non-properties
        prop = self.db.all()
        for doc in prop:
            name.append(doc['Name'])
            timesLanded.append(doc['Landed'])
            costs.append(doc['Cost'])
            rents.append(doc['Rent'])
        timesLanded = self.convertToPercent(timesLanded)
        _graph = Graph(name, timesLanded, costs, rents)

        #_graph.barChart()
        _graph.lineChart()

    def convertToPercent(self, values):
        timesLanded = []
        total = 0
        for value in values:
            total += value
        for num in values:
            percent = (num / total) * 100
            timesLanded.append(round(percent, 2))
        return timesLanded

    def removeDataPoints(self):
        Place = Query()
        self.db.remove(Place.Name == 'Chance')
        self.db.remove(Place.Name == 'GO')
        self.db.remove(Place.Name == 'Community Chest')
        self.db.remove(Place.Name == 'Jail')
        self.db.remove(Place.Name == 'Free Parking')
        self.db.remove(Place.Name == 'GO TO Jail')
        self.db.remove(Place.Name == 'Income Tax')
        self.db.remove(Place.Name == 'Luxury Tax')
        