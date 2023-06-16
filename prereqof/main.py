import requests # HTTP 요청
import re # 정규 표현식 사용
import csv # csv 파일 다루기

from bs4 import BeautifulSoup # 웹 브라우저 자동화
from selenium.webdriver.chrome.options import Options # Chrome 웹 드라이버 설정
from selenium.webdriver.common.keys import Keys  # 키 입력
from selenium.webdriver.common.by import By # 요소 검색


def math_pre_req_of(code):
    # code : course code of a course, format in ABC123 (e.g. MAT223 for linear algebra)

    # Passes in the course code parameter and convert into the right format if needed,
    # Then this function goes through each course under the 'Mathematics Courses section and
    # find if the course is a pre-requisite of the following course. If yes, then store it
    # in a list and after every course has been checked, returns a list of courses that require
    # the course of the parameter as a pre-requisite

    # using the helper function, capitalize the course code





    return lst


def capitalize_code(code):
    # a helper function to help capitalize the course code.
    # code : course code of a course

    # the course code is not in a valid format
    if (len(code) != 6):
        print("The course code you typed is not in the right format, make sure " +
              " the course code is in the right format and try again (e.g. MAT223)")
        return 0 # indicates an error

    else:
        capitalized_code = code.upper()
        code = capitalized_code
        return 1 # indicates success