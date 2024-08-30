#qualtrics api

import urllib.request 
import json
import uuid
import pandas as pd 

def create_block(survey_id,desc):
    payload = {
      "Type":"Standard",
      "Description":desc,
      "Options":{
        "BlockLocking":"false",
        "RandomizeQuestions":"false",
        "BlockVisibility":"Expanded"
      }
    }
    res = _send_api("post",f"https://xxxx.qualtrics.com/api/xxx/{survey_id/blocks}",payload = payload)
    block_id = res["result"]["BlockId"]
    reeturn block_id

# create OIB 
results = []
for idx,row in df.iterrows():
    if row["score"]>1:
        subset = df[df["id"]==row["id"]]
        substr_list = []
        seq = 1
        for _,subrow in subset.iterrows():
            substr_list.append(f"point {seq}=Q{subrow["number_in_oib"]}")
            seq += 1 
        substr = ",".join(substr_list)
        results.append(f"Q{row["number_in_oib"]} (total point = {row['total point']},{substr})")
    else:
        results.append(f"{row['scoring']}")

for r in results: 
    print(r)

#machine learning 
for _est in [10,50,100,200]:
    print(f"RF with {_est} trees:")
    rf_clg = RandomForestClassifier(_est, n_jobs = -1, random_state = 7).fit(x_train,y_train)
    get_prediction_precision(rf_clg,x_test,y_test)
    y_pred = rf_clg.predict(x_test)
    print(classification_report(y_test,y_pred,targeet_names= ["class 0","class 1"]))
    print(confusion_matrix(y_test,y_pred))