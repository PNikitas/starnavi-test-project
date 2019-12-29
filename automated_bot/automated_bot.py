from selenium import webdriver
import configurations as conf
import functions as func
import random


def main():
    func.driver.get('http://127.0.0.1:8000/')
    for index in range(conf.number_of_users):
        func.useWay()

        for index_two in range(0, random.randint(1, conf.max_posts_per_user)):
            add_new_post = func.driver.find_element_by_class_name('fifth')
            add_new_post.click()
            del add_new_post

            title = func.driver.find_element_by_name('title')
            title.send_keys(func.receiveRandomTitleOrDescription(random.randint(5, 30)))
            del title

            desctiption = func.driver.find_element_by_name('desctiption')
            desctiption.send_keys(func.receiveRandomTitleOrDescription(random.randint(50, 500)))
            del desctiption

            submit_new_post = func.driver.find_element_by_class_name('sixth')
            submit_new_post.click()
            del submit_new_post

            func.driver.switch_to.alert.accept()

        home_page = func.driver.find_element_by_class_name('homePage')
        home_page.click()
        del home_page

        likes_left = conf.max_likes_per_user
        while True:
            likes_used = func.leaveLike(likes_left)
            likes_left = likes_left - likes_used
            # if likes_left == 0:
            #     break
            if random.randint(0, 1) == 0 or likes_left == 0:  # In my personal opinion, the commented code above is better. Fixed number of likes :)
                break
            try:
                next_btn = func.driver.find_element_by_class_name('nextBtn')
                next_btn.click()
                del next_btn
            except:
                break
        
        func.driver.get('http://127.0.0.1:8000/')

        log_out = func.driver.find_element_by_class_name('logOut')
        log_out.click()
        del log_out

    func.driver.get('http://127.0.0.1:8000/')


main() if __name__ == '__main__' else 'Error'