import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.utils import platform
from kivy.metrics import dp, sp
#import kivymd

import random
import clipboard 
import requests



KV = """
Screen:
    FloatLayout:
        size_hint: (1,1)
        ScrollView:
            size_hint_y:0.9
            
            pos_hint: {'x':0,'y':0.1}
            FloatLayout:
                id: main_lay
                size_hint: (1,5)
        Button:
            size_hint: 0.1,0.1
            pos_hint: {'x':0.9}
            text: "Refresh"
            on_press:app.build_feed()
        


"""

"""
tmp = [{'title':'1Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'2Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://cdn.futura-sciences.com/buildsv6/images/wide1920/6/5/2/652a7adb1b_98148_01-intro-773.jpg'},
    {'title':'3Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'4Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'5Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'6Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'7Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'8Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'9Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'10Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'},
    {'title':'11Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien arcu, egestas vel dictum nec, consequat ','img':'https://raw.githubusercontent.com/Qypol342/App_EsayReadApi/main/tmp_img.png'}]
"""
tmp = [{'title': 'Blue Origin, Rocket Lab, SpaceX, ULA win Space Force contracts for rocket technology projects', 'img': 'https://spacenews.com/wp-content/uploads/2021/09/50219312327_6aff9d5883_5k-scaled.jpg'}, {'title': 'Inside Varda Space’s plans to revolutionize in-space manufacturing', 'img': 'https://www.nasaspaceflight.com/wp-content/uploads/2021/09/photon-orbit.jpg'}, {'title': 'UN secretary-general criticizes “billionaires joyriding to space”', 'img': 'https://spacenews.com/wp-content/uploads/2021/09/unsecgen.jpg'}, {'title': 'Orbit Fab to launch propellant tanker to fuel satellites in geostationary orbit', 'img': 'https://spacenews.com/wp-content/uploads/2021/09/Screen-Shot-2021-09-23-at-3.49.32-PM.png'}, {'title': 'NASA seeks a new ride for astronauts to the Artemis launch pad', 'img': 'https://cdn.arstechnica.net/wp-content/uploads/2021/09/KSC-2011-4822_large.jpg'}, {'title': 'House committee presses NOAA on commercial weather data and space traffic management', 'img': 'https://spacenews.com/wp-content/uploads/2019/03/spire-lemur-2019.jpg'}, {'title': 'Rocket Report: Analyst dings Virgin Galactic, Astranis moves to Falcon Heavy', 'img': 'https://cdn.arstechnica.net/wp-content/uploads/2021/09/51494577685_5e3c633172_k.jpg'}, {'title': 'SpaceX’s next commercial Falcon Heavy launch to carry Astranis rideshare satellite', 'img': 'https://www.teslarati.com/wp-content/uploads/2019/04/Falcon-Heavy-Flight-2-prelaunch-041119-Pauline-Acalin-clouds-pano-1-c.jpg'}, {'title': 'Photos: Landsat 9 encapsulated inside Atlas payload shroud', 'img': 'https://mk0spaceflightnoa02a.kinstacdn.com/wp-content/uploads/2021/09/KSC-20210816-PH-RNB01_0070large-2.jpg'}, {'title': 'Northrop Grumman to launch new satellite-servicing robot aimed at commercial and government market', 'img': 'https://spacenews.com/wp-content/uploads/2021/09/CV_Capture.4k-scaled.jpg'}]





class MainApp(App):#MDApp
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_length = 42
        self.screen = Builder.load_string(KV)


    def better_text(self, text):
        splt_text = text.split(" ")
        htg_ed = []
        line_len = 0
        for i in splt_text:
            if line_len+len(i)<self.max_length:
                htg_ed.append(i)
                line_len += len(i)
            else:
                htg_ed.append("\n")
                htg_ed.append(i)
                line_len = len(i)

        regrouped = " ".join(htg_ed)
        return regrouped



  

    def random_col(self):
        return (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255,1)


    def button_callback(self,df=None):
        for i in range(len(self.btn_list)):
            if df == self.btn_list[i]:
        
                
                clipboard.copy(df.text)


                print(kivy.utils.platform)
                if  kivy.utils.platform == 'win' :
                    path = ''
                elif kivy.utils.platform == 'android' : #android.permissions = WRITE_EXTERNAL_STORAGE
                    path = '/sdcard/Download/'
                
                
                img_data = requests.get(self.btn_list_info[i]).content
                with open(path+'Twitter_image.jpg', 'wb') as handler:
                    handler.write(img_data)
                

           
       
        #self.button1.background_color=self.random_col()
        

    def build_feed(self):

       
        print(Window.size)
        self.max_length = 42*Window.size[0]*0.003
        print(self.max_length)
        self.B_S = 0.2
        self.S_S = 0.2*len(tmp)*2#with image
        self.screen.ids.main_lay.size_hint = (1,self.S_S)

        self.screen.ids.main_lay.clear_widgets()
        self.btn_list = []
        self.btn_list_info = []
        print(0,len(tmp[0]['title']))
        for i in range(len(tmp)-1,-1,-1):
            print(i)
            
            s_y = 1/(len(tmp)*2)
            
            
            b = Button(text=self.better_text(tmp[i]['title']),background_color=(self.random_col()),
             size_hint=(1,s_y), pos_hint={'y':s_y*i*2+s_y},background_normal= '', font_size=sp(15))
            b.bind(on_press=self.button_callback)
            im = AsyncImage(source=tmp[i]['img'],allow_stretch= True,size_hint_y=s_y, pos_hint={'y':s_y*(i-0.5)*2+s_y})
            


            self.screen.ids.main_lay.add_widget(b)
            self.screen.ids.main_lay.add_widget(im)
            self.btn_list.append(b)
            self.btn_list_info.append(tmp[i]['img'])

    


    def build(self):
        print("[INFO   ] [MOI         ] Build")
        self.build_feed()
        

        """

        self.button1 = Button(text='Hello world', font_size=14, background_color=(self.random_col()), size_hint=(0.5,0.5), pos_hint={'x':0.25,'y':0.25})
        self.button1.bind(on_press=self.button_callback)
        """
        
        
        return self.screen



    



if __name__ == "__main__":


    MainApp().run()
