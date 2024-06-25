import praw
import csv
import time

crawler=praw.Reddit(
    client_id="-wyIovEMB3k6erJ_liKahQ",
    client_secret="0EydvqoHWMQcz4bs3cCB3nEoySt1ZQ",
    user_agent="vikyath123"

)

def comments_crawler(submission_url):
    start_time=time.time()
    submission=crawler.submission(url=submission_url)
    submission.comments.replace_more(limit=None)
    
    c=0

    with open("comments_with_1sec", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Comment"])  # Writing the header            
    
        for comment in submission.comments.list():
            c+=1
            writer.writerow([comment.body])
            if c>100:
                c=0
                time.sleep(2.5)
        

    end_time=time.time()
    
    print(end_time-start_time)

comments_crawler("https://www.reddit.com/r/Cricket/comments/1dkb1w5/match_thread_43rd_match_super_eights_group_1/")