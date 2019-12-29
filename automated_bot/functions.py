from selenium import webdriver
import string
import random


driver = webdriver.Chrome()
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


def useWay():
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


def leaveLike(likes_left):
    support_variable, posts = 0, []
    for post in driver.find_elements_by_class_name('title'):
        support_variable = post.find_element_by_class_name('post-title')
        posts.append(post.text)

    post_count = len(posts)
    likes_used_value = 0

    if likes_left < post_count:
        post_count = likes_left

    for index_three in range(0, random.randint(1, post_count)):
        random_post = random.choice(posts)
        post_title = driver.find_element_by_xpath('//a[contains(text(),'+f"'{random_post}'"+')]')
        posts.remove(random_post)
        del random_post
        post_title.click()
        del post_title

        try:
            like_bth = driver.find_element_by_class_name('like-btn')
            like_bth.click()
            del like_bth
            likes_used_value += 1
        finally:
            driver.execute_script('window.history.go(-1)')
        
    return likes_used_value