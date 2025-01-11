import pygame

pygame.init()

def ideal_kilo_hesapla(input_text_yas, input_text_cinsiyet, input_text_boy):
    try:
        yas = int(input_text_yas)
        boy = float(input_text_boy)
    except ValueError:
        return "Deficient"

    temel_bmi = 22
    if yas < 18:
        temel_bmi -= 2  
    elif yas > 60:
        temel_bmi += 1  
    if input_text_cinsiyet.lower() == "male":
        temel_bmi += 1  
    elif input_text_cinsiyet.lower() == "female":
        temel_bmi -= 1  

    ideal_kilo = temel_bmi * (boy ** 2)
    return round(ideal_kilo, 2)

width, height = 500, 330
ekran = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load('icon.png'))
pygame.display.set_caption('Ideal Weight Calculation')

input_text_yaş = ""
yaş_alan_rect = pygame.draw.rect(ekran,(255,255,2),(160,40,250,40),border_radius=15)
yaş_alan = 0

input_text_boy = ""
boy_alan_rect = pygame.draw.rect(ekran,(255,255,2),(160,110,250,40),border_radius=15)
boy_alan = 0

input_text_cinsiyet = ""
cinsiyet_alan_rect = pygame.draw.rect(ekran,(255,255,2),(160,180,250,40),border_radius=15)
cinsiyet_alan = 0

result_rect = pygame.draw.rect(ekran,(255,255,2),(30,255,110,40),border_radius=15)
result = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN:
                if yaş_alan == 1:
                  input_text_yaş = "" 
                if boy_alan == 1:
                  input_text_boy = "" 
                if cinsiyet_alan == 1:
                  input_text_cinsiyet = "" 
            elif event.key == pygame.K_BACKSPACE:
                if yaş_alan == 1:
                  input_text_yaş = input_text_yaş[:-1]
                if boy_alan == 1:
                  input_text_boy = input_text_boy[:-1]
                if cinsiyet_alan == 1:
                  input_text_cinsiyet = input_text_cinsiyet[:-1]
            else:
                if yaş_alan == 1:
                  input_text_yaş += event.unicode 
                if boy_alan == 1:
                  input_text_boy += event.unicode 
                if cinsiyet_alan == 1:
                  input_text_cinsiyet += event.unicode 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if yaş_alan_rect.collidepoint(mouse_pos):
                yaş_alan = 1
                boy_alan = 0
                cinsiyet_alan = 0
            if boy_alan_rect.collidepoint(mouse_pos):
                boy_alan = 1
                yaş_alan = 0
                cinsiyet_alan = 0
            if cinsiyet_alan_rect.collidepoint(mouse_pos):
                cinsiyet_alan = 1
                boy_alan = 0
                yaş_alan = 0
            if result_rect.collidepoint(mouse_pos):
              result = 1

    ideal_kilo = ideal_kilo_hesapla(input_text_yaş, input_text_cinsiyet, input_text_boy)
    ekran.fill((28, 178, 228))  
    pygame.draw.rect(ekran,(255,255,255),(30,255,110,40),border_radius=15)
    pygame.draw.rect(ekran,(255,255,255),(160,40,250,40),border_radius=15)
    pygame.draw.rect(ekran,(255,255,255),(160,110,250,40),border_radius=15)
    pygame.draw.rect(ekran,(255,255,255),(160,180,250,40),border_radius=15)
    text_input = pygame.font.Font(None,32).render(input_text_yaş, True, (0, 0, 0)) 
    ekran.blit(text_input, (170, 50))  
    text_input2 = pygame.font.Font(None,32).render(input_text_boy, True, (0, 0, 0)) 
    ekran.blit(text_input2, (170, 120))  
    text_input3 = pygame.font.Font(None,32).render(input_text_cinsiyet, True, (0, 0, 0)) 
    ekran.blit(text_input3, (170, 190))  
    text = pygame.font.Font(None,42).render('Age:', True, (0, 0, 0)) 
    ekran.blit(text, (30, 45))  
    text = pygame.font.Font(None,42).render('Height:', True, (0, 0, 0)) 
    ekran.blit(text, (30, 115))  
    text = pygame.font.Font(None,42).render('Gender:', True, (0, 0, 0)) 
    ekran.blit(text, (30, 185))  
    text = pygame.font.Font(None,42).render('Result', True, (0, 0, 0)) 
    ekran.blit(text, (40, 262))  
    if result == 1:
      text = pygame.font.Font(None,42).render(f'Ideal weight:{ideal_kilo}', True, (0, 0, 0)) 
      ekran.blit(text, (165, 262))  
    pygame.display.flip()

pygame.quit()