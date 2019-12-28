from selenium import webdriver
import configurations as conf
import random
import string


driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/')
emails = [
    'gmail.com',
    'yahoo.com',
    'bing.com',
]


def receiveRandomUserNameOrPassword(username_length=random.randint(8, 15)):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for index in range(username_length))


def receiveRandomTitleOrDescription(title_length):
    letters = string.ascii_letters
    text_without_spaces = ''.join(random.choice(letters) for index in range(title_length))
    text_with_spaces = [ ''.join(text_without_spaces[::-1][i:i+random.randint(1, 10)])[::-1] for i in range(0,len(text_without_spaces),random.randint(1, 10))]
    return ' '.join(text_with_spaces[::-1])


def leaveLike():
        support_variable, posts = 0, []
        for post in driver.find_elements_by_class_name('title'):
            support_variable = post.find_element_by_class_name('post-title')
            posts.append(post.text)
        print(posts)  # post1, post2, post3

        for index_three in range(0, random.randint(1, len(posts))):
            random_post = random.choice(posts)
            print(random_post)
            post_title = driver.find_element_by_xpath('//a[contains(text(),'+f"'{random_post}'"+')]')
            posts.remove(random_post)
            del random_post
            post_title.click()
            del post_title

            try:
                like_bth = driver.find_element_by_class_name('like-btn')
                like_bth.click()
                del like_bth
            finally:
                driver.execute_script('window.history.go(-1)')


def main():   
    for index in range(2):
        sign_up = driver.find_element_by_class_name('first')
        sign_up.click()
        del sign_up

        user_template = receiveRandomUserNameOrPassword()
        username = driver.find_element_by_name('username')
        username.send_keys(user_template)
        del username

        email = driver.find_element_by_name('email')
        email.send_keys(f'{user_template}@{random.choice(emails)}')
        del email

        password_template = receiveRandomUserNameOrPassword()
        password1 = driver.find_element_by_name('password1')
        password1.send_keys(password_template)
        del password1

        password2 = driver.find_element_by_name('password2')
        password2.send_keys(password_template)
        del password2

        submit_sign_up = driver.find_element_by_class_name('second')
        submit_sign_up.click()
        del submit_sign_up

        username = driver.find_element_by_name('username')
        username.send_keys(user_template)
        del username
        del user_template

        password = driver.find_element_by_name('password')
        password.send_keys(password_template)
        del password
        del password_template

        log_in = driver.find_element_by_class_name('third')
        log_in.click()
        del log_in

        profile = driver.find_element_by_class_name('fourth')
        profile.click()
        del profile

        for index_two in range(1, random.randint(2, conf.max_posts_per_user)):
            add_new_post = driver.find_element_by_class_name('fifth')
            add_new_post.click()
            del add_new_post

            title = driver.find_element_by_name('title')
            title.send_keys(receiveRandomTitleOrDescription(random.randint(5, 30)))
            del title

            desctiption = driver.find_element_by_name('desctiption')
            desctiption.send_keys(receiveRandomTitleOrDescription(random.randint(50, 500)))
            del desctiption

            submit_new_post = driver.find_element_by_class_name('sixth')
            submit_new_post.click()
            del submit_new_post

            driver.switch_to.alert.accept()

        home_page = driver.find_element_by_class_name('homePage')
        home_page.click()
        del home_page

        while True:
            leaveLike()
            try:
                next_btn = driver.find_element_by_class_name('nextBtn')
                next_btn.click()
                del next_btn
            except:
                break
        
        driver.get('http://127.0.0.1:8000/')

        log_out = driver.find_element_by_class_name('logOut')
        log_out.click()
        del log_out

main() if __name__ == '__main__' else 'Error'
