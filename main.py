from pytrends.request import TrendReq
import pyautogui

def get_trending():
    pytrends = TrendReq(hl='en-PH', tz=480)
    trending = pytrends.trending_searches(pn='philippines')

    trending_list = []
    for trend in trending[0]:
        trending_list.append(trend)
    return trending_list

def main():
    trending_list = get_trending()

    for trend in trending_list:
        # x=316, y=108 for the search bar
        pyautogui.click(316, 108)
        # ctrl+a to select all
        pyautogui.hotkey('ctrl', 'a')
        # delete to clear the search bar
        pyautogui.press('delete')
        # type the trending search
        pyautogui.typewrite(trend, interval=0.3)
        # enter to search
        pyautogui.press('enter')
        # wait for the page to load
        pyautogui.sleep(5)
        # scroll down a bit and scroll back again to the top
        pyautogui.scroll(-200)
        pyautogui.sleep(2)
        pyautogui.scroll(200)
        pyautogui.sleep(1)

main()

