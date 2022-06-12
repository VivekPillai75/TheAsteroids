from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot

import plotly.express as px
#we are loading the model using pickle
model = pickle.load(open('SOI', 'rb'))

def plots(df): #should take in labelled data!!
    #processing the dataframe
    classes = df[['AFP', 'NTP', 'PC', 'UNK']]
    l = []
    for i in range(len(classes['AFP'])):
        
            if classes['AFP'][i] == 1:
                l.append('AFP')
                continue
            elif classes['NTP'][i] == 1:
                l.append('NTP')
                continue
            elif classes['PC'][i] == 1:
                l.append('PC')
                continue
            else:
                l.append('UNK')
    df['labels'] = l
    #now, labels have been created
    
    
    
    fig4=px.scatter(df,x='tce_period',y='tce_duration', color='labels')
    fig5 = px.scatter_3d(df, x='tce_eqt', y='tce_steff', z='tce_period',
                    color='labels',
                    title="3D Scatter Plot")
    fig6 = px.scatter_3d(df, x='tce_prad', y='tce_eqt', z='tce_period',
                    color='labels',
                    title="3D Scatter Plot")
    df_p=df[df['labels']=='PC']
    fig7= px.scatter(df_p,x='tce_steff',y='tce_slogg',size='tce_sradius') #df_p is for PC-only
    fig1=px.scatter(df_p,x='tce_period',y='tce_duration',size='tce_prad')
    df_count = df['labels'].value_counts().rename_axis('TEC').reset_index(name='counts')
    fig0 = px.bar(x = df_count['TEC'], y = df_count['counts'], 
                  title = 'Occurrences of Each TCE Class')
    
    plot(fig4,filename='templates\TransitDur_OrbPeriod_Scatter.html',config={'displayModeBar': False})
    plot(fig5,filename='templates\PlanTemp_StEff_OrbPer_3dscatter.html',config={'displayModeBar': False})
    plot(fig6,filename='templates\PlanRad_PlanTemp_OrbPer_3dscatter.html',config={'displayModeBar': False})
    plot(fig0,filename='templates\Category_Count.html',config={'displayModeBar': False})
    plot(fig1,filename='templates\TranDur_OrbPer_PlanRad.html',config={'displayModeBar': False})
    plot(fig7,filename='templates\StEff_SLogG_SRad_Bubble.html',config={'displayModeBar': False})
    
    
def predictor(df):
    df = df[[ 'tce_plnt_num', 'tce_period', 'tce_period_err', 'tce_time0bk',
       'tce_time0bk_err', 'tce_impact', 'tce_impact_err', 'tce_duration',
       'tce_duration_err', 'tce_depth', 'tce_depth_err', 'tce_model_snr',
       'tce_prad', 'tce_prad_err', 'tce_eqt', 'tce_eqt_err', 'tce_steff',
       'tce_steff_err', 'tce_slogg', 'tce_slogg_err', 'tce_sradius',
       'tce_sradius_err']]
    predictions=model.predict(df)
    #df['predictions']=predictions
    pred = pd.DataFrame(predictions)
    print(pred.head())
    pred = pd.concat([df, pred], axis = 1)
    pred['AFP'] = pred[0]
    pred['NTP'] = pred[1]
    pred['PC'] = pred[2]
    pred['UNK'] = pred[3]
    pred.drop([0, 1, 2, 3], inplace= True)
    return(pred)