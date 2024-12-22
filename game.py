def l():
    for a in range(0,700,50):
        pygame.draw.line(screen,red,(a,0),(a,700),1)
    for a in range(0,700,50):
        pygame.draw.line(screen,red,(0,a),(700,a),1)
    pygame.display.update()
    
#importing modules
import pygame
pygame.init()
import pygame.mixer
pygame.mixer.init()

#defining a screen surface
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Car Driving Simulation")


                                                            #---loading screen---
#loading files
while True:
    #initialising the required colours
    black,white=(0,0,0),(250,250,250)
    red,dark_red=(250,0,0),(150,0,0)
    green=(0,150,0)
    dark_grey=(90,90,90)
    light_grey=(150,150,150)
    surface_color,outline_color,background_color,border_color=(239,221,111),(96,61,2),(205,133,63),(128,0,0)
    #loading the images
    while True:
        #openning image
        openning_image=pygame.image.load("D:\\Car Driving Simulation\\images\\road crash game openning image.jpg")
        #roads
        road_image=pygame.image.load("D:\\Car Driving Simulation\\images\\road image.png")
        #houses
        house1_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 1.jpg")
        house2_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 2.jpg")
        house3_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 3.jpg")
        house4_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 4.jpg")
        house5_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 5.jpg")
        house6_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 6.jpg")
        house7_image=pygame.image.load("D:\\Car Driving Simulation\\images\\house images\\house 7.png")
        #trees
        tree1_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 1.png")
        tree2_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 2.png")
        tree3_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 3.png")
        tree4_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 4.png")
        tree5_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 5.png")
        tree6_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 6.png")
        tree7_image=pygame.image.load("D:\\Car Driving Simulation\\images\\tree images\\tree 7.png")
        #cars
        car1_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\red car image.png")
        car2_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\green car image.png")
        car3_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\blue car image.png")
        car4_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\dark green car image.png")
        car5_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\yellowish green car image.png")
        car6_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\yellow car.png")
        car7_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\grey car image.png")
        car8_image=pygame.image.load("D:\\Car Driving Simulation\\images\\vehicle images\\car images\\dark blue car image.png")
        #car parts
        accelerator_image=pygame.image.load("D:\\Car Driving Simulation\\images\\car parts images\\accelerator image.png")
        brake_image=pygame.image.load("D:\\Car Driving Simulation\\images\\car parts images\\brake image.png")
        clutch_image=pygame.image.load("D:\\Car Driving Simulation\\images\\car parts images\\clutch image.png")
        stearing_image=pygame.image.load("D:\\Car Driving Simulation\\images\\car parts images\\stearing image.png")
        break
    #resizing the loaded images
    while True:
        openning_image=pygame.transform.scale(openning_image,(700,700))
        #road
        road_image=pygame.transform.scale(road_image,(1000,1000))
        #houses
        house1_image=pygame.transform.scale(house1_image,(100,100))
        house2_image=pygame.transform.scale(house2_image,(100,100))
        house3_image=pygame.transform.scale(house3_image,(100,100))
        house4_image=pygame.transform.scale(house4_image,(100,100))
        house5_image=pygame.transform.scale(house5_image,(100,100))
        house6_image=pygame.transform.scale(house6_image,(100,100))
        house7_image=pygame.transform.scale(house7_image,(100,100))
        #trees
        tree1_image=pygame.transform.scale(tree1_image,(40,40))
        tree7_image=pygame.transform.scale(tree7_image,(30,30))
        #cars
        car_image=pygame.transform.scale(car8_image,(40,80))
        #car parts
        accelerator_image=pygame.transform.scale(accelerator_image,(30,70))
        brake_image=pygame.transform.scale(brake_image,(30,70))
        clutch_image=pygame.transform.scale(clutch_image,(30,70))
        stearing_image=pygame.transform.scale(stearing_image,(100,100))
        break
    #defining essential fuctions
    while True:
        #defining function for rotating objects
        def rotate_on_axis(surface,size,angle,position):
            box = [pygame.math.Vector2(p) for p in [(0, 0), (size[0], 0), (size[0], -size[1]), (0, -size[1])]]
            box_rotate = [p.rotate(angle) for p in box]
            min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
            max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
            pivot = pygame.math.Vector2(size[0]/2, -size[1]/2)
            pivot_rotate = pivot.rotate(angle)
            pivot_move   = pivot_rotate - pivot
            origin = (position[0] + min_box[0] - pivot_move[0], position[1] - max_box[1] + pivot_move[1])
            rotated_surface = pygame.transform.rotate(surface, angle)
            screen.blit(rotated_surface, origin)
        #defining function for adding text
        def add_text(word,size,position,bg_color,color):
            font=pygame.font.SysFont("Calibri",size) 
            text=font.render(word,True,color,bg_color)
            screen.blit(text,position)
        #defining fuction for borders
        def border():
            pygame.draw.rect(screen,border_color,(0,0,700,700),10)
            pygame.draw.rect(screen,black,(0,0,700,700),2)
            pygame.draw.rect(screen,black,(10,10,680,680),2)
        #defining fuction for shading surfaces
        def shade(surface_size,position,transperancy):
            surface_object=pygame.Surface(surface_size)
            surface_object.set_alpha(transperancy)
            screen.blit(surface_object,position)
        #defining function for opening screen
        def openning_screen():
            #pasting the openning image
            screen.blit(openning_image,(0,0))
            #designing buttons
                #--play button
            pygame.draw.rect(screen,outline_color,(550,50,100,50))
            pygame.draw.rect(screen,black,(550,50,100,50),2)
            pygame.draw.rect(screen,surface_color,(555,55,90,40),border_radius=5)
            pygame.draw.rect(screen,black,(555,55,90,40),2,border_radius=5)
            add_text("  Play",30,(560,60),surface_color,black)
            #bordering
            border()
        #defining function for second screen(car selection screen)
        def car_selection_screen(car_options_pos):
            #filling the screen with background colour
            screen.fill(background_color)
            #showing the car options and designing buttons for moving options
                #---previous cars
            pre_pos=car_options_pos-1
            if pre_pos>0:
                pygame.draw.rect(screen,outline_color,(75,225,150,150))
                pygame.draw.rect(screen,black,(75,225,150,150),2)
                pygame.draw.rect(screen,surface_color,(80,230,140,140),border_radius=10)
                pygame.draw.rect(screen,black,(80,230,140,140),2,border_radius=10)
                screen.blit(pygame.transform.scale(car_options[pre_pos][0],(50,100)),(125,250))
                shade((150,150),(75,225),150)
                #---selected cars
            pygame.draw.rect(screen,outline_color,(250,150,200,400))
            pygame.draw.rect(screen,black,(250,150,200,400),2)
            pygame.draw.rect(screen,surface_color,(260,160,180,380),border_radius=20)
            pygame.draw.rect(screen,black,(260,160,180,380),2,border_radius=20)
            screen.blit(pygame.transform.scale(car_options[car_options_pos][0],(100,200)),(300,175))
            add_text("Car: "+car_options[car_options_pos][1],15,(265,400),surface_color,black)
            add_text("Maximum gear: "+str(car_options[car_options_pos][2]),15,(265,425),surface_color,black)
            add_text("Maximum speed: "+str(car_options[car_options_pos][5])+" Kmph",15,(265,450),surface_color,black)
            add_text("Engine rating: "+str(car_options[car_options_pos][3])+"/5",15,(265,475),surface_color,black)
            add_text("Brake rating: "+str(car_options[car_options_pos][4])+"/5",15,(265,500),surface_color,black)
                #---next cars
            post_pos=car_options_pos+1
            if post_pos<=len(car_options):
                pygame.draw.rect(screen,outline_color,(475,225,150,150))
                pygame.draw.rect(screen,black,(475,225,150,150),2)
                pygame.draw.rect(screen,surface_color,(480,230,140,140),border_radius=10)
                pygame.draw.rect(screen,black,(480,230,140,140),2,border_radius=10)
                screen.blit(pygame.transform.scale(car_options[post_pos][0],(50,100)),(525,250))
                shade((150,150),(475,225),150)
            #designing buttons
                #---"<" button
            if pre_pos>0:
                add_text("<",50,(25,300),background_color,black)
                #---">" button
            if post_pos<=len(car_options):
                add_text(">",50,(650,300),background_color,black)
                #--- select button
            pygame.draw.rect(screen,outline_color,(300,600,100,50))
            pygame.draw.rect(screen,black,(300,600,100,50),2)
            pygame.draw.rect(screen,surface_color,(305,605,90,40),border_radius=5)
            pygame.draw.rect(screen,black,(305,605,90,40),2,border_radius=5)
            add_text("Select",33,(310,610),surface_color,black)
            #bordering
            border()
        break
    #finding rect points for buttons
    while True:
        #play button
        play_button_size=(100,50)
        play_button_position=(550,50)
        play_button=pygame.draw.rect(screen,black,(550,50,100,50))
        #previous car button "<"
        pre_button_size=(50,100)
        pre_button_position=(25,300)
        pre_button=pygame.draw.rect(screen,black,(25,300,50,100))
        #next car button ">"
        post_button_size=(50,100)
        post_button_position=(650,300)
        post_button=pygame.draw.rect(screen,black,(650,300,50,100))
        #select button
        select_button_size=(100,50)
        select_button_position=(300,600)
        select_button=pygame.draw.rect(screen,black,(300,600,100,50))
        #change car button
        change_car_button_size=(100,50)
        change_car_button_position=(25,625)
        change_car_button=pygame.draw.rect(screen,black,(25,625,100,50))
        break
    #creating a surfaces for game
    while True:
        #openning screen surface
        openning_screen()
        openning_screen_copy=screen.copy()
        #car selection screen surfaces
        car_options={1:[car1_image,"Classic",4,1,3,80],2:[car2_image,"Snake",4,1,4,80],3:[car3_image,"Style",5,1,2,100],
                     4:[car4_image,"Swift",5,3,2,100],5:[car5_image,"Yellgreen",5,4,3,100],6:[car6_image,"Smart",5,3,3,100],
                     7:[car7_image,"Eagle",6,3,5,120],8:[car8_image,"Superior",6,5,1,120]}
        car_selection_screen_surfaces={}
        for z in range(1,len(car_options)+1,1):
            car_selection_screen(z)
            pygame.draw.rect(screen,outline_color,(25,25,400,75),border_radius=10)
            pygame.draw.rect(screen,black,(25,25,400,75),2,border_radius=10)
            pygame.draw.rect(screen,surface_color,(35,35,380,55),border_radius=10)
            pygame.draw.rect(screen,black,(35,35,380,55),2,border_radius=10)
            add_text("Choose your car for driving...",30,(50,50),surface_color,black)
            car_selection_screen_copy=screen.copy()
            car_selection_screen_surfaces[z]=car_selection_screen_copy
        #game screen surface
            #---creating a 1000*1000 pygame surface
        surface=pygame.Surface((1000,1000))
            #---filling the surface with green colour
        surface.fill(green)
            #---setting road platform
        pygame.draw.rect(surface,light_grey,(325,0,350,1000))
        pygame.draw.rect(surface,light_grey,(0,325,1000,350))
        pygame.draw.line(surface,black,(325,0),(325,325),1)
        pygame.draw.line(surface,black,(0,325),(325,325),1)
        pygame.draw.line(surface,black,(675,0),(675,325),1)
        pygame.draw.line(surface,black,(0,675),(325,675),1)
        pygame.draw.line(surface,black,(325,675),(325,1000),1)
        pygame.draw.line(surface,black,(675,675),(675,1000),1)
        pygame.draw.line(surface,black,(675,675),(1000,675),1)
        pygame.draw.line(surface,black,(675,325),(1000,325),1)
            #---setting road parking
        pygame.draw.rect(surface,dark_grey,(0,350,1000,300))
        pygame.draw.rect(surface,dark_grey,(350,0,300,1000))
        pygame.draw.line(surface,black,(350,0),(350,350),1)
        pygame.draw.line(surface,black,(0,350),(350,350),1)
        pygame.draw.line(surface,black,(650,0),(650,350),1)
        pygame.draw.line(surface,black,(0,650),(350,650),1)
        pygame.draw.line(surface,black,(350,650),(350,1000),1)
        pygame.draw.line(surface,black,(650,350),(1000,350),1)
        pygame.draw.line(surface,black,(650,650),(1000,650),1)
        pygame.draw.line(surface,black,(650,650),(650,1000),1)
            #---pasting cross road image
        surface.blit(road_image,(0,0))
            #---pasting houses
        surface.blit(pygame.transform.scale(house1_image,(150,100)),(0,200))
        surface.blit(house2_image,(200,200))
        surface.blit(house3_image,(200,50))
        surface.blit(house3_image,(700,200))
        surface.blit(house4_image,(850,200))
        surface.blit(house7_image,(700,50))
        surface.blit(house4_image,(0,700))
        surface.blit(house5_image,(200,700))
        surface.blit(house7_image,(200,900))
        surface.blit(house6_image,(700,700))
        surface.blit(house2_image,(850,700))
        surface.blit(pygame.transform.scale(house1_image,(100,150)),(700,850))
        
        screen.blit(pygame.transform.scale(surface,(700,700)),(0,0))
        l()
        pygame.display.update()
        break
    break

                                                            #---openning screen---
#displaying the openning screen
screen.blit(openning_screen_copy,(0,0))
pygame.display.update()

#checking whether the play button is pressed or not in the openning screen
message1=message2=""
while True:
    #getting the events
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_point=pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_point):
                shade(play_button_size,play_button_position,50)
                pygame.display.update()
                message1="enter"
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_point=pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_point):
                screen.blit(openning_screen_copy,(0,0))
                pygame.display.update()
                message2="enter"
        if event.type==pygame.QUIT:
            pygame.quit()
    #breaking the loop 
    if message1==message2=="enter":
        break
pygame.time.delay(500)

#closing the openning screen with gradual darkening
d=0
while d<256:
    shade((1000,700),(0,0),d)
    pygame.display.update()
    screen.blit(openning_screen_copy,(0,0))
    d=d+2
screen.fill(black)


                                                            #---car selection screen---
#displaying the car selection screen
car_options_pos=1
car_selection_screen(car_options_pos)
pygame.display.update()

#popping the message
pygame.time.delay(1000)
pygame.draw.rect(screen,outline_color,(25,25,400,75),border_radius=10)
pygame.draw.rect(screen,black,(25,25,400,75),2,border_radius=10)
pygame.draw.rect(screen,surface_color,(35,35,380,55),border_radius=10)
pygame.draw.rect(screen,black,(35,35,380,55),2,border_radius=10)
add_text("Choose your car for driving...",30,(50,50),surface_color,black)
pygame.display.update()

#checking whether the next button is pressed or not in the car selection screen
message1=message2=""
while True:
    #getting the events
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_point=pygame.mouse.get_pos()
            if pre_button.collidepoint(mouse_point):
                if car_options_pos>1:
                    car_options_pos=car_options_pos-1
                    screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
            if post_button.collidepoint(mouse_point):
                if car_options_pos<len(car_options):
                    car_options_pos=car_options_pos+1
                    screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
            if select_button.collidepoint(mouse_point):
                selected_car=car_options[car_options_pos][0]
                shade((100,50),(300,600),50)
                pygame.display.update()
                message1="selected"
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_point=pygame.mouse.get_pos()
            if select_button.collidepoint(mouse_point):
                screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
                pygame.display.update()
                message2="selected"
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if car_options_pos>1:
                    car_options_pos=car_options_pos-1
                    screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
            if event.key==pygame.K_RIGHT:
                if car_options_pos<len(car_options):
                    car_options_pos=car_options_pos+1
                    screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
            if event.key==pygame.K_RETURN:
                selected_car=car_options[car_options_pos][0]
                message1=message2="selected"
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    #breaking the loop 
    if message1==message2=="selected":
        break
pygame.time.delay(500)

#closing the car selction screen with gradual darkening
d=0
while d<256:
    shade((1000,700),(0,0),d)
    pygame.display.update()
    screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
    d=d+2
screen.fill(black)


                                                            #---game screen---
def game():     
    #pre game initialisations
    acc_power=car_options[car_options_pos][3]
    brake_power=car_options[car_options_pos][4]
    max_gear=car_options[car_options_pos][2]
    max_kmph=car_options[car_options_pos][5]
    gears=[]
    for j in range(1,max_gear+1,1):
        gears=gears+[str(j)]
    angle=0
    car_xpos=350
    surface_xpos=-150
    a=-150
    b=-1150
    speed_limit=y=120
    speeds={}
    for x in range(1,speed_limit+1,1):
        speeds[x]=y
        y=y-1
    movement=speed=0
    horn=clutch=brake=accelerator="released"
    on="no"
    off="yes"
    car_engine="off"
    deviation=""
    reverse_gear=gear=""
    gear_state="N"
    message1=message2=""
    #displaying the game screen
    screen.blit(surface,(-150,a))
    screen.blit(surface,(-150,b))
    screen.blit(tree1_image,(500,700))
    #driving the car
    while True:
        #copying the screen
        screen_copy=screen.copy()
        #getting the events
        for event in pygame.event.get():
            #key pressing events
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    on="yes"
                if event.key==pygame.K_BACKSPACE:
                    off="yes"
                if event.key==pygame.K_UP:
                    accelerator="pressed"
                if event.key==pygame.K_DOWN:
                    brake="pressed"
                if event.key==pygame.K_c:
                    clutch="pressed"
                if event.key==pygame.K_n:
                    gear="neutral"
                if event.key==pygame.K_1:
                    gear="1"
                if event.key==pygame.K_2:
                    gear="2"
                if event.key==pygame.K_3:
                    gear="3"
                if event.key==pygame.K_4:
                    gear="4"
                if event.key==pygame.K_5:
                    gear="5"
                if event.key==pygame.K_6:
                    gear="6"
                if event.key==pygame.K_r:
                    gear="reverse"
                if event.key==pygame.K_h:
                    horn="pressed"
                if event.key==pygame.K_LEFT:
                    deviation="left"
                if event.key==pygame.K_RIGHT:
                    deviation="right"
            #key releasing events
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    on="no"
                if event.key==pygame.K_UP:
                    accelerator="released"
                if event.key==pygame.K_DOWN:
                    brake="released"
                if event.key==pygame.K_c:
                    clutch="released"
                if event.key==pygame.K_n:
                    gear=""
                if event.key==pygame.K_1:
                    gear=""
                if event.key==pygame.K_2:
                    gear=""
                if event.key==pygame.K_3:
                    gear=""
                if event.key==pygame.K_4:
                    gear=""
                if event.key==pygame.K_5:
                    gear=""
                if event.key==pygame.K_6:
                    gear=""
                if event.key==pygame.K_r:
                    gear=""
                if event.key==pygame.K_h:
                    horn="released"
                if event.key==pygame.K_LEFT:
                    deviation=""
                if event.key==pygame.K_RIGHT:
                    deviation=""
            #mouse pressing events
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_point=pygame.mouse.get_pos()
                if change_car_button.collidepoint(mouse_point):
                    shade((100,50),(25,625),50)
                    pygame.display.update()
                    message1="change"
            #mouse releasing events
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_point=pygame.mouse.get_pos()
                if change_car_button.collidepoint(mouse_point):
                    screen.blit(screen_copy,(0,0))
                    pygame.display.update()
                    message2="change"
            #quit event
            if event.type==pygame.QUIT:
                pygame.quit()
        #changes the car
        if message1==message2=="change":
            message1=message2==""
            return "change"
        #changes the parameters according to the keyboard input
            #---ignites or kills the car engine
        if clutch=="pressed" and on=="yes" and car_engine=="off":
            car_engine="on"
            off="no"
        if off=="yes":
            car_engine="off"
            #---increases the speed if accelerator is pressed   
        if accelerator=="pressed" and car_engine=="on" and clutch=="released":
            if speed<=speed_limit-1 and gear_state!="N":
                speed=int(speed+acc_power)
                if speed>speed_limit:
                    speed=speed_limit
            #---decreases the speed if break is pressed   
        if brake=="pressed":
            if speed>=1:
                speed=int(speed-brake_power)
                if speed<0:
                    speed=0
                if speed<10 and clutch=="released" and gear_state!="N":
                    off="yes"
            #---changes car position on the road
        if deviation=="right":
            if car_xpos<460 and speed!=0:
                car_xpos=car_xpos+1
        if deviation=="left":
            if car_xpos>200 and speed!=0:
                car_xpos=car_xpos-1
            #---decreases the speed if accelerator is released 
        if accelerator=="released" and car_engine=="on":
            if speed>10:
                speed=int(speed-0.00000000000001)
            #---decreases the speed if gear changed to neutral
        if gear_state=="N" and speed!=0 and car_engine=="on":
            if speed>=1:
                speed=int(speed-0.00000000000001)
            #---decreases the speed if car engine is killed
        if speed!=0 and car_engine=="off":
            if speed>=1:
                speed=int(speed-0.00000000000001)
            #---decreases the speed if clutch is pressed
        if clutch=="pressed" and car_engine=="on":
            if speed>=1:
                speed=int(speed-0.00000000000001)
            #---sets a initial speed if clutch is released in gear
        if clutch=="released" and gear_state in ["R","1","2","3","4","5","6"] and speed<10 and car_engine=="on":
            speed=10
            #---increase or decrease the gear if there is a gear change
        if gear=="neutral" and clutch=="pressed":
            movement,gear_state=0,"N"
        if gear=="1" and clutch=="pressed":
            movement,gear_state=1,"1"
        if gear=="2" and clutch=="pressed":
            movement,gear_state=2,"2"
        if gear=="3" and clutch=="pressed":
            movement,gear_state=3,"3"
        if gear=="4" and clutch=="pressed":
            if gear in gears:
                movement,gear_state=4,"4"
        if gear=="5" and clutch=="pressed":
            if gear in gears:
                movement,gear_state=5,"5"
        if gear=="6" and clutch=="pressed":
            if gear in gears:
                movement,gear_state=6,"6"
        if gear=="reverse" and clutch=="pressed":
            movement,gear_state=-1,"R"
        if movement==-1:
            reverse_gear="yes"
        else:
            reverse_gear="no"
        #helps in endless revolution of surface
        if reverse_gear=="yes":
            if b==-150:
                a=850
            if a==-150:
                b=850
        if reverse_gear=="no":
            if b+movement>=-150 and b<-150:
                b=-150
                a=-1150
            if a+movement>=-150 and a<-150:
                a=-150
                b=-1150
        #updates the screen
            #---shows normal movement
        if speed!=0 and car_engine=="on" and gear_state!="N":
            pygame.time.delay(speeds[speed])
            screen.blit(surface,(surface_xpos,a))
            a=a+movement
            screen.blit(surface,(surface_xpos,b))
            b=b+movement
            screen.blit(pygame.transform.scale(selected_car,(40,80)),(car_xpos,550))
            #---shows movement when gear is in neutral
        if gear_state=="N" and speed!=0 and car_engine=="on":
            pygame.time.delay(speeds[speed])
            screen.blit(surface,(surface_xpos,a))
            a=a+2
            screen.blit(surface,(surface_xpos,b))
            b=b+2
            screen.blit(pygame.transform.scale(selected_car,(40,80)),(car_xpos,550))
            #---shows movement when engine is in off
        if speed!=0 and car_engine=="off" and gear_state in ["1","2","3","4","5","6"]:
            pygame.time.delay(speeds[speed])
            screen.blit(surface,(surface_xpos,a))
            a=a+2
            screen.blit(surface,(surface_xpos,b))
            b=b+2
            screen.blit(pygame.transform.scale(selected_car,(40,80)),(car_xpos,550))
            #---shows movement when engine is in off (reverse)
        if speed!=0 and car_engine=="off" and gear_state=="R":
            pygame.time.delay(speeds[speed])
            screen.blit(surface,(surface_xpos,a))
            a=a-2
            screen.blit(surface,(surface_xpos,b))
            b=b-2
            screen.blit(pygame.transform.scale(selected_car,(40,80)),(car_xpos,550))
            #---maintains the position when speed is in 0
        if speed==0:
            screen.blit(surface,(surface_xpos,a))
            screen.blit(surface,(surface_xpos,b))
            screen.blit(pygame.transform.scale(selected_car,(40,80)),(car_xpos,550))
            #---indicates the engine status
        if car_engine=="on":
            pygame.draw.circle(screen,red,(670,675),12)
            pygame.draw.circle(screen,black,(670,675),12,1)
            add_text("ON",13,(661,670),red,black)
        if car_engine=="off":
            pygame.draw.circle(screen,dark_red,(670,675),12)
            pygame.draw.circle(screen,black,(670,675),12,1)
            add_text("ON",13,(661,670),dark_red,black)
            #---shows acceleration,brake and clutch movements
        if accelerator=="released":
            screen.blit(accelerator_image,(620,615))
        if accelerator=="pressed":
            screen.blit(pygame.transform.scale(accelerator_image,(30,60)),(620,615))
        if brake=="released":
            screen.blit(brake_image,(585,615))
        if brake=="pressed":
            screen.blit(pygame.transform.scale(brake_image,(30,60)),(585,615))
        if clutch=="released":
            screen.blit(clutch_image,(550,615))
        if clutch=="pressed":
            screen.blit(pygame.transform.scale(clutch_image,(30,60)),(550,615))
            #---shows stearing rotations
        if deviation=="right":
            if car_xpos<400:
                if angle>-90:
                    angle=int(angle-4)
                    if angle<-45:
                        angle=-45
        if deviation=="left":
            if car_xpos>250:
                if angle<90:
                    angle=int(angle+4)
                    if angle>45:
                        angle=45
        if deviation=="":
            if angle>0:
                if angle>0:
                    angle=int(angle-8)
                    if angle<0:
                        angle=0
            if angle<0:
                if angle<0:
                    angle=int(angle+8)
                    if angle>0:
                        angle=0
            if angle==0:
                angle=0
        rotate_on_axis(stearing_image,(100,100),angle,(545,510))
            #---shows changes in gear
        pygame.draw.circle(screen,black,(530,625),15)
        add_text(gear_state,20,(524,617),black,white)
        pygame.draw.circle(screen,white,(530,625),15,1)
            #---shows changes in speedometer
                #---designing speedometer outline
        pygame.draw.rect(screen,black,(655,510,30,150),border_radius=5)
        pygame.draw.rect(screen,white,(655,510,30,150),1,border_radius=5)
        pygame.draw.rect(screen,white,(660,515,5,120),border_radius=2)
                #---calculating the kmph
        if gear_state in ["1","2","3","4","5","6"]:
            kmph=abs(int((int(gear_state)*speed)/6))
        if gear_state=="R":
            kmph=abs(int(speed/6))
        if gear_state=="N":
            kmph=abs(int(speed/6))
                #---updating the moving column according to the kmph
        pygame.draw.rect(screen,red,(660,635-kmph,5,kmph),border_radius=2)
                #---pasting numerals for speedometer
        f=120
        for e in range(515,635,20):
            if max_kmph==f:
                pygame.draw.line(screen,black,(660,e),(665,e),1)
                add_text(str(f),12,(665,e-2),black,white)
            if max_kmph>f:
                pygame.draw.line(screen,black,(660,e),(665,e),1)
                add_text(str(f),10,(665,e),black,white)
            f=f-20
        add_text("0",12,(666,630),black,white)
        add_text("Kmph",10,(659,642),black,white)
            #---designing buttons
                #---change car button
        pygame.draw.rect(screen,outline_color,(25,625,100,50))
        pygame.draw.rect(screen,black,(25,625,100,50),2)
        pygame.draw.rect(screen,surface_color,(30,630,90,40),border_radius=5)
        pygame.draw.rect(screen,black,(30,630,90,40),2,border_radius=5)
        add_text("Change car",18,(35,640),surface_color,black)
            #for co vehicles
        
            #---draws  border
        border()
            #---update the changes
        pygame.display.update()
#runs the game() function
while True:
    #calling and getting the returned output from the function
    op=game()
    #displays the car selection screen for changing the car
    if op=="change":
        #displaying the car selection screen
        car_options_pos=1
        car_selection_screen(car_options_pos)
        pygame.display.update()
        #popping the message
        pygame.draw.rect(screen,outline_color,(25,25,400,75),border_radius=10)
        pygame.draw.rect(screen,black,(25,25,400,75),2,border_radius=10)
        pygame.draw.rect(screen,surface_color,(35,35,380,55),border_radius=10)
        pygame.draw.rect(screen,black,(35,35,380,55),2,border_radius=10)
        add_text("Choose your car for driving...",30,(50,50),surface_color,black)
        pygame.display.update()
        #checking whether the next button is pressed or not in the car selection screen
        message1=message2=""
        while True:
            #getting the events
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_point=pygame.mouse.get_pos()
                    if pre_button.collidepoint(mouse_point):
                        if car_options_pos>1:
                            car_options_pos=car_options_pos-1
                            screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
                    if post_button.collidepoint(mouse_point):
                        if car_options_pos<len(car_options):
                            car_options_pos=car_options_pos+1
                            screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
                    if select_button.collidepoint(mouse_point):
                        selected_car=car_options[car_options_pos][0]
                        shade((100,50),(300,600),50)
                        pygame.display.update()
                        message1="selected"
                if event.type==pygame.MOUSEBUTTONUP:
                    mouse_point=pygame.mouse.get_pos()
                    if select_button.collidepoint(mouse_point):
                        screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
                        pygame.display.update()
                        message2="selected"
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        if car_options_pos>1:
                            car_options_pos=car_options_pos-1
                            screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
                    if event.key==pygame.K_RIGHT:
                        if car_options_pos<len(car_options):
                            car_options_pos=car_options_pos+1
                            screen.blit(car_selection_screen_surfaces[car_options_pos],(0,0))
                    if event.key==pygame.K_RETURN:
                        selected_car=car_options[car_options_pos][0]
                        message1=message2="selected"
                if event.type==pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
            #breaking the loop 
            if message1==message2=="selected":
                break
        pygame.time.delay(500)
