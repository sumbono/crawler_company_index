# crawler_company_index
This app created using Python with Scrapy framework.

This app crawling data list of company index information from [sgmaritime.com](https://www.sgmaritime.com/company-listings). THis app crawl information provided on the page and can follow pagination link.

## Prerequisite
Install python on your machine. You can use [python](https://www.python.org/) or [anaconda](https://www.anaconda.com/).

Install scrapy:
```bash
#if using pip:
pip install Scrapy

#if using anaconda
conda install -c conda-forge scrapy
#or
conda install -c conda-forge/label/cf201901 scrapy
```

## Usage
Firstly download or clone this repo.

### Download Delay
We need to be nice to any site, which we wanted to crawl, by setting a download delay in settings.py:

```python
DOWNLOAD_DELAY = 5

```

### Crawl
On your command line:
```bash
scrapy crawl sgmarine -o company_index.json -t json
```

#### Explanation:

The "sgmarine" is name of this crawler. you can change this name on /spiders/stack_spyder.py, in class StackSpider.
```python
...
  name = "sgmarine"
  ...
```

The "company_index.json" is the output file name. You can change file format to other like a csv by change this part "-t json" to "-t csv"


#### Result:
The running time is depend on your "download_delay" setting and the data itself.
