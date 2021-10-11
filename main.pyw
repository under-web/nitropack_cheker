import threading
import time
import PySimpleGUI as sg
import csv
import os.path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_info_site(site):
    global driver
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        # driver = webdriver.Firefox()
        url = 'https://nitropack.io/demo#' + site
    except Exception as e:
        print('err 1', e)
    try:
        driver.get(url)
        time.sleep(60)
    except Exception as e:
        print('err 2', e)
    try:
        score_before = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[2]/div[2]/div[1]')
        score_after = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[2]/div[2]/div[2]')

        estimated_visitor_loss_before = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[3]/div[1]')
        estimated_visitor_loss_after = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[3]/div[2]')

        time_to_first_byte_before = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[4]/div[1]')
        time_to_first_byte_after = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[4]/div[2]')

        speed_index_before = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[2]/div[5]/div[1]')
        speed_index_after = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[2]/div[5]/div[2]')

        first_contentful_paint_before = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[6]/div[1]')
        first_contentful_paint_after = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[6]/div[2]')

        first_meaningful_paint_before = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[7]/div[1]')
        first_meaningful_paint_after = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[7]/div[2]')

        total_blocking_time_before = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[8]/div[1]')
        total_blocking_time_after = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[2]/div[8]/div[2]')

        image_savings_before = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[2]/div[9]/div[1]')
        image_savings_after = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[2]/div[9]/div[2]')

        # -------Mobile--------

        score_before_m = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[5]/div[2]/div[1]')
        score_after_m = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[5]/div[2]/div[2]')

        estimated_visitor_loss_before_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[3]/div[1]')
        estimated_visitor_loss_after_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[3]/div[2]')

        time_to_first_byte_before_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[4]/div[1]')
        time_to_first_byte_after_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[4]/div[2]')

        speed_index_before_m = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[5]/div[5]/div[1]')
        speed_index_after_m = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[5]/div[5]/div[2]')

        first_contentful_paint_before_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[6]/div[1]')
        first_contentful_paint_after_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[6]/div[2]')

        first_meaningful_paint_before_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[7]/div[1]')
        first_meaningful_paint_after_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[7]/div[2]')

        total_blocking_time_before_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[8]/div[1]')
        total_blocking_time_after_m = driver.find_element_by_xpath(
            '/html/body/main/section[3]/div[2]/div[5]/div[8]/div[2]')

        image_savings_before_m = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[5]/div[9]/div[1]')
        image_savings_after_m = driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[5]/div[9]/div[2]')

        out_data = [score_before.text,
                    score_after.text,
                    estimated_visitor_loss_before.text,
                    estimated_visitor_loss_after.text,
                    time_to_first_byte_before.text,
                    time_to_first_byte_after.text,
                    speed_index_before.text,
                    speed_index_after.text,
                    first_contentful_paint_before.text,
                    first_contentful_paint_after.text,
                    first_meaningful_paint_before.text,
                    first_meaningful_paint_after.text,
                    total_blocking_time_before.text,
                    total_blocking_time_after.text,
                    image_savings_before.text,
                    image_savings_after.text,
                    score_before_m.text,
                    score_after_m.text,
                    estimated_visitor_loss_before_m.text,
                    estimated_visitor_loss_after_m.text,
                    time_to_first_byte_before_m.text,
                    time_to_first_byte_after_m.text,
                    speed_index_before_m.text,
                    speed_index_after_m.text,
                    first_contentful_paint_before_m.text,
                    first_contentful_paint_after_m.text,
                    first_meaningful_paint_before_m.text,
                    first_meaningful_paint_after_m.text,
                    total_blocking_time_before_m.text,
                    total_blocking_time_after_m.text,
                    image_savings_before_m.text,
                    image_savings_after_m.text
                    ]
    except Exception as e:
        print('err 3', e)
        out_data = []

    save_csv(out_data)
    driver.close()
    driver.quit()


def save_csv(out_data):
    heder = ['score_before',
             'score_after',
             'estimated_visitor_loss_before',
             'estimated_visitor_loss_after',
             'time_to_first_byte_before',
             'time_to_first_byte_after',
             'speed_index_before',
             'speed_index_after',
             'first_contentful_paint_before',
             'first_contentful_paint_after',
             'first_meaningful_paint_before',
             'first_meaningful_paint_after',
             'total_blocking_time_before',
             'total_blocking_time_after',
             'image_savings_before',
             'image_savings_after',
             'mob_score_before',
             'mob_score_after',
             'mob_estimated_visitor_loss_before',
             'mob_estimated_visitor_loss_after',
             'mob_time_to_first_byte_before',
             'mob_time_to_first_byte_after',
             'mob_speed_index_before',
             'mob_speed_index_after',
             'mob_first_contentful_paint_before',
             'mob_first_contentful_paint_after',
             'mob_first_meaningful_paint_before',
             'mob_first_meaningful_paint_after',
             'mob_total_blocking_time_before',
             'mob_total_blocking_time_after',
             'mob_image_savings_before',
             'mob_image_savings_after'
             ]
    check_file = os.path.exists('data.csv')
    if check_file:
        with open("data.csv", mode="a", encoding='utf-8', errors='ignore') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=";")
            file_writer.writerow(out_data)
    else:
        with open("data.csv", mode="a", encoding='utf-8', errors='ignore') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=";")
            file_writer.writerow(heder)
            file_writer.writerow(out_data)


def main():
    sg.theme('LightGrey1')

    layout = [  [sg.Text('Выбрать файл с сайтами')],
                [sg.Text('', size=(15, 10)), sg.Output(k='out'), [sg.FileBrowse('FileBrowse')]],
                [sg.Button('Cancel'), sg.Button('Go')] ]
    window = sg.Window('Cheker_nitropack.io', layout)
    s = 1
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Go':
            with open(values['FileBrowse'], 'r') as file:
                site_list = file.readlines()
                print(f'Всего сайтов в файле {len(site_list)}')
                for url in site_list:
                    # threading_1 = threading.Thread(target=get_info_site, args=(url.strip(),))
                    # threading_1.start()
                    # threading_1.join()
                    print(f'Анализирую {s}-й сайт  ({url.strip()})')
                    s += 1
                    get_info_site(url.strip())
    driver.close()
    driver.quit()
    window.close()

if __name__ == '__main__':
    main()
