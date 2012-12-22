import sys
rare_engine = "C:/rosie/source_code/RARE_ENGINE"
sys.path.append(rare_engine)
from Rosie_Recommendation import *

#This gets the recommendations for all registered users
(userids,reco) = rare_recommendation()
for i in range(len(userids)):
    print "-----------------------"
    print "USER: ", userids[i]
    print "RECOMMEND PRODUCTS: ", reco[i]
    


#This can be enhanced to timely invocation
#Return userid and corresponding recommendation to frontend
