class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass


    def _getTabletService(self):
        tabletService = None
        try:
            tabletService = self.session().service("ALTabletService")
        except Exception as e:
            self.logger.error(e)
        return tabletService


    def _getAbsoluteUrl(self, partial_url):
        import os
        subPath = os.path.join(self.packageUid(), os.path.normpath(partial_url).lstrip("\\/"))
        # We create TabletService here in order to avoid
        # problems with connections and disconnections of the tablet during the life of the application
        return "http://%s/apps/%s" %(self._getTabletService().robotIp(), subPath.replace(os.path.sep, "/"))
        

    def _displayImage(self, url):
    
        tabletService = self._getTabletService()
        if tabletService:
            try:
                url = url + ""

                if url == '':
                    self.logger.error("URL of the image is empty")
                if not url.startswith('http'):
                    url = self._getAbsoluteUrl(url)
                tabletService.showImage(url)

            except Exception as err:
                self.logger.error("Error during ShowImage : %s " % err)
                #self.onStopped()
                
                

    def onInput_onStart(self):
    
        tts = ALProxy("ALTextToSpeech", "192.168.1.35", 9559)
        
        tts.say("Good Morning everyone!")
        
        time.sleep(10)
        
        tts.say("Today we are going to build a computer screen and it is soooo easy. Remember: you will have to be attentive and work together as a team.")

        self._displayImage("images/p5.jpg")

        tts.say("Everyone needs to share and take turn please. What do you think about project folks?")

        time.sleep(10)

        tts.say("But first let me check that you have all components to make the touch screen. Ummmh!")

        time.sleep(2)

        self._displayImage("images/p6.jpeg")

        tts.say("I can see that you have a brain block, power card, a diy cable, a memory card, a cable block, a data block, red split power cable, battery, a touch and a case and the HDMI cable. Awesome job everyone!")

        time.sleep(10)

        tts.say("First, I need to tell you that screens are all shapes and sizes, and today we are going to learn how they work. Before computers, people printed messages on punch cards")

        self._displayImage("images/6A.jpeg")

        tts.say("and used automatic typewriters.")

        self._displayImage("images/6B.jpeg")

        tts.say("  Did you know that in the 1960s, screens were like large boxes,")

        self._displayImage("images/6C.jpeg")

        tts.say(" but now they are so small they can be held in our hands?")

        self._displayImage("images/6D.jpeg")

        time.sleep(10)

        tts.say("Today we are going to build the brain for the computer.")

        self._displayImage("images/page 8.PNG")

        tts.say("First, push the brain onto the block using the holes.")

        self._displayImage("images/page 9.PNG")

        tts.say("Fantastic! Noe let's give the brain new powers. Take the memory card and slide out the micro card.")

        time.sleep(10)

        tts.say("Turn the brain over and securely slide in the micro card.")

        self._displayImage("images/page 12.PNG")

        time.sleep(10)

        tts.say("Turn the brain over and securely slide out the micro card.")

        self._displayImage("images/page 13.PNG")

        tts.say("Has everyone completed this?")

        time.sleep(10)

        tts.say("Great job! Now pick up the screen and plug the brain carefully onto the screen. It should fit like a building block, so make sure it is pushed all the way down.")

        self._displayImage("images/page 15.PNG")

        time.sleep(10)

        tts.say("Fantastic, brain is in place. Next, pick up the cable block an snap it onto screen.")

        self._displayImage("images/page 18.PNG")

        tts.say("Remember- the cable block keeps the cables organised.")

        tts.say("Magnificent! ")

        tts.say("Now we are able to see the driver board which is the screen's command centre.")

        self._displayImage("images/page 20.PNG")

        tts.say("Do you know that the driver board gets millions of messages for your computer every second and passes them to your screen.")

        time.sleep(10)

        tts.say("Brilliant! Now grab the yellow HDMI cable which is made up of thousands of copper fibres twisted into 19 wires. This cable carries pictures from computer to the screen.")

        self._displayImage("images/page 22.PNG")

        tts.say("Now plug the yellow HDMI cable into the brain and then into the driver board.")

        self._displayImage("images/page 24.PNG")

        tts.say("Now push the cable into the channel of the cable block.")

        self._displayImage("images/page 25.PNG")

        tts.say("Great work! Pick up the orange touch cable that will send the data when the screen is touched to the computer.")

        self._displayImage("images/page 26.PNG")

        tts.say("Now plug the larger end of the orange touch cable into the brain and the smaller end into the driver board before pushing the cable into the channel.")

        self._displayImage("images/page 29.PNG")

        tts.say("How is it all going?")

        time.sleep(10)

        tts.say("Awesome! Now we can give the computer a voice, so you will need to locate the blue DIY speaker, which has an audio jack for sound and a USB cable for power. The audio cable sends signals that will vibrate the magnet, membrane and the air inside. So plug the power cable into the brain's USB and then the audio jack, making sure that you push the cable all the way in.")

        self._displayImage("images/page 34.PNG")

        tts.say("Great work! Now push the cable onto the cable block")

        self._displayImage("images/page 37.PNG")

        tts.say("Take the green USB hub and carefully push it onto the block using teh holes and making sure the USB ports fit properly.")

        self._displayImage("images/page 40.PNG")

        tts.say("Super! Now plug the USB end into the brain and please do not forget to push teh green cable into the channel.")

        self._displayImage("images/page 42.PNG")

        tts.say("Fantastic job! Now let's add some electricity, so take hold of the battery. Do you know that inside the battery, there are millions of moving electrons that create electricity?")

        time.sleep(10)

        tts.say("Now push the battery firmly onto the screen.")

        self._displayImage("images/page 45.PNG")

        tts.say("Good job! Next grab the short end of the red split power cable and plug it into the power board.")

        self._displayImage("images/page 48.PNG")

        tts.say("Line the power board up with the brain's pins making sure it covers all of the pins and push all the way down.")

        tts.say("Awesome! Now you have connected the board to the general purpose input and output pins. Are you all ready for the next step?")

        time.sleep(15)

        tts.say("Great! Take the longer end of the red spilt power cable and plug it into the screen's driver board.")

        self._displayImage("images/page 52.PNG")

        tts.say("Plug the larger end of the red split power cable into the USB port on the battery.")

        self._displayImage("images/page 54.PNG")

        tts.say("Now take the small red micro cable and plug one end it into the battery")

        self._displayImage("images/page 56.PNG")

        tts.say("and the other end into the screen edge.")

        self._displayImage("images/page 57.PNG")

        tts.say("Fantastic! Now your computer is ready to make sounds, images and connections.")

        self._displayImage("images/page 58.PNG")

        tts.say("So pick up the keyboard, flip it over and push the power button.")

        self._displayImage("images/page 60.PNG")

        tts.say("Remember: the red wire is used only for charging. Now take out the white radio antennae ")

        self._displayImage("images/page 61.PNG")

        tts.say("and plug it into the brain.")

        self._displayImage("images/page 62.PNG")

        tts.say("Awesome! The key board and the computer are now connected. We need to keep the computer strong and safe, so push the screen case firmly onto the screen case firmly onto the screen.")

        self._displayImage("images/page 65.PNG")

        tts.say("Is everyone ready for the next step?")

        time.sleep(10)

        tts.say("We must not forget the sound sensor beacuse this allows us to the world around us.")

        self._displayImage("images/page 66.PNG")

        tts.say("Now plug this into the USB hub.")

        self._displayImage("images/page 67.PNG")

        tts.say("Marvellous!")

        tts.say("Now we are ready to make sound controlled apps, art and games. You will need to hold the power button down for 3 seconds to bring the computer to life.")

        self._displayImage("images/page 68.PNG")

        tts.say("Remember: The 3 coloured lights on the keyboard are important. When it is green there is successful radio connection. Orange means CAPS LOCK is on and red means it needs charging.")

        self._displayImage("images/page 73.PNG")

        tts.say("When the keyboard requires charging, you will plug the red cable into the computer.")

        self._displayImage("images/page 76.PNG")

        tts.say("To recharge the computer's battery, you will need to plug the small end of the red cable into the computer and the larger into the wall socket. Finally place the power plug into the wall socket and look for the light. Now we can see the computer booting up and it is ready to use.")

        self._displayImage("images/page 69.PNG")

        tts.say ("What do you think about the computer you have made? ")

        time.sleep(20)

        tts.say("What have you learned today? ")

        time.sleep(30)

        tts.say("I can see that we have all enjoyed a truly awesome time assembling this computer, and I look forward to sharing some of the art and games you have been a great team.")

        tts.say("I hope you have enjoyed today's lessons. See you next time.")

        time.sleep(15)
        

        self.onStopped() #activate the output of the box

        pass



    def onInput_onStop(self):

        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
        
        
