from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch


# Create your views here.

def index(request):
    return render(request,'form.html')

def submit(request):
    # tournament = request.POST['tournamentname']
    match = int(request.POST['matchname'])
    model = request.POST['modelname']
    match_id = match
    file_name=str(match_id)+'.json'
    print(model)
    import json
    with open('E:/SoccermaticsForPython-master/statsbomb/data/events/'+file_name, encoding="utf8") as data_file:
        data = json.load(data_file)

    from pandas import json_normalize
    df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

    passes = df.loc[df['type_name'] == 'Pass'].set_index('id')
    shots = df.loc[df['type_name'] == 'Shot'].set_index('id')

    if (model == "1"):  
        home_team_required = df['team_name'][0]
        away_team_required = df['team_name'][1]
        print(home_team_required,away_team_required,passes)
        # from mplsoccer.pitch import Pitch
        pitch = Pitch(pitch_type='statsbomb', pitch_color='w', line_color='#c7d5cc' ,figsize=(16, 11),constrained_layout=True, tight_layout=False )
        fig, ax = pitch.draw()
        fig.set_facecolor('#22312b')
        import matplotlib.pyplot as plt
        import numpy as np
        pitchLengthX=120
        pitchWidthY=80
        for i,shot in shots.iterrows():
            x=shot['location'][0]
            y=shot['location'][1]

            goal=shot['shot_outcome_name']=='Goal'
            team_name=shot['team_name']
            plt.gca().invert_yaxis()
            circleSize=2
            # circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12

            if (team_name==home_team_required):
                if goal:
                    shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
                    plt.text((x+1),pitchWidthY-y+1,shot['player_name'].split()[0]) 
                else:
                    shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
                    shotCircle.set_alpha(.2)
                    #plt.text((x+1),pitchWidthY-y+1,shot['player_name'].split()[0])
            elif (team_name==away_team_required):
                if goal:
                    shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
                    plt.text((pitchLengthX-x+1),y+1,shot['player_name'].split()[0]) 
                else:
                    shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")      
                    shotCircle.set_alpha(.2)
                    #plt.text((pitchLengthX-x+1),y+1,shot['player_name'].split()[0]) 
            ax.add_patch(shotCircle)
        
        
        plt.text(5,75,away_team_required + ' shots') 
        plt.text(80,75,home_team_required + ' shots') 
        fig.set_size_inches(10, 7)
        # print(shots,pitchWidthY,pitchWidthY)
        fig.savefig('E:/Django/projects/sample/static/images/shots.png', dpi=100) 

    elif (model == "2"):
        # print('condition is false')
        # df['passer'] = df['position_id']
        # df['recepient'] = df['position_id'].shift(-1)
        # average_locations = passes.groupby('passer').agg({['location'][0]:['mean'],['location'][1]:['mean','count']})
        # average_locations.columns = [['location'][0],['location'][1],'count']
        # average_locations['passer'] = average_locations.index
        # pass_between = passes.groupby(['passer','recepient']).id.count().reset_index()
        # pass_between.rename({'id':'pass_count'},axis = 'columns', inplace = True)
        # pass_between = pass_between.merge(average_locations, left_on= 'passer', right_index = True)
        # pass_between = pass_between.merge(average_locations, left_on= 'recepient', right_index = True,suffixes=['','_end'])

        # pass_between = pass_between[pass_between['pass_count']>3]
        # pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc',figsize=(16, 11), constrained_layout=True, tight_layout=False)
        # fig, ax = pitch.draw()
        # fig.set_facecolor("#22312b")

        # arrows = pitch.lines(1.2*pass_between.x,.8*pass_between.y,
        #                     1.2*pass_between.x_end,.8*pass_between.y_end,ax=ax,
        #                     lw = pass_between.pass_count*1, color = 'White',zorder =1, alpha= 0.5)
        # nodes = pitch.scatter(1.2*average_locations.x,.8*average_locations.y,s = 600,color = '#d3d3d3',
        #                     edgecolors= 'black',linewidth = 2.5, alpha = 1, ax=ax)
        # for index, row in average_locations.iterrows():
        #     pitch.annotate(int(row.passer), xy=(row.x*1.2, row.y*.8), c='Black', va='center',
        #                 ha='center', size=13, weight='bold', ax=ax)     
        # ax.set_title('Barcelona vs Valladolida', color='#dee6ea',fontsize=30)
        # fig.savefig('E:/Django/projects/sample/static/images/shots.png', dpi=100)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # import pandas as pd
        # import matplotlib as mpl

        # df = pd.read_csv('E:\mckayjohnes\github\Shotmaps-main\shotmaps.csv')

        # fig,ax= plt.subplots(figsize=(13,8.5))
        # fig.set_facecolor('#22312b')
        # ax.patch.set_facecolor('#22312b')

        # pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b',
        #             orientation='vertical', line_color='#c7d5cc',view='half',
        #             figsize=(16, 11), constrained_layout=True, tight_layout=False)
        # pitch.draw(ax=ax)
        # plt.scatter(df['x'], df['y'],c='red',s=80,alpha=0.6)
        # -*- coding: utf-8 -*-        
        import pandas as pd
        df = pd.read_csv('E:\mckayjohnes\github\ValladolidA.csv')
        df = df[df['teamId']=='Barcelona']

        df['passer'] = df['playerId']
        df['recepient'] = df['playerId'].shift(-1)

        passes = df[df['type']=='Pass']
        successful = passes[passes['outcome'] == 'Successful']

        #finding the substite time and proceeding till that occures
        subs = df[df['type'] == 'SubstitutionOff']
        subs = subs['minute']
        firstsub = subs.min()

        successful = successful[successful['minute']<firstsub]

        average_locations = successful.groupby('passer').agg({'x':['mean'],'y':['mean','count']})
        average_locations.columns = ['x','y','count']
        average_locations['passer'] = average_locations.index

        # pasr = pd.to_numeric(average_locations['passer'],downcast='integer')
        # average_locations['passer']= pasr

        pass_between = successful.groupby(['passer','recepient']).id.count().reset_index()
        pass_between.rename({'id':'pass_count'},axis = 'columns', inplace = True)

        pass_between = pass_between.merge(average_locations, left_on= 'passer', right_index = True)
        pass_between = pass_between.merge(average_locations, left_on= 'recepient', right_index = True,suffixes=['','_end'])

        pass_between = pass_between[pass_between['pass_count']>3]

        pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc',figsize=(16, 11), constrained_layout=True, tight_layout=False)
        fig, ax = pitch.draw()
        fig.set_facecolor("#22312b")

        arrows = pitch.lines(1.2*pass_between.x,.8*pass_between.y,
                            1.2*pass_between.x_end,.8*pass_between.y_end,ax=ax,
                            lw = pass_between.pass_count*1, color = 'White',zorder =1, alpha= 0.5)
        nodes = pitch.scatter(1.2*average_locations.x,.8*average_locations.y,s = 600,color = '#d3d3d3',
                            edgecolors= 'black',linewidth = 2.5, alpha = 1, ax=ax)
        for index, row in average_locations.iterrows():
            pitch.annotate(int(row.passer), xy=(row.x*1.2, row.y*.8), c='Black', va='center',
                        ha='center', size=13, weight='bold', ax=ax)

        # ax.set_title('Barcelona vs Valladolida', color='#dee6ea',fontsize=30)
        fig.set_size_inches(10, 7)    
            
            
        fig.savefig('E:/Django/projects/sample/static/images/shots.png', dpi=100)
    elif (model == "3"):
    
        pitch = Pitch(pitch_type='statsbomb', pitch_color='green', line_color='#c7d5cc' ,figsize=(16, 11),constrained_layout=True, tight_layout=False )
        fig, ax = pitch.draw()
        fig.set_facecolor('#22312b')

        import matplotlib.pyplot as plt
        pitchLengthX=120
        pitchWidthY=80

        #Looping to scatter the data
        for i,passs in passes.iterrows():
            x=passs['location'][0]
            y=passs['location'][1]    
            
            circleSize=2
            pitch.scatter(x, pitchWidthY-y, ax=ax,s=100, edgecolor='black', facecolor='cornflowerblue')

        plt.gca().invert_yaxis()
        fig.set_size_inches(10, 7)    
        
        # ax.set_title('Touches by M.Salah against spurs in 2018-19 UEFA Final',fontsize = 32)
        fig.savefig('E:/Django/projects/sample/static/images/shots.png', dpi=100)

        #print(tournament,match,model, file_name,shots )
    else:
        # from mplsoccer.pitch import Pitch
        pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc',figsize=(16, 11), constrained_layout=True, tight_layout=False)
        fig, ax = pitch.draw()
        fig.set_facecolor('#22312b')
                

        for i,pas in passes.iterrows():
            x=pas['location'][0]
            y=pas['location'][1]
            endx = pas['pass_end_location'][0]
            endy = pas['pass_end_location'][1]
        # name=pas['player_name']=='Mohamed Salah'
        # if name:
            pitch.scatter(x, y, ax=ax,s=50, edgecolor='black', facecolor='cornflowerblue')
            pitch.arrows(x,y,endx,endy, width=2,headwidth=2, headlength=2, color='#ad993c', ax=ax, label='completed passes')
            
        # ax.set_title('VVD vs Spurs', color='#dee6ea',fontsize=25)
        fig.set_size_inches(10, 7)    
        fig.savefig('E:/Django/projects/sample/static/images/shots.png', dpi=100)

    return render(request,'result.html',{fig:fig})