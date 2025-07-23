# All-about-best-cs-scientists

## Problem Statement:<br/>

The goal of this project is gather information of best 2000 computer researchers from [This website](https://research.com/scientists-rankings/computer-science) <br/>
later we utilize the scrape data to understand the following demographics and correlations using tableau dashboard

1. A world map of each countries average publications.
2.  Number of scientists in each country using tree map.
3. Which european universities are good at research? (using citation as matric)
4. Which column is directly correlated with the World Rank column? We want to understand how the ranking was done.

you can visit the public dashboard [Here](https://public.tableau.com/app/profile/md.shakhawat.hossain7416/viz/Allaboutofbestcsscientists/Dashboard1)
<br/>


All-about-best-cs-scientists

## build from sources and run the selenium scraper
1. clone the repo
```bash
git clone https://github.com/Rafixyz007/All-about-best-cs-scientists.git
```
2. initialize and activate virtual environment (for windows)

```bash
virtual environment
source dynamic_web_scrape/Scripts/activate
```
3. install dependencies
```bash
pip install -r requirements.txt
```
4. Download GeckoDriver from  https://github.com/mozilla/geckodriver/releases

5. run the scraper
```bash
python dynamic_web_scrape/scraper.py --geckodriver_path <path_to_geckodriver>
```
6. you will get a file name `best_cs_scientists.csv` containing all required fields.

alternatively check our scrape data here: https://github.com/Rafixyz007/All-about-best-cs-scientists/blob/main/best_cs_scientists.csv
