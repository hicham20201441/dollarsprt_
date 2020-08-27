# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
#import lxml.html
import BeautifulSoup as bs
#
s="""https://dollarsprout.com/make-money-college/
https://dollarsprout.com/buying-an-engagement-ring/
https://dollarsprout.com/50-30-20-budget-calculator/
https://dollarsprout.com/american-express-personal-savings-review/
https://dollarsprout.com/mistplay-review/
https://dollarsprout.com/how-to-sell-your-services-online/
https://dollarsprout.com/should-i-buy-bitcoin/
https://dollarsprout.com/residual-income-ideas/
https://dollarsprout.com/branded-surveys-review/
https://dollarsprout.com/sweatcoin-review/
https://dollarsprout.com/how-to-take-your-offline-business-online/
https://dollarsprout.com/steps-freelancers-should-take-during-the-coronavirus/
https://dollarsprout.com/how-to-earn-income-as-a-virtual-consultant/
https://dollarsprout.com/fincon-2019/
https://dollarsprout.com/how-to-avoid-lifestyle-inflation/
https://dollarsprout.com/what-to-bring-to-a-job-interview/
https://dollarsprout.com/how-to-negotiate-your-salary/
https://dollarsprout.com/skills-employers-look-for/
https://dollarsprout.com/how-to-stand-out-at-work/
https://dollarsprout.com/how-to-prepare-for-a-job-interview/
https://dollarsprout.com/moms-make-money-blogging/
https://dollarsprout.com/ways-to-make-quick-cash-dog/
https://dollarsprout.com/make-more-money-as-a-freelance-writer/
https://dollarsprout.com/how-these-5-millennials-make-money-blogging/
https://dollarsprout.com/bizarre-side-hustle/
https://dollarsprout.com/entrepreneur-success-stories-podreacher/
https://dollarsprout.com/survey-voices-review/
https://dollarsprout.com/how-to-drop-ship/
https://dollarsprout.com/make-money-renting-out-your-space/
https://dollarsprout.com/make-money-selling-ebooks/
https://dollarsprout.com/paid-research-studies/
https://dollarsprout.com/online-writing-courses/
https://dollarsprout.com/make-money-blogging/
https://dollarsprout.com/make-money-on-twitter/
https://dollarsprout.com/get-paid-to-write/
https://dollarsprout.com/get-paid-to-write-reviews/
https://dollarsprout.com/how-to-make-your-resume-stand-out/
https://dollarsprout.com/how-to-become-a-web-designer/
https://dollarsprout.com/online-jobs-for-teens/
https://dollarsprout.com/online-typing-jobs/
https://dollarsprout.com/smart-consumer-study/
https://dollarsprout.com/sell-makeup-online/
https://dollarsprout.com/motif-investing-review/
https://dollarsprout.com/data-collection-apps/
https://dollarsprout.com/get-paid-to-search-the-web/
https://dollarsprout.com/best-real-estate-investing-books/
https://dollarsprout.com/what-is-micro-investing/
https://dollarsprout.com/category/investing/investing-basics/page/3/
https://dollarsprout.com/category/investing/investing-basics/page/2/
https://dollarsprout.com/fundrise-review/
https://dollarsprout.com/what-is-peer-to-peer-lending/
https://dollarsprout.com/category/investing/broker-reviews/
https://dollarsprout.com/best-short-term-investments/
https://dollarsprout.com/how-to-invest-in-real-estate/
https://dollarsprout.com/clink-app-review/
https://dollarsprout.com/wealthsimple-review/
https://dollarsprout.com/equity-multiple-review/
https://dollarsprout.com/category/investing/investing-apps/page/2/
https://dollarsprout.com/paypal-alternatives/
https://dollarsprout.com/category/banking/banking-apps/
https://dollarsprout.com/category/investing/investing-apps/
https://dollarsprout.com/lending-club-investing-review/
https://dollarsprout.com/m1-finance-review/
https://dollarsprout.com/roth-ira-vs-traditional-ira/
https://dollarsprout.com/what-is-an-etf/
https://dollarsprout.com/robinhood-review/
https://dollarsprout.com/stash-review/
https://dollarsprout.com/best-source-of-cheap-caffeine/
https://dollarsprout.com/cheap-starbucks-drinks/
https://dollarsprout.com/side-hustle-statistics-2020/
https://dollarsprout.com/federal-tax-brackets/
https://dollarsprout.com/how-to-avoid-an-unexpected-tax-bill/
https://dollarsprout.com/ebay-alternatives/
https://dollarsprout.com/diy-room-decor-ideas/
https://dollarsprout.com/what-is-inflation/
https://dollarsprout.com/debt-to-income-calculator/
https://dollarsprout.com/ynab-vs-mint/
https://dollarsprout.com/zero-based-budget-calculator/
https://dollarsprout.com/empower-finance-review/
https://dollarsprout.com/types-of-debit-cards/
https://dollarsprout.com/what-is-a-prepaid-debit-card/
https://dollarsprout.com/cash-back-stores-debit-card/
https://dollarsprout.com/credit-karma-review/
https://dollarsprout.com/credit-karma-savings/
https://dollarsprout.com/credit-sesame-vs-credit-karma/
https://dollarsprout.com/credit-monitoring-services/
https://dollarsprout.com/credit-score-range/
https://dollarsprout.com/freeze-credit/
https://dollarsprout.com/best-states-for-entrepreneurs/
https://dollarsprout.com/support-black-lives-matter-personal-finance/
https://dollarsprout.com/category/lifestyle/page/3/
https://dollarsprout.com/category/lifestyle/page/5/
https://dollarsprout.com/category/lifestyle/page/2/
https://dollarsprout.com/side-hustle-statistics/
https://dollarsprout.com/should-you-get-a-graduate-degree/
https://dollarsprout.com/when-to-take-a-pay-cut/
https://dollarsprout.com/passive-income-for-students/
https://dollarsprout.com/what-is-a-budget/
https://dollarsprout.com/budgeting-systems/
https://dollarsprout.com/compound-interest/
https://dollarsprout.com/synchrony-bank-review/
https://dollarsprout.com/ally-bank-review/
https://dollarsprout.com/discover-bank-review/
https://dollarsprout.com/radius-bank-high-yield-savings-account/
https://dollarsprout.com/category/banking/savings/
https://dollarsprout.com/author/holly-welles/
https://dollarsprout.com/category/side-gigs-and-hustles/online-surveys/
https://dollarsprout.com/ipsos-i-say-review/
https://dollarsprout.com/vindale-research-review/
https://dollarsprout.com/google-jobs/
https://dollarsprout.com/dosh-review/
https://dollarsprout.com/drop-app-review/
https://dollarsprout.com/get-paid-to-take-pictures/
https://dollarsprout.com/get-paid-to-advertise-on-your-car/
https://dollarsprout.com/should-parents-pay-for-college/
https://dollarsprout.com/category/banking/bank-credit-union-reviews/
https://dollarsprout.com/emergency-fund-calculator/
https://dollarsprout.com/barclays-bank-online-savings-account-review/
https://dollarsprout.com/how-to-make-1000-fast/
https://dollarsprout.com/best-places-to-sell-textbooks/
https://dollarsprout.com/bookscouter-review/
https://dollarsprout.com/small-scale-business-ideas/
https://dollarsprout.com/buybackboss-review/
https://dollarsprout.com/sell-video-games/
https://dollarsprout.com/wealthfront-review/
https://dollarsprout.com/betterment-review/
https://dollarsprout.com/blooom-review/
https://dollarsprout.com/how-to-make-money-in-college/
https://dollarsprout.com/gazelle-review/
https://dollarsprout.com/work-from-home-scams/
https://dollarsprout.com/free-international-calls/
https://dollarsprout.com/author/annette-miller/
https://dollarsprout.com/how-to-save-1000/
https://dollarsprout.com/i-need-money-now/
https://dollarsprout.com/get-paid-to-teach-with-outschool/
https://dollarsprout.com/digital-product-ideas/
https://dollarsprout.com/freelance-jobs/
https://dollarsprout.com/flexjobs-review/
https://dollarsprout.com/dos-donts-online-side-hustles/
https://dollarsprout.com/how-to-make-passive-income-with-your-car/
https://dollarsprout.com/become-an-instacart-shopper/
https://dollarsprout.com/driving-for-doordash-driver-review/
https://dollarsprout.com/micro-jobs/
https://dollarsprout.com/make-money-delivering/
https://dollarsprout.com/shipt-shopper-review/
https://dollarsprout.com/virtual-assistant-companies/
https://dollarsprout.com/online-chat-jobs/
https://dollarsprout.com/transcription-jobs/
https://dollarsprout.com/online-jobs-for-college-students/
https://dollarsprout.com/vipkid-review/
https://dollarsprout.com/decluttr-review/
https://dollarsprout.com/letgo-review/
https://dollarsprout.com/rover-dog-sitting/
https://dollarsprout.com/online-tutoring-jobs/
https://dollarsprout.com/make-money-proofreading/
https://dollarsprout.com/graphic-designer/
https://dollarsprout.com/how-to-become-a-freelance-writer/
https://dollarsprout.com/social-media-influencer/
https://dollarsprout.com/sell-crafts-online/
https://dollarsprout.com/how-to-make-money-as-a-kid/
https://dollarsprout.com/get-paid-to-test-websites/
https://dollarsprout.com/jobs-for-teens/
https://dollarsprout.com/house-sitting-jobs/
https://dollarsprout.com/thanksgiving-gifts/
https://dollarsprout.com/blockchain-technology/
https://dollarsprout.com/should-you-marry-someone-in-debt/
https://dollarsprout.com/investing-tips/
https://dollarsprout.com/etf-vs-mutual-fund/
https://dollarsprout.com/how-much-should-i-invest/
https://dollarsprout.com/how-to-start-investing-with-100/
https://dollarsprout.com/free-books/
https://dollarsprout.com/first-time-home-buyer-mistakes/
https://dollarsprout.com/hate-your-job-and-want-to-quit/
https://dollarsprout.com/what-is-the-4-percent-rule/
https://dollarsprout.com/what-is-a-bond/
https://dollarsprout.com/van-life-matt-alli-owen/
https://dollarsprout.com/credit-card-fees/
https://dollarsprout.com/how-to-open-an-ira/
https://dollarsprout.com/category/investing/investing-basics/
https://dollarsprout.com/stock-market-correction/
https://dollarsprout.com/bear-market/
https://dollarsprout.com/how-to-invest-in-your-thirties/
https://dollarsprout.com/best-investing-books/
https://dollarsprout.com/how-to-manage-money-after-college/
https://dollarsprout.com/how-to-solve-money-problems-lifestyle/
https://dollarsprout.com/how-much-income-goes-toward-debt/
https://dollarsprout.com/refinance-student-loans/
https://dollarsprout.com/how-to-choose-a-bank/
https://dollarsprout.com/best-online-brokers/
https://dollarsprout.com/axos-invest/
https://dollarsprout.com/td-ameritrade-review/
https://dollarsprout.com/bill-negotiation/
https://dollarsprout.com/acorns-review/
https://dollarsprout.com/how-to-use-your-biases-to-prepare-financially/
https://dollarsprout.com/free-credit-score/
https://dollarsprout.com/credit-sesame-review/
https://dollarsprout.com/make-500-fast/
https://dollarsprout.com/how-to-pay-bills-online/
https://dollarsprout.com/apy-vs-apr/
https://dollarsprout.com/how-to-find-a-financial-advisor/
https://dollarsprout.com/married-couples-should-have-separate-bank-accounts/
https://dollarsprout.com/how-to-become-a-virtual-assistant/
https://dollarsprout.com/work-from-home-jobs/
https://dollarsprout.com/category/lifestyle/debt-stories/
https://dollarsprout.com/debt-success-stories-micah-jankowski/
https://dollarsprout.com/wish-app-review/
https://dollarsprout.com/cheap-gas/
https://dollarsprout.com/groupon-review/
https://dollarsprout.com/disney-world-for-free/
https://dollarsprout.com/apps-like-ibotta/
https://dollarsprout.com/should-a-saver-marry-a-spender/
https://dollarsprout.com/get-paid-to-shop/
https://dollarsprout.com/how-to-set-savings-goals/
https://dollarsprout.com/tip-yourself-review/
https://dollarsprout.com/get-paid-to-test-products/
https://dollarsprout.com/crowdtap-review/
https://dollarsprout.com/how-to-get-free-clothes-online/
https://dollarsprout.com/dollarsprout-turns-5/
https://dollarsprout.com/how-to-be-an-airbnb-host/
https://dollarsprout.com/selling-plasma/
https://dollarsprout.com/free-music-apps/
https://dollarsprout.com/free-things-to-do/
https://dollarsprout.com/cheap-vacation-ideas/
https://dollarsprout.com/you-need-a-budget-review/
https://dollarsprout.com/personal-capital-vs-mint/
https://dollarsprout.com/make-money-driving-with-uber/
https://dollarsprout.com/good-debt-vs-bad-debt/
https://dollarsprout.com/travel-budget/
https://dollarsprout.com/what-is-a-cd-ladder/
https://dollarsprout.com/compound-interest-calculator/
https://dollarsprout.com/savings-calculator/
https://dollarsprout.com/credit-utilization-calculator/
https://dollarsprout.com/cit-bank-review/
https://dollarsprout.com/what-is-a-savings-account/
https://dollarsprout.com/credit-card-vs-debit-card/
https://dollarsprout.com/enneagram-spending-habits/
https://dollarsprout.com/free-car/
https://dollarsprout.com/pink-tax/
https://dollarsprout.com/category/money-management/finance/page/3/
https://dollarsprout.com/category/money-management/finance/page/5/
https://dollarsprout.com/category/money-management/finance/page/2/
https://dollarsprout.com/how-to-make-a-million-dollars/
https://dollarsprout.com/hobbies-that-make-money/
https://dollarsprout.com/things-to-sell/
https://dollarsprout.com/things-to-consider-before-starting-a-new-side-hustle/
https://dollarsprout.com/selling-aluminum-cans/
https://dollarsprout.com/what-are-overdraft-fees/
https://dollarsprout.com/billshark-review/
https://dollarsprout.com/clarity-money-review/
https://dollarsprout.com/cable-tv-alternatives/
https://dollarsprout.com/truebill-vs-trim/
https://dollarsprout.com/get-paid-to-watch-netflix/
https://dollarsprout.com/free-movie-websites/
https://dollarsprout.com/last-minute-christmas-gifts/
https://dollarsprout.com/christmas-gifts-for-men/
https://dollarsprout.com/valentines-day-gifts-for-him/
https://dollarsprout.com/goal-setting-activities/
https://dollarsprout.com/get-paid-to-walk/
https://dollarsprout.com/money-cant-buy-happiness/
https://dollarsprout.com/how-to-become-a-social-media-manager/
https://dollarsprout.com/how-to-maximize-productivity-and-earnings/
https://dollarsprout.com/things-to-do-on-new-years-eve/
https://dollarsprout.com/meal-prep-on-a-budget-50/
https://dollarsprout.com/bank-account-interest-taxes/
https://dollarsprout.com/maximum-tax-refund/
https://dollarsprout.com/online-business-ideas/
https://dollarsprout.com/best-business-books/
https://dollarsprout.com/lease-or-buy-a-car/
https://dollarsprout.com/cit-bank-savings-builder-review/
https://dollarsprout.com/what-is-a-credit-union/
https://dollarsprout.com/category/lifestyle/health/
https://dollarsprout.com/new-years-resolution-ideas/
https://dollarsprout.com/get-paid-to-lose-weight/
https://dollarsprout.com/52-week-money-challenge/
https://dollarsprout.com/change-your-life/
https://dollarsprout.com/make-money-at-home/
https://dollarsprout.com/home-exercise-programs/
https://dollarsprout.com/healthywage-review/
https://dollarsprout.com/minimalist-living/
https://dollarsprout.com/sell-used-furniture/
https://dollarsprout.com/six-figures-to-homeless-felicia-kelly/
https://dollarsprout.com/travel-jobs/
https://dollarsprout.com/how-to-write-a-resignation-letter/
https://dollarsprout.com/how-to-quit-your-job/
https://dollarsprout.com/how-to-ask-for-a-raise/
https://dollarsprout.com/why-not-to-lend-money-to-family/
https://dollarsprout.com/why-i-pay-for-all-star-cheer/
https://dollarsprout.com/signs-of-a-shopping-addiction/
https://dollarsprout.com/work-from-home-mental-health/
https://dollarsprout.com/how-to-retire-early/
https://dollarsprout.com/net-worth-calculator/
https://dollarsprout.com/what-is-a-sinking-fund/
https://dollarsprout.com/invest-100000/
https://dollarsprout.com/how-to-pay-off-holiday-debt/
https://dollarsprout.com/free-government-money/
https://dollarsprout.com/how-to-get-a-personal-loan/
https://dollarsprout.com/credit-score-drop/
https://dollarsprout.com/stop-living-paycheck-to-paycheck/
https://dollarsprout.com/cheap-christmas-gifts/
https://dollarsprout.com/christmas-on-a-budget/
https://dollarsprout.com/money-making-apps/
https://dollarsprout.com/ways-to-save-money-on-a-wedding/
https://dollarsprout.com/debt-reduction/
https://dollarsprout.com/companies-hiring-seasonal-workers/
https://dollarsprout.com/how-to-pay-off-medical-debt/
https://dollarsprout.com/need-help-paying-bills/
https://dollarsprout.com/category/money-management/debt/
https://dollarsprout.com/pay-off-debt-or-save/
https://dollarsprout.com/dave-ramsey-baby-steps/
https://dollarsprout.com/lendingtree-review/
https://dollarsprout.com/what-is-a-financial-plan/
https://dollarsprout.com/advice-from-trim-money-savers/
https://dollarsprout.com/saver-success-stories-tana-williams/
https://dollarsprout.com/wikibuy-review/
https://dollarsprout.com/how-to-find-cheap-flights/
https://dollarsprout.com/category/money-management/save-money/page/3/
https://dollarsprout.com/category/money-management/save-money/page/7/
https://dollarsprout.com/category/money-management/save-money/page/2/
https://dollarsprout.com/amazon-alternatives/
https://dollarsprout.com/make-money-on-amazon/
https://dollarsprout.com/amazon-fresh-review/
https://dollarsprout.com/free-phone/
https://dollarsprout.com/spotify-premium-free-deals/
https://dollarsprout.com/how-to-get-free-money/
https://dollarsprout.com/birthday-freebies/
https://dollarsprout.com/how-to-get-free-furniture/
https://dollarsprout.com/lucktastic-review/
https://dollarsprout.com/rakuten-review/
https://dollarsprout.com/data-entry-jobs-from-home/
https://dollarsprout.com/raise-gift-cards/
https://dollarsprout.com/discounted-gift-cards/
https://dollarsprout.com/inboxdollars-review/
https://dollarsprout.com/survey-junkie-review/
https://dollarsprout.com/free-amazon-prime/
https://dollarsprout.com/honey-review/
https://dollarsprout.com/tiller-money-review/
https://dollarsprout.com/trim-review/
https://dollarsprout.com/cheap-cell-phone-plans/
https://dollarsprout.com/truebill-review/
https://dollarsprout.com/sell-wedding-dress/
https://dollarsprout.com/valentines-day-gifts-for-her/
https://dollarsprout.com/how-to-sell-your-house/
https://dollarsprout.com/ways-to-save-electricity/
https://dollarsprout.com/how-to-buy-a-house/
https://dollarsprout.com/mortgage-pre-approval/
https://dollarsprout.com/category/lifestyle/gift-guides/
https://dollarsprout.com/free-baby-samples/
https://dollarsprout.com/easter-basket-ideas/
https://dollarsprout.com/free-diapers/
https://dollarsprout.com/baby-shower-gift-ideas/
https://dollarsprout.com/free-baby-stuff/
https://dollarsprout.com/stay-at-home-mom-jobs/
https://dollarsprout.com/should-kids-get-paid-to-do-chores/
https://dollarsprout.com/make-money-on-youtube/
https://dollarsprout.com/stopped-spending-money-for-30-days/
https://dollarsprout.com/free-gas-cards/
https://dollarsprout.com/best-travel-sites/
https://dollarsprout.com/vacation-rental-sites/
https://dollarsprout.com/earny-review/
https://dollarsprout.com/save-money-on-christmas/
https://dollarsprout.com/become-a-lyft-driver/
https://dollarsprout.com/gifts-to-never-buy/
https://dollarsprout.com/christmas-gifts-for-mom/
https://dollarsprout.com/christmas-gifts-for-her/
https://dollarsprout.com/christmas-gifts-for-dad/
https://dollarsprout.com/free-amazon-gift-cards/
https://dollarsprout.com/mothers-day-gift-ideas/
https://dollarsprout.com/types-of-life-insurance/
https://dollarsprout.com/whole-life-vs-universal-life/
https://dollarsprout.com/reasons-you-need-an-estate-plan/
https://dollarsprout.com/how-to-start-investing-for-beginners/
https://dollarsprout.com/types-of-insurance/
https://dollarsprout.com/debt-success-stories-aja-mcclanahan/
https://dollarsprout.com/401k-vs-ira/
https://dollarsprout.com/what-is-term-life-insurance/
https://dollarsprout.com/best-cash-back-apps/
https://dollarsprout.com/shopping-apps/
https://dollarsprout.com/free-paypal-money/
https://dollarsprout.com/category/money-management/finance/
https://dollarsprout.com/what-is-a-stock/
https://dollarsprout.com/how-to-earn-money-online/
https://dollarsprout.com/how-much-money-do-i-need-to-retire/
https://dollarsprout.com/saving-for-a-house/
https://dollarsprout.com/zero-based-budget/
https://dollarsprout.com/50-30-20-budget/
https://dollarsprout.com/cash-envelope-system/
https://dollarsprout.com/personal-capital-review/
https://dollarsprout.com/how-to-get-out-of-debt/
https://dollarsprout.com/how-to-improve-your-credit-score/
https://dollarsprout.com/get-rich/
https://dollarsprout.com/track-expenses/
https://dollarsprout.com/budget-tips/
https://dollarsprout.com/financial-mistakes-to-avoid-holidays/
https://dollarsprout.com/sell-shoes-online/
https://dollarsprout.com/sell-jewelry-online/
https://dollarsprout.com/discount-shoes-online/
https://dollarsprout.com/how-to-make-money-on-facebook/
https://dollarsprout.com/online-thrift-store/
https://dollarsprout.com/sites-like-craigslist/
https://dollarsprout.com/sell-electronics/
https://dollarsprout.com/sell-used-dvds/
https://dollarsprout.com/sell-iphone/
https://dollarsprout.com/selling-apps/
https://dollarsprout.com/sell-clothes-online/
https://dollarsprout.com/sell-on-craigslist/
https://dollarsprout.com/sell-my-phone/
https://dollarsprout.com/free-magazines/
https://dollarsprout.com/free-cable-tv/
https://dollarsprout.com/free-internet-access/
https://dollarsprout.com/how-to-get-a-free-laptop/
https://dollarsprout.com/free-kids-books/
https://dollarsprout.com/get-free-stuff-online/
https://dollarsprout.com/free-gift-cards/
https://dollarsprout.com/best-mystery-shopping-companies/
https://dollarsprout.com/cheap-date-ideas/
https://dollarsprout.com/how-to-start-couponing/
https://dollarsprout.com/best-grocery-delivery-services/
https://dollarsprout.com/ibotta-review/
https://dollarsprout.com/best-coupon-websites/
https://dollarsprout.com/fresh-food-delivery-meal-kits/
https://dollarsprout.com/how-to-save-money-on-groceries/
https://dollarsprout.com/how-to-save-money/
https://dollarsprout.com/category/money-management/save-money/
https://dollarsprout.com/frugal-living-tips/
https://dollarsprout.com/no-spend-weekend-ideas/
https://dollarsprout.com/digital-couponing-browser-extensions/
https://dollarsprout.com/living-on-one-income/
https://dollarsprout.com/steps-to-financial-freedom/
https://dollarsprout.com/pay-off-debt-fast/
https://dollarsprout.com/spouse-on-board-paying-off-debt/
https://dollarsprout.com/emergency-fund/
https://dollarsprout.com/list-of-financial-goals/
https://dollarsprout.com/how-many-bank-accounts-should-i-have/
https://dollarsprout.com/money-and-relationships/
https://dollarsprout.com/free-financial-advice/
https://dollarsprout.com/qapital-review/
https://dollarsprout.com/sofi-review/
https://dollarsprout.com/how-to-cancel-a-check/
https://dollarsprout.com/bank-statement/
https://dollarsprout.com/what-is-direct-deposit/
https://dollarsprout.com/money-market-vs-cd/
https://dollarsprout.com/category/banking/banking-basics/
https://dollarsprout.com/open-a-bank-account-online/
https://dollarsprout.com/where-to-cash-a-check/
https://dollarsprout.com/cashiers-check/
https://dollarsprout.com/what-is-paypal/
https://dollarsprout.com/best-cd-rates/
https://dollarsprout.com/digit-review/
https://dollarsprout.com/switching-banks/
https://dollarsprout.com/chime-bank-review/
https://dollarsprout.com/category/banking/checking/
https://dollarsprout.com/what-is-a-checking-account/
https://dollarsprout.com/fill-out-money-order/
https://dollarsprout.com/credit-union-vs-bank/
https://dollarsprout.com/what-is-a-routing-number/
https://dollarsprout.com/checking-vs-savings-account/
https://dollarsprout.com/cd-vs-savings-account/
https://dollarsprout.com/bbva-review/
https://dollarsprout.com/certificate-of-deposit-cd/
https://dollarsprout.com/what-is-a-money-market-account/
https://dollarsprout.com/what-is-online-banking/
https://dollarsprout.com/category/lifestyle/
https://dollarsprout.com/financial-infidelity/
https://dollarsprout.com/debt-success-stories-emma-healey/
https://dollarsprout.com/challenges-of-being-a-female-breadwinner/
https://dollarsprout.com/debt-success-stories-veneta-lusk/
https://dollarsprout.com/managing-your-money/
https://dollarsprout.com/how-to-make-a-budget/
https://dollarsprout.com/best-personal-finance-books/
https://dollarsprout.com/debt-success-stories-kyle-adrian-hildebrand/
https://dollarsprout.com/best-finance-podcasts/
https://dollarsprout.com/best-side-hustle-ideas/
https://dollarsprout.com/bad-financial-advice/
https://dollarsprout.com/how-to-make-money-fast-100/
https://dollarsprout.com/online-jobs/
https://dollarsprout.com/passive-income-ideas/
https://dollarsprout.com/gig-economy-jobs/
https://dollarsprout.com/how-to-start-a-blog/
https://dollarsprout.com/postmates-driver-review/
https://dollarsprout.com/paid-online-surveys/
https://dollarsprout.com/free-netflix/
https://dollarsprout.com/side-hustle-apps/
https://dollarsprout.com/get-paid-to-watch-videos/
https://dollarsprout.com/swagbucks-review/
https://dollarsprout.com/get-paid-to-watch-ads/
https://dollarsprout.com/how-to-get-cheap-movie-tickets/
https://dollarsprout.com/real-money-earning-games/
https://dollarsprout.com/category/side-gigs-and-hustles/
https://dollarsprout.com/category/jobs/
https://dollarsprout.com/category/investing/
https://dollarsprout.com/category/passive-income/
https://dollarsprout.com/category/make-money-apps/
https://dollarsprout.com/category/freelance/
https://dollarsprout.com/category/online-business/
https://dollarsprout.com/category/career/
https://dollarsprout.com/category/money-management/
https://dollarsprout.com/category/budget/
https://dollarsprout.com/category/banking/
https://dollarsprout.com/category/credit/
https://dollarsprout.com/category/research/
https://dollarsprout.com/category/lifestyle/opinion/
https://dollarsprout.com/financial-calculators/
https://dollarsprout.com/best-budgeting-apps/
https://dollarsprout.com/best-investment-apps/
https://dollarsprout.com/best-online-savings-accounts/
https://dollarsprout.com/best-checking-accounts/
https://dollarsprout.com/best-money-market-rates/
https://dollarsprout.com/blog/
https://dollarsprout.com/careers/
https://dollarsprout.com/how-we-make-money/
https://dollarsprout.com/contact/
https://dollarsprout.com/privacy-policy/
https://dollarsprout.com/terms-of-use/
"""
# # Read in a page
for e in s.split():
  try:
    html = scraperwiki.scrape(e)
    root = bs.BeuatifulSoup(html)
    j=root.find_all('div',attrs={'class':'blog-col'})
    print(j)
    for u in j:
      scraperwiki.sqlite.save(unique_keys=['link'], data={"link": e, "html": u.decode('utf-8')})
  except:
    pass
  
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
