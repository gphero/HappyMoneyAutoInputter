import time
import pyautogui as pag

#파이참 administrater로 켰는지?

# target positions
auto_button_pos = {'left': 1150, 'top': 895, 'width': 40, 'height': 30}

pag.PAUSE = 0.1
totalCounter = 0
quaterCounter = 1
# mouse click
def move_and_click(coords):
    pag.moveTo(x=coords[0]+10, y=coords[1]+5, duration=0.0)
    pag.click()

# 키보드 버튼 누르기
def press_button(button_code):
    pag.press(button_code)


if __name__ == '__main__':

    # 더 충전하기 한번 클릭
    plus5_button_center = pag.locateOnScreen('./plus5_button_2.PNG')
    # print(plus5_button_center)
    # if plus5_button_center == None :
    #     plus5_button_center = pag.locateOnScreen('../plus5_button_2.PNG')
    #     if plus5_button_center == None :
    #         plus5_button_center = pag.locateOnScreen('../plus5_button_3.PNG')

    print(plus5_button_center)
    move_and_click(plus5_button_center)


    #첫번째 칸으로 이동
    columnName_PIN_button_center = pag.locateOnScreen('./columnName_PIN_2.PNG')
    print(columnName_PIN_button_center)
    # if columnName_PIN_button_center == None :
    #     columnName_PIN_button_center = pag.locateOnScreen('../columnName_PIN_2.PNG')
    #     if columnName_PIN_button_center == None:
    #         columnName_PIN_button_center = pag.locateOnScreen('../columnName_PIN_3.PNG')

    print(columnName_PIN_button_center)
    move_and_click(columnName_PIN_button_center)

    # 파일읽기
    with open('./ticketNumbers.txt', "r") as FILE:
        numbers = FILE.read()
    #print(numbers)
    #print('1111')
    #파일 내 공백 대쉬 언더라인 지우기
    numbers = numbers.replace(',', '').replace('-', '').replace('_', '').replace(' ', '').replace('\n', '')
    time.sleep(1)
    #길이 240 필요함 4+4+4+4+8 = 24 * 10
    #print(len(numbers))

    press_button('tab')

    key_0 = pag.locateOnScreen('./key_0.PNG')
    print(key_0)
    key_1 = pag.locateOnScreen('./key_1.PNG')
    print(key_1)
    key_2 = pag.locateOnScreen('./key_2.PNG')
    print(key_2)
    key_3 = pag.locateOnScreen('./key_3.PNG')
    print(key_3)
    key_4 = pag.locateOnScreen('./key_4.PNG')
    print(key_4)
    key_5 = pag.locateOnScreen('./key_5.PNG')
    print(key_5)
    key_6 = pag.locateOnScreen('./key_6.PNG')
    print(key_6)
    key_7 = pag.locateOnScreen('./key_7.PNG')
    print(key_7)
    key_8 = pag.locateOnScreen('./key_8.PNG')
    print(key_8)
    key_9 = pag.locateOnScreen('./key_9.PNG')
    print(key_9)

    if len(numbers) != 240 :
        print("번호입력 10개 다한거 맞음?")
    else :
        #번호 입력 10개.
        for atom in numbers :
            # totalCounter = totalCounter + 1  # start with 0
            # if totalCounter >= 5 && totalCounter <= 8 :
            #
            print(atom)

            if atom == '1' :
                move_and_click(key_1)
            elif atom == '2' :
                move_and_click(key_2)
            elif atom == '3':
                move_and_click(key_3)
            elif atom == '4':
                move_and_click(key_4)
            elif atom == '5':
                move_and_click(key_5)
            elif atom == '6':
                move_and_click(key_6)
            elif atom == '7':
                move_and_click(key_7)
            elif atom == '8':
                move_and_click(key_8)
            elif atom == '9':
                move_and_click(key_9)
            elif atom == '0':
                move_and_click(key_0)
