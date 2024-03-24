from pytrends.request import TrendReq
import pyautogui
import random

def get_trending():
    pytrends = TrendReq(hl='en-PH', tz=480)
    # pn = 'philippines', 'united_states', 'worldwide'
    # switch pn if you need more searches
    trending = pytrends.trending_searches(pn='united_states') 

    trending_list = []
    for trend in trending[0]:
        trending_list.append(trend)
    return trending_list

def main():
    trending_list = get_trending()

    for trend in trending_list:
        # x=316, y=108 for the search bar
        pyautogui.click(316, 108)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        pyautogui.typewrite(trend, interval=0.1)
        pyautogui.press('enter')
        pyautogui.sleep(5)
        # scroll down a bit
        total_scroll = 0
        for _ in range(0, 3):
            random_scroll_pos = random.randint(100, 500)
            random_scroll_time = random.uniform(0.5, 1)
            pyautogui.scroll(-random_scroll_pos)
            pyautogui.sleep(random_scroll_time)
            total_scroll += random_scroll_pos
        # scroll back to the top
        pyautogui.sleep(1)
        pyautogui.scroll(total_scroll)
        pyautogui.sleep(1)
main()

