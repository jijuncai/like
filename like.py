

# imports
from instapy import InstaPy
from instapy.util import smart_run
import time
import sys

# login credentials
insta_username = 'jimmycai88'
insta_password = 'Caijijun12'
INT_MAX = sys.maxsize

users_username_subset = ['instagood.sfsv.jeff','photooftheday.sfsv.tom','fashion.sfsv.arraff','beautiful.sfsv.merry','happy.sfsv.honey','photography.sfsv.andy','like4like.sfsv.lucy','art.sfsv.whendy','love.sfsv.happy','instagood.sfsv.write','photooftheday.sfsv.tim','fashion.sfsv.fany','beautiful.sfsv.kitty']
users_password_subset = ['lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv','lovesfsv']

# get an InstaPy session!
# set headless_browserTrue to run InstaPy in the background
for i in range(0,len(users_username_subset)):
        
        session = InstaPy(username=users_username_subset[i],
                          password=users_password_subset[i],
                          headless_browser=False,
                          bypass_suspicious_attempt=True)

        # run the task
        with smart_run(session):

            cur = time.time()
    #       session.set_user_interact(amount=1, randomize=False, percentage=100, media='Photo')
    #       session.like_by_tags(['Fitness', 'Gym', 'Bodybuilding', 'fit'], amount=1, interact=False)
            session.like_by_users(['minhaodeng','jimmy_cai8','hotgirls.funnystories'],amount=6000, randomize=False, media=None)
            print( time.time() - cur)

            time.sleep(10)


        
