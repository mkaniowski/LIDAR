import env, sensors
import pygame

enviroment = env.buildEnv((1200, 600))
enviroment.originalMap = enviroment.map.copy()
laser = sensors.LaserSensor(250, enviroment.originalMap, noise=(0.5, 0.01))
enviroment.map.fill((0, 0, 0))
enviroment.infomap = enviroment.map.copy()


running = True

while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    
    if sensorON: 
        laser.pos = pygame.mouse.get_pos()
        enviroment.dataStorage(laser.detect())
        enviroment.showData()
    enviroment.map.blit(enviroment.infomap, (0, 0))
    pygame.display.update()