from scrapy import cmdline
# 一時停止可能な実行
# scrapy crawl jobbole -s JOBDIR=jobs/001  001->各クローラーは独自なファイルが必要

# doda
cmdline.execute("scrapy crawl doda".split())

# Green
#cmdline.execute("scrapy crawl green".split())

# en
# cmdline.execute("scrapy crawl en".split())

# wantedly
#cmdline.execute("scrapy crawl wantedly".split())
