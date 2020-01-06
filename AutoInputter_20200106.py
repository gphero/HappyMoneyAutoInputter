import time
import pyautogui as pag
import re
import sqlite3
import datetime

# 충전 페이지 URL : c
pag.PAUSE = 0.05
totalCounter = 0

# 키보드 버튼 누르기
def press_button(button_code):
    #pag.press(button_code)
    pag.keyDown(button_code)
    pag.keyUp(button_code)

if __name__ == '__main__':
    dt = datetime.datetime.now()
    today = str(dt.year) + str(dt.month) + str(dt.day)
    print(today)

    # 1.파일읽기 ANSI
    with open('./ticketNumbers.txt', "r") as FILE:
    # 파일읽기 UTF-8
    #with open('./ticketNumbers.txt', "r", encoding = 'UTF-8') as FILE:
        file_contents = FILE.read()
    #print('1111')

    # 2.해피머니 상품권 번호 추출
    p = re.compile('\d{4}[-]\d{4}[-]\d{4}[-]\d{4}[_]\d{8}')
    result = p.findall(file_contents)
    happyList = []

    print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 3")
    time.sleep(1)
    print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 2")
    time.sleep(1)
    print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 1")
    time.sleep(1)
    print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 시작!")

    # 3.입력
    i = 0
    for r in result:
        # 첫번째칸 위에 놓으세요~ 아니면 아래 탭을 주석처리~!!
        # press_button('tab')
        i = i + 1
        print(i)
        print(r)

        numbers = r.replace('-', '').replace('_', '').replace(' ', '').replace('\n', '')
        happyList.append((numbers, today))

        #번호 입력 10개.
        for atom in numbers :
            totalCounter = totalCounter + 1  # start with 0
            #print(atom)
            press_button(atom)

            # 앞에 핀번호 16자리는 4자리마다 입력 후 탭 누름(칸 이동)
            if (totalCounter % 4 == 0) and (totalCounter <= 17):
                press_button('tab')
            # 24번째는 다음줄로
            elif totalCounter == 24 :
                press_button('tab')

            #한줄 초과 시 카운터 초기화
            if totalCounter > 24 :
                totalCounter = 1

        if i % 10 == 0 :
            input("10개 입력했다. 충전완료하고 엔터눌러라.")
            print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 3")
            time.sleep(1)
            print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 2")
            time.sleep(1)
            print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 1")
            time.sleep(1)
            print("입력을 시작합니다. 첫 번째 칸에 커서 놓으세요. 시작!")

    # 4. sqlite 에 insert
    conn = sqlite3.connect("happylist.db")
    with conn:
        cur = conn.cursor()
        sql = "insert into happylist(number, date ) values (?, ?)"
        cur.executemany(sql, happyList)

        conn.commit()

        # print(type(rows))
        #
