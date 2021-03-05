import kivy.utils
from kivy.graphics import Color, Line, Ellipse
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.vector import Vector
#from doric.tiles import MapTile, SpacerTile
#from doric.map import Coordinates
#from doric.terrain import Terrain
from math import ceil
#from doric.map import Coordinates
#from doric.tiles import MapTile
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from doric.terrain import Terrain
from doric.map import Coordinates

class Tree(object):
    #global data
    #global length
    #global neighbour
    #global distance
    #global neighbour_details
    #global numerical_neighbour_details
    #global coord
    
    
    #df=pd.read_csv('tile_features.csv')
    #length=len(df)
    #data = np.genfromtxt("tile_features.csv", delimiter=',', skip_header=1,dtype={'names': ('Terrain', 'Environment', 'Elevation', 'Difficulty', 'Distance','Class'),'formats': ('i4', 'i4', 'i4', 'i4', 'f8', 'U10')})
    #data=pd.read_csv('tile_features.csv',header=1)
    #fraction_training = 0.70
    def __init__(self, row, col,data,length,neighbour,distance,neighbour_details,numerical_neighbour_details,coord):
        self.row = row
        self.col = col 
        self.data = data
        self.length = length
        self.neighbour = neighbour
        self.distance = distance
        self.neighbour_details = neighbour_details
        self.numerical_neighbour_details = numerical_neighbour_details
        self.coord = coord
    
        
    
  
    
        
    def neighbours(self):
        a0_x=(self.coord_x)+1
        a1_x=(self.coord_x)-1
        a0_y=(self.coord_y)+1
        a1_y=(self.coord_y)-1
        
        self.neighbour = []
        if(self.coord_x==0 & self.coord_y==0):
            self.neighbour.extend([(a0_x,self.coord_y),(a0_x,a0_y),(self.coord_x,a0_y)])
        elif(self.coord_x==0 & 4>self.coord_y>0):
            self.neighbour.extend([(a0_x,a1_y),(a0_x,self.coord_y),(a0_x,a0_y),(self.coord_x,a0_y),(self.coord_x,a0_y)])
        elif(self.coord_x==0 & self.coord_y==4):
            self.neighbour.extend([(a0_x,self.coord_y),(a0_x,a1_y),(self.coord_x,a1_y)])
        elif(self.coord_y==0 & 4>self.coord_x>0):
            self.neighbour.extend([(a1_x,self.coord_y),(a0_x,self.coord_y),(self.coord_x,a0_y),(a1_x,a0_y),(a0_x,a0_y)])
        elif(self.coord_y==4 & 4>self.coord_x>0):
            neighbour=[[a1_x,a1_y],[a0_x,self.coord_y],[a1_x,self.coord_y],[self.coord_x,a1_y],[a0_x,a1_y]]
        elif(self.coord_y==0 & self.coord_x==4):
            neighbour=[[a1_x,self.coord_y],[a1_x,a0_y],[self.coord_x,a0_y]]
        elif(self.coord_x==4 & 4>self.coord_y>0):        
            neighbour=[[self.coord_x,a1_y],[a1_x,a1_y],[self.coord_x,a0_y],[a1_x,self.coord_y],[a0_x,a1_y]]
        else:
            neighbour=[[self.coord_x,a1_y],[a1_x,a1_y],[self.coord_x,a0_y],[a1_x,self.coord_y],[a0_x,a1_y],[a0_x,self.coord_y]]
        #predicted=Tree.distance(neighbour,coord) 
        #return predicted
    
    
    def distance_val(self):
        
        self.distance = []
        for i in len(self.neighbour):
            self.distance.append(np.linalg.norm(self.neighbour[i],self.coord))
        #predicted=get_details(neighbour,distance)
        #return True
    
    def get_details(self):
        
        neighbour_details=[]
       
        numerical_neighbour_details=[]
        for i in len(self.neighbour):
            #neighbour_details[i]=[terrain_description,distance[i]]
            #[grass,ruins,-5,1, 1.92
            # grass,ruins,-5,1, 1.92
            #make a loop
            neighbour_details=neighbour_details.extend(Terrain.full_description,distance[i])
            numerical_neighbour_details=neighbour_details
        for i in len(numerical_neighbour_details):
            if(numerical_neighbour_details[i][0]=="grass"):
                numerical_neighbour_details[i][0]=0
            elif(numerical_neighbour_details[i][0]=="sand"):
                numerical_neighbour_details[i][0]=1
            elif(numerical_neighbour_details[i][0]=="rock"):
                numerical_neighbour_details[i][0]=2
            elif(numerical_neighbour_details[i][0]=="water"):
                numerical_neighbour_details[i][0]=3
            elif(numerical_neighbour_details[i][0]=="space"):
                numerical_neighbour_details[i][0]=5
        for i in len(numerical_neighbour_details):
            if(numerical_neighbour_details[i][1]=="empty"):
                numerical_neighbour_details[i][1]=0
            elif(numerical_neighbour_details[i][1]=="bush"):
                numerical_neighbour_details[i][1]=1
            elif(numerical_neighbour_details[i][1]=="forest"):
                numerical_neighbour_details[i][1]=2
            elif(numerical_neighbour_details[i][1]=="jungle"):
                numerical_neighbour_details[i][1]=3
            elif(numerical_neighbour_details[i][1]=="road"):
                numerical_neighbour_details[i][1]=4
            elif(numerical_neighbour_details[i][1]=="ruins"):
                numerical_neighbour_details[i][1]=5
            elif(numerical_neighbour_details[i][1]=="town"):
                numerical_neighbour_details[i][1]=6 
            elif(numerical_neighbour_details[i][1]=="city"):
                numerical_neighbour_details[i][1]=7
             
    
    @classmethod
    def decision_tree(cls,df,length,neighbour_details):

        df=pd.read_csv('tile_features.csv')
        length=len(df)
        #print(df.head())
        #df.loc[len(df)] = neighbour_details
        df2 = pd.dataFrame(neighbour_details,columns=['A','B','C','D','E'])
        #df = df.append(df2, ignore_index=True)
        
        df = df.append(df2, ignore_index=True)
        df.to_csv('tile_features.csv', mode='a', header=False)
    
        
        
        
    @classmethod   
    def splitdata_train_test(cls,data,length):
        #shuffle the numpy array
        np.random.seed(0)
        np.random.shuffle(data)
        split = int(len(data)-length)
        return data[:split], data[split:]


    #shuffle the numpy array
    @classmethod
    def generate_features_targets(cls,data):
        targets = data['Class']
    # assign selected columns to features
        features = np.empty(shape=(len(data), 5))
        features[:, 0] = data['Terrain']
        features[:, 1] = data['Distance'] # feature calculated in csv file via Excel
        features[:, 2] = data['Difficulty'] 
        features[:, 3] = data['Elevation']
        features[:, 4] = data['Environment']
        return features, targets

    # assign the last column 'Class' to targets
    

    @classmethod
    def dtc_predict_actual(cls,data,length):

        # split the data into training and testing sets using a training fraction of 0.7
        train, test = Tree.splitdata_train_test(data,length)

    # generate the feature and targets for the training and test sets
    # i.e. train_features, train_targets, test_features, test_targets
        train_features, train_targets = Tree.generate_features_targets(train)
        test_features, test_targets = Tree.generate_features_targets(test)

    # instantiate a decision tree classifier
        dtc = DecisionTreeClassifier()

    # train the classifier with the train_features and train_targets
        dtc.fit(train_features, train_targets)

    # get predictions for the test_features
        predictions = dtc.predict(test_features)

    # return the predictions and the test_targets
        return predictions, test_targets

    @classmethod
    def predicted_coordinates(cls,data,length):
        predicted_class, actual_class = Tree.dtc_predict_actual(data,length) 
        score=[]
        for i in len(predicted_class):
            if (predicted_class[i]=="Recommended"):
                score[i]= 1-[((0.4*numerical_neigbhour_data[0][i])+(0.07*numerical_neigbhour_data[0][i])+(0.13*abs(numerical_neigbhour_data[0][i]))+(0.2*numerical_neigbhour_data[0][i])+(0.2*numerical_neigbhour_data[0][i]))/10]
        position=score.index(max(score)) 
        return neighbour     

    def coordinates(self):
        
        self.coord = Coordinates.even_r_coordinate_text(self)
        
        #int_coord=[]
        #map_object = map(int,coord)
        #for i in range(0,len(coord)):
            #int_coord[i]=int(coord[i])
        coord_x=self.coord[0]
        coord_y=self.coord[1]
        #neighbour=Tree.neighbours(coord_x,coord_y,coord)
        print(neighbour)
        
        #print(Terrain.description(self))
        print(self.terr)
        
        predicted_coord= Tree.predicted_coordinates(data,length)
        return predicted_coord  









        


           


