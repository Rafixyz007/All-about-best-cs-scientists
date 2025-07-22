# All-about-best-cs-scientists

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
python dynamic_web_scrape/scraper.py --geckodriver_path <path to geckodriver>
```
6. you will get a file name `best_cs_scientists.csv` containing all required fields.

alternatively check our scrape data here: https://github.com/Rafixyz007/All-about-best-cs-scientists/blob/main/best_cs_scientists.csv

Tableau public view  https://public.tableau.com/app/profile/md.shakhawat.hossain7416/viz/Allaboutofbestcsscientists/Dashboard1
