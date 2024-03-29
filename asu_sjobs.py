#!/usr/bin/env python

from __future__ import unicode_literals
import os
from addict import Dict
os.environ["LANG"] = "en_US.UTF-8"

import config
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

N_THREADS = 3
TIMEOUT = 60 
MAX_JOBS = 0

def load_applied_jobs(username):
    filename = str(username+"_applied_jobs.txt")
    if not os.path.exists(filename):
        open(filename, 'w').close()
    
    with open(filename, 'r') as f:
        lines = set(f.read().splitlines())
        f.close()
    return lines

def save_applied_jobs(applied_jobs, username):
    applied_jobs = list(dict.fromkeys(applied_jobs))
    with open(str(username+"_applied_jobs.txt"), 'w') as f:
        f.write('\n'.join(applied_jobs))
        f.close()

def already_applied(driver):
    try:
        driver.find_element_by_css_selector("#appLbl")
        return True
    except NoSuchElementException:
        return False

def apply_to_job(job_link, driver, conf):
    try: 
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(job_link)
        if already_applied(driver):
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            return job_link
        driver.find_element_by_css_selector("#applyFromDetailBtn > span.ladda-label").click()
        driver.find_element_by_css_selector("#startapply").click()
        driver.find_element_by_css_selector("#shownext").click()
        driver.find_element_by_css_selector("#radio-44674-Yes").click()
        driver.find_element_by_css_selector("#radio-61829-Yes").click()
        driver.find_element_by_css_selector("#custom_44925_1291_fname_slt_0_44925-button_text").click()
        driver.find_element_by_css_selector("#ui-id-5").click()
        driver.find_element_by_css_selector("#shownext").click()
        driver.find_element_by_css_selector("#AddResumeLink").click()
        driver.switch_to.frame(driver.find_element_by_id("profileBuilder"))
        driver.find_element_by_css_selector("#btnSelectedSavedRC").click()
        driver.find_elements_by_xpath('//*[@id="FileList"]')[-1].click() 
        driver.find_element_by_css_selector("body > div.encompassingDiv.ImportProfile.ng-scope > div > div:nth-child(5) > div > div.Marginbottom20.clearfix > button").click()
        driver.switch_to.default_content()
        driver.find_element_by_css_selector("#AddCLLink").click()
        driver.switch_to.frame(driver.find_element_by_id("profileBuilder"))
        driver.find_element_by_css_selector("#btnSelectedSavedRC").click()
        driver.find_elements_by_xpath('//*[@id="FileList"]')[-1].click() 
        driver.find_element_by_css_selector("body > div.encompassingDiv.ImportProfile.ng-scope > div > div:nth-child(5) > div > div.Marginbottom20.clearfix > button").click()
        driver.switch_to.default_content()
        driver.find_element_by_css_selector("#shownext").click()
        driver.find_element_by_css_selector("#attachmentWidget > div > div.fieldcontain > p > a").click()
        driver.switch_to.frame(driver.find_element_by_id("profileBuilder"))
        driver.find_element_by_css_selector("#btnSelectedSavedRC").click()
        for el in driver.find_elements_by_xpath('//*[@id="FileList"]'):
            if el.find_element_by_tag_name('label').text in conf.file_list:
                el.click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("body > div.encompassingDiv.ImportProfile.ng-scope > div > div:nth-child(5) > div > div.Marginbottom20.clearfix > button").click()
        driver.switch_to.default_content()
        driver.find_element_by_css_selector("#shownext").click()
        WebDriverWait(driver, TIMEOUT).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#custom_42326_1300_fname_txt_0"))
                    )
        driver.find_element_by_css_selector("#shownext").click()
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#div-50740 > div > div > div.fieldcontain.baseColorPalette.question-44828-container.custom > fieldset > div > div:nth-child(2) > label"))
        )
        driver.find_element_by_css_selector("#shownext").click()
        WebDriverWait(driver, TIMEOUT).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkbox-44744-Asian"))
                )
        driver.find_element_by_css_selector("#shownext").click()
        if not config.DISABLE_SAVE_SUBMIT:
            driver.find_element_by_css_selector("#save").click()
            time.sleep(0.5)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            return job_link
        time.sleep(0.5)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

    except Exception as e:
        print(e)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        return

def main(conf):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.maximize_window()
    driver.get("https://students.asu.edu/employment/search")
    time.sleep(0.5)
    driver.find_element_by_css_selector("#skip-to-content > article > div.layout__fixed-width > div > div > div > div > div > div.pt-3.block.block-layout-builder.block-inline-blockgrid-links > div > a:nth-child(1)").click()
    time.sleep(0.5)
    WebDriverWait(driver, TIMEOUT).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))
                )
    driver.find_element_by_id('username').send_keys(conf.username)
    driver.find_element_by_id('password').send_keys(conf.password)
    driver.find_element_by_name('submit').click()

    WebDriverWait(driver, 360).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#initialSearchBox > div > h1"))
            )
    driver.implicitly_wait(4)
    results = int(driver.find_element_by_css_selector("#initialSearchBox > div > h1").get_attribute("innerHTML").split()[3])

    WebDriverWait(driver, TIMEOUT).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#searchControls_BUTTON_2"))
                    )
    driver.find_element_by_id('searchControls_BUTTON_2').click()

    time.sleep(0.3)
    for i in range(int(results/50)):
        time.sleep(0.2)
        WebDriverWait(driver, TIMEOUT).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#showMoreJobs"))
            )
        driver.find_element_by_css_selector("#showMoreJobs").click()

    job_links = []
    job_defs = Dict()

    for i in range(results):
        try:
            jlel = driver.find_element_by_css_selector(f"#Job_{str(i)}")
            job_links.append(jlel.get_attribute("href"))
            job_defs[jlel.get_attribute("href")] = str(
                                
                                driver.find_element_by_css_selector(
                                    f"#mainJobListContainer > div > div > ul > li:nth-child({str(i-1)}) > div > div:nth-child(3) > p"
                                ).text + "\t" +
                                jlel.text
                            )
        except Exception as e:
            continue

    applied_jobs = load_applied_jobs(conf.username)
    job_links = list(set(job_links) - set(applied_jobs))

    if MAX_JOBS:
        job_links = job_links[:MAX_JOBS]

    print(f"\nTotal jobs to be applied: {str(len(job_links))}")
    print("\nApplying for jobs:")
    for job_link in job_links:
        print(job_defs[job_link])

    applied_jobs = list(applied_jobs)
    ctr = 0 

    driver.execute_script("window.open('');")
    for i, job_link in enumerate(job_links):
        try:
            if i%10 == 0:
                save_applied_jobs(applied_jobs, conf.username)
            applied_job = apply_to_job(job_link, driver, conf)
            if applied_job:
                ctr += 1
                applied_jobs.append(applied_job)
            
        except Exception as e:
            continue

    save_applied_jobs(applied_jobs, conf.username)
    print(f"Total jobs applied: {str(ctr)}")
    print("Execution Complete")
    driver.refresh()
    driver.close()
    driver.quit()


if __name__ == '__main__':
    for conf in config.configs:
        main(Dict(conf))
